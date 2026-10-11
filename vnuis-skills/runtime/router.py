# -*- coding: utf-8 -*-
"""Bộ chọn skill: (1) tìm kiếm từ khóa BM25 trên chỉ mục, (2) nếu chưa chắc thì nhờ model chọn trong tối đa 8 ứng viên.
Dùng: python3 router.py "soạn thông báo nghỉ lễ"            (chỉ tìm kiếm, không tốn token)
      python3 router.py "..." --llm deepseek-v4-flash        (có bước model khi chưa chắc)"""
import json, math, re, sys, unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
STOP = set("và của cho các một là để có trong này đã được khi với những không từ ra vào theo về thì nhưng cần xem làm tôi mình em anh chị giúp nhờ hãy muốn đang sẽ cũng rất hay bị còn nào gì đó đây thế".split())

def strip_accents(s):
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def toks(text):
    return [w for w in re.findall(r"[\w&]+", unicodedata.normalize("NFC", text.lower())) if w not in STOP]

def terms(text):
    out = []
    for form, pre in ((text, ""), (strip_accents(text), "u:")):
        w = toks(form)
        out += [pre + x for x in w] + [pre + a + "_" + b for a, b in zip(w, w[1:])]
    return out

class Router:
    def __init__(self, base=HERE):
        base = Path(base)
        self.idx = json.loads((base / "skills-index.json").read_text(encoding="utf-8"))
        syn = json.loads((base / "synonyms.json").read_text(encoding="utf-8"))
        self.abbr = {k.lower(): v for k, v in syn["viet_tat"].items()}
        extra = syn["tu_khoa_them"]
        self.by_name = {s["name"]: s for s in self.idx}
        self.docs = {}
        for s in self.idx:
            slug = s["name"].split("-", 2)[2].replace("-", " ")
            prev = (s.get("previous_name") or "").replace("vnuis-", "").replace("-", " ")
            fields = [(s["title"], 3), (slug, 3), (" ".join(extra.get(s["name"], [])), 3), (prev, 2), (s["description"], 1), (s["group_label"] or "", 1), (s["unit"], 1)]
            c = Counter()
            for text, w in fields:
                for t in terms(self.expand(text)): c[t] += w
            self.docs[s["name"]] = c
        self.N = len(self.docs); self.avg = sum(sum(c.values()) for c in self.docs.values()) / self.N
        df = Counter()
        for c in self.docs.values(): df.update(c.keys())
        self.idf = {t: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for t, n in df.items()}

    def expand(self, text):
        return " ".join(self.abbr.get(w, w) if w in self.abbr else w for w in re.findall(r"[\w&]+|[^\w\s]", text.lower(), re.U)) + " " + text.lower()

    def retrieve(self, query, k=8):
        q = Counter(terms(self.expand(query)))
        res = []
        for name, c in self.docs.items():
            L = sum(c.values()); s = 0.0
            for t, qf in q.items():
                f = c.get(t, 0)
                if f: s += self.idf.get(t, 0) * (f * 2.2) / (f + 1.2 * (0.25 + 0.75 * L / self.avg)) * (1 + 0.3 * (qf - 1))
            res.append((name, s))
        res.sort(key=lambda x: -x[1])
        return res[:k]

    @staticmethod
    def confident(cand, ratio=1.25, floor=8.0):
        if len(cand) < 2: return True
        return cand[0][1] >= floor and cand[0][1] >= ratio * cand[1][1]

    def prompt(self, query, cand):
        lines = []
        for name, _ in cand:
            s = self.by_name[name]
            lines.append(f"- {name} | {s['title']} | {s['description'].split(' Dùng khi')[0][:220]} | cần: {', '.join(s['required_inputs'][:6])}")
        sys_ = ("Bạn là bộ chọn skill nghiệp vụ cho Trường Quốc tế – ĐHQGHN. Chọn đúng MỘT skill phù hợp nhất với yêu cầu, chỉ trong danh sách. "
                "Nếu hai skill đều có thể đúng và yêu cầu chưa đủ để phân biệt, hoặc không skill nào hợp, trả skill=null và đặt đúng một câu hỏi làm rõ. "
                "Không bịa tên skill. Chỉ trả JSON: {\"skill\": \"tên hoặc null\", \"do_tin_cay\": \"cao|vua|thap\", \"ly_do\": \"một câu\", \"cau_hoi_lam_ro\": \"câu hỏi hoặc rỗng\", \"thay_the\": [\"tên\"]}")
        return [{"role": "system", "content": sys_}, {"role": "user", "content": f"Yêu cầu: {query}\n\nDanh sách skill:\n" + "\n".join(lines)}]

    def route(self, query, llm=None, k=8):
        cand = self.retrieve(query, k)
        top = [dict(skill=n, diem=round(s, 2)) for n, s in cand]
        if llm is None or self.confident(cand):
            return dict(skill=cand[0][0], phuong_phap="tu-khoa", do_tin_cay="cao" if self.confident(cand) else "thap", ung_vien=top, cau_hoi_lam_ro="")
        try:
            r = llm.chat_json(self.prompt(query, cand), temperature=0, thinking=False, max_tokens=300)
            sk = r.get("skill")
            if sk not in self.by_name: sk = None
            return dict(skill=sk, phuong_phap="model", do_tin_cay=r.get("do_tin_cay", "thap"), ly_do=r.get("ly_do", ""), cau_hoi_lam_ro=r.get("cau_hoi_lam_ro", ""), thay_the=r.get("thay_the", []), ung_vien=top)
        except Exception as e:
            return dict(skill=cand[0][0], phuong_phap="tu-khoa (model lỗi: %s)" % str(e)[:80], do_tin_cay="thap", ung_vien=top, cau_hoi_lam_ro="")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("query"); ap.add_argument("--llm"); ap.add_argument("--config")
    a = ap.parse_args(); r = Router()
    llm = None
    if a.llm:
        from llm import LLM, load_config
        llm = LLM(load_config(a.config), a.llm)
    print(json.dumps(r.route(a.query, llm), ensure_ascii=False, indent=1))

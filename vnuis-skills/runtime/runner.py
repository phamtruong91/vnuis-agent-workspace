# -*- coding: utf-8 -*-
"""Chạy một skill đã biên dịch qua API model: (1) chọn skill, (2) thu thập input, (3) soạn, (4) tự kiểm tra, (5) xuất file.
Model KHÔNG tạo file: nó trả Markdown theo cấu trúc đầu ra; ứng dụng xuất .docx/.xlsx (export.py).
CLI: python3 runner.py "yêu cầu" [--skill TÊN] [--mode single|steps] [--input file.txt] [--out thư_mục] [--no-check]"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent

def load_skill(name, base=HERE):
    return json.loads((Path(base) / "compiled" / f"{name}.json").read_text(encoding="utf-8"))

def _bul(xs): return "\n".join("- " + x for x in xs)

MARK = "=== GHI CHÚ NỘI BỘ ==="
SOURCE_CAP = 24000  # ký tự dữ liệu gốc đưa vào bước tự kiểm tra

def split_notes(md):
    a, _, b = md.partition(MARK)
    return a.rstrip() + "\n", b.strip()

def system_prompt(sk):
    p = [f"Bạn là trợ lý nghiệp vụ của {sk['unit']}, Trường Quốc tế – ĐHQGHN. Nhiệm vụ: \"{sk['title']}\". Luôn viết tiếng Việt, đúng văn phong hành chính khi là văn bản.",
         "Bạn chỉ trả nội dung Markdown của sản phẩm. Không tạo file, không nói đã gửi/đã ký/đã duyệt. Không bịa số liệu, số hiệu văn bản, căn cứ pháp lý hay tên người; thiếu thông tin thì chừa chỗ theo mẫu (dòng dấu chấm, dấu gạch hoặc ô trống), không điền giả định, không dùng mã chờ như [CẦN BỔ SUNG].",
         "## Thông tin đã xác định (dùng sẵn, không hỏi lại)\n" + "\n".join(f"- {d['muc']}: {d['gia_tri']}" for d in sk["defaults"])]
    if sk.get("legal_pre"): p.append("## Căn cứ pháp lý (chỉ trích khi đúng bối cảnh, chưa chắc thì ghi cần kiểm tra)\n" + sk["legal_pre"])
    elif sk.get("legal"): p.append("## Căn cứ pháp lý\n" + sk["legal"][:1500])
    p.append("## Giới hạn chung\n" + sk["limits_std"])
    if sk["guardrails"]: p.append("## Quy tắc cấm\n" + _bul(sk["guardrails"]))
    if sk.get("adjustments"): p.append("## Điều chỉnh theo Trường\n" + _bul(sk["adjustments"]))
    p.append("## Cấu trúc đầu ra bắt buộc (theo đúng thứ tự)\n" + sk["output_structure_raw"])
    p.append("## Cổng duyệt\n" + _bul(sk["gates"]))
    p.append("## Ghi chú nội bộ\nNếu có điểm cần người phụ trách xác nhận (mâu thuẫn, thiếu dữ liệu, nội dung nhạy cảm đã loại), đặt SAU sản phẩm, tách bằng một dòng đúng như sau và không dùng dòng đó ở nơi khác:\n" + MARK + "\nPhần trước dòng này là sản phẩm giao đi, không chứa ghi chú nội bộ, danh mục kiểm hay mã chờ.")
    return "\n\n".join(p)

def collect_inputs(llm, sk, text, thinking=False):
    spec = "\n".join(f"- {i['key']} ({'bắt buộc' if i['required'] else 'tùy chọn'}): {i['desc']}" for i in sk["inputs"])
    sys_ = ("Trích thông tin đầu vào từ yêu cầu của người dùng cho skill. Chỉ lấy điều người dùng thực sự nêu; không suy đoán. "
            "Trả JSON: {\"gia_tri\": {key: nội dung}, \"thieu_bat_buoc\": [key], \"cau_hoi\": [\"tối đa 3 câu hỏi ngắn cho phần thiếu quan trọng nhất\"]}")
    r = llm.chat_json([{"role": "system", "content": sys_}, {"role": "user", "content": f"Các input của skill:\n{spec}\n\nYêu cầu người dùng:\n{text}"}], temperature=0, thinking=thinking, max_tokens=1200)
    req = [i["key"] for i in sk["inputs"] if i["required"]]
    vals = {k: v for k, v in (r.get("gia_tri") or {}).items() if v not in (None, "", [], {})}
    return dict(gia_tri=vals, thieu_bat_buoc=[k for k in req if k not in vals], cau_hoi=(r.get("cau_hoi") or [])[:3])

def _facts(sk, vals, raw):
    desc = {i["key"]: i["desc"] for i in sk["inputs"]}
    return "## Dữ liệu người dùng cung cấp\n" + "\n".join(f"- {desc.get(k, k)}: {v}" for k, v in vals.items()) + f"\n\n## Nguyên văn yêu cầu/tài liệu\n{raw}"

def draft(llm, sk, vals, raw, mode="single", thinking=None):
    sysm = system_prompt(sk); facts = _facts(sk, vals, raw)
    if mode == "single":
        steps = "\n".join(f"{s['n']}. {s['title']}: {s['lam_gi']}" for s in sk["steps"])
        u = f"{facts}\n\n## Quy trình cần theo\n{steps}\n\nHãy soạn sản phẩm hoàn chỉnh theo cấu trúc đầu ra."
        return llm.chat([{"role": "system", "content": sysm}, {"role": "user", "content": u}], temperature=0.3, thinking=thinking)
    notes = []
    for s in sk["steps"]:
        u = (f"{facts}\n\n## Kết quả các bước trước\n" + ("\n\n".join(notes) or "(chưa có)") +
             f"\n\n## Làm bước {s['n']}: {s['title']}\n{s['lam_gi']}\nLưu ý: {s.get('luu_y','')}\nKết quả cần có: {s.get('ket_qua','')}\nChỉ trả kết quả bước này, ngắn gọn, ghi rõ chỗ thiếu dữ liệu.")
        notes.append(f"### Bước {s['n']}: {s['title']}\n" + llm.chat([{"role": "system", "content": sysm}, {"role": "user", "content": u}], temperature=0.3, thinking=thinking, max_tokens=1500))
    u = f"{facts}\n\n## Kết quả từng bước\n" + "\n\n".join(notes) + "\n\nTổng hợp thành sản phẩm hoàn chỉnh đúng cấu trúc đầu ra. Không thêm số liệu mới."
    return llm.chat([{"role": "system", "content": sysm}, {"role": "user", "content": u}], temperature=0.2, thinking=thinking)

def self_check(llm, sk, text, fix=True, thinking=None, source=""):
    items = "\n".join(f"{i+1}. {c}" for i, c in enumerate(sk["checks"])) + f"\n{len(sk['checks'])+1}. Không có số liệu, số hiệu, căn cứ hay tên riêng bị bịa; chỗ thiếu đã chừa trống theo mẫu, không điền giả định."
    sys_ = "Bạn là người kiểm tra độc lập. Đánh giá bản soạn theo từng mục, nghiêm khắc. Nếu có dữ liệu gốc thì đối chiếu từng số liệu, tên, ngày với dữ liệu gốc và coi số không có trong dữ liệu gốc là lỗi (trừ số do phép tính đúng từ dữ liệu gốc). Trả JSON: {\"muc\": [{\"so\": 1, \"dat\": true, \"ghi_chu\": \"\"}], \"loi_chinh\": [\"...\"]}"
    r = llm.chat_json([{"role": "system", "content": sys_}, {"role": "user", "content": f"Mục kiểm tra:\n{items}\n\n" + (f"Dữ liệu gốc (đối chiếu số liệu, tên, ngày với phần này; có thể đã bị cắt bớt):\n{source[:SOURCE_CAP]}\n\n" if source else "") + f"Bản soạn:\n{text}"}], temperature=0, thinking=thinking, max_tokens=1500)
    bad = [m for m in r.get("muc", []) if not m.get("dat")]
    res = dict(dat=not bad, khong_dat=bad, loi_chinh=r.get("loi_chinh", []), da_sua=False, text=text)
    if bad and fix:
        u = ("Sửa bản soạn để khắc phục đúng các lỗi sau, giữ nguyên phần đã đạt (kể cả dòng tách ghi chú nội bộ), không thêm số liệu mới:\n" + json.dumps(bad, ensure_ascii=False) +
             "\n\nBản soạn:\n" + text)
        res["text"] = llm.chat([{"role": "system", "content": system_prompt(sk)}, {"role": "user", "content": u + (f"\n\nDữ liệu gốc:\n{source[:SOURCE_CAP]}" if source else "")}], temperature=0.2, thinking=thinking); res["da_sua"] = True
    return res

def footer(sk):
    return f"\n\n---\n**Lưu ý:** {sk['limits_std']}\n\n- [ ] {sk['human_gate_check']}\n"

def run(llm_by_role, skill, text, mode="single", check=True, vals=None):
    """llm_by_role: dict vai trò -> LLM (thu_thap_input, soan, tu_kiem_tra). Trả dict kết quả; nếu thiếu input bắt buộc thì trả trạng thái 'can_hoi'."""
    sk = skill if isinstance(skill, dict) else load_skill(skill)
    if vals is None:
        ci = collect_inputs(llm_by_role["thu_thap_input"], sk, text)
        if ci["thieu_bat_buoc"]:
            return dict(trang_thai="can_hoi", thieu=ci["thieu_bat_buoc"], cau_hoi=ci["cau_hoi"], gia_tri=ci["gia_tri"])
        vals = ci["gia_tri"]
    md = draft(llm_by_role["soan"], sk, vals, text, mode)
    kc = None
    if check:
        kc = self_check(llm_by_role["tu_kiem_tra"], sk, md, source=text); md = kc.pop("text")
    md, notes = split_notes(md)
    return dict(trang_thai="xong", markdown=md, ghi_chu_noi_bo=notes, luu_y=footer(sk), format=sk["format"], kiem_tra=kc, gia_tri=vals)

def roles(cfg_path=None):
    from llm import LLM, load_config
    cfg = load_config(cfg_path); cache = {}
    def get(n): return cache.setdefault(n, LLM(cfg, n))
    return {r: get(n) for r, n in cfg["vai_tro"].items() if not r.startswith("_")}, cfg

if __name__ == "__main__":
    import argparse
    from router import Router
    from export import export
    ap = argparse.ArgumentParser(); ap.add_argument("query"); ap.add_argument("--skill"); ap.add_argument("--mode", default="single")
    ap.add_argument("--input", nargs="+", help="một hoặc nhiều tệp (.docx .xlsx .csv .txt .pdf)"); ap.add_argument("--out", default="out"); ap.add_argument("--config"); ap.add_argument("--no-check", action="store_true")
    a = ap.parse_args()
    rl, cfg = roles(a.config)
    q = a.query
    if a.input:
        from extract import merge, est_tokens
        body = merge(a.input); q = a.query + "\n\n" + body
        print(f"Đầu vào: {len(a.input)} tệp, {len(body)} ký tự, ước tính ~{est_tokens(body)} token (ước lượng thô)")
    name = a.skill or Router().route(a.query, rl["router"])["skill"]
    if not name: print("Chưa xác định được skill; hãy nêu rõ hơn hoặc dùng --skill."); sys.exit(2)
    print("Skill:", name)
    r = run(rl, name, q, a.mode, not a.no_check)
    if r["trang_thai"] == "can_hoi":
        print("Cần bổ sung:", ", ".join(r["thieu"])); [print(" -", c) for c in r["cau_hoi"]]; sys.exit(3)
    Path(a.out).mkdir(exist_ok=True)
    fmt = {"docx": "docx", "xlsx": "xlsx"}.get(r["format"], "md")
    p = export(r["markdown"], fmt, str(Path(a.out) / name)); print("Đã xuất:", p)
    if r["ghi_chu_noi_bo"]:
        np_ = Path(a.out) / (name + "_ghi_chu_noi_bo.md"); np_.write_text(r["ghi_chu_noi_bo"], encoding="utf-8"); print("Ghi chú nội bộ (không gửi đi):", np_)
    print(r["luu_y"].strip())
    if r["kiem_tra"]: print("Tự kiểm tra:", "đạt" if r["kiem_tra"]["dat"] else "còn lỗi", r["kiem_tra"]["loi_chinh"])

# -*- coding: utf-8 -*-
"""Biên dịch skills/*/SKILL.md thành JSON có cấu trúc (compiled/) và chỉ mục tra cứu (skills-index.json).
Chạy: python3 compile.py            (đọc ../skills, ghi ./compiled và ./skills-index.json)
Chỉ dùng thư viện chuẩn."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACK = HERE.parent
SKILLS = PACK / "skills"

def sections(text):
    parts = re.split(r"\n(?=## )", text)
    head, out = parts[0], {}
    for p in parts[1:]:
        h, _, body = p.partition("\n")
        out[h[3:].strip()] = body.strip("\n")
    return head, out

def bullets(body):
    """Gộp các dòng '- ' (kể cả dòng nối tiếp thụt lề) thành danh sách chuỗi."""
    items = []
    for line in body.split("\n"):
        if re.match(r"^\s*[-*] ", line):
            items.append(re.sub(r"^\s*[-*] ", "", line).strip())
        elif items and line.strip() and not line.startswith("#") and not line.startswith("|"):
            items[-1] += " " + line.strip()
    return items

def parse_inputs(body):
    ins = []
    for line in body.split("\n"):
        m = re.match(r"^\| `([a-z0-9_]+)` \| (.*) \| (.*) \|\s*$", line)
        if m:
            req = m.group(3).strip()
            ins.append(dict(key=m.group(1), desc=m.group(2).strip(), required=req.startswith("Có"), note=req))
    return ins

def parse_defaults(body):
    rows = []
    m = re.search(r"### Thông tin VNU-IS đã điền sẵn.*?\n\n(\|.*?)(?:\n\n|\Z)", body, re.S)
    if m:
        for line in m.group(1).split("\n")[2:]:
            c = [x.strip() for x in line.strip("|").split("|")]
            if len(c) >= 2: rows.append(dict(muc=c[0], gia_tri="|".join(c[1:]).strip()))
    return rows

LABELS = ["Làm gì", "Dùng input", "Vai trò", "Lưu ý nghiệp vụ", "→ Kết quả bước"]
def parse_steps(body):
    legal, rest = body, ""
    i = body.find("**Bước 1.")
    pre = body[:i] if i >= 0 else ""
    steps = []
    for m in re.finditer(r"\*\*Bước (\d+)\. (.*?)\*\*\n(.*?)(?=\n\*\*Bước \d+\.|\Z)", body, re.S):
        blk = m.group(3)
        fields, cur = {}, None
        for line in blk.split("\n"):
            lm = re.match(r"^- (Làm gì|Dùng input|Vai trò|Lưu ý nghiệp vụ|→ Kết quả bước|Lưu ý[^:]*|Kết quả[^:]*):\s*(.*)$", line)
            if lm:
                cur = lm.group(1); fields[cur] = lm.group(2).strip()
            elif cur and line.strip():
                fields[cur] += " " + line.strip()
        ins = re.findall(r"`([a-z0-9_]+)`", fields.get("Dùng input", ""))
        steps.append(dict(n=int(m.group(1)), title=m.group(2).strip(), lam_gi=fields.get("Làm gì", ""), inputs=ins,
                          vai_tro=re.sub(r"\s*·\s*⏱.*$", "", fields.get("Vai trò", "")), luu_y=fields.get("Lưu ý nghiệp vụ", "") or next((v for k, v in fields.items() if k.startswith("Lưu ý")), ""),
                          ket_qua=fields.get("→ Kết quả bước", "") or next((v for k, v in fields.items() if k.startswith("Kết quả")), "")))
    pre = re.sub(r"^\*⏱.*?\*\s*", "", pre.strip())
    return pre.strip(), steps

def sect(secs, *names):
    for n in names:
        for k, v in secs.items():
            if k.startswith(n): return v
    return ""

def numbered(body):
    out = []
    for line in body.split("\n"):
        m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if m: out.append(m.group(2).strip())
        elif out and line.strip() and not line.startswith("#") and not line.startswith("Cấu trúc này"):
            out[-1] += " " + line.strip()
    return out

def compile_skill(d):
    t = (d / "SKILL.md").read_text(encoding="utf-8")
    head, secs = sections(t)
    fm = dict(re.findall(r'^(name|description): "(.*)"$', head, re.M))
    title = re.search(r"^# (.*)$", head, re.M).group(1)
    ver = json.loads((d / "references/version.json").read_text(encoding="utf-8"))
    pre, steps = parse_steps(secs["Quy trình"])
    ovl = secs.get("Bối cảnh riêng của VNU-IS", "")
    adj = re.search(r"\*\*Điều chỉnh khi dùng cho VNU-IS\*\*\n(.*?)(?=\n\*\*|\nNếu người dùng|\Z)", ovl, re.S)
    cho = re.search(r"\*\*Chờ xác nhận khi khảo sát\*\*\n(.*?)(?=\nNếu người dùng|\Z)", ovl, re.S)
    unit = re.search(r"\*\*Đơn vị thường dùng:\*\* (.*)", ovl)
    qc = (d / "references/quy-cach-dau-ra.md").read_text(encoding="utf-8")
    _, qs = sections(qc)
    struct = numbered(sect(qs, "Cấu trúc sản phẩm"))
    phap = (d / "references/phap-ly.md")
    inp = secs.get("Đầu vào (Input)", secs.get("Đầu vào", ""))
    gate = sect(secs, "Human gate")
    guard = sect(secs, "Giới hạn (guardrails)", "Giới hạn\n")
    guard_b = bullets(guard)
    # quy tắc cấm còn nằm trong mục "Căn cứ & lưu ý" (kể cả khi đã có mục guardrails): gộp cả hai, bỏ trùng
    extra = [b for b in bullets(secs.get("Căn cứ & lưu ý", "")) if re.match(r"(Không|Cấm|Tuyệt đối|Chỉ )", b) and not b.startswith("Không đưa dữ liệu cá nhân thật")]
    guard_b = guard_b + [b for b in extra if b not in guard_b]
    checks = [re.sub(r"^\[ \] ", "", b) for b in bullets(sect(secs, "Kiểm tra nội bộ"))]
    return dict(
        name=fm["name"], title=title, description=fm["description"], group=ver.get("group"), group_label=ver.get("group_label"),
        previous_name=ver.get("previous_name"), format=ver.get("default_output_format"), version=ver.get("version"),
        unit=unit.group(1).strip().rstrip(".") if unit else "", when=sect(secs, "Khi nào dùng").strip(),
        inputs=parse_inputs(inp), defaults=parse_defaults(inp), legal_pre=pre, steps=steps, checks=checks,
        gates=bullets(gate), guardrails=guard_b, limits_std=sect(secs, "Giới hạn và human gate").split("Bản đầy đủ:")[0].strip(),
        adjustments=bullets(adj.group(1)) if adj else [], cho_xac_nhan=bullets(cho.group(1)) if cho else [],
        output_structure=struct, output_structure_raw=sect(qs, "Cấu trúc sản phẩm").split("Cấu trúc này là hướng dẫn")[0].strip(),
        human_gate_check=next((c for c in checks if "Human gate" in c), ""),
        header_info=sect(qs, "Thông tin đầu văn bản"), legal=phap.read_text(encoding="utf-8") if phap.exists() else "",
        outputs_dir=str((d / "references").relative_to(PACK)))

def main():
    out = HERE / "compiled"; out.mkdir(exist_ok=True)
    idx, problems = [], []
    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir(): continue
        c = compile_skill(d)
        if not c["steps"] or not c["inputs"] or not c["checks"]: problems.append((c["name"], len(c["steps"]), len(c["inputs"]), len(c["checks"])))
        (out / f"{c['name']}.json").write_text(json.dumps(c, ensure_ascii=False, indent=1), encoding="utf-8")
        idx.append({k: c[k] for k in ("name", "title", "description", "group", "group_label", "previous_name", "format", "unit")} |
                   dict(required_inputs=[i["key"] for i in c["inputs"] if i["required"]], n_steps=len(c["steps"]), n_inputs=len(c["inputs"])))
    (HERE / "skills-index.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(idx), "skill; cần xem:", problems[:10])
if __name__ == "__main__":
    main()

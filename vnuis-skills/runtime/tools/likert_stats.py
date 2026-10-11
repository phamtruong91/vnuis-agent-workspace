# -*- coding: utf-8 -*-
"""Tiền xử lý khảo sát Likert TRƯỚC khi đưa cho model (model không tự cộng 400 dòng được).
Chỉ dùng thư viện chuẩn Python. Ví dụ:
  python tools/likert_stats.py du_lieu.tsv --id ID --items Q1-Q10 --group Khoa --group "Chương trình" \
      --reverse Q7 --min 1 --max 5 --blank-max 0.3 --min-n 30 --baseline "3.85,4.05,3.75,3.55,3.6,3.4,2.7,3.7,3.35,3.8" > ket_qua.md
Đầu ra là văn bản Markdown (số liệu đã tính + danh sách phiếu bị loại); dán vào --input của runner cùng câu hỏi mở.
Quy tắc làm sạch (khớp skill dc-phan-tich-ket-qua-khao-sat): bỏ ID trùng (giữ dòng đầu), bỏ phiếu có giá trị ngoài thang,
bỏ phiếu bỏ trống > ngưỡng, bỏ phiếu chọn một đáp án cho mọi câu (straight-line). Mỗi lý do loại được ghi lại."""
import argparse, csv, re, sys, statistics as st
from collections import Counter, OrderedDict

def expand(spec, header):
    out = []
    for part in spec.split(","):
        part = part.strip()
        m = re.fullmatch(r"([A-Za-z]+)(\d+)-\1(\d+)", part) or re.fullmatch(r"([A-Za-z]+)(\d+)-([A-Za-z]*)(\d+)", part)
        if m and part.count("-") == 1 and not part in header:
            g = m.groups(); pre = g[0]
            a, b = int(g[1]), int(g[-1])
            out += [f"{pre}{i}" for i in range(a, b + 1)]
        else:
            out.append(part)
    return out

def num(x):
    x = (x or "").strip().replace(",", ".")
    try: return float(x)
    except ValueError: return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file"); ap.add_argument("--id", default="ID")
    ap.add_argument("--items", required=True); ap.add_argument("--group", action="append", default=[])
    ap.add_argument("--reverse", default=""); ap.add_argument("--min", type=int, default=1); ap.add_argument("--max", type=int, default=5)
    ap.add_argument("--blank-max", type=float, default=0.3); ap.add_argument("--min-n", type=int, default=30)
    ap.add_argument("--baseline", default=""); ap.add_argument("--overall", default="", help="mã câu hỏi 'hài lòng chung' để so sánh nhóm (mặc định: câu cuối)")
    ap.add_argument("--sent", type=int, default=0, help="tổng số phiếu phát ra / số SV trong diện (để tính tỷ lệ phản hồi)")
    a = ap.parse_args()
    delim = "\t" if a.file.lower().endswith(".tsv") else ","
    rows = list(csv.DictReader(open(a.file, encoding="utf-8-sig"), delimiter=delim))
    header = list(rows[0].keys())
    items = expand(a.items, header); rev = set(expand(a.reverse, header)) if a.reverse else set()
    overall = a.overall or items[-1]
    raw_n = len(rows); log = OrderedDict((k, []) for k in ["trùng ID", "giá trị ngoài thang", "bỏ trống quá ngưỡng", "chọn một đáp án cho mọi câu"])
    seen, kept = set(), []
    for r in rows:
        i = r[a.id].strip()
        if i in seen: log["trùng ID"].append(i); continue
        seen.add(i); kept.append(r)
    after_dedup = len(kept); valid = []
    for r in kept:
        vals = [num(r.get(q)) for q in items]
        blanks = sum(v is None for v in vals)
        if any(v is not None and not (a.min <= v <= a.max) for v in vals): log["giá trị ngoài thang"].append(r[a.id]); continue
        if blanks / len(items) > a.blank_max: log["bỏ trống quá ngưỡng"].append(r[a.id]); continue
        present = [v for v in vals if v is not None]
        if len(present) >= 5 and len(set(present)) == 1: log["chọn một đáp án cho mọi câu"].append(r[a.id]); continue
        r["_v"] = {q: v for q, v in zip(items, vals)}; valid.append(r)
    def score(r, q):
        v = r["_v"][q]
        return None if v is None else (a.min + a.max - v if q in rev else v)
    def mean(rs, q, raw=False):
        xs = [(r["_v"][q] if raw else score(r, q)) for r in rs]; xs = [x for x in xs if x is not None]
        return (sum(xs) / len(xs)) if xs else None
    P = lambda *s: print(*s)
    base = [float(x) for x in a.baseline.replace(";", ",").split(",") if x.strip()] if a.baseline else []
    P("# Số liệu khảo sát đã tính sẵn (do công cụ tính, không phải model)\n")
    P("## 1. Làm sạch dữ liệu\n")
    P(f"- Dòng thô: {raw_n}; sau bỏ trùng ID: {after_dedup}; phiếu hợp lệ: **{len(valid)}**.")
    if a.sent: P(f"- Tỷ lệ phản hồi: {len(valid)}/{a.sent} = {100*len(valid)/a.sent:.1f}%.")
    else: P("- Tỷ lệ phản hồi: **chưa tính được** vì chưa có tổng số phiếu phát ra / số người trong diện (tham số --sent).")
    for k, v in log.items(): P(f"- Loại do {k}: {len(v)}" + (f" ({', '.join(v)})" if v else ""))
    if rev and base: P("> Lưu ý: số kỳ trước của câu đảo được hiểu là điểm GỐC (chưa mã hóa ngược). Nếu kỳ trước đã mã hóa ngược thì phải hỏi lại đơn vị trước khi so sánh.\n")
    P("\n## 2. Thống kê từng câu (trên phiếu hợp lệ; câu đảo đã mã hóa ngược)\n")
    P("| Câu | Đảo | TB gốc | TB dùng để đánh giá | " + " | ".join(f"%{k}" for k in range(a.min, a.max + 1)) + " | Số trả lời | Kỳ trước | Chênh |")
    P("|---|---|---|---|" + "---|" * (a.max - a.min + 1) + "---|---|---|")
    for j, q in enumerate(items):
        xs = [x for x in (score(r, q) for r in valid) if x is not None]; c = Counter(int(x) for x in xs); n = len(xs)
        raw = mean(valid, q, True); m = mean(valid, q)
        if base and j < len(base):
            d = f"{raw - base[j]:+.2f} (câu đảo: so điểm gốc với điểm gốc kỳ trước; GIẢM là tốt hơn)" if q in rev else f"{m - base[j]:+.2f}"
        else: d = ""
        P(f"| {q} | {'có' if q in rev else ''} | {raw:.2f} | {m:.2f} | " + " | ".join(f"{100*c[k]/n:.1f}" for k in range(a.min, a.max + 1)) + f" | {n} | {base[j] if base and j < len(base) else ''} | {d} |")
    P(f"\nTB toàn bộ câu (đã mã hóa ngược): {st.mean([mean(valid, q) for q in items]):.2f}.")
    for g in a.group:
        P(f"\n## 3. Theo nhóm: {g} (câu {overall}; nhóm dưới {a.min_n} phiếu được đánh dấu, không kết luận riêng)\n")
        P("| Nhóm | Số phiếu | TB " + overall + " | " + " | ".join(items) + " |"); P("|---|---|---|" + "---|" * len(items))
        groups = {}
        for r in valid: groups.setdefault(r[g], []).append(r)
        for k, rs in sorted(groups.items()):
            flag = " (nhóm nhỏ)" if len(rs) < a.min_n else ""
            P(f"| {k}{flag} | {len(rs)} | {mean(rs, overall):.2f} | " + " | ".join(f"{mean(rs, q):.2f}" for q in items) + " |")
    P(f"\n## 4. Độ nhạy\n\n- TB {overall} nếu KHÔNG loại phiếu chọn một đáp án: " + (lambda xs: f"{sum(xs)/len(xs):.2f}")([score({'_v': {q: num(r.get(q)) for q in items}}, overall) for r in kept if r[a.id] not in set(log['giá trị ngoài thang']) | set(log['bỏ trống quá ngưỡng']) and score({'_v': {q: num(r.get(q)) for q in items}}, overall) is not None]) + f"; nếu loại: {mean(valid, overall):.2f}.")
if __name__ == "__main__": main()

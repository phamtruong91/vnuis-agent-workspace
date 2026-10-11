# -*- coding: utf-8 -*-
"""Đo độ chính xác bộ chọn skill trên eval/router_testset.jsonl.
python3 eval/eval_router.py                  # chỉ tìm kiếm từ khóa (không tốn token)
python3 eval/eval_router.py --llm <tên model trong models.json>   # đo cả bước model"""
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from router import Router
ap = argparse.ArgumentParser(); ap.add_argument("--llm"); ap.add_argument("--config"); ap.add_argument("--set", default=str(Path(__file__).with_name("router_testset.jsonl")))
a = ap.parse_args()
rows = [json.loads(l) for l in open(a.set, encoding="utf-8")]
r = Router(); llm = None
if a.llm:
    from llm import LLM, load_config
    llm = LLM(load_config(a.config), a.llm)
t1 = t3 = t5 = 0; fail = []; fast_ok = fast_n = 0; final_ok = 0; calls = 0
for row in rows:
    cand = r.retrieve(row["query"], 8); names = [n for n, _ in cand]
    t1 += names[0] == row["expected"]; t3 += row["expected"] in names[:3]; t5 += row["expected"] in names[:5]
    if names[0] != row["expected"]: fail.append((row["expected"], names[:3], row["query"]))
    if r.confident(cand): fast_n += 1; fast_ok += names[0] == row["expected"]
    if llm:
        res = r.route(row["query"], llm); calls += res["phuong_phap"] == "model"; final_ok += res["skill"] == row["expected"]
n = len(rows)
print(json.dumps(dict(so_cau=n, top1=round(t1 / n, 3), top3=round(t3 / n, 3), top5=round(t5 / n, 3), duong_nhanh_tu_khoa=dict(so_cau=fast_n, ty_le_cau=round(fast_n / n, 3), dung=round(fast_ok / max(fast_n, 1), 3)),
                 **({"sau_buoc_model": dict(dung=round(final_ok / n, 3), so_lan_goi_model=calls)} if llm else {})), ensure_ascii=False, indent=1))
for e, got, q in fail[:40]: print("SAI:", e[6:], "<-", [g[6:] for g in got], "|", q[:70])

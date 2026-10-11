# -*- coding: utf-8 -*-
"""Máy chủ giả kiểu OpenAI để kiểm thử đường ống (KHÔNG đánh giá chất lượng model). Chạy: python3 eval/mock_server.py 8765"""
import json, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        b = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        s = b["messages"][0]["content"]; u = b["messages"][-1]["content"]
        import os
        with open(os.environ.get("MOCK_LOG", "/tmp/t/mock.log"), "a", encoding="utf-8") as lg:
            lg.write(f"{sum(len(x['content']) for x in b['messages'])}\t{s[:28].strip()!r}\n")
        if s.startswith("Trích thông tin"):
            import re
            keys = re.findall(r"^- (\w+) \(", u, re.M)
            have = {k: "giá trị thử" for k in keys if "mơ hồ" not in u}
            t = json.dumps({"gia_tri": have, "thieu_bat_buoc": [], "cau_hoi": ["Bạn cho biết thêm?"]})
        elif s.startswith("Bạn là người kiểm tra"):
            bad = "FIXME" in u or "Lưu ý chưa sửa" in u
            t = "```json\n" + json.dumps({"muc": [{"so": 1, "dat": not (bad and "SUA" not in u[:0]), "ghi_chu": "thiếu"}], "loi_chinh": ["x"] if bad else []}) + "\n```"
        elif s.startswith("Bạn là bộ chọn"): t = json.dumps({"skill": "vnuis-ts-theo-doi-pheu-thi-sinh", "do_tin_cay": "cao", "ly_do": "mock", "cau_hoi_lam_ro": "", "thay_the": []})
        elif u.startswith("Sửa bản soạn"): t = "# Bản đã sửa\n\n| Giai đoạn | Số lượng |\n|---|---|\n| Quan tâm | ........ |"
        else: t = "# Bản soạn thử\n\n**Tiêu đề** mock\n\n| Giai đoạn | Số lượng |\n|---|---|\n| Quan tâm | ........ |\n\n- ý 1\n- FIXME"
        out = json.dumps({"choices": [{"message": {"content": t}}], "usage": {"prompt_tokens": 10, "completion_tokens": 5}}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers(); self.wfile.write(out)
HTTPServer(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 8765), H).serve_forever()

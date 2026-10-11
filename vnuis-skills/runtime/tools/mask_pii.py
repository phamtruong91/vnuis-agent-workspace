# -*- coding: utf-8 -*-
"""Che thông tin định danh TRƯỚC khi gửi văn bản ra model. Chỉ thư viện chuẩn.
  python tools/mask_pii.py cau_tra_loi_mo.txt > da_che.txt
Che: số điện thoại (có hoặc không có dấu cách/chấm), email, số CCCD/CMND 9–12 số, mã sinh viên theo mẫu --id-pattern (mặc định không che).
KHÔNG che được: tên riêng không có dấu hiệu rõ, hoàn cảnh cá nhân, chức danh + tên viết tắt ("Thầy T."), tình trạng sức khỏe.
Phần đó phải do người đọc lại; công cụ chỉ in cảnh báo các dòng có từ khóa nhạy cảm."""
import re, sys
PAT = [(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", "[EMAIL]"),
       (r"(?<!\d)(?:\+?84|0)[\s.\-]?\d{2,3}[\s.\-]?\d{3}[\s.\-]?\d{3,4}(?!\d)", "[SĐT]"),
       (r"(?<!\d)\d{9}(?:\d{3})?(?!\d)", "[SỐ GIẤY TỜ]")]
SENS = re.compile(r"\b(?:Thầy|Cô|Anh|Chị|ông|bà)\s+[A-ZĐ]\.|bệnh|mẹ mất|bố mất|qua đời|hoàn cảnh|ung thư|trầm cảm|tự tử|kỷ luật|khiếu nại", re.I)
def mask(t, id_pattern=None):
    for p, r in PAT: t = re.sub(p, r, t)
    if id_pattern: t = re.sub(id_pattern, "[MÃ]", t)
    return t
if __name__ == "__main__":
    src = open(sys.argv[1], encoding="utf-8").read(); out = mask(src, sys.argv[2] if len(sys.argv) > 2 else None)
    sys.stdout.write(out)
    for i, l in enumerate(out.splitlines(), 1):
        if SENS.search(l): sys.stderr.write(f"CẢNH BÁO dòng {i}: có thể chứa tên người/hoàn cảnh cá nhân – người đọc lại: {l[:90]}\n")

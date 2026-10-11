# Phân tích trước khi customize skill cho VNU-IS

Ngày lập 10/10/2026. Phân biệt rõ: **đã xác minh** (đọc trực tiếp từ file hoặc website), **suy luận** (tôi rút ra), **giả định** (cần xác nhận).

## 1. Đã xác minh

**File CES (30/07/2026):**
- 10 sheet: danh mục 12 đơn vị, kế hoạch khảo sát 19–20/08/2026, hướng dẫn chuẩn bị, 7 phiếu theo phòng, khoa, viện, hội đồng.
- 68 nghiệp vụ gợi ý (không tính 6 dòng "nghiệp vụ khác" để trống): TC&QT 12, Đào tạo 12, TT&TS 10, KHCN&HTPT 10, Viện 10, Hội đồng 9, Khoa 5 nhóm.
- Cột "người thực hiện" và "các bước xử lý" còn là chữ hướng dẫn mặc định, nên **phiếu chưa được điền**.

**Website https://www.is.vnu.edu.vn (đọc 10/10/2026, qua công cụ tóm tắt trang):**
- Cơ cấu khớp với Excel: 4 phòng, 6 khoa, 1 viện, 1 hội đồng; trực thuộc ĐHQGHN; 3 cơ sở.
- 5 mô hình đào tạo: ĐHQGHN cấp bằng, liên kết quốc tế, song bằng, tích hợp cử nhân–thạc sĩ, dự bị (và mô hình 2+2).
- Tuyển sinh 2026: 4 phương thức, 130 chỉ tiêu xét tuyển trực tiếp chương trình liên kết nước ngoài cấp bằng.
- Nhiều hệ thống số: E-Office, LMS, cổng sinh viên, cổng việc làm, tra cứu văn bằng, thư viện, nền tảng AI tư vấn tuyển sinh.

**Skill TC&QT do người dùng cung cấp:** dùng ký hiệu số `…/TQT-TC&QT` và `…/BC-TC&QT`, ký "KT. HIỆU TRƯỞNG", công văn gửi ĐHQGHN qua đơn vị đầu mối.

## 2. Phát hiện đáng chú ý

1. **Website tự mâu thuẫn về số chương trình:** trang chủ 30; trang tuyển sinh 23 (và "15 chương trình"); trang đào tạo 17 + 8 + 2 = 27. Đây là ví dụ thật cho nhu cầu `vnuis-ts-ra-soat-nhat-quan-thong-tin` và nguyên tắc "một nguồn số liệu duy nhất" (C4).
2. **Đơn vị kiêm nhiệm:** nhiều Phó Hiệu trưởng kiêm Trưởng phòng; giao việc và phê duyệt phải gắn với *vai trò*, nếu không sẽ lẫn.
3. **Phòng Đào tạo gộp nhiều mảng từ 2025** (đào tạo, sau đại học, công tác sinh viên, khảo thí, đảm bảo chất lượng): không có phòng CTSV riêng, nên các skill về người học và khảo thí đều quy về Phòng Đào tạo.
4. **Chương trình liên kết và song bằng có căn cứ khác nhau:** skill gốc viết cho "trường đại học" nói chung, dễ áp nhầm quy chế của loại này cho loại khác.
5. **Hội đồng KH&ĐT có đại diện ĐHQGHN làm Chủ tịch:** ảnh hưởng đến người ban hành và ký các nghị quyết, kết luận.
6. **Đã có nền tảng AI tư vấn tuyển sinh:** skill FAQ và kịch bản phải trùng nguồn với nền tảng đó, không tạo nguồn thứ hai mâu thuẫn.

## 3. Suy luận (đã dùng khi thiết kế, cần kiểm tra)

- Hầu hết nghiệp vụ trong phiếu khớp với skill gốc về tên và mục đích. Tôi ghép theo tên và mô tả, chưa đọc kỹ từng skill gốc để kiểm tra phạm vi.
- Điểm nghẽn chung ở mọi phiên (tài liệu phân tán, đối chiếu thủ công, dễ bỏ sót) là phần phiếu CES tự gợi ý, không phải lời của đơn vị.
- Thứ tự căn cứ pháp lý cần đặt quy định của ĐHQGHN trên quy định chung; tôi đề xuất như vậy nhưng chưa có văn bản để kiểm.

## 4. Giả định cần xác nhận

Xem C1–C8 trong `docs/CAU_HOI_CAN_XAC_NHAN.md`. Ba điểm rủi ro cao nhất: thẩm quyền ký (C1), quy chế riêng cho chương trình liên kết (C2), chính sách dữ liệu khi dùng AI (C5).

## 5. Phạm vi đã chọn (theo xác nhận của người dùng)

- v0.1: lớp ngữ cảnh dùng chung + 33 skill chỉnh sâu + 8 skill mới.
- v0.2 (gộp): thêm 119 skill chỉnh sâu (toàn bộ 116 skill áp dụng được và 3 skill chuyển từ nhóm chưa chắc: kế hoạch thanh tra năm, kết luận thanh tra, kế hoạch đoàn ra vào) và 7 skill mới. 19 skill gốc chưa đưa vào, chờ khảo sát xác nhận.
- Đóng gói .zip để bàn giao nội bộ CES, không đẩy lên GitHub.
- v0.3: đặt lại tên theo nhóm nghiệp vụ, thay tên đơn vị của bộ gốc bằng đơn vị thực của VNU-IS, điền sẵn thông tin đã xác định, chuẩn hóa tiêu đề mục.
- Dữ liệu thật chưa có; đầu ra là bản v0.3.

## 6. Rủi ro còn lại

- **Dễ thành "skill chung đổi nhãn"** nếu không bổ sung dữ liệu khảo sát. Mục "Điều chỉnh khi dùng cho VNU-IS" cố gắng cụ thể từ website, nhưng độ sâu nghiệp vụ thật chỉ có sau khảo sát.
- **Thông tin trên website có thể lỗi thời hoặc tự mâu thuẫn**; mọi con số tuyển sinh, người học, việc làm trong gói chỉ dùng để nhận diện, không để đưa vào văn bản.
- **Dữ liệu cá nhân:** danh sách nhân sự trong Excel đã không đưa vào gói; skill chỉ nêu chức danh.
- **Giới hạn kiểm tra:** bộ kiểm tra chỉ xác nhận cấu trúc đóng gói, không xác nhận chất lượng nghiệp vụ hay tính đúng pháp lý.

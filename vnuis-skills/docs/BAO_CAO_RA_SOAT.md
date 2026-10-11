# Báo cáo rà soát và xử lý (gói v0.4.1, 11/10/2026)

Báo cáo này ghi lại đợt rà soát chi tiết 167 skill ngày 11/10/2026 và những gì đã sửa. Phạm vi rà soát: quét tự động toàn bộ skill, trích và tra một số văn bản pháp lý then chốt, đọc kỹ một số skill rủi ro cao. **Chưa** đọc từng dòng cả 167 skill, chưa kiểm tra đúng/sai nghiệp vụ từng bước, chưa đối chiếu văn bản nội bộ của VNU-IS/ĐHQGHN, chưa tra hiệu lực khoảng 65 văn bản pháp lý còn lại.

Mức tin cậy: **ĐÃ KIỂM** = tự kiểm bằng quét file; **NGUỒN THỨ CẤP** = trang tổng hợp pháp luật, chưa đối chiếu văn bản gốc; **SUY LUẬN** = cần Trường xác nhận.

## Đã xử lý

| Mã | Vấn đề | Cách xử lý | Mức tin cậy |
|---|---|---|---|
| N1 | Gói dẫn Luật GDĐH 2012/2018 là căn cứ còn hiệu lực; chưa có Luật 125/2025/QH15 (hiệu lực 01/01/2026) và TT 58/2026/TT-BGDĐT | Thêm hai mục vào `phap-ly.md` của 27 skill thuộc nhóm đào tạo, sau đại học, khảo thí, công tác sinh viên, ĐBCL, hội đồng, hợp tác quốc tế, pháp chế, tuyển sinh, khoa; thay dẫn cũ trong thân 34 file | NGUỒN THỨ CẤP |
| N2 | 166 skill dặn "không dùng tên thật của trường/cá nhân" (mâu thuẫn với thông tin Trường điền sẵn) | Thay bằng: ví dụ chỉ để minh họa, không đưa dữ liệu cá nhân thật; tên Trường theo bảng điền sẵn | ĐÃ KIỂM |
| N3 | Tuyến báo cáo, tuyến duyệt ghi cứng "gửi Bộ GD&ĐT" ở 7 skill | Đổi thành "cơ quan tiếp nhận (ĐHQGHN hoặc Bộ GD&ĐT, chờ C2)"; skill mở ngành thêm ghi chú theo Điều 21, 24 Luật 125/2025 | SUY LUẬN |
| (mới) | Hội đồng KH&ĐT chỉ còn tư vấn (Điều 18); hội đồng trường công lập chấm dứt từ 01/01/2026 (Điều 46) | Thêm ghi chú vào 5 skill hội đồng; "Hội đồng có thẩm quyền (C6)" đổi thành "cấp có thẩm quyền (C6)"; C2, C6 cập nhật nội dung cần xác nhận | NGUỒN THỨ CẤP |
| V1 | 19 skill ghi mục kiểm cổng duyệt khác chuẩn | Thống nhất thành "Đã qua Human gate: ..." ở cả 167 skill | ĐÃ KIỂM |
| V3 | Từ tiếng Anh còn sót (checklist, KPI, brief, ticket, SLA, rubric, helpdesk, PMO...) | Thay bằng tiếng Việt trong thân, mô tả, quy cách đầu ra, giao diện; mã định danh trong dấu `` ` `` và tên skill gốc giữ nguyên | ĐÃ KIỂM |
| V4 | 216 liên kết hỏng trong `quy-tac-chung.md` | Sửa đường dẫn; quét lại: 0 liên kết hỏng | ĐÃ KIỂM |
| V5 | Câu lặp "Hội đồng có thẩm quyền (C6)..." | Viết lại | ĐÃ KIỂM |
| V6 | SKILL.md ghi "phải tạo file" nhưng chạy qua API không tạo được file | Thêm chỉ dẫn chạy qua API (trả nội dung, ứng dụng xuất file) | ĐÃ KIỂM |
| R1 | Runner dùng mã `[CẦN BỔ SUNG]` trái quy tắc "chừa chỗ theo mẫu" | Sửa runner và bộ tự kiểm tra | ĐÃ KIỂM |
| R2 | Bộ biên dịch bỏ sót cổng duyệt của 19 skill, thiếu quy tắc cấm | Đã sửa; runner nay luôn kèm "Giới hạn chung" của từng skill | ĐÃ KIỂM |

## Đính chính so với báo cáo rà soát trước
- **V2 (110 skill "thiếu mục guardrails") nêu quá mức.** Mục "Giới hạn (guardrails)" chỉ có ở skill mà bộ gốc có quy tắc cấm riêng (ví dụ phân loại yêu cầu hỗ trợ CNTT); skill khác dùng mục "Giới hạn và human gate" chuẩn, có ở cả 167 skill. Không thêm quy tắc cấm bịa thêm; chỉ sửa bộ biên dịch để lấy các dòng "Không..." trong mục "Căn cứ & lưu ý".
- Con số "14 trong 19 skill" ở báo cáo trước sai; đúng là 11 trong 19 là skill văn phòng dùng chung.

## Còn lại (chưa xử lý được)
1. **Chưa đọc toàn văn** Luật 125/2025/QH15, Điều 46 chỉ nắm qua bản tóm tắt; chưa đọc nghị định hướng dẫn về cấp phép/mở ngành, quy chế/điều lệ ĐHQGHN và VNU-IS. `phap-ly.md` đã ghi rõ giới hạn này.
2. **Chưa xác minh hiệu lực**: TT 16/2015 (đánh giá rèn luyện), TT 04/2016, TT 08/2021, 23/2021, 18/2021 (quy chế đào tạo), NĐ 13/2012 (sáng kiến) và khoảng 60 văn bản khác trong `phap-ly.md`.
3. **Tuyến báo cáo, tuyến duyệt, thẩm quyền mở ngành** của VNU-IS: chờ C2, C6. Mọi chỗ đã sửa chỉ là bỏ giả định cứng, chưa phải kết luận.
4. **Thời hạn nộp báo cáo năm (15/01)** trong skill KHCN: giữ ghi chú "bản gốc ghi, chưa xác minh cho VNU-IS".
5. Còn vài thuật ngữ nghề truyền thông (hashtag, SMART...) và tiêu đề mục chuẩn (Input, Workflow, Human gate, guardrails) giữ nguyên vì bộ kiểm tra cấu trúc yêu cầu.
6. File `references/quy-trinh-lich-su.md` là bản lưu quy trình gốc, giữ nguyên căn cứ cũ và đã ghi rõ "không phải quy trình hiện hành".
7. Chưa chạy skill với model thật; điểm router đo trên bộ câu hỏi do người soạn gói tự viết.
8. 21 skill có cấu trúc đầu ra dưới 4 mục chưa được đánh giá là đủ hay thiếu.

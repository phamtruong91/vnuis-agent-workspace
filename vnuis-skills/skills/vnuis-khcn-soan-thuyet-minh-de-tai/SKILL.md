---
name: "vnuis-khcn-soan-thuyet-minh-de-tai"
description: "Dùng khi chủ nhiệm đề tài chuẩn bị hồ sơ đăng ký hoặc bảo vệ trước hội đồng xét duyệt và cần soạn thuyết minh đề tài NCKH: tính cấp thiết, mục tiêu, nội dung, sản phẩm, kinh phí, tiến độ."
---

# Soạn thuyết minh đề tài NCKH

## Khi nào dùng
Khi chủ nhiệm đề tài (hoặc Phòng KHCN&HTPT hỗ trợ) cần soạn bản thuyết minh đề tài NCKH
để nộp hồ sơ đăng ký, bảo vệ trước hội đồng xét duyệt các cấp (cấp trường, cấp bộ,
cấp nhà nước). Thuyết minh là căn cứ để hội đồng đánh giá, phê duyệt và sau này
ký hợp đồng thực hiện đề tài.

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

**Chạy qua API (không có công cụ tạo file):** trả đủ nội dung dạng văn bản có tiêu đề, bảng; ứng dụng gọi sẽ xuất file.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Khi người dùng yêu cầu bộ slide (.pptx), đọc mục “Xuất PowerPoint (.pptx) khi được yêu cầu” trong quy cách đầu ra.

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Bối cảnh riêng của VNU-IS

Bản chỉnh cho Trường Quốc tế – ĐHQGHN (VNU-IS), v0.4.2. Dựng từ website công khai và phiếu khảo sát CES còn trống; **chưa có dữ liệu khảo sát thực tế của đơn vị**. Đọc [bối cảnh VNU-IS](references/boi-canh-vnuis.md) trước khi chạy; các mã C1–C8 nằm ở mục 6 của file đó.

- **Đơn vị thường dùng:** Phòng KHCN và Hợp tác phát triển; các khoa, nhóm nghiên cứu.
- **Nghiệp vụ trong phiếu CES:** "Quản lý đề tài: Tiếp nhận và kiểm tra hồ sơ đề xuất đề tài" (sheet `06_KS_KHCN_HTPT`). Tần suất gợi ý: Theo hồ sơ/vụ việc. Đầu vào gợi ý: Thuyết minh; biểu mẫu; tiêu chí; hồ sơ chủ nhiệm. Khó khăn gợi ý: Tài liệu phân tán, nhiều định dạng; Đọc và đối chiếu thủ công mất thời gian; Dễ thiếu thành phần, sai logic hoặc bỏ sót ngoại lệ; Đầu ra phụ thuộc kinh nghiệm từng cá nhân. Đây là gợi ý có sẵn của CES, chưa phải xác nhận của đơn vị.

**Điều chỉnh khi dùng cho VNU-IS**
- Website phân đề tài theo cấp: Nhà nước hoặc Bộ, ĐHQGHN, tỉnh hoặc thành phố, cơ sở. Kiểm tra hồ sơ theo biểu mẫu của đúng cấp; không dùng chung biểu mẫu.
- Phân biệt đề tài giảng viên và nghiên cứu khoa học sinh viên (website có mục NCKH sinh viên và câu lạc bộ sinh viên nghiên cứu).
- Hồ sơ chủ nhiệm: kiểm tra điều kiện theo biểu mẫu của cấp đề tài; không tự suy ra điều kiện.
- Đề tài quốc tế có thể viết thuyết minh bằng tiếng Anh: giữ bản gốc và ghi ngôn ngữ.

**Chờ xác nhận khi khảo sát**
- Biểu mẫu từng cấp và quy chế quản lý đề tài (C2, C8).
- Người xét duyệt sơ bộ (C6).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_de_tai` | Tên đầy đủ của đề tài | Có |
| `cap_de_tai` | Cấp trường / Cấp bộ (tỉnh) / Cấp nhà nước | Có |
| `chu_nhiem` | Họ tên, học hàm/học vị chủ nhiệm đề tài | Có |
| `co_quan_chu_tri` | Đơn vị chủ trì (khoa/viện/trung tâm) | Có |
| `thanh_vien` | Danh sách thành viên tham gia chính | Không |
| `thoi_gian_thuc_hien` | Tổng thời gian (tháng), từ tháng/năm đến tháng/năm | Có |
| `tong_kinh_phi` | Tổng kinh phí dự kiến (đồng) | Có |
| `y_tinh_cap_thiet` | Các ý chính về thực trạng, khoảng trống nghiên cứu, ý nghĩa | Có |
| `muc_tieu` | Mục tiêu chung và các mục tiêu cụ thể | Có |
| `noi_dung_nghien_cuu` | Các nội dung/mảng công việc nghiên cứu | Có |
| `phuong_phap` | Phương pháp luận, phương pháp thu thập và xử lý dữ liệu, phạm vi | Có |
| `san_pham_du_kien` | Sản phẩm khoa học, ứng dụng, đào tạo dự kiến | Có |
| `du_toan_kinh_phi` | Chi tiết kinh phí theo từng khoản mục | Có |
| `tien_do` | Các mốc thời gian theo giai đoạn, gắn sản phẩm | Có |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Phòng KHCN và Hợp tác phát triển; các khoa, nhóm nghiên cứu |
| Cơ sở | Xuân Thủy (Cầu Giấy); Phan Tây Nhạc (Xuân Phương); Hòa Lạc (tòa HT1, Khu Đô thị ĐHQGHN). Ghi rõ cơ sở khi nội dung gắn địa điểm |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Hệ thống nguồn dữ liệu có trên website | Kho tài nguyên số; E-Office. Skill không kết nối hệ thống, chỉ dùng file xuất/tải lên (C5) |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Xác định cấp đề tài và chọn biểu mẫu**
- Làm gì: đọc `cap_de_tai` để chọn biểu mẫu thuyết minh tương ứng (cấp càng cao yêu cầu càng chi tiết); lập khối thông tin hành chính: `ten_de_tai`, `chu_nhiem`, `thanh_vien`, `co_quan_chu_tri`, `thoi_gian_thuc_hien`, `tong_kinh_phi` (ghi cả số và chữ); tra cứu danh mục đề tài của trường để kiểm tra tên đề tài không trùng với đề tài đã/đang thực hiện.
- Dùng input: `cap_de_tai`, `ten_de_tai`, `chu_nhiem`, `thanh_vien`, `co_quan_chu_tri`, `thoi_gian_thuc_hien`, `tong_kinh_phi`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: tra cứu biểu mẫu đúng cấp và kiểm tra trùng tên đề tài · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: tên đề tài phải ngắn gọn, nêu rõ đối tượng + phạm vi + yếu tố mới; tránh tên quá chung chung hoặc quá dài khó nhớ.
- → Kết quả bước: khối thông tin hành chính + biểu mẫu đã chọn đúng cấp đề tài.

**Bước 2. Viết mục 1 – Tính cấp thiết**
- Làm gì: từ `y_tinh_cap_thiet` viết 4 ý theo thứ tự: (a) thực trạng vấn đề (kèm số liệu minh họa); (b) tổng quan trong và ngoài nước ngắn gọn → chỉ ra khoảng trống nghiên cứu; (c) lý do phải nghiên cứu ngay; (d) ý nghĩa khoa học và ý nghĩa thực tiễn.
- Dùng input: `y_tinh_cap_thiet`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: soạn dự thảo từ ý chính · ⏱ ~45–60 phút (ước tính)
- Lưu ý nghiệp vụ: bẫy thường gặp — viết dài dòng như tổng quan luận văn; hội đồng chỉ cần thấy rõ "khoảng trống" và "tại sao là bây giờ"; mỗi ý viết 1 đoạn ngắn.
- → Kết quả bước: dự thảo mục 1 – Tính cấp thiết.

**Bước 3. Viết mục 2 – Mục tiêu nghiên cứu**
- Làm gì: từ `muc_tieu` viết 01 mục tiêu chung + 3–5 mục tiêu cụ thể, diễn đạt theo nguyên tắc SMART (cụ thể, đo lường được, khả thi); đánh số các mục tiêu cụ thể để đối chiếu ở các mục sau.
- Dùng input: `muc_tieu`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: diễn đạt theo SMART và đánh số · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi mục tiêu cụ thể phải đo lường được (có con số: ≥85%, 5.000 mẫu, 03 HTX); tránh viết mục tiêu dạng hoạt động ("tiến hành thu thập...") thay vì kết quả cần đạt.
- → Kết quả bước: dự thảo mục 2 – Mục tiêu (chung + cụ thể đã đánh số).

**Bước 4. Viết mục 3 – Nội dung nghiên cứu**
- Làm gì: từ `noi_dung_nghien_cuu` chia thành các nội dung đánh số (Nội dung 1, 2, 3...); mỗi nội dung mô tả công việc cụ thể và ghi rõ "phục vụ mục tiêu cụ thể số mấy" (đối chiếu với kết quả bước 3).
- Dùng input: `noi_dung_nghien_cuu`, kết quả bước 3.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: chia nội dung và gắn mục tiêu tương ứng · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: nguyên tắc 1–1 — mỗi mục tiêu cụ thể phải có ít nhất 01 nội dung đáp ứng; nội dung nào không gắn với mục tiêu nào là thừa, cần cắt bỏ.
- → Kết quả bước: dự thảo mục 3 – Nội dung nghiên cứu (mỗi nội dung đã gắn mục tiêu tương ứng).

**Bước 5. Viết mục 4 – Phương pháp nghiên cứu**
- Làm gì: từ `phuong_phap` viết 4 ý: cách tiếp cận/phương pháp luận; phương pháp thu thập dữ liệu; phương pháp xử lý/phân tích; đối tượng và phạm vi nghiên cứu (không gian, thời gian).
- Dùng input: `phuong_phap`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: soạn dự thảo 4 ý · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: phải đủ chi tiết để người khác có thể lặp lại nghiên cứu; ghi rõ công cụ/phần mềm sử dụng và phương pháp đánh giá (VD: kiểm chứng chéo k-fold).
- → Kết quả bước: dự thảo mục 4 – Phương pháp nghiên cứu.

**Bước 6. Viết mục 5 – Sản phẩm dự kiến**
- Làm gì: từ `san_pham_du_kien` liệt kê theo 3 nhóm: (a) sản phẩm khoa học (bài báo, báo cáo, sáng chế); (b) sản phẩm ứng dụng (quy trình, phần mềm, mô hình); (c) sản phẩm đào tạo (thạc sĩ, sinh viên NCKH); mỗi sản phẩm ghi rõ số lượng và yêu cầu chất lượng; đối chiếu: mỗi nội dung ở bước 4 phải cho ra ít nhất 01 sản phẩm.
- Dùng input: `san_pham_du_kien`, kết quả bước 4.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: liệt kê theo 3 nhóm và đối chiếu với nội dung · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: yêu cầu chất lượng phải cụ thể ("tạp chí trong nước có phản biện", không ghi chung chung "bài báo"); số lượng sản phẩm phải tương xứng với kinh phí và thời gian thực hiện.
- → Kết quả bước: dự thảo mục 5 – Sản phẩm dự kiến (3 nhóm, có số lượng + yêu cầu chất lượng).

**Bước 7. Lập mục 6 – Dự toán kinh phí chi tiết**
- Làm gì: từ `du_toan_kinh_phi` lập bảng các khoản mục (thuê khoán nhân công, vật tư/thiết bị, hội thảo, công tác phí, quản lý phí, dự phòng...), mỗi khoản mục ghi nội dung chi và thành tiền; cộng tổng và đối chiếu phải khớp `tong_kinh_phi` đúng từng đồng; kiểm tra tỷ lệ các khoản mục không vượt định mức (VD: quản lý phí khoảng 10%).
- Dùng input: `du_toan_kinh_phi`, `tong_kinh_phi`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: lập bảng, tính tổng và kiểm tra định mức · ⏱ ~45–60 phút (ước tính)
- Lưu ý nghiệp vụ: bẫy hay gặp — cộng tổng sai do làm tròn; quản lý phí vượt trần quy định; khoản "dự phòng" bị cắt ở một số cấp đề tài — kiểm tra quy định của cấp đề tài trước khi chốt.
- → Kết quả bước: dự thảo mục 6 – Dự toán kinh phí (bảng chi tiết, tổng khớp từng đồng).

**Bước 8. Lập mục 7 – Tiến độ thực hiện**
- Làm gì: từ `tien_do` lập bảng theo quý (hoặc 6 tháng); mỗi giai đoạn ghi công việc và sản phẩm hoàn thành; kiểm tra: tổng số quý phải bằng `thoi_gian_thuc_hien` (VD: 24 tháng = 8 quý), mốc cuối cùng phải là nghiệm thu; mỗi sản phẩm ở bước 6 phải xuất hiện trong ít nhất 01 mốc tiến độ.
- Dùng input: `tien_do`, `thoi_gian_thuc_hien`, kết quả bước 6.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: lập bảng theo quý và gắn sản phẩm · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: tiến độ phải chừa thời gian viết báo cáo tổng kết và nghiệm thu ở quý cuối; không dồn toàn bộ sản phẩm vào 1–2 quý cuối.
- → Kết quả bước: dự thảo mục 7 – Tiến độ thực hiện (bảng theo quý, gắn sản phẩm, mốc cuối là nghiệm thu).

**Bước 9. Kiểm tra tính logic xuyên suốt**
- Làm gì: lập bảng kiểm đối chiếu 6 chiều: mục tiêu ↔ nội dung ↔ phương pháp ↔ sản phẩm ↔ kinh phí ↔ tiến độ; đánh dấu từng ô khớp/không khớp; sửa các điểm lệch rồi mới chuyển sang bước 10.
- Dùng input: kết quả bước 2–8.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: đối chiếu logic 6 chiều và đánh dấu điểm lệch cần sửa · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: 3 lỗi phổ biến nhất — (1) sản phẩm không có nội dung nào tạo ra; (2) kinh phí cho khoản mục không có trong nội dung; (3) tiến độ không đủ thời gian cho nội dung đã đăng ký.
- → Kết quả bước: bảng kiểm logic 6 chiều đã khớp + danh sách điểm đã sửa.

**Bước 10. Hoàn thiện và xuất bản**
- Làm gì: kiểm tra chính tả, số liệu, tính khả thi lần cuối; trình chủ nhiệm ký duyệt; xuất thuyết minh hoàn chỉnh file theo định dạng đầu ra của skill, sẵn sàng in/xuất file Word.
- Dùng input: kết quả bước 9, `chu_nhiem`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: chuẩn bị hồ sơ trình ký, nhắc lịch và theo dõi tiến độ · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: sau khi chủ nhiệm ký, mọi thay đổi phải có văn bản điều chỉnh — không sửa tay vào bản đã ký.
- → Kết quả bước: bản thuyết minh hoàn chỉnh đã ký duyệt + bảng kiểm logic.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Đầu vào"/] --> B1["Bước 1: Xác định cấp đề tài và chọn biểu mẫu"]
    B1 --> B2["Bước 2: Viết mục 1 – Tính cấp thiết"]
    B2 --> B3["Bước 3: Viết mục 2 – Mục tiêu nghiên cứu"]
    B3 --> B4["Bước 4: Viết mục 3 – Nội dung nghiên cứu"]
    B4 --> B5["Bước 5: Viết mục 4 – Phương pháp nghiên cứu"]
    B5 --> B6["Bước 6: Viết mục 5 – Sản phẩm dự kiến"]
    B6 --> B7["Bước 7: Lập mục 6 – Dự toán kinh phí chi tiết"]
    B7 --> B8["Bước 8: Lập mục 7 – Tiến độ thực hiện"]
    B8 --> B9["Bước 9: Kiểm tra tính logic xuyên suốt"]
    B9 --> B10["Bước 10: Hoàn thiện và xuất bản"]
    B10 --> HG["👤 Bước 10: Chủ nhiệm ký duyệt"]
    HG --> OUT[["Thuyết minh hoàn chỉnh và bảng kiểm logic"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Số liệu trong output khớp Input: tổng kinh phí (số + chữ) = `tong_kinh_phi`; tổng các khoản mục dự toán khớp từng đồng; số quý tiến độ = `thoi_gian_thuc_hien`
- [ ] Không bịa đặt số liệu, công trình công bố, trích dẫn tài liệu
- [ ] Đúng biểu mẫu thuyết minh của cấp đề tài; bảng dự toán và tiến độ trình bày rõ ràng
- [ ] Căn cứ pháp lý đầy đủ, còn hiệu lực (quy chế quản lý đề tài cấp trường / biểu mẫu của Bộ chủ quản)
- [ ] Tính logic xuyên suốt: mỗi mục tiêu cụ thể có ít nhất 01 nội dung đáp ứng; mỗi nội dung cho ra ít nhất 01 sản phẩm; bảng kiểm logic 6 chiều đã khớp
- [ ] Mục tiêu cụ thể viết theo SMART, đo lường được; tên đề tài không trùng đề tài đã/đang thực hiện
- [ ] Dự toán tuân thủ định mức chi hiện hành và trần kinh phí của cấp đề tài (quản lý phí, dự phòng đúng quy định)
- [ ] Đã qua Human gate: chủ nhiệm đề tài đã kiểm tra và ký duyệt

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Căn cứ & lưu ý
- Quy chế quản lý đề tài NCKH cấp trường của Trường Quốc tế – ĐHQGHN (giả lập);
  biểu mẫu thuyết minh của Bộ chủ quản đối với đề tài cấp bộ/nhà nước.
- Mục tiêu cụ thể nên viết theo SMART; tránh mục tiêu chung chung, không đo lường được.
- Dự toán kinh phí phải tuân thủ định mức chi hiện hành và khớp với định mức của cấp đề tài.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `thuyet-minh-de-tai-nckh` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

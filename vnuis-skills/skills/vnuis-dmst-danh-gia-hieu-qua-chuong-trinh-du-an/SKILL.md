---
name: "vnuis-dmst-danh-gia-hieu-qua-chuong-trinh-du-an"
description: "Dùng khi chương trình, khóa bồi dưỡng, dự án hoặc đợt thử nghiệm đã xong và cần đánh giá bằng số liệu: so chỉ số cam kết với kết quả thực tế, phản hồi người tham gia, chi phí, bài học."
---

# Đánh giá hiệu quả chương trình hoặc dự án

## Khi nào dùng
Khi chương trình, khóa bồi dưỡng, dự án hoặc thử nghiệm kết thúc và cần đánh giá bằng số liệu thay vì cảm nhận.

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

**Chạy qua API (không có công cụ tạo file):** trả đủ nội dung dạng văn bản có tiêu đề, bảng; ứng dụng gọi sẽ xuất file.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Khi người dùng yêu cầu bộ slide (.pptx), đọc mục “Xuất PowerPoint (.pptx) khi được yêu cầu” trong quy cách đầu ra.

Khi báo cáo có số liệu cần so sánh hoặc nêu xu hướng, đọc mục “Biểu đồ và hình trong báo cáo số liệu” trong quy cách đầu ra trước khi vẽ.

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Bối cảnh riêng của VNU-IS

Skill mới cho Trường Quốc tế – ĐHQGHN (VNU-IS), v0.4.2. Dựng từ website công khai và phiếu khảo sát CES còn trống; **chưa có dữ liệu khảo sát thực tế của đơn vị**. Đọc [bối cảnh VNU-IS](references/boi-canh-vnuis.md) trước khi chạy; các mã C1–C8 nằm ở mục 6 của file đó.

- **Đơn vị thường dùng:** Viện ĐMST&CGCN; Phòng KHCN và Hợp tác phát triển.
- **Nghiệp vụ trong phiếu CES:** "Đánh giá hiệu quả: Tổng hợp chỉ số đánh giá, phản hồi và bài học sau chương trình/dự án" (sheet `08_KS_Vien_DMST_CGCN`). Tần suất gợi ý: Cuối kỳ/dự án. Đầu vào gợi ý: chỉ số đánh giá kế hoạch; dữ liệu triển khai; phiếu phản hồi; minh chứng; chi phí. Khó khăn gợi ý: Dữ liệu nhiều định dạng; khó đối chiếu trước–sau và truy xuất nguồn.

**Chờ xác nhận khi khảo sát**
- Chỉ số và cách đo của các chương trình đang chạy (C4, C8).
- Mẫu báo cáo đánh giá (C8).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `muc_tieu_chi_so` | Mục tiêu và chỉ số cam kết ban đầu, kèm cách đo | Có |
| `ket_qua_thuc_te` | Số liệu thực tế: số người tham gia, sản phẩm bàn giao, kết quả đo | Có |
| `phan_hoi` | Khảo sát hoặc ý kiến người tham gia | Không |
| `chi_phi` | Chi phí thực tế và nguồn | Không |
| `ky_danh_gia` | Thời gian chương trình và mốc đánh giá | Có |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Viện ĐMST&CGCN; Phòng KHCN và Hợp tác phát triển |
| Cơ sở | Xuân Thủy (Cầu Giấy); Phan Tây Nhạc (Xuân Phương); Hòa Lạc (tòa HT1, Khu Đô thị ĐHQGHN). Ghi rõ cơ sở khi nội dung gắn địa điểm |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Chốt chỉ số và cách đo**
- Làm gì: Liệt kê chỉ số cam kết; chỉ số nào không có cách đo hoặc số liệu thì ghi "không đánh giá được".
- Dùng input: `muc_tieu_chi_so`, `ky_danh_gia`
- Vai trò: Quản lý chương trình · AI hỗ trợ: lập bảng chỉ số · ⏱ thời gian do đơn vị ước tính sau khảo sát
- Lưu ý nghiệp vụ: Không bổ sung chỉ số sau khi đã có kết quả.
- → Kết quả bước: Bảng chỉ số đánh giá.

**Bước 2. Đối chiếu mục tiêu và kết quả**
- Làm gì: Tính chênh lệch từng chỉ số; nêu đạt, một phần, chưa đạt theo ngưỡng cam kết.
- Dùng input: `ket_qua_thuc_te`
- Vai trò: Quản lý chương trình · AI hỗ trợ: tính chênh lệch · ⏱ thời gian do đơn vị ước tính sau khảo sát
- Lưu ý nghiệp vụ: Không tự hạ ngưỡng để thành đạt.
- → Kết quả bước: Bảng đạt hay chưa đạt.

**Bước 3. Tổng hợp phản hồi và chi phí**
- Làm gì: Gom phản hồi theo chủ đề và đếm; chi phí trên đầu người chỉ tính khi có cả hai số.
- Dùng input: `phan_hoi`, `chi_phi`
- Vai trò: Quản lý chương trình · AI hỗ trợ: phân nhóm phản hồi · ⏱ thời gian do đơn vị ước tính sau khảo sát
- Lưu ý nghiệp vụ: Cỡ mẫu nhỏ thì nêu rõ, không khái quát.
- → Kết quả bước: Bảng phản hồi và chi phí.

**Bước 4. Lập báo cáo và bài học**
- Làm gì: Ghép báo cáo: kết quả, nguyên nhân người phụ trách xác nhận, bài học, đề xuất tiếp theo.
- Dùng input: `ket_qua_thuc_te`, `phan_hoi`
- Vai trò: Trưởng đơn vị · AI hỗ trợ: dự thảo báo cáo · ⏱ thời gian do đơn vị ước tính sau khảo sát
- Lưu ý nghiệp vụ: Nguyên nhân do người phụ trách xác nhận; AI chỉ nêu giả thuyết có gắn nhãn.
- → Kết quả bước: Báo cáo đánh giá hiệu quả.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/Đầu vào của đơn vị/] --> B1["Bước 1. Chốt chỉ số và cách đo"]
    B1 --> B2["Bước 2. Đối chiếu mục tiêu và kết quả"]
    B2 --> B3["Bước 3. Tổng hợp phản hồi và chi phí"]
    B3 --> B4["Bước 4. Lập báo cáo và bài học"]
    B4 --> G["👤 Người có thẩm quyền duyệt"] --> Z[/Đánh giá hiệu quả chương trình hoặc dự án/]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Mọi chỉ số trong báo cáo có trong bảng chỉ số ban đầu.
- [ ] Chỉ số không đo được được ghi rõ.
- [ ] Cỡ mẫu phản hồi được nêu.
- [ ] Nguyên nhân được tách khỏi số liệu.
- [ ] Đã qua Human gate.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Human gate (người kiểm duyệt)
- **Trưởng đơn vị chủ trì** kiểm tra số liệu và kết luận.
- **Lãnh đạo có thẩm quyền** duyệt nếu báo cáo gửi ra ngoài.

## Giới hạn (guardrails)
- KHÔNG tự đổi chỉ số hoặc ngưỡng đạt.
- KHÔNG kết luận nguyên nhân khi người phụ trách chưa xác nhận.

## Căn cứ & lưu ý
- Căn cứ pháp lý và quy định nội bộ do người dùng cung cấp; chưa có thì ghi `[CẦN XÁC MINH]`, không suy diễn.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11); hồ sơ tại [references/version.json](references/version.json). Skill mới, không có bản gốc trong bộ 171 skill; dùng khung và quy cách đầu ra của skill `hop-nhat-bao-cao-don-vi`.
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ, chờ khảo sát; kiểm tra pháp lý trước thực thi.
- Giấy phép theo LICENSE của kho (bản quyền CES Global).

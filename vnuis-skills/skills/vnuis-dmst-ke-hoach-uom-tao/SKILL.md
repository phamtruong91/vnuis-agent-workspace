---
name: "vnuis-dmst-ke-hoach-uom-tao"
description: "Dùng khi Viện tổ chức đợt ươm tạo đổi mới sáng tạo (startup của sinh viên, giảng viên, dự án khởi nghiệp) và cần kế hoạch: tiêu chí tuyển chọn, lộ trình theo giai đoạn, nguồn lực, chỉ tiêu đầu ra."
---

# Kế hoạch ươm tạo ĐMST

## Khi nào dùng
Khi Viện ĐMST & CGCN tổ chức chương trình ươm tạo (startup sinh viên, giảng viên, dự án spin-off):
cần kế hoạch gồm tiêu chí tuyển chọn, lộ trình các giai đoạn, nguồn lực hỗ trợ và chỉ tiêu đầu ra.

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

- **Đơn vị thường dùng:** Viện ĐMST&CGCN.
- **Nghiệp vụ trong phiếu CES:** "Ươm tạo – hỗ trợ dự án: Theo dõi hồ sơ, cố vấn, mốc phát triển và kết quả của dự án/nhóm khởi nghiệp" (sheet `08_KS_Vien_DMST_CGCN`). Tần suất gợi ý: Theo chương trình. Đầu vào gợi ý: Hồ sơ dự án; kế hoạch; nhật ký cố vấn; chỉ số đánh giá; minh chứng kết quả. Khó khăn gợi ý: Cập nhật từ nhiều đầu mối; khó theo dõi cam kết, mốc và minh chứng. Đây là gợi ý có sẵn của CES, chưa phải xác nhận của đơn vị.

**Điều chỉnh khi dùng cho VNU-IS**
- Đối tượng ươm tạo có thể là sinh viên, giảng viên hoặc dự án bên ngoài; kế hoạch ghi rõ đối tượng và tiêu chí tuyển chọn cho từng nhóm.
- Theo phiếu CES: lập bảng theo dõi mốc, cam kết và minh chứng cho từng dự án (hồ sơ, kế hoạch, nhật ký cố vấn, chỉ số đánh giá).
- Không cam kết kinh phí, đầu tư hay khả năng gọi vốn khi chưa có phê duyệt.

**Chờ xác nhận khi khảo sát**
- Nguồn lực mentor, không gian, kinh phí hỗ trợ (C8).
- Quy chế chương trình ươm tạo của Viện (C2).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_chuong_trinh` | Tên chương trình ươm tạo + đợt/năm | Có |
| `doi_tuong` | Sinh viên / giảng viên / startup ngoài / hỗn hợp | Có |
| `linh_vuc_uu_tien` | Các lĩnh vực ưu tiên (VD: AI, nông nghiệp thông minh...) | Không |
| `nguon_luc` | Mentor, phòng lab, vốn mồi, hỗ trợ pháp lý... hiện có | Có |
| `thoi_gian` | Thời gian mỗi giai đoạn và toàn chương trình | Có |
| `chi_tieu` | Số lượng dự án tuyển, tỷ lệ tốt nghiệp mong muốn | Không |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Viện ĐMST&CGCN |
| Cơ sở | Xuân Thủy (Cầu Giấy); Phan Tây Nhạc (Xuân Phương); Hòa Lạc (tòa HT1, Khu Đô thị ĐHQGHN). Ghi rõ cơ sở khi nội dung gắn địa điểm |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Xây dựng bộ tiêu chí tuyển chọn và thang điểm**
- Làm gì: Thiết kế bộ tiêu chí chấm thang 100 điểm: tính đổi mới sáng tạo, tính khả thi
  kỹ thuật, năng lực đội ngũ, tiềm năng thị trường, phù hợp lĩnh vực ưu tiên; mỗi tiêu
  chí có trọng số và thang tiêu chí chấm mô tả các mức điểm để giám khảo chấm nhất quán; đặt ngưỡng
  trúng tuyển.
- Dùng input: `ten_chuong_trinh`, `doi_tuong`, `linh_vuc_uu_tien`, `chi_tieu` (số lượng
  tuyển → mức ngưỡng điểm phù hợp).
- Vai trò: Hội đồng tuyển chọn · AI hỗ trợ: soạn bộ tiêu chí, thang điểm và thang tiêu chí chấm dự thảo · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: trọng số phải phản ánh mục tiêu chương trình (ươm tạo trong trường
  thì coi trọng tính đổi mới + đội ngũ hơn doanh thu tức thì); thang tiêu chí chấm phải cụ thể, tránh
  tiêu chí định tính chung chung khó chấm.
- → Kết quả bước: Bộ tiêu chí + thang điểm 100 + thang tiêu chí chấm + ngưỡng trúng tuyển
  (dự thảo trình hội đồng ươm tạo duyệt).

**Bước 2. Thiết kế lộ trình ươm tạo theo giai đoạn**
- Làm gì: Chia chương trình thành 4 giai đoạn khớp `thoi_gian`: (1) Tuyển chọn — các mốc
  phát động/nhận hồ sơ/chấm/phỏng vấn/công bố; (2) Ươm tạo — hoàn thiện MVP, lịch đào tạo
  kỹ năng, mentor 1-1; (3) Tăng tốc — kết nối thị trường, tập gọi vốn; (4) Tốt nghiệp —
  demo day, đánh giá. Mỗi giai đoạn ghi: thời gian, mục tiêu đầu ra, tiêu chí "qua cửa"
  để sang giai đoạn tiếp theo.
- Dùng input: `thoi_gian`, `chi_tieu`, `doi_tuong`.
- Vai trò: Chuyên viên ươm tạo · AI hỗ trợ: thiết kế timeline 4 giai đoạn dự thảo, ban tổ chức chốt mốc và tiêu chí qua cửa · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: mỗi giai đoạn phải có "cửa kiểm tra" (gate) với tiêu chí rõ ràng —
  dự án không đạt thì dừng hỗ trợ hoặc kéo dài có điều kiện, tránh nuôi dự án không triển
  vọng; mốc thời gian phải chừa đệm cho tuyển chọn (thường 6–8 tuần).
- → Kết quả bước: Timeline chi tiết 4 giai đoạn (mốc thời gian, đầu ra, tiêu chí qua cửa).

**Bước 3. Phân bổ nguồn lực hỗ trợ**
- Làm gì: Từ `nguon_luc` hiện có: ghép mentor cho từng dự án theo lĩnh vực chuyên môn, lập
  lịch dùng lab/phòng làm việc chung, gói hỗ trợ pháp lý–kế toán (đăng ký doanh nghiệp,
  SHTT), thiết kế cơ chế giải ngân vốn mồi theo mốc (tỷ lệ % từng đợt gắn với chỉ số đánh giá giai đoạn).
- Dùng input: `nguon_luc`, `chi_tieu` (số dự án tuyển → chia nguồn lực cho vừa).
- Vai trò: Chuyên viên ươm tạo · AI hỗ trợ: lập bảng phân bổ nguồn lực dự thảo, ban tổ chức xác nhận mentor và lịch lab · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: vốn mồi giải ngân theo mốc đạt được, không cấp một lần; mentor phải
  cam kết thời gian tối thiểu (VD: 2 giờ/tuần/dự án); kiểm tra tổng cam kết không vượt
  nguồn lực thực có.
- → Kết quả bước: Bảng phân bổ nguồn lực (ghép mentor–dự án, lịch lab, lịch giải ngân
  vốn mồi theo mốc).

**Bước 4. Thiết lập chỉ số đánh giá và cơ chế đánh giá – tốt nghiệp**
- Làm gì: Đặt chỉ số đánh giá đầu ra định lượng (số dự án tốt nghiệp, số MVP hoàn thiện, số dự án gọi
  được vốn, việc làm tạo ra) gắn với `chi_tieu`; thiết kế tiêu chí đánh giá cuối kỳ,
  format demo day (thành phần ban giám khảo, thang điểm), chính sách hỗ trợ sau ươm tạo
  (mạng lưới alumni, ưu đãi dùng lab).
- Dùng input: `chi_tieu`, `thoi_gian`.
- Vai trò: Hội đồng tuyển chọn · AI hỗ trợ: đề xuất chỉ số đánh giá và quy chế đánh giá cuối kỳ · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chỉ số đánh giá phải đo được và có mốc thời gian; quy định rõ điều kiện "tốt
  nghiệp" so với "chưa đạt" và quyền lợi khác nhau của 2 nhóm.
- → Kết quả bước: Bộ chỉ số đánh giá đầu ra + quy chế đánh giá cuối kỳ, demo day và tốt nghiệp.

**Bước 5. Tổng hợp thành văn bản kế hoạch và trình phê duyệt**
- Làm gì: Ghép kết quả các bước 1–4 thành văn bản kế hoạch hoàn chỉnh theo cấu trúc chuẩn;
  kiểm tra tính khả thi tổng thể (nguồn lực có đủ cho số dự án tuyển không, tổng vốn mồi
  cam kết có vượt ngân sách không); trình hội đồng ươm tạo và viện trưởng phê duyệt.
- Dùng input: `ten_chuong_trinh`, `doi_tuong` (tiêu đề, đối tượng chương trình).
- Vai trò: Viện trưởng · AI hỗ trợ: ghép văn bản và kiểm tra chéo tính khả thi · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: kiểm tra chéo lần cuối — số mentor đủ cho số dự án, lịch lab không
  chồng chéo, mốc giải ngân khớp timeline; kế hoạch phải ban hành trước khi phát động
  tuyển chọn.
- → Kết quả bước: Văn bản kế hoạch chương trình ươm tạo hoàn chỉnh (trình phê duyệt).

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/Nhu cầu ươm tạo, nguồn lực hiện có/] --> B["Bước 1. Xây dựng bộ tiêu chí tuyển chọn và thang điểm"]
    B --> C["👤 Hội đồng ươm tạo duyệt bộ tiêu chí"]
    C --> D["Bước 2. Thiết kế lộ trình ươm tạo theo giai đoạn"]
    D --> E["Bước 3. Phân bổ nguồn lực hỗ trợ"]
    E --> F["Bước 4. Thiết lập chỉ số đánh giá và cơ chế đánh giá - tốt nghiệp"]
    F --> G["Bước 5. Tổng hợp thành văn bản kế hoạch và trình phê duyệt"]
    G --> H["👤 Viện trưởng phê duyệt kế hoạch"]
    H --> I[/Kế hoạch chương trình ươm tạo/]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Số liệu khớp với Input: số dự án tuyển, nguồn lực (mentor, lab, vốn mồi), thời gian.
- [ ] Không bịa đặt cam kết gọi vốn, cam kết đầu tư hay nguồn lực không có thật.
- [ ] Bộ tiêu chí thang 100 điểm có trọng số và thang tiêu chí chấm cụ thể cho từng mức điểm, ngưỡng trúng tuyển rõ ràng.
- [ ] Mỗi giai đoạn có "cửa kiểm tra" với tiêu chí qua cửa rõ ràng; dự án không đạt thì dừng hỗ trợ hoặc kéo dài có điều kiện.
- [ ] Tổng cam kết nguồn lực (mentor, lịch lab, vốn mồi giải ngân theo mốc) không vượt nguồn lực thực có.
- [ ] chỉ số đánh giá định lượng được, có mốc thời gian; quy định rõ điều kiện tốt nghiệp so với chưa đạt và quyền lợi khác nhau.
- [ ] Kế hoạch ban hành trước khi phát động tuyển chọn.
- [ ] Đã qua Human gate: hội đồng ươm tạo duyệt bộ tiêu chí, viện trưởng phê duyệt kế hoạch và danh sách trúng tuyển.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Human gate (người kiểm duyệt)
- **Hội đồng ươm tạo** chấm tuyển chọn và đánh giá tốt nghiệp theo thang điểm đã duyệt.
- **Viện trưởng** phê duyệt danh sách trúng tuyển và quyết định giải ngân vốn mồi theo mốc.

## Giới hạn (guardrails)
- KHÔNG cam kết khả năng gọi vốn thành công cho dự án ươm tạo.
- KHÔNG quyết định đầu tư/góp vốn thay mặt nhà trường khi chưa có phê duyệt thẩm quyền.
- KHÔNG tiết lộ ý tưởng/dữ liệu của dự án này cho dự án khác khi chưa được đồng ý.

## Căn cứ & lưu ý
- Quy chế hoạt động vườn ươm/cơ sở ươm tạo của trường (nếu có); quy định quản lý vốn mồi.
- Mọi số liệu trong ví dụ đều giả lập.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `ke-hoach-uom-tao-dmst` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

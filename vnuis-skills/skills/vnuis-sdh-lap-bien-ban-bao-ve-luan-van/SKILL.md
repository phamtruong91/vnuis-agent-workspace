---
name: "vnuis-sdh-lap-bien-ban-bao-ve-luan-van"
description: "Dùng ngay sau buổi bảo vệ luận văn thạc sĩ hoặc luận án tiến sĩ, khi thư ký hội đồng cần lập biên bản: diễn biến, phiếu đánh giá, kết luận đạt hay không, yêu cầu chỉnh sửa."
---

# Biên bản bảo vệ luận văn / luận án

## Khi nào dùng
Ngay sau khi kết thúc buổi bảo vệ luận văn thạc sĩ / luận án tiến sĩ: thư ký hội đồng tổng hợp
ghi chép diễn biến, phiếu đánh giá của từng thành viên để lập biên bản làm căn cứ ra quyết định
công nhận tốt nghiệp và cấp văn bằng.

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

- **Đơn vị thường dùng:** Phòng Đào tạo (sau đại học).
- **Nghiệp vụ trong phiếu CES:** không có dòng riêng trong phiếu CES; đề xuất theo chức năng đơn vị ở sheet 00 và cần xác nhận khi khảo sát.

**Điều chỉnh khi dùng cho VNU-IS**
- Biên bản ghi theo mẫu của đơn vị cấp bằng: Trường hoặc đối tác nước ngoài (C2).
- Hội đồng có thành viên nước ngoài: ghi ngôn ngữ bảo vệ.

**Chờ xác nhận khi khảo sát**
- Mẫu biên bản bảo vệ (C8).
- Ngôn ngữ luận văn (C3).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `bac_dao_tao` | Thạc sĩ / Tiến sĩ | Có |
| `ho_ten_hv` | Họ tên học viên / NCS, mã HV, ngành | Có |
| `ten_de_tai` | Tên đề tài luận văn / luận án | Có |
| `quyet_dinh_hd` | Số quyết định thành lập hội đồng, ngày ký | Có |
| `thanh_phan_tham_du` | Danh sách thành viên hội đồng có mặt / vắng mặt (lý do) | Có |
| `dien_bien` | Tóm tắt phần trình bày của học viên; câu hỏi của từng thành viên và trả lời tóm tắt | Có |
| `phieu_danh_gia` | Điểm đánh giá của từng thành viên (thang 10), nhận xét tóm tắt | Có |
| `ket_luan` | Đạt / Không đạt; yêu cầu chỉnh sửa, bổ sung (nếu có); thời hạn nộp bản hoàn chỉnh | Có |
| `thoi_gian_dia_diem` | Ngày, giờ, địa điểm buổi bảo vệ | Có |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Phòng Đào tạo (sau đại học) |
| Mô hình đào tạo | Chọn đúng mô hình trước khi áp quy tắc, không áp quy tắc của mô hình này cho mô hình khác: (1) ĐHQGHN cấp bằng; (2) liên kết quốc tế, đối tác nước ngoài cấp bằng; (3) song bằng; (4) cử nhân – thạc sĩ tích hợp; (5) tiếng Anh dự bị và mô hình 2+2 |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Hệ thống nguồn dữ liệu có trên website | LMS; cổng sinh viên. Skill không kết nối hệ thống, chỉ dùng file xuất/tải lên (C5) |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Ghi nhận thông tin chung và kiểm tra thành phần tham dự**
- Làm gì: ghi căn cứ quyết định thành lập hội đồng (số, ngày ký, người ký); thời gian, địa điểm
  buổi bảo vệ; thông tin HV/NCS (họ tên, mã, ngành, đề tài, người hướng dẫn); lập danh sách thành
  viên hội đồng có mặt / vắng mặt (ghi rõ lý do vắng). Kiểm tra điều kiện tiến hành: buổi bảo vệ
  chỉ được tiến hành khi có ít nhất 4/5 thành viên (thạc sĩ) hoặc 5/7 thành viên (tiến sĩ) có mặt,
  trong đó bắt buộc có Chủ tịch, Thư ký và ít nhất 01 phản biện — nếu không đủ thì hoãn và hẹn lại.
- Dùng input: `quyet_dinh_hd`, `thanh_phan_tham_du`, `ho_ten_hv`, `ten_de_tai`, `thoi_gian_dia_diem`,
  `bac_dao_tao`
- Vai trò: Thư ký hội đồng bảo vệ · AI hỗ trợ: chuẩn bị mẫu biên bản, danh sách thành phần đối chiếu trước buổi bảo vệ · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: ghi chính xác số quyết định thành lập hội đồng (sai số là lỗi pháp lý); vắng
  Chủ tịch hoặc Thư ký thì bắt buộc hoãn, không thay thế tùy tiện.
- → Kết quả bước: phần thông tin chung của biên bản + xác nhận đủ điều kiện tiến hành buổi bảo vệ
  (hoặc quyết định hoãn).

**Bước 2. Ghi diễn biến buổi bảo vệ theo trình tự**
- Làm gì: ghi tóm tắt diễn biến theo đúng trình tự: (1) Chủ tịch tuyên bố lý do, giới thiệu hội
  đồng, công bố quyết định thành lập; (2) HV/NCS trình bày tóm tắt luận văn/luận án (15–20 phút);
  (3) các phản biện đọc nhận xét; (4) thành viên hội đồng nêu câu hỏi, HV/NCS trả lời; (5) hội đồng
  họp kín thảo luận, bỏ phiếu đánh giá; (6) công bố kết quả. Ghi tóm tắt trung thực từng câu hỏi
  và ý trả lời chính, không ghi nguyên văn dài dòng.
- Dùng input: `dien_bien`, `thanh_phan_tham_du`
- Vai trò: Thư ký hội đồng bảo vệ · AI hỗ trợ: chuẩn bị đề cương diễn biến mẫu theo đúng trình tự · ⏱ trong buổi bảo vệ, ~2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: ghi rõ ai hỏi – hỏi gì – trả lời thế nào (gắn tên thành viên với câu hỏi);
  không bỏ sót câu hỏi của phản biện vì đây là cơ sở của yêu cầu chỉnh sửa ở bước 4.
- → Kết quả bước: phần diễn biến buổi bảo vệ (theo trình tự, gắn câu hỏi với từng thành viên).

**Bước 3. Tổng hợp phiếu đánh giá của hội đồng**
- Làm gì: lập bảng điểm đánh giá của từng thành viên (thang điểm 10) kèm nhận xét tóm tắt; tính
  điểm trung bình; đếm số phiếu "đạt"/"không đạt". Áp nguyên tắc đạt: thạc sĩ đạt khi điểm trung
  bình ≥ 5,5 và không có quá 01 phiếu dưới 5,0; luận án tiến sĩ đạt khi đa số phiếu tán thành và
  không có phiếu phản đối về tính trung thực khoa học.
- Dùng input: `phieu_danh_gia`, `bac_dao_tao`
- Vai trò: Thư ký hội đồng bảo vệ · AI hỗ trợ: tổng hợp bảng điểm tự động, tính điểm trung bình · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: kiểm tra từng phiếu có chữ ký của thành viên — phiếu không ký không có giá trị;
  tính lại điểm trung bình độc lập, không copy số liệu từ ghi chép tay.
- → Kết quả bước: bảng tổng hợp điểm đánh giá từng thành viên + điểm trung bình + số phiếu
  đạt/không đạt.

**Bước 4. Ghi kết luận của hội đồng**
- Làm gì: ghi kết luận theo 2 trường hợp: (a) ĐẠT — ghi rõ đạt không cần chỉnh sửa, hay đạt nhưng
  cần chỉnh sửa/bổ sung (liệt kê từng yêu cầu chỉnh sửa chi tiết kèm thời hạn nộp bản hoàn chỉnh);
  (b) KHÔNG ĐẠT — nêu lý do và hướng xử lý (bảo vệ lại, thời gian bảo vệ lại).
- Dùng input: `ket_luan`, `phieu_danh_gia`
- Vai trò: Hội đồng bảo vệ luận văn · AI hỗ trợ: chuẩn bị mẫu kết luận theo 2 trường hợp đạt/không đạt · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: yêu cầu chỉnh sửa phải cụ thể, kiểm chứng được (tránh ghi chung chung kiểu
  "hoàn thiện thêm"); thời hạn nộp bản hoàn chỉnh phải khả thi và được hội đồng thống nhất.
- → Kết quả bước: phần kết luận của hội đồng (đạt/không đạt + danh mục yêu cầu chỉnh sửa kèm
  thời hạn).

**Bước 5. Hoàn thiện biên bản, ký và lưu hồ sơ**
- Làm gì: hoàn thiện biên bản đầy đủ các phần; thư ký ký, chủ tịch hội đồng ký xác nhận; đính kèm
  phiếu đánh giá của từng thành viên (tài liệu bắt buộc); ghi rõ số bản và nơi lưu (hồ sơ HV/NCS,
  Phòng Đào tạo (sau đại học), người hướng dẫn); chuyển Phòng Đào tạo (sau đại học) làm thủ tục công nhận tốt nghiệp.
- Dùng input: `ket_luan`, `thoi_gian_dia_diem`
- Vai trò: Thư ký và Chủ tịch hội đồng ký biên bản · AI hỗ trợ: kiểm tra đầy đủ chữ ký và phụ lục đính kèm trước khi lưu · ⏱ ~1 giờ (ước tính)
- Lưu ý nghiệp vụ: biên bản thiếu chữ ký Chủ tịch hoặc thiếu phiếu đánh giá đính kèm thì không đủ
  căn cứ ra quyết định công nhận tốt nghiệp; lưu bản chính, không chỉ lưu bản photo.
- → Kết quả bước: biên bản buổi bảo vệ hoàn chỉnh (có chữ ký, có phiếu đánh giá đính kèm), đã
  phân phối và lưu hồ sơ.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Input: Quyết định hội đồng, thành viên, phiếu đánh giá"/]
    A["Bước 1: Ghi nhận thông tin chung và kiểm tra thành phần tham dự"]
    B{"Đủ số thành viên tối thiểu?"}
    C["Hoãn buổi bảo vệ, hẹn lại"]
    D["Bước 2: Ghi diễn biến buổi bảo vệ theo trình tự"]
    E["Bước 3: Tổng hợp phiếu đánh giá của hội đồng"]
    F{"Kết luận của hội đồng"}
    G["Bước 4: Ghi kết luận ĐẠT + yêu cầu chỉnh sửa"]
    H["Bước 4: Ghi kết luận KHÔNG ĐẠT + hướng bảo vệ lại"]
    I["Bước 5: Hoàn thiện biên bản, ký và lưu hồ sơ"]
    OUT[/"Output: Biên bản buổi bảo vệ"/]

    IN --> A --> B
    B -->|Không| C
    B -->|Có| D --> E --> F
    F -->|Đạt| G --> I
    F -->|Không đạt| H --> I
    I --> OUT
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao
- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Số liệu/nội dung trong output khớp với Input đã cho (bậc đào tạo, thông tin HV/NCS, đề tài, quyết định hội đồng, thành viên, diễn biến, phiếu điểm, kết luận, thời gian – địa điểm).
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn.
- [ ] Đúng thể thức văn bản hành chính của biên bản.
- [ ] Căn cứ pháp lý đầy đủ, còn hiệu lực (Thông tư 23/2021/TT-BGDĐT đối với thạc sĩ; Thông tư 18/2021/TT-BGDĐT đối với tiến sĩ).
- [ ] Đã qua Human gate: thư ký và Chủ tịch hội đồng đã ký biên bản; phiếu đánh giá của từng thành viên có chữ ký và đã đính kèm đầy đủ.
- [ ] Buổi bảo vệ chỉ được tiến hành khi đủ số thành viên tối thiểu (thạc sĩ 4/5, tiến sĩ 5/7) trong đó bắt buộc có Chủ tịch, Thư ký và ít nhất 01 phản biện; số quyết định thành lập hội đồng ghi chính xác.
- [ ] Diễn biến ghi rõ ai hỏi – hỏi gì – trả lời thế nào, gắn tên thành viên với từng câu hỏi; không bỏ sót câu hỏi của phản biện.
- [ ] Điểm trung bình được tính lại độc lập; nguyên tắc đạt áp đúng quy chế (thạc sĩ: ĐTB ≥ 5,5 và không quá 01 phiếu dưới 5,0; tiến sĩ: đa số phiếu tán thành, không phiếu phản đối về tính trung thực khoa học).
- [ ] Yêu cầu chỉnh sửa cụ thể, kiểm chứng được, có thời hạn khả thi được hội đồng thống nhất; ghi rõ số bản biên bản và nơi lưu.
Tiêu chí đạt = tất cả các ô được đánh dấu.

## Căn cứ & lưu ý

> ⚠ Cập nhật pháp lý (rà soát 11/10/2026, nguồn thứ cấp, cần người phụ trách pháp chế xác nhận): Thông tư 53/2026/TT-BGDĐT (ban hành 30/06/2026) quy định quy chế tuyển sinh và đào tạo sau đại học thạc sĩ, tiến sĩ và thay thế Thông tư 23/2021/TT-BGDĐT, Thông tư 18/2021/TT-BGDĐT; theo nguồn thứ cấp, Thông tư áp dụng cho các khóa thông báo tuyển sinh từ 01/01/2027. Trước khi dẫn căn cứ: đọc toàn văn và điều khoản chuyển tiếp, xác định khóa/đợt thuộc văn bản nào; không tự trích điều khoản của Thông tư cũ nếu chưa xác định còn áp dụng.
- Thông tư 23/2021/TT-BGDĐT (Quy chế đào tạo trình độ thạc sĩ); Thông tư 18/2021/TT-BGDĐT
  (Quy chế tuyển sinh và đào tạo trình độ tiến sĩ).
- Buổi bảo vệ chỉ tiến hành khi đủ số thành viên tối thiểu có mặt (thạc sĩ: 4/5 gồm
  Chủ tịch, Thư ký và ít nhất 01 phản biện; tiến sĩ: 5/7).
- Phiếu đánh giá của từng thành viên là tài liệu đính kèm bắt buộc của biên bản.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `bien-ban-bao-ve-luan-van` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

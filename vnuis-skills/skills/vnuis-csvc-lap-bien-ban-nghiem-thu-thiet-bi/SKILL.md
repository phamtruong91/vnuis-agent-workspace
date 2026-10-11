---
name: "vnuis-csvc-lap-bien-ban-nghiem-thu-thiet-bi"
description: "Dùng khi nhà thầu đã giao, lắp đặt xong thiết bị mua sắm và cần lập biên bản nghiệm thu, bàn giao: đối chiếu hợp đồng, kiểm tra số lượng, chủng loại, chạy thử, ghi đạt hoặc không đạt."
---

# Lập biên bản nghiệm thu thiết bị

## Khi nào dùng
Khi thiết bị đã được giao, lắp đặt xong và cần nghiệm thu trước khi thanh toán;
khi bàn giao thiết bị cho đơn vị sử dụng quản lý.

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

- **Đơn vị thường dùng:** Phòng Tổ chức và Quản trị (cơ sở vật chất).
- **Nghiệp vụ trong phiếu CES:** không có dòng riêng trong phiếu CES; đề xuất theo chức năng đơn vị ở sheet 00 và cần xác nhận khi khảo sát.

**Điều chỉnh khi dùng cho VNU-IS**
- Biên bản nghiệm thu đối chiếu hợp đồng và thông số kỹ thuật; điểm không đạt được nêu rõ, không làm mềm.
- Thiết bị CNTT có đại diện bộ phận hạ tầng CNTT tham gia.

**Chờ xác nhận khi khảo sát**
- Thành phần nghiệm thu (C6).
- Mẫu biên bản (C8).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `hop_dong` | Số hợp đồng, ngày ký, các bên | Có |
| `danh_muc` | Bảng thiết bị: tên, model, số serial, số lượng, đơn vị tính | Có |
| `ket_qua_kiem_tra` | Kết quả kiểm tra từng hạng mục: đạt / không đạt, ghi chú lỗi (nếu có) | Có |
| `thanh_phan` | Thành phần hội đồng nghiệm thu (đại diện các bên, chức vụ) | Có |
| `thoi_gian_dia_diem` | Thời gian, địa điểm nghiệm thu | Có |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Phòng Tổ chức và Quản trị (cơ sở vật chất) |
| Cơ sở | Xuân Thủy (Cầu Giấy); Phan Tây Nhạc (Xuân Phương); Hòa Lạc (tòa HT1, Khu Đô thị ĐHQGHN). Ghi rõ cơ sở khi nội dung gắn địa điểm |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Chuẩn bị hồ sơ nghiệm thu**
- Làm gì: tập hợp hợp đồng (`hop_dong`), HSMT, biên bản giao hàng, catalogue/thông số kỹ
  thuật của thiết bị; từ `danh_muc` lập danh sách kiểm tra (tên, model, số serial, số lượng
  từng hạng mục) để dùng khi đối chiếu thực tế.
- Dùng input: `hop_dong`, `danh_muc`.
- Vai trò: Tổ nghiệm thu · AI hỗ trợ: tổng hợp, chuẩn hóa dữ liệu, đối chiếu tự động, cảnh báo sai lệch · ⏱ ~0,5–1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: thiếu biên bản giao hàng hoặc catalogue thì chưa đủ cơ sở nghiệm thu —
  yêu cầu nhà thầu cung cấp trước buổi nghiệm thu.
- → Kết quả bước: bộ hồ sơ nghiệm thu + danh sách kiểm tra theo danh mục hợp đồng.

**Bước 2. Đối chiếu hồ sơ: số lượng, chủng loại, số serial**
- Làm gì: kiểm tra thực tế từng hạng mục so với hợp đồng: đếm số lượng, đối chiếu chủng loại,
  model và số serial từng chiếc với danh mục hợp đồng; ghi lại mọi chênh lệch (thiếu số
  lượng, sai model, serial không khớp).
- Dùng input: `danh_muc`, kết quả Bước 1.
- Vai trò: Chuyên viên Phòng TC&QT (cơ sở vật chất) · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: số serial là định danh duy nhất của từng thiết bị — phải đối chiếu từng
  chiếc, không kiểm tra mẫu; chênh lệch serial phải được làm rõ ngay tại buổi nghiệm thu.
- → Kết quả bước: bảng đối chiếu hồ sơ (từng hạng mục: khớp/lệch so với hợp đồng).

**Bước 3. Kiểm tra thực tế: ngoại quan và chạy thử**
- Làm gì: kiểm tra ngoại quan (nguyên đai, nguyên kiện; móp méo, trầy xước); kiểm tra tình
  trạng hoạt động và chạy thử các chức năng chính theo tiêu chí đã thống nhất trong
  `ket_qua_kiem_tra`; thực hiện tại `thoi_gian_dia_diem` đã ấn định với đầy đủ thành phần.
- Dùng input: `ket_qua_kiem_tra`, `thoi_gian_dia_diem`.
- Vai trò: Cán bộ Phòng TC&QT (cơ sở vật chất) (thực hiện trực tiếp) · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chạy thử phải bao phủ chức năng chính mà thiết bị sẽ phục vụ (ví dụ máy
  tính: khởi động, kiểm tra cấu hình, chạy phần mềm chuyên dụng); ghi nhận cụ thể từng lỗi
  phát hiện, không ghi chung chung "chưa đạt".
- → Kết quả bước: biên bản ghi nhận kiểm tra thực tế (ngoại quan + chạy thử từng hạng mục).

**Bước 4. Ghi nhận kết quả từng hạng mục**
- Làm gì: tổng hợp kết quả Bước 2 – 3 thành bảng: mỗi hạng mục ghi Đạt hoặc Không đạt, kèm
  mô tả cụ thể tồn tại (nếu có: lỗi gì, số serial nào, mức độ).
- Dùng input: kết quả Bước 2 – 3.
- Vai trò: Chuyên viên Phòng TC&QT (cơ sở vật chất) · AI hỗ trợ: tổng hợp, chuẩn hóa dữ liệu · ⏱ ~0,5–1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: kết quả phải khách quan, dựa trên bằng chứng kiểm tra — đây là căn cứ
  để kết luận nghiệm thu và xử lý bảo hành về sau.
- → Kết quả bước: bảng kết quả Đạt/Không đạt từng hạng mục.

**Bước 5. Kết luận nghiệm thu**
- Làm gì: căn cứ bảng kết quả Bước 4, đưa ra một trong ba kết luận: (1) nghiệm thu toàn bộ
  (tất cả đạt); (2) nghiệm thu có điều kiện (ghi rõ nội dung phải khắc phục, thời hạn khắc
  phục, và tổ chức nghiệm thu lại sau khắc phục); (3) từ chối nghiệm thu (không đạt ở mức
  không thể chấp nhận).
- Dùng input: kết quả Bước 4.
- Vai trò: Tổ nghiệm thu · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~0,5–1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: nghiệm thu có điều kiện phải ghi rõ thời hạn khắc phục và trách nhiệm
  của nhà thầu; không thanh toán đợt cuối khi chưa nghiệm thu đạt.
- → Kết quả bước: dự thảo kết luận nghiệm thu.

**Bước 6. Lập và ký biên bản**
- Làm gì: viết biên bản theo cấu trúc: tiêu đề → căn cứ (hợp đồng) → thời gian, địa điểm,
  thành phần hội đồng (`thanh_phan`, `thoi_gian_dia_diem`) → I. Thiết bị nghiệm thu
  (danh mục) → II. Kết quả kiểm tra (số lượng, ngoại quan, chạy thử) → III. Kết luận →
  số bản biên bản → chữ ký các thành viên (ghi rõ họ tên, chức vụ); đính kèm phụ lục bảng
  chi tiết thiết bị kèm số serial.
- Dùng input: `thanh_phan`, `thoi_gian_dia_diem`, kết quả Bước 4 – 5.
- Vai trò: Tổ nghiệm thu (ký biên bản) · AI hỗ trợ: soạn dự thảo, đối chiếu tự động, cảnh báo sai lệch · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: biên bản phải có chữ ký của đủ thành phần (chủ tịch hội đồng, đơn vị sử
  dụng, đại diện nhà thầu); phụ lục serial là tài liệu bắt buộc đính kèm.
- → Kết quả bước: biên bản nghiệm thu, bàn giao thiết bị hoàn chỉnh, đã ký.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Hợp đồng và biên bản giao hàng"/] --> B["Bước 1: Chuẩn bị hồ sơ, catalogue, danh sách kiểm tra"]
    B --> C["Bước 2: Đối chiếu số lượng, chủng loại, serial với hợp đồng"]
    C --> D["Bước 3: Kiểm tra thực tế: ngoại quan, chạy thử"]
    D --> E["Bước 4: Ghi nhận Đạt hoặc Không đạt từng hạng mục"]
    E --> F{"Kết luận nghiệm thu?"}
    F -->|Đạt toàn bộ| G["Nghiệm thu toàn bộ"]
    F -->|Có tồn tại| H["Nghiệm thu có điều kiện: khắc phục và nghiệm thu lại"]
    F -->|Không đạt| I["Bước 5: Từ chối nghiệm thu"]
    G --> J["Bước 6: Lập biên bản và ký"]
    H --> J
    I --> J
    J --> HG["👤 Hội đồng nghiệm thu ký biên bản"]
    HG --> K[["Biên bản nghiệm thu, bàn giao"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Có đầy đủ sản phẩm: Biên bản nghiệm thu, bàn giao thiết bị
- [ ] Có đầy đủ sản phẩm: Bảng chi tiết thiết bị kèm số serial (phụ lục)
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Thiếu biên bản giao hàng hoặc catalogue thì chưa đủ cơ sở nghiệm thu —
- [ ] Số serial là định danh duy nhất của từng thiết bị — phải đối chiếu từng

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Căn cứ & lưu ý
- Hợp đồng mua sắm đã ký; HSMT và HSDT của nhà thầu trúng thầu.
- Trường hợp nghiệm thu có điều kiện: ghi rõ nội dung phải khắc phục và thời hạn, nghiệm thu lại sau khắc phục.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `bien-ban-nghiem-thu-thiet-bi` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

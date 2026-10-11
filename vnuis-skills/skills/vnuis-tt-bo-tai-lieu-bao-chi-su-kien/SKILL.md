---
name: "vnuis-tt-bo-tai-lieu-bao-chi-su-kien"
description: "Dùng khi tổ chức sự kiện lớn cần mời báo chí (khai giảng, kỷ niệm, hội thảo, ký kết, ngày hội tuyển sinh) và cần bộ tài liệu báo chí (press kit): thông cáo, thông tin tóm tắt, tiểu sử diễn giả, đầu mối liên hệ."
---

# Bộ tài liệu báo chí cho sự kiện

## Khi nào dùng
Khi tổ chức sự kiện cần mời báo chí đưa tin: lễ khai giảng, kỷ niệm thành lập, hội thảo lớn,
ký kết hợp tác, ngày hội tuyển sinh...

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf, .txt, .md, .html. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

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

- **Đơn vị thường dùng:** Phòng Truyền thông và Tuyển sinh.
- **Nghiệp vụ trong phiếu CES:** không có dòng riêng trong phiếu CES; đề xuất theo chức năng đơn vị ở sheet 00 và cần xác nhận khi khảo sát.

**Điều chỉnh khi dùng cho VNU-IS**
- Bộ tài liệu báo chí có bản tiếng Anh khi sự kiện có khách quốc tế.
- Số liệu và thông tin đối tác chỉ ghi khi đã được duyệt công bố.

**Chờ xác nhận khi khảo sát**
- Người duyệt công bố (C6).
- Danh sách báo chí nhận tin (C8).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_su_kien` | Tên sự kiện | Có |
| `thoi_gian_dia_diem` | Thời gian, địa điểm tổ chức | Có |
| `noi_dung_chinh` | Các điểm nhấn của sự kiện (diễn giả, nội dung, con số nổi bật) | Có |
| `dien_gia` | Danh sách diễn giả/khách mời chính + tiểu sử ngắn | Không |
| `so_lieu` | Số liệu bắt buộc có nguồn (quy mô, thành tựu...) | Không |
| `lien_he_bao_chi` | Đầu mối báo chí của trường (tên, điện thoại, email) | Có |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Phòng Truyền thông và Tuyển sinh |
| Cơ sở | Xuân Thủy (Cầu Giấy); Phan Tây Nhạc (Xuân Phương); Hòa Lạc (tòa HT1, Khu Đô thị ĐHQGHN). Ghi rõ cơ sở khi nội dung gắn địa điểm |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Kiểm định và chuẩn hóa thông tin đầu vào**
- Làm gì: gom toàn bộ các trường input; lập bảng đối chiếu từng số liệu trong `so_lieu` và `noi_dung_chinh` với nguồn kèm theo; kiểm tra `lien_he_bao_chi` đủ tên – điện thoại – email; đối chiếu `thoi_gian_dia_diem` với giấy mời/thông báo chính thức của sự kiện.
- Dùng input: `ten_su_kien`, `thoi_gian_dia_diem`, `noi_dung_chinh`, `dien_gia`, `so_lieu`, `lien_he_bao_chi`.
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch, lập bảng biểu, định dạng · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: số liệu không có nguồn được đưa vào danh sách "chờ xác nhận", tuyệt đối không đưa vào thông cáo; thời gian/địa điểm sai dù một chi tiết cũng gây sự cố với báo chí.
- → Kết quả bước: Bảng kiểm định dữ liệu (OK / thiếu nguồn / cần xác nhận) + bộ dữ liệu sạch đã chuẩn hóa.

**Bước 2. Soạn thông cáo báo chí theo tháp ngược**
- Làm gì: viết tiêu đề 1 dòng chứa tin mới nhất; đoạn mở 2–3 câu trả lời 5W1H; thân bài triển khai các điểm nhấn từ `noi_dung_chinh`, chèn trích dẫn lãnh đạo; đoạn nền 2–3 câu giới thiệu trường; khối liên hệ báo chí ở cuối.
- Dùng input: toàn bộ trường input + bộ dữ liệu sạch (Bước 1).
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: soạn dự thảo · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi con số trong bài phải gắn với nguồn đã kiểm định ở Bước 1; trích dẫn phải được người phát ngôn đọc và xác nhận nguyên văn trước khi đưa vào; tránh tính từ tuyệt đối ("hàng đầu", "duy nhất") nếu không chứng minh được.
- → Kết quả bước: Dự thảo thông cáo báo chí (mỗi số liệu có đánh dấu nguồn).

**Bước 3. Lập fact sheet 1 trang**
- Làm gì: rút gọn dự thảo thông cáo thành bảng 1 trang: tên sự kiện, thời gian, địa điểm, quy mô, diễn giả chính, 3–5 con số nổi bật kèm ghi chú nguồn từng số.
- Dùng input: `ten_su_kien`, `thoi_gian_dia_diem`, `dien_gia`, `so_lieu` + dự thảo thông cáo (Bước 2).
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: soạn dự thảo · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: fact sheet không được chứa số liệu nào không có trong thông cáo; mọi con số phải khớp tuyệt đối giữa hai tài liệu.
- → Kết quả bước: Fact sheet 1 trang (dự thảo).

**Bước 4. Chuẩn bị tiểu sử diễn giả và danh mục ảnh**
- Làm gì: viết tiểu sử 3–5 dòng/người từ `dien_gia` (học vị, chức danh, lĩnh vực); lập danh mục ảnh cần có (chân dung diễn giả, toàn cảnh sự kiện, ảnh điểm nhấn) kèm ghi chú bản quyền và sự đồng ý sử dụng.
- Dùng input: `dien_gia` + dự thảo thông cáo (Bước 2).
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: soạn dự thảo · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: học vị, chức danh phải đúng quyết định bổ nhiệm; chỉ dùng ảnh rõ nguồn và đã được đồng ý bằng văn bản.
- → Kết quả bước: Tiểu sử diễn giả (3–5 dòng/người) + danh mục ảnh kèm ghi chú bản quyền.

**Bước 5. Kiểm tra chéo và xin xác nhận**
- Làm gì: đối chiếu 3 chiều — thông cáo ↔ fact sheet ↔ nguồn gốc — cho từng số liệu; gửi trích dẫn cho người phát ngôn xác nhận nguyên văn; kiểm tra lại thông tin liên hệ báo chí.
- Dùng input: bán thành phẩm Bước 2–4 + `so_lieu` gốc.
- Vai trò: Trưởng Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: quy tắc "3 nguồn khớp nhau" cho con số nhạy cảm (quy mô, kinh phí); một lỗi số liệu nhỏ trên báo chí tốn rất nhiều công đính chính.
- → Kết quả bước: Bộ press kit đã xác nhận (có xác nhận trích dẫn của người phát ngôn) + biên bản kiểm tra.

**Bước 6. Đóng gói và lập danh mục kiểm phát hành**
- Làm gì: gom thông cáo + fact sheet + tiểu sử diễn giả + danh mục ảnh thành một bộ; lập danh mục kiểm phát hành: gửi trước sự kiện bao lâu, danh sách báo/nhà báo nhận, kênh gửi (email), người gửi.
- Dùng input: bộ press kit đã xác nhận (Bước 5).
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: chuẩn bị bản phát hành · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: gửi trước sự kiện 3–5 ngày cho báo in, 1–2 ngày cho báo điện tử; người gửi phải đúng là đầu mối báo chí đã nêu trong thông cáo.
- → Kết quả bước: Bộ press kit hoàn chỉnh + danh mục kiểm phát hành.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Thông tin sự kiện + diễn giả"/] --> B["Bước 1. Kiểm định và chuẩn hóa thông tin đầu vào"]
    B --> C["Bước 2. Soạn thông cáo báo chí theo tháp ngược"]
    C --> D["Bước 3. Lập fact sheet 1 trang"]
    D --> E["Bước 4. Chuẩn bị tiểu sử diễn giả + danh mục ảnh"]
    E --> F["Bước 5. Kiểm tra chéo và xin xác nhận"]
    F --> G{"Số liệu có nguồn, trích dẫn được xác nhận?"}
    G -->|Chưa| H["Bổ sung nguồn / xin xác nhận"]
    H --> F
    G -->|Đạt| I["Bước 6. Đóng gói và lập danh mục kiểm phát hành"]
    I --> HG["👤 Trưởng phòng → Lãnh đạo trường duyệt"]
    HG --> J[["Bộ press kit hoàn chỉnh"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Có đầy đủ sản phẩm: Thông cáo báo chí hoàn chỉnh
- [ ] Có đầy đủ sản phẩm: Fact sheet 1 trang + danh mục ảnh + thông tin liên hệ
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Số liệu không có nguồn được đưa vào danh sách "chờ xác nhận", tuyệt đối không đưa vào thông cáo
- [ ] Mỗi con số trong bài phải gắn với nguồn đã kiểm định ở Bước 1

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Human gate (người kiểm duyệt)
- Trưởng phòng duyệt thông cáo và fact sheet.
- Lãnh đạo trường duyệt trước khi phát hành cho báo chí.
- Người phát ngôn xác nhận mọi trích dẫn mang tên mình.

## Giới hạn (guardrails)
- Không phát hành press kit khi chưa được lãnh đạo duyệt.
- Không đưa số liệu chưa có nguồn xác thực.
- Không dùng ảnh không rõ bản quyền hoặc chưa được đồng ý.
- Không tự gửi thông cáo cho báo chí.

## Căn cứ & lưu ý
- Thông cáo báo chí viết theo cấu trúc tháp ngược (quan trọng nhất lên đầu).
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `press-kit-su-kien` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

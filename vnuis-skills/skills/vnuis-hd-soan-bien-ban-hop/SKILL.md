---
name: "vnuis-hd-soan-bien-ban-hop"
description: "Dùng khi vừa kết thúc phiên họp Hội đồng Khoa học và Đào tạo (định kỳ hoặc đột xuất) và cần lập biên bản: diễn biến, ý kiến từng thành viên, kết quả biểu quyết từng nội dung."
---

# Biên bản họp Hội đồng KH&ĐT

## Khi nào dùng
Sau mỗi phiên họp Hội đồng Khoa học và Đào tạo (định kỳ hoặc đột xuất) cần lập biên bản ghi
nhận đầy đủ diễn biến, ý kiến thành viên và kết quả biểu quyết từng nội dung làm căn cứ ban hành
nghị quyết.

## Khi nào KHÔNG dùng
- Là cuộc họp thông thường (giao ban, họp đơn vị) → dùng `vnuis-vp-soan-bien-ban-hop`.

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

- **Đơn vị thường dùng:** Hội đồng Khoa học và Đào tạo (thư ký).
- **Nghiệp vụ trong phiếu CES:** "Tổ chức và ghi nhận họp: Ghi nhận diễn biến, ý kiến, biểu quyết và nội dung kết luận" (sheet `09_KS_HD_KH_DT`). Tần suất gợi ý: Theo phiên họp. Đầu vào gợi ý: Chương trình; tài liệu; ghi âm/ghi chép; phiếu biểu quyết; danh sách tham dự. Khó khăn gợi ý: Khối lượng ghi chép lớn; dễ thiếu ý, sai tên hoặc chưa tách rõ quyết định. Đây là gợi ý có sẵn của CES, chưa phải xác nhận của đơn vị.

**Điều chỉnh khi dùng cho VNU-IS**
- Theo Điều 18 Luật 125/2025/QH15, Hội đồng khoa học và đào tạo chỉ tư vấn; "nghị quyết", "kết luận" của Hội đồng là ý kiến tham mưu, quyết định thuộc Hiệu trưởng hoặc cấp có thẩm quyền (chờ C6). Không viết như quyết định có hiệu lực thi hành. Hội đồng trường công lập đã chấm dứt từ 01/01/2026 (Điều 46).
- Tách thành 4 phần: diễn biến, ý kiến, biểu quyết (ghi dạng x/y), kết luận. Phiếu nêu khó khăn là chưa tách rõ quyết định.
- Người dự họp ghi theo chức danh trong Hội đồng; họ tên do thư ký xác nhận.
- Phiên có chuyên gia ngoài hoặc đại diện ĐHQGHN: ghi rõ tư cách tham dự.
- Họp có ghi âm: chỉ dùng bản được phép (C5).

**Chờ xác nhận khi khảo sát**
- Thể thức biên bản của Hội đồng (C1, C8).
- Cách thức biểu quyết theo quy chế (C2).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `phien_hop` | Phiên họp thứ mấy, năm học | Có |
| `thoi_gian` | Ngày, giờ bắt đầu – kết thúc | Có |
| `dia_diem` | Địa điểm họp (chọn cơ sở: Xuân Thủy, Phan Tây Nhạc, Hòa Lạc) | Có |
| `chu_tich` | Chủ tịch hội đồng (chủ trì) | Có |
| `thu_ky` | Thư ký hội đồng | Có |
| `thanh_vien` | Danh sách thành viên: dự họp / vắng mặt (lý do) | Có |
| `noi_dung` | Từng nội dung: tờ trình/báo cáo trình bày, ý kiến thảo luận chính | Có |
| `bieu_quyet` | Kết quả biểu quyết từng nội dung: tán thành / không tán thành / không ý kiến | Có |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Hội đồng Khoa học và Đào tạo (thư ký) |
| Cơ sở | Xuân Thủy (Cầu Giấy); Phan Tây Nhạc (Xuân Phương); Hòa Lạc (tòa HT1, Khu Đô thị ĐHQGHN). Ghi rõ cơ sở khi nội dung gắn địa điểm |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Hệ thống nguồn dữ liệu có trên website | E-Office (văn bản điều hành). Skill không kết nối hệ thống, chỉ dùng file xuất/tải lên (C5) |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Ghi phần mở đầu và điểm danh**
- Làm gì: ghi phiên họp (`phien_hop`), `thoi_gian`, `dia_diem`, chủ trì (`chu_tich`), thư ký (`thu_ky`); điểm danh `thanh_vien` (dự họp/vắng mặt + lý do); xác nhận đủ túc số theo quy chế (thường > 1/2 thành viên dự họp).
- Dùng input: `phien_hop`, `thoi_gian`, `dia_diem`, `chu_tich`, `thu_ky`, `thanh_vien`.
- Vai trò: Thư ký hội đồng (soạn phần mở đầu, điểm danh, xác nhận túc số) · AI hỗ trợ: soạn thảo phần mở đầu, kiểm tra túc số từ danh sách thành viên · ⏱ ~10–15 phút (ước tính)
- Lưu ý nghiệp vụ: nếu không đủ túc số thì không họp tiếp — ghi rõ lý do dừng vào biên bản và kết thúc tại bước này.
- → Kết quả bước: phần mở đầu biên bản (phiên họp, chủ trì, điểm danh, xác nhận túc số).

**Bước 2. Ghi diễn biến từng nội dung**
- Làm gì: với mỗi nội dung trong `noi_dung`, ghi người trình bày → tóm tắt ý kiến thảo luận chính (ghi tên thành viên + ý chính) → kết quả biểu quyết trong `bieu_quyet` (số tán thành/không tán thành/không ý kiến).
- Dùng input: `noi_dung`, `bieu_quyet`.
- Vai trò: Thư ký hội đồng (ghi diễn biến, ý kiến và kết quả biểu quyết tại phiên họp) · AI hỗ trợ: chuẩn bị trước khung biên bản (chương trình, danh sách thành viên) phục vụ ghi chép · ⏱ theo thời lượng phiên họp (ước tính)
- Lưu ý nghiệp vụ: chỉ ghi ý kiến thực sự phát biểu tại phiên họp, không suy diễn, không thêm bớt; số liệu biểu quyết phải đếm thực tế tại chỗ.
- → Kết quả bước: phần nội dung biên bản (từng nội dung có trình bày – ý kiến – biểu quyết).

**Bước 3. Tổng hợp kết luận phiên họp**
- Làm gì: liệt kê các nội dung được thông qua / chưa thông qua / cần bổ sung; ghi rõ đầu mối đơn vị thực hiện và thời hạn nếu có.
- Dùng input: kết quả bước 2 (diễn biến và biểu quyết từng nội dung).
- Vai trò: Thư ký / Chủ tịch hội đồng (xác nhận kết luận phiên họp) · AI hỗ trợ: tổng hợp kết luận phiên họp sơ bộ từ diễn biến và biểu quyết · ⏱ ~15–20 phút (ước tính)
- Lưu ý nghiệp vụ: kết luận phải rõ ràng, không để nội dung lửng lơ (nội dung chưa thông qua phải ghi rõ lý do và hướng xử lý tiếp theo).
- → Kết quả bước: phần kết luận phiên họp.

**Bước 4. Ghi bế mạc và ký xác nhận**
- Làm gì: ghi thời gian bế mạc; trình Chủ tịch và thư ký ký xác nhận; các thành viên được quyền kiểm tra, đề nghị đính chính trước khi ký.
- Dùng input: `chu_tich`, `thu_ky`, kết quả bước 1–3.
- Vai trò: Chủ tịch hội đồng và Thư ký hội đồng (ký xác nhận sau khi mọi đính chính hoàn tất) · AI hỗ trợ: chuẩn bị tài liệu, tổng hợp trước các đính chính cần ký · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: mọi đính chính phải hoàn tất trước khi ký; biên bản đã ký là căn cứ ban hành nghị quyết.
- → Kết quả bước: biên bản họp có chữ ký chủ tịch và thư ký.

**Bước 5. Kiểm tra biên bản trước khi lưu hồ sơ**
- Làm gì: đối chiếu tổng số phiếu biểu quyết từng nội dung với số thành viên dự họp (bước 1); kiểm tra nội dung kết luận rõ ràng, có đầu mối thực hiện nếu cần; sửa lỗi chính tả, số liệu.
- Dùng input: kết quả bước 1–4.
- Vai trò: Thư ký hội đồng (đối chiếu, kiểm tra trước khi lưu hồ sơ) · AI hỗ trợ: đối chiếu tổng số phiếu với số thành viên dự họp, kiểm tra lỗi số liệu/chính tả · ⏱ ~10–15 phút (ước tính)
- Lưu ý nghiệp vụ: tổng số phiếu không được vượt số người dự họp; phát hiện sai lệch thì đối chiếu lại với ghi chép tại chỗ, tuyệt đối không tự điều chỉnh số liệu biểu quyết.
- → Kết quả bước: biên bản họp hoàn chỉnh, sẵn sàng ký và lưu hồ sơ.
## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Tài liệu họp Hội đồng KH-ĐT"/] --> B1["Bước 1: Ghi phần mở đầu và điểm danh"]
    B1 --> B2["Bước 2: Ghi diễn biến từng nội dung"]
    B2 --> B3["Bước 3: Tổng hợp kết luận phiên họp"]
    B3 --> B4["Bước 4: Ghi bế mạc và ký xác nhận"]
    B4 --> B5["Bước 5: Kiểm tra biên bản trước khi lưu hồ sơ"]
    B5 --> HG["👤 Chủ tịch hội đồng ký xác nhận biên bản"]
    HG --> OUT[["Biên bản họp đã ký"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Điểm danh đủ dự/vắng (kèm lý do vắng); xác nhận đủ túc số theo quy chế (thường > 1/2 thành viên dự họp) — không đủ túc số thì không họp tiếp.
- [ ] Chỉ ghi ý kiến thực sự phát biểu tại phiên họp — không suy diễn, không thêm bớt.
- [ ] Tổng số phiếu biểu quyết từng nội dung không vượt số thành viên dự họp; sai lệch phải đối chiếu lại ghi chép tại chỗ, tuyệt đối không tự điều chỉnh số liệu biểu quyết.
- [ ] Kết luận phiên họp rõ ràng: nội dung nào thông qua/chưa thông qua/cần bổ sung (+ lý do và hướng xử lý với nội dung chưa thông qua); có đầu mối đơn vị thực hiện và thời hạn nếu cần.
- [ ] Mọi đính chính hoàn tất trước khi ký; biên bản có chữ ký của thư ký và chủ tịch hội đồng.
- [ ] Đã qua Human gate: các thành viên được kiểm tra, đề nghị đính chính trước khi ký; Chủ tịch ký xác nhận biên bản.

> Tiêu chí đạt: tất cả các ô được đánh dấu.

## Human gate (người kiểm duyệt)
- **Thư ký hội đồng** chịu trách nhiệm ghi chép trung thực, đầy đủ.
- **Chủ tịch hội đồng** ký xác nhận biên bản; các thành viên được quyền kiểm tra, đề nghị
  đính chính trước khi ký.

## Giới hạn (guardrails)
- KHÔNG suy diễn, thêm bớt ý kiến của thành viên không phát biểu trong phiên họp.
- KHÔNG thay đổi kết quả biểu quyết đã được ghi nhận.
- Biên bản là tài liệu mật nội bộ — không phát tán khi chưa được phép.

## Căn cứ & lưu ý
- Quy chế tổ chức và hoạt động của Hội đồng Khoa học và Đào tạo của trường.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `bien-ban-hop-hoi-dong-khdt` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

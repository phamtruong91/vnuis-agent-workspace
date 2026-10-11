---
name: "vnuis-dmst-lap-ho-so-hop-dong-dich-vu"
description: "Dùng khi trung tâm, viện hoặc Phòng KHCN&HTPT nhận dịch vụ khoa học công nghệ cho khách hàng ngoài trường (tư vấn, phân tích mẫu, đào tạo theo đặt hàng) và cần báo giá, hợp đồng, nghiệm thu, thanh lý."
---

# Hồ sơ hợp đồng dịch vụ KHCN

## Khi nào dùng
Khi trung tâm/viện/Phòng KHCN&HTPT của trường cung cấp dịch vụ cho tổ chức, doanh nghiệp bên ngoài:
tư vấn kỹ thuật, phân tích – kiểm nghiệm mẫu, chuyển giao công nghệ, đào tạo theo đặt hàng...
cần lập báo giá, ký hợp đồng, nghiệm thu và thanh lý đúng quy định.

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
- **Nghiệp vụ trong phiếu CES:** "Chuyển giao công nghệ: Xây dựng phương án, hồ sơ và thỏa thuận chuyển giao công nghệ" (sheet `08_KS_Vien_DMST_CGCN`). Tần suất gợi ý: Theo giao dịch/dự án. Đầu vào gợi ý: Hồ sơ công nghệ; nhu cầu bên nhận; phương án tài chính; mẫu hợp đồng; quy định. Khó khăn gợi ý: Nhiều vòng trao đổi; điều khoản và phạm vi dễ thay đổi; cần kiểm tra pháp lý. Đây là gợi ý có sẵn của CES, chưa phải xác nhận của đơn vị.

**Điều chỉnh khi dùng cho VNU-IS**
- Hồ sơ hợp đồng dịch vụ KH&CN của Viện: chỉ lập từ thỏa thuận và báo giá có sẵn; không tự đặt giá.
- Pháp chế rà trước khi trình ký.

**Chờ xác nhận khi khảo sát**
- Mẫu hợp đồng dịch vụ và thẩm quyền ký (C1, C8).
- Danh mục dịch vụ Viện cung cấp (C8).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_dich_vu` | Tên dịch vụ KHCN cung cấp | Có |
| `khach_hang` | Tên, địa chỉ, người đại diện của bên thuê dịch vụ | Có |
| `don_vi_thuc_hien` | Đơn vị của trường thực hiện dịch vụ | Có |
| `pham_vi_cong_viec` | Nội dung công việc chi tiết, sản phẩm bàn giao | Có |
| `don_gia` | Báo giá chi tiết theo hạng mục | Có |
| `thoi_gian` | Thời gian thực hiện, các mốc bàn giao | Có |
| `dieu_khoan_thanh_toan` | Tạm ứng, thanh toán theo tiến độ, giữ lại | Không (mặc định: tạm ứng 30%, quyết toán sau nghiệm thu) |

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

**Bước 1. Lập báo giá chi tiết và chốt giá với khách hàng**
- Làm gì: Bóc tách `pham_vi_cong_viec` thành các hạng mục công việc; mỗi hạng mục ghi: nội
  dung, đơn vị tính, số lượng, đơn giá, thành tiền; cộng tổng giá trị, ghi rõ đã/chưa bao
  gồm VAT; gửi khách hàng, thương thảo và chốt giá trị hợp đồng bằng văn bản (email xác
  nhận hoặc biên bản làm việc).
- Dùng input: `ten_dich_vu`, `pham_vi_cong_viec`, `don_gia`, `khach_hang`.
- Vai trò: Chuyên viên dịch vụ KHCN · AI hỗ trợ: bóc tách hạng mục và lập bảng báo giá dự thảo, đơn vị chốt đơn giá theo biểu giá đã duyệt · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: đơn giá theo biểu giá dịch vụ đã được trường phê duyệt (nếu có); chi
  phí phát sinh ngoài phạm vi phải ghi rõ cách tính ngay từ báo giá; không báo giá miệng —
  mọi chốt giá phải có văn bản để đối chiếu khi quyết toán.
- → Kết quả bước: Bảng báo giá chi tiết đã được khách hàng xác nhận bằng văn bản.

**Bước 2. Soạn thảo hợp đồng**
- Làm gì: Soạn hợp đồng đầy đủ các điều khoản bắt buộc: thông tin hai bên, đối tượng và
  phạm vi công việc, sản phẩm bàn giao, giá trị hợp đồng, tiến độ và các mốc bàn giao,
  điều khoản thanh toán, nghiệm thu, bảo hành/bảo mật, phạt vi phạm, chấm dứt hợp đồng,
  hiệu lực.
- Dùng input: `ten_dich_vu`, `khach_hang`, `don_vi_thuc_hien`, `pham_vi_cong_viec`,
  `don_gia`, `thoi_gian`, `dieu_khoan_thanh_toan`.
- Vai trò: Chuyên viên dịch vụ KHCN · AI hỗ trợ: soạn dự thảo hợp đồng theo mẫu chuẩn của trường · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: dùng mẫu hợp đồng chuẩn của trường (nếu có); số liệu giá trị, tiến độ
  phải khớp báo giá đã chốt ở bước 1; điều khoản phạt vi phạm phải cân đối hai chiều
  (cả bên cung cấp và bên thuê).
- → Kết quả bước: Dự thảo hợp đồng dịch vụ KHCN.

**Bước 3. Thẩm định và trình ký hợp đồng**
- Làm gì: Đơn vị thực hiện tự rà soát dự thảo → gửi Phòng KHCN&HTPT thẩm định tính pháp lý →
  trình lãnh đạo trường ký theo phân cấp ủy quyền; sau khi hai bên ký, lưu số hợp đồng,
  ngày ký, bản chính.
- Dùng input: (dự thảo hợp đồng — kết quả bước 2).
- Vai trò: Viện trưởng · AI hỗ trợ: tổng hợp danh mục kiểm tra, đối chiếu hồ sơ · ⏱ 3–5 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: kiểm tra người ký đúng thẩm quyền theo giá trị hợp đồng (phân cấp);
  hợp đồng chỉ có hiệu lực khi đủ chữ ký hai bên và đóng dấu; mỗi bên giữ ít nhất 01 bản
  chính.
- → Kết quả bước: Hợp đồng đã ký, đóng dấu (bản chính lưu tại đơn vị và Phòng KHCN&HTPT).

**Bước 4. Triển khai thực hiện và giám sát tiến độ**
- Làm gì: Lập kế hoạch triển khai chi tiết theo các mốc trong hợp đồng; theo dõi tiến độ
  từng hạng mục; lập biên bản làm việc/bàn giao từng phần có chữ ký hai bên (nếu hợp đồng
  chia nhiều đợt); ghi nhận phát sinh (nếu có) và xử lý theo điều khoản hợp đồng.
- Dùng input: `thoi_gian`, `pham_vi_cong_viec`.
- Vai trò: Chuyên viên dịch vụ KHCN · AI hỗ trợ: soạn nhật ký theo dõi và nhắc mốc · ⏱ 30–60 phút mỗi đợt theo dõi (ước tính)
- Lưu ý nghiệp vụ: mọi thay đổi phạm vi/tiến độ phải lập phụ lục hợp đồng, không thỏa
  thuận miệng; chậm mốc nào phải báo ngay cho khách hàng và ghi vào biên bản làm việc.
- → Kết quả bước: Nhật ký triển khai + biên bản bàn giao từng phần (nếu có).

**Bước 5. Tổ chức nghiệm thu dịch vụ**
- Làm gì: Thành lập hội đồng nghiệm thu có đại diện hai bên; kiểm tra sản phẩm bàn giao
  đối chiếu từng nội dung trong hợp đồng (số lượng, chất lượng, thời hạn); lập biên bản
  nghiệm thu ghi rõ: đạt/không đạt từng hạng mục, tồn tại cần khắc phục (nếu có) và thời
  hạn khắc phục.
- Dùng input: `pham_vi_cong_viec`, `thoi_gian` (làm tiêu chí nghiệm thu).
- Vai trò: Hội đồng nghiệm thu · AI hỗ trợ: tổng hợp danh mục kiểm tra, đối chiếu hồ sơ · ⏱ 0,5–1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: chỉ nghiệm thu khi đủ sản phẩm theo hợp đồng; nếu không đạt, ghi rõ
  nội dung phải làm lại và hạn hoàn thành — không ký "nghiệm thu có điều kiện" chung chung.
- → Kết quả bước: Biên bản nghiệm thu dịch vụ (hai bên ký).

**Bước 6. Thanh lý hợp đồng và quyết toán**
- Làm gì: Đối chiếu giá trị thực hiện với hợp đồng (trừ tạm ứng đã nhận, phạt vi phạm nếu
  có); lập biên bản thanh lý hợp đồng; xuất hóa đơn VAT; hạch toán doanh thu và thực hiện
  nghĩa vụ tài chính theo quy định của trường; lưu trọn bộ hồ sơ.
- Dùng input: `dieu_khoan_thanh_toan`, `don_gia` (giá trị quyết toán).
- Vai trò: Chuyên viên dịch vụ KHCN · AI hỗ trợ: đối chiếu số liệu và soạn biên bản thanh lý, kế toán đối chiếu và xuất hóa đơn · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chỉ thanh lý khi đã nghiệm thu đạt và đã thu đủ tiền (hoặc có cam kết
  thanh toán bằng văn bản); đối chiếu số liệu với Phòng TC&QT (kế hoạch – tài chính) trước khi xuất hóa đơn.
- → Kết quả bước: Biên bản thanh lý hợp đồng + hồ sơ quyết toán đầy đủ.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/Yêu cầu dịch vụ từ khách hàng/] --> B["Bước 1. Lập báo giá chi tiết và chốt giá với khách hàng"]
    B --> C{"Khách hàng chốt giá?"}
    C -->|Không| B
    C -->|Có| D["Bước 2. Soạn thảo hợp đồng"]
    D --> E["Bước 3. Thẩm định và trình ký hợp đồng"]
    E --> F["👤 Phòng KHCN&HTPT thẩm định pháp lý"]
    F --> G["👤 Lãnh đạo trường ký hợp đồng"]
    G --> H["Bước 4. Triển khai thực hiện và giám sát tiến độ"]
    H --> I["Bước 5. Tổ chức nghiệm thu dịch vụ"]
    I --> J{"Nghiệm thu đạt?"}
    J -->|Không| H
    J -->|Có| K["Bước 6. Thanh lý hợp đồng và quyết toán"]
    K --> L[/Hồ sơ hợp đồng và biên bản hoàn chỉnh/]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Số liệu (giá trị, tiến độ) khớp với Input (báo giá, phạm vi công việc) đã cho.
- [ ] Không bịa đặt chữ ký, biên bản nghiệm thu hay xác nhận thanh toán không có thật.
- [ ] Báo giá chốt bằng văn bản của khách hàng; ghi rõ đã/chưa bao gồm VAT.
- [ ] Hợp đồng đầy đủ các điều khoản bắt buộc; người ký đúng thẩm quyền theo phân cấp; đủ chữ ký hai bên và đóng dấu.
- [ ] Nghiệm thu đối chiếu từng hạng mục hợp đồng; tồn tại cần khắc phục có hạn hoàn thành cụ thể.
- [ ] Thanh lý chỉ khi đã nghiệm thu đạt và đã thu đủ tiền (hoặc có cam kết thanh toán bằng văn bản).
- [ ] Căn cứ pháp lý đầy đủ, còn hiệu lực: Luật Khoa học và Công nghệ, quy định nội bộ về hoạt động dịch vụ KHCN.
- [ ] Đã qua Human gate: Phòng KHCN&HTPT thẩm định pháp lý, lãnh đạo trường ký hợp đồng, hội đồng hai bên ký biên bản nghiệm thu.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Human gate (người kiểm duyệt)
- **Lãnh đạo đơn vị thực hiện** thẩm định phạm vi công việc và báo giá trước khi trình.
- **Phòng KHCN&HTPT** thẩm định tính pháp lý của hợp đồng.
- **Lãnh đạo trường** (theo phân cấp ủy quyền) ký hợp đồng; **hội đồng nghiệm thu 2 bên**
  ký biên bản nghiệm thu dịch vụ.

## Giới hạn (guardrails)
- AI không tự quyết giá dịch vụ thay đơn vị (giá do đơn vị đề xuất, lãnh đạo phê duyệt).
- Không cam kết tiến độ/chất lượng vượt năng lực thực tế của đơn vị.
- Không thay kế toán lập chứng từ thanh toán, xuất hóa đơn.

## Căn cứ & lưu ý
- Luật Khoa học và Công nghệ; quy định nội bộ về hoạt động dịch vụ KHCN của trường.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `ho-so-hop-dong-dich-vu-khcn` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

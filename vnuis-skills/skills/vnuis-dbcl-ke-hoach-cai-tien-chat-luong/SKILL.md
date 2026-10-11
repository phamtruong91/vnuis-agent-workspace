---
name: "vnuis-dbcl-ke-hoach-cai-tien-chat-luong"
description: "Dùng khi đã có kết quả tự đánh giá hoặc kết luận đánh giá ngoài và cần chuyển các khuyến nghị, tồn tại thành kế hoạch cải tiến có đơn vị thực hiện, thời hạn, kinh phí, tiêu chí đánh giá."
---

# Kế hoạch cải tiến chất lượng

## Khi nào dùng
Khi có kết quả tự đánh giá hoặc kết luận của đoàn đánh giá ngoài, cần chuyển các khuyến nghị /
tồn tại thành kế hoạch hành động cụ thể.

## Định dạng và file đầu ra
Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

**Chạy qua API (không có công cụ tạo file):** trả đủ nội dung dạng văn bản có tiêu đề, bảng; ứng dụng gọi sẽ xuất file.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Khi người dùng yêu cầu bộ slide (.pptx), đọc mục “Xuất PowerPoint (.pptx) khi được yêu cầu” trong quy cách đầu ra.

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Nếu có cập nhật pháp lý dưới đây, đọc [căn cứ và điều kiện áp dụng](references/phap-ly.md) trước khi làm. Quy trình dưới đây giữ nghiệp vụ từ bản gốc; mọi viện dẫn văn bản, mẫu biểu, điều khoản phải theo căn cứ đã chọn trong phap-ly.md, không theo văn bản cũ.

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Bối cảnh riêng của VNU-IS

Bản chỉnh cho Trường Quốc tế – ĐHQGHN (VNU-IS), v0.4.2. Dựng từ website công khai và phiếu khảo sát CES còn trống; **chưa có dữ liệu khảo sát thực tế của đơn vị**. Đọc [bối cảnh VNU-IS](references/boi-canh-vnuis.md) trước khi chạy; các mã C1–C8 nằm ở mục 6 của file đó.

- **Đơn vị thường dùng:** Phòng Đào tạo (đảm bảo chất lượng).
- **Nghiệp vụ trong phiếu CES:** không có dòng riêng trong phiếu CES; đề xuất theo chức năng đơn vị ở sheet 00 và cần xác nhận khi khảo sát.

**Điều chỉnh khi dùng cho VNU-IS**
- Kế hoạch cải tiến lấy từ các điểm yếu trong báo cáo tự đánh giá hoặc phản hồi đã có; không tự thêm vấn đề.
- Mỗi hành động có đơn vị phụ trách, thời hạn, chỉ số; thời hạn do đơn vị cam kết.

**Chờ xác nhận khi khảo sát**
- Chu kỳ rà soát cải tiến (C6).
- Nguồn lực được duyệt (C6).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)
| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `nguon_khuyen_nghi` | Báo cáo tự đánh giá / Kết luận đoàn đánh giá ngoài (số, ngày) | Có |
| `danh_sach_ton_tai` | Bảng: tiêu chí, nội dung tồn tại/khuyến nghị | Có |
| `don_vi_thuc_hien` | Các phòng/khoa được giao | Có |
| `thoi_han_chung` | Thời hạn hoàn thành toàn bộ kế hoạch | Có |
| `kinh_phi_du_kien` | Tổng kinh phí dự kiến (nếu có) | Không |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Phòng Đào tạo (đảm bảo chất lượng) |
| Mô hình đào tạo | Chọn đúng mô hình trước khi áp quy tắc, không áp quy tắc của mô hình này cho mô hình khác: (1) ĐHQGHN cấp bằng; (2) liên kết quốc tế, đối tác nước ngoài cấp bằng; (3) song bằng; (4) cử nhân – thạc sĩ tích hợp; (5) tiếng Anh dự bị và mô hình 2+2 |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Ràng buộc pháp lý khi thực hiện** (trích references/phap-ly.md; đối chiếu toàn văn và hiệu lực tại ngày nghiệp vụ):
- Thông tư 20/2026/TT-BGDĐT, hiệu lực 15/05/2026: Yêu cầu ngày hoàn tất tự đánh giá, ngày đăng ký đánh giá ngoài, khung tiêu chuẩn và minh chứng. Điều 51: chỉ cơ sở đã tự đánh giá VÀ đăng ký đánh giá ngoài trước 15/05/2026 được tiếp tục khung 12/2017, hoàn tất chậm nhất 31/12/2026. Ngoài chuyển tiếp dùng 20/2026; không chuyển thang điểm cơ học.
- Thông tư 04/2025/TT-BGDĐT, hiệu lực 04/04/2025: Tách kiểm định chương trình khỏi kiểm định cơ sở. Yêu cầu phiên bản tiêu chuẩn, ngày đăng ký và bộ minh chứng; trích tiêu chí từ phụ lục hiện hành. Không mặc định khung 11 tiêu chuẩn của 04/2016 là khung hiện hành; đối chiếu chuyển tiếp trước khi tiếp tục hồ sơ cũ.
- Trước Bước 1: chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi nhận nội bộ [CẦN XÁC MINH] (không đưa vào file giao), để trống phần tương ứng, chưa kết luận tuân thủ.
- Các con số, thời hạn, số điều, số mức xếp loại, hệ số và mẫu biểu nêu trong các bước dưới đây được giữ từ quy trình gốc (trước cập nhật pháp lý); chỉ dùng khi đã đối chiếu đúng với căn cứ đã chọn, khác thì theo căn cứ. Danh sách điểm cần đối chiếu: docs/DIEM_CAN_DOI_CHIEU_PHAP_LY.md.

**Bước 1. Tổng hợp tồn tại/khuyến nghị**
- Làm gì: Trích toàn bộ tồn tại và khuyến nghị từ `nguon_khuyen_nghi` (báo cáo tự đánh giá / kết luận đoàn đánh giá ngoài: số, ngày ban hành); nhóm các nội dung theo lĩnh vực (đào tạo, NCKH, đội ngũ, CSVC, quản trị...); loại bỏ nội dung trùng lặp, đánh số thứ tự từng tồn tại.
- Dùng input: `nguon_khuyen_nghi`, `danh_sach_ton_tai`.
- Vai trò: Chuyên viên Phòng Đào tạo (khảo thí, đảm bảo chất lượng) · AI hỗ trợ: trích và nhóm tồn tại/khuyến nghị theo lĩnh vực, loại nội dung trùng lặp · ⏱ ~1 giờ (ước tính)
- Lưu ý nghiệp vụ: mỗi khuyến nghị của đoàn đánh giá ngoài đều phải có trong danh sách — sót khuyến nghị là lỗi nghiêm trọng khi tái kiểm định; ghi rõ khuyến nghị thuộc tiêu chí nào để tiện đối chiếu.
- → Kết quả bước: Bảng tổng hợp tồn tại/khuyến nghị đã nhóm theo lĩnh vực, đánh số thứ tự.

**Bước 2. Xây dựng giải pháp cho từng nội dung**
- Làm gì: Với mỗi tồn tại, xây dựng 01 hoặc nhiều giải pháp cụ thể, đo lường được (trả lời: làm gì, làm như thế nào, đạt mức nào); mỗi giải pháp phải gắn với tiêu chí đánh giá sẽ nêu ở Bước 6.
- Dùng input: `danh_sach_ton_tai`.
- Vai trò: Đơn vị chuyên môn phụ trách lĩnh vực (rà soát tính khả thi) · AI hỗ trợ: đề xuất giải pháp sơ bộ cho từng tồn tại · ⏱ ~2 giờ (ước tính)
- Lưu ý nghiệp vụ: bẫy thường gặp — giải pháp chung chung ("nâng cao chất lượng đội ngũ") không thực thi được; giải pháp phải cụ thể đến mức có thể kiểm chứng hoàn thành hay chưa.
- → Kết quả bước: Bảng tồn tại – giải pháp tương ứng (dự thảo cột 1–2 của bảng hành động).

**Bước 3. Phân công trách nhiệm**
- Làm gì: Với mỗi giải pháp, chỉ định 01 đơn vị chủ trì và các đơn vị phối hợp từ danh sách `don_vi_thuc_hien`; gửi dự thảo để các đơn vị góp ý, xác nhận khả năng thực hiện trước khi chốt.
- Dùng input: `don_vi_thuc_hien`.
- Vai trò: Lãnh đạo trường (chốt phân công sau khi các đơn vị góp ý) · AI hỗ trợ: tổng hợp ý kiến góp ý của các đơn vị trước khi chốt · ⏱ ~2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: mỗi giải pháp chỉ có 01 đơn vị chủ trì duy nhất để rõ trách nhiệm; đơn vị phối hợp phải được hỏi ý kiến trước, tránh giao việc mà đơn vị không biết.
- → Kết quả bước: Bảng giải pháp đã gắn đơn vị chủ trì/phối hợp (dự thảo cột 3).

**Bước 4. Ấn định thời hạn và mốc kiểm tra**
- Làm gì: Ấn định thời hạn hoàn thành cho từng giải pháp (không vượt quá `thoi_han_chung`); đặt các mốc kiểm tra giữa kỳ cho giải pháp dài hạn (VD: giải pháp 12 tháng thì có mốc 6 tháng); ghi thời hạn theo tháng/năm cụ thể.
- Dùng input: `thoi_han_chung`.
- Vai trò: Lãnh đạo trường (quyết định thời hạn và mốc kiểm tra) · AI hỗ trợ: gợi ý thời hạn sơ bộ cho từng giải pháp · ⏱ ~2 giờ (ước tính)
- Lưu ý nghiệp vụ: thời hạn phải thực tế — quá gấp đơn vị không làm được, quá dài mất tính cam kết; mốc kiểm tra giữa kỳ là cơ sở để Phòng Đào tạo (khảo thí, đảm bảo chất lượng) giám sát.
- → Kết quả bước: Bảng giải pháp đã có thời hạn và mốc kiểm tra (dự thảo cột 4).

**Bước 5. Dự toán kinh phí**
- Làm gì: Lập dự toán kinh phí cho từng giải pháp (nếu có): nội dung chi, số tiền, nguồn kinh phí (ngân sách trường/dự án/tài trợ); tổng hợp thành tổng kinh phí của kế hoạch, đối chiếu với `kinh_phi_du_kien` (nếu có).
- Dùng input: `kinh_phi_du_kien`.
- Vai trò: Phòng TC&QT (kế hoạch – tài chính) (thẩm tra kinh phí) · AI hỗ trợ: lập bảng dự toán sơ bộ theo từng giải pháp · ⏱ ~4 giờ (ước tính)
- Lưu ý nghiệp vụ: giải pháp không có kinh phí vẫn phải ghi rõ "không sử dụng kinh phí" thay vì để trống; kinh phí lớn cần có ý kiến của Phòng TC&QT (kế hoạch – tài chính) trước khi ban hành.
- → Kết quả bước: Bảng dự toán kinh phí theo từng giải pháp + tổng kinh phí (dự thảo cột 5).

**Bước 6. Xác định tiêu chí đánh giá**
- Làm gì: Với mỗi giải pháp, xác định kết quả đầu ra mong đợi dưới dạng đo lường được (con số, tỷ lệ, sản phẩm cụ thể) và cách kiểm chứng (minh chứng nào chứng minh đã hoàn thành); ghi vào cột tiêu chí đánh giá của bảng hành động.
- Dùng input: `danh_sach_ton_tai`.
- Vai trò: Chuyên viên Phòng Đào tạo (khảo thí, đảm bảo chất lượng) · AI hỗ trợ: gợi ý tiêu chí đo lường và minh chứng kiểm chứng cho từng giải pháp · ⏱ ~2 giờ (ước tính)
- Lưu ý nghiệp vụ: tiêu chí đánh giá phải đo lường được, tránh định tính ("tốt hơn", "nâng cao"); mỗi tiêu chí nên gắn với 01 minh chứng cụ thể để đoàn kiểm định tái kiểm tra.
- → Kết quả bước: Bảng hành động hoàn chỉnh 6 cột (nội dung – giải pháp – đơn vị – thời hạn – kinh phí – tiêu chí đánh giá).

**Bước 7. Ban hành và giám sát**
- Làm gì: Hoàn thiện văn bản kế hoạch (căn cứ, mục tiêu, bảng hành động, tổ chức thực hiện), trình Hiệu trưởng ký ban hành; Phòng Đào tạo (khảo thí, đảm bảo chất lượng) làm đầu mối theo dõi tiến độ, đôn đốc các đơn vị báo cáo định kỳ (6 tháng/lần); tổng hợp báo cáo tiến độ, lưu đầy đủ minh chứng hoàn thành từng giải pháp.
- Dùng input: `nguon_khuyen_nghi`, `thoi_han_chung`.
- Vai trò: Hiệu trưởng ký ban hành, Phòng Đào tạo (khảo thí, đảm bảo chất lượng) theo dõi tiến độ định kỳ · AI hỗ trợ: soạn văn bản kế hoạch hoàn chỉnh, tổng hợp báo cáo tiến độ định kỳ · ⏱ ~1 tuần (ước tính)
- Lưu ý nghiệp vụ: kế hoạch cải tiến là minh chứng bắt buộc trong chu kỳ kiểm định tiếp theo — phải lưu đầy đủ báo cáo tiến độ và minh chứng hoàn thành, không chỉ lưu văn bản kế hoạch.
- → Kết quả bước: Kế hoạch cải tiến chất lượng đã ban hành + cơ chế giám sát tiến độ định kỳ.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Input: khuyến nghị, danh sách tồn tại"/]
    A["Bước 1. Tổng hợp tồn tại theo lĩnh vực"]
    B["Bước 2. Xây dựng giải pháp cụ thể"]
    C["Bước 3. Phân công trách nhiệm"]
    D["Bước 4. Ấn định thời hạn, mốc kiểm tra"]
    E["Bước 5. Dự toán kinh phí"]
    F["Bước 6. Xác định tiêu chí đánh giá"]
    HG["👤 Hiệu trưởng ký ban hành"]
    G["Bước 7. Giám sát tiến độ định kỳ"]
    OUT[/"Output: Kế hoạch cải tiến chất lượng"/]
    IN --> A --> B --> C --> D --> E --> F --> HG --> G --> OUT
```

## Đầu ra
- Văn bản kế hoạch cải tiến chất lượng hoàn chỉnh.
- Bảng hành động chi tiết (nội dung – giải pháp – đơn vị – thời hạn – kinh phí – tiêu chí đánh giá).

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao
Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Đủ các phần và đúng bố cục theo cấu trúc tại references/quy-cach-dau-ra.md (không theo cấu trúc của bản gốc).
- [ ] Toàn bộ khuyến nghị của đoàn đánh giá ngoài đều có trong danh sách (không sót), ghi rõ thuộc tiêu chí nào; số liệu khớp với Input.
- [ ] Không bịa đặt tồn tại, giải pháp, kinh phí.
- [ ] Đúng thể thức văn bản hành chính theo Nghị định 30/2020/NĐ-CP.
- [ ] Căn cứ (kết luận đoàn đánh giá ngoài / báo cáo tự đánh giá: số, ngày ban hành) đầy đủ, còn hiệu lực.
- [ ] Đã qua Human gate: người có thẩm quyền theo quy trình đã duyệt.
- [ ] Mỗi giải pháp có 01 đơn vị chủ trì duy nhất đã được hỏi ý kiến trước; thời hạn không vượt quá thời hạn chung, có mốc kiểm tra giữa kỳ cho giải pháp dài hạn.
- [ ] Tiêu chí đánh giá đo lường được (con số, tỷ lệ, sản phẩm cụ thể) và gắn minh chứng kiểm chứng; giải pháp không dùng kinh phí ghi rõ "không sử dụng kinh phí" thay vì để trống.

## Căn cứ & lưu ý
- Căn cứ hiện hành: xem [căn cứ và điều kiện áp dụng](references/phap-ly.md); phải đối chiếu văn bản gốc, hiệu lực và chuyển tiếp tại ngày nghiệp vụ.
- Kế hoạch cải tiến là minh chứng bắt buộc trong chu kỳ kiểm định tiếp theo — phải lưu
  đầy đủ báo cáo tiến độ và minh chứng hoàn thành.
- Mỗi giải pháp cần gắn với 01 tiêu chí đánh giá đo lường được, tránh chung chung.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Tư liệu đối chiếu
Bản gốc trước cập nhật pháp lý (kèm ví dụ giả lập) lưu tại `references/quy-trinh-lich-su.md`, chỉ để đối chiếu hồ sơ lịch sử; không dùng căn cứ, mẫu hay số liệu trong đó làm chỉ dẫn hiện hành.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `ke-hoach-cai-tien-chat-luong` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

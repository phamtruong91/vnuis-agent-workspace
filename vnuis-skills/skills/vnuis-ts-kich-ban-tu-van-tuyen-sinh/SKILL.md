---
name: "vnuis-ts-kich-ban-tu-van-tuyen-sinh"
description: "Dùng trước mùa tuyển sinh khi cần kịch bản cho đội tư vấn (ngày hội, livestream, tư vấn tại trường THPT, hotline, fanpage) theo từng đối tượng học sinh, phụ huynh."
---

# Xây dựng kịch bản tư vấn tuyển sinh & hướng nghiệp

## Khi nào dùng
Trước mỗi chiến dịch/mùa tuyển sinh, khi Phòng Truyền thông và Tuyển sinh (hoặc Phòng Truyền thông và Tuyển sinh)
cần chuẩn bị kịch bản cho đội ngũ tư vấn: ngày hội tư vấn, livestream, tư vấn tại trường THPT,
trực hotline, trả lời fanpage.

## Khi nào KHÔNG dùng
- Cần bộ hỏi đáp có trích nguồn cho website, chatbot → dùng `vnuis-ts-hoi-dap-tuyen-sinh`.

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
- **Nghiệp vụ trong phiếu CES:** "Nội dung tư vấn: Soạn email/tin nhắn theo từng giai đoạn tuyển sinh" (sheet `05_KS_TT_Tuyen_sinh`). Tần suất gợi ý: Thường xuyên. Đầu vào gợi ý: Thông tin chương trình; giai đoạn; đối tượng; chính sách. Khó khăn gợi ý: Tài liệu phân tán, nhiều định dạng; Đọc và đối chiếu thủ công mất thời gian; Dễ bỏ sót trường dữ liệu/phiên bản; Đầu ra phụ thuộc kinh nghiệm từng cá nhân. Đây là gợi ý có sẵn của CES, chưa phải xác nhận của đơn vị.

**Điều chỉnh khi dùng cho VNU-IS**
- Soạn theo giai đoạn do Phòng chốt (ví dụ quan tâm, đăng ký, xét tuyển, nhập học) và theo kiểu chương trình.
- Không cam kết kết quả xét tuyển, học bổng, việc làm khi chưa có văn bản; thông tin điều kiện, mốc thời gian lấy từ thông báo hiện hành.
- Học sinh có thể chưa đủ 18 tuổi: dùng thông tin liên hệ tối thiểu và theo mục đích tư vấn.

**Chờ xác nhận khi khảo sát**
- Danh sách giai đoạn và kênh liên lạc (C8).
- Chính sách lưu và sử dụng thông tin liên hệ (C5).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `doi_tuong` | Học sinh lớp 12 / Phụ huynh / Cả hai | Có |
| `kenh_tu_van` | Trực tiếp / Livestream / Hotline / Fanpage | Có |
| `nganh_noi_bat` | Các ngành cần đẩy mạnh tư vấn | Không |
| `chinh_sach` | Học bổng, học phí, ký túc xá, việc làm sau tốt nghiệp (số liệu chính thức) | Có |
| `cau_hoi_thuong_gap` | Danh sách hỏi đáp cần chuẩn hóa câu trả lời | Không |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Phòng Truyền thông và Tuyển sinh |
| Mô hình đào tạo | Chọn đúng mô hình trước khi áp quy tắc, không áp quy tắc của mô hình này cho mô hình khác: (1) ĐHQGHN cấp bằng; (2) liên kết quốc tế, đối tác nước ngoài cấp bằng; (3) song bằng; (4) cử nhân – thạc sĩ tích hợp; (5) tiếng Anh dự bị và mô hình 2+2 |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Hệ thống nguồn dữ liệu có trên website | Biểu mẫu tuyển sinh; nền tảng AI tư vấn (ai.vnuis.edu.vn); hotline và is@vnu.edu.vn. Skill không kết nối hệ thống, chỉ dùng file xuất/tải lên (C5) |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Phân nhóm đối tượng và lập bản đồ mối quan tâm**
- Làm gì: từ `doi_tuong`, tách nhóm học sinh (quan tâm: ngành học, việc làm, môi trường học tập) và phụ huynh (quan tâm: học phí, uy tín, an toàn, ký túc xá); với từng nhóm liệt kê 5–7 mối quan tâm chính theo thứ tự ưu tiên; ghi nhận khác biệt theo `kenh_tu_van` (trực tiếp/livestream/hotline/fanpage).
- Dùng input: `doi_tuong`, `kenh_tu_van`.
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: cùng một câu hỏi nhưng cách trả lời cho học sinh và phụ huynh khác nhau (học sinh cần cảm hứng, phụ huynh cần số liệu chắc chắn).
- → Kết quả bước: Bản đồ mối quan tâm theo nhóm đối tượng.

**Bước 2. Chốt thông điệp chính có số liệu**
- Làm gì: từ `chinh_sach`, chọn 3–5 điểm nổi bật nhất của trường/ngành (`nganh_noi_bat`); mỗi điểm gắn 1 số liệu chính thức (học bổng, học phí, KTX, tỷ lệ việc làm); đối chiếu từng số liệu với văn bản đã công bố (quyết định học bổng, đề án tuyển sinh).
- Dùng input: `chinh_sach`, `nganh_noi_bat`.
- Vai trò: Trưởng Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: tuyệt đối không bịa số liệu; số liệu nào chưa có văn bản công bố thì loại khỏi thông điệp.
- → Kết quả bước: Bộ thông điệp chính (3–5 điểm, mỗi điểm kèm số liệu + nguồn văn bản).

**Bước 3. Soạn bộ hỏi đáp chuẩn có trích nguồn**
- Làm gì: từ `cau_hoi_thuong_gap`, với mỗi câu hỏi viết câu trả lời chuẩn ngắn gọn, có số liệu, ghi nguồn văn bản (tên văn bản + số quyết định nếu có); bổ sung câu hỏi còn thiếu cho đủ các nhóm: điểm chuẩn, học phí, học bổng, KTX, việc làm.
- Dùng input: `cau_hoi_thuong_gap`, `chinh_sach`.
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: soạn dự thảo · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: câu trả lời về điểm chuẩn năm trước phải ghi rõ phương thức xét tuyển đi kèm; không hứa hẹn điểm chuẩn năm nay.
- → Kết quả bước: Bộ hỏi đáp chuẩn (câu hỏi → câu trả lời → nguồn văn bản).

**Bước 4. Viết kịch bản tư vấn theo kênh**
- Làm gì: theo `kenh_tu_van`, viết kịch bản 5 pha: mở đầu (câu chào + câu hỏi mở) → khai thác nhu cầu (3–5 câu hỏi gợi mở) → tư vấn (gắn thông điệp Bước 2 + hỏi đáp Bước 3) → xử lý từ chối (kỹ thuật đồng cảm + số liệu) → chốt hành động (đăng ký tư vấn sâu / tham quan trường / theo dõi fanpage); viết riêng phiên bản cho học sinh và phụ huynh.
- Dùng input: `kenh_tu_van` + bản đồ mối quan tâm (Bước 1) + thông điệp (Bước 2) + hỏi đáp (Bước 3).
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: soạn dự thảo · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: kịch bản livestream cần thêm phần tương tác bình luận; kịch bản hotline cần câu hỏi xác nhận thông tin liên hệ để chăm sóc tiếp.
- → Kết quả bước: Kịch bản tư vấn theo kênh (đủ 5 pha, 2 phiên bản đối tượng).

**Bước 5. Chuẩn bị tình huống khó**
- Làm gì: liệt kê 5–8 tình huống nhạy cảm (điểm chuẩn cao, học phí tăng, tin đồn tiêu cực, so sánh với trường khác, "điểm em thấp có đỗ không"...); mỗi tình huống viết cách trả lời mẫu theo nguyên tắc: trung thực – không né tránh – không hứa hẹn quá mức – không hạ thấp trường khác.
- Dùng input: bộ hỏi đáp (Bước 3) + `chinh_sach`.
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: soạn dự thảo · ⏱ ~30–90 phút (ước tính)
- Lưu ý nghiệp vụ: câu "điểm em thấp có đỗ không" → không hứa hẹn trúng tuyển, chỉ hướng dẫn phương thức phù hợp và ngưỡng năm trước để tham khảo.
- → Kết quả bước: Bộ tình huống khó kèm cách xử lý mẫu.

**Bước 6. Lập danh mục kiểm cho tư vấn viên**
- Làm gì: liệt kê tài liệu mang theo (tờ rơi, mã QR), kiến thức bắt buộc nắm (đề án tuyển sinh, học phí, học bổng, KTX), và bài kiểm tra nhanh 10 câu trước chiến dịch; quy định "3 không": không hứa hẹn trúng tuyển, không bịa số liệu, không hạ thấp trường khác.
- Dùng input: kịch bản (Bước 4) + hỏi đáp (Bước 3).
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: tư vấn viên chưa qua kiểm tra nhanh thì không được trực tiếp tư vấn.
- → Kết quả bước: Danh mục kiểm tư vấn viên + bài kiểm tra nhanh.

**Bước 7. Rà soát cuối và hoàn thiện**
- Làm gì: đối chiếu mọi số liệu trong kịch bản + hỏi đáp với đề án tuyển sinh năm hiện hành đã công bố; kiểm tra ngôn ngữ phù hợp từng đối tượng; đóng gói thành tài liệu nội bộ hoàn chỉnh.
- Dùng input: toàn bộ bán thành phẩm Bước 2–6 + `chinh_sach`.
- Vai trò: Chuyên viên Phòng Truyền thông và Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chỉ một con số sai (học phí, điểm chuẩn) cũng đủ gây khiếu nại; người rà soát cuối nên khác người soạn.
- → Kết quả bước: Kịch bản tư vấn hoàn chỉnh (sẵn sàng trình duyệt và tập huấn).

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Đề án tuyển sinh + chính sách học bổng"/] --> B["Bước 1. Phân nhóm đối tượng và lập bản đồ mối quan tâm"]
    B --> C["Bước 2. Chốt thông điệp chính có số liệu"]
    C --> D["Bước 3. Soạn bộ hỏi đáp chuẩn có trích nguồn"]
    D --> E["Bước 4. Viết kịch bản tư vấn theo kênh"]
    E --> F["Bước 5. Chuẩn bị tình huống khó"]
    F --> G["Bước 6. Lập danh mục kiểm cho tư vấn viên"]
    G --> H["Bước 7. Rà soát cuối và hoàn thiện"]
    H --> HG["👤 Trưởng Phòng Truyền thông và Tuyển sinh duyệt"]
    HG --> I[["Kịch bản tư vấn + bộ hỏi đáp + danh mục kiểm"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Có đầy đủ sản phẩm: Kịch bản tư vấn hoàn chỉnh theo đối tượng và kênh
- [ ] Có đầy đủ sản phẩm: Bộ hỏi đáp có câu trả lời chuẩn + danh mục kiểm cho tư vấn viên
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Cùng một câu hỏi nhưng cách trả lời cho học sinh và phụ huynh khác nhau (học sinh cần cảm hứng, phụ huynh cần số liệu chắc chắn).
- [ ] Tuyệt đối không bịa số liệu

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Human gate (người kiểm duyệt)
- Trưởng Phòng Truyền thông và Tuyển sinh (hoặc Phòng Truyền thông và Tuyển sinh) duyệt toàn bộ nội dung,
  đặc biệt là số liệu học phí, học bổng, điểm chuẩn, tỷ lệ việc làm.
- Tư vấn viên phải được tập huấn và kiểm tra nhanh trước khi tham gia tư vấn.

## Giới hạn (guardrails)
- AI không bịa điểm chuẩn, tỷ lệ việc làm, mức học bổng — mọi số liệu phải theo văn bản đã công bố.
- AI không hứa hẹn trúng tuyển dưới bất kỳ hình thức nào.
- AI không so sánh hạ thấp trường khác; không tư vấn ngoài phạm vi đề án tuyển sinh.

## Căn cứ & lưu ý
- Đề án tuyển sinh năm hiện hành của trường.
- Quy chế tuyển sinh của Bộ Giáo dục và Đào tạo.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `kich-ban-tu-van-tuyen-sinh` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

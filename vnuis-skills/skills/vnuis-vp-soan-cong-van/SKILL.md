---
name: "vnuis-vp-soan-cong-van"
description: "Dùng khi cần ban hành công văn đi đúng thể thức Nghị định 30/2020/NĐ-CP: phúc đáp, đề nghị phối hợp, thông báo, giải trình với cơ quan ngoài trường hoặc giữa các đơn vị trong trường."
---

# Soạn công văn đi

## Khi nào dùng
Khi cần ban hành văn bản hành chính để trao đổi công việc: phúc đáp công văn đến, đề nghị phối hợp,
thông báo, giải trình, báo cáo đột xuất.

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

- **Đơn vị thường dùng:** Phòng Tổ chức và Quản trị; mọi đơn vị cần phát hành công văn.
- **Nghiệp vụ trong phiếu CES:** "Hành chính: Soạn thông báo, công văn, giấy mời, lịch công tác" (sheet `03_KS_TCQT`). Tần suất gợi ý: Theo chu kỳ/kế hoạch. Đầu vào gợi ý: Yêu cầu; mẫu văn bản; danh sách nhận; mốc thời gian. Khó khăn gợi ý: Tài liệu phân tán, nhiều định dạng; Đọc và đối chiếu thủ công mất thời gian; Dễ bỏ sót trường dữ liệu/phiên bản; Đầu ra phụ thuộc kinh nghiệm từng cá nhân. Đây là gợi ý có sẵn của CES, chưa phải xác nhận của đơn vị.

**Điều chỉnh khi dùng cho VNU-IS**
- Phần đầu văn bản theo cơ quan chủ quản: ĐẠI HỌC QUỐC GIA HÀ NỘI / TRƯỜNG QUỐC TẾ. Số hiệu theo mẫu `…/TQT-…` của skill TC&QT sẵn có `[CẦN XÁC MINH]` (C1); luôn để trống số và ngày cho người có thẩm quyền điền.
- Báo cáo hiện trạng hoặc công văn đề xuất chính sách gửi ĐHQGHN (có số liệu khảo sát và kiến nghị đánh số): nếu người dùng đã có skill "Trợ lý soạn báo cáo/công văn gửi ĐHQGHN (TC&QT)" thì dùng skill đó cho loại này; skill hiện tại dành cho công văn thông thường.
- Thông báo, giấy mời, lịch công tác là các nghiệp vụ trong cùng dòng phiếu: dùng các skill vnuis-vp-soan-thong-bao, vnuis-vp-soan-giay-moi, vnuis-vp-lap-lich-cong-tac-tuan.
- Công văn gửi đối tác nước ngoài: soạn bản Việt, rồi chuyển qua vnuis-tt-dich-song-ngu-va-thuat-ngu; không dịch thẳng tên chức danh ký.

**Chờ xác nhận khi khảo sát**
- Mẫu công văn đang dùng và người ký, ủy quyền (C1).
- Có phát hành qua E-Office không (C5).

Nếu người dùng chưa trả lời mục chờ xác nhận liên quan, hỏi lại; không tự điền giả định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `loai_cong_van` | Phúc đáp / Đề nghị / Thông báo / Giải trình / Báo cáo | Có |
| `trich_yeu` | Trích yếu nội dung (1 dòng, sau "V/v") | Có |
| `noi_dung` | Các ý chính cần truyền đạt, dạng gạch đầu dòng | Có |
| `cong_van_den` | Số, ký hiệu, ngày tháng công văn đến cần phúc đáp (nếu loại Phúc đáp) | Không |
| `noi_nhan` | Danh sách nơi nhận (cơ quan + lưu) | Có |
| `nguoi_ky` | Hiệu trưởng / Phó Hiệu trưởng / Trưởng phòng (thừa ủy quyền) | Có |
| `do_khan` | Thường / Khẩn / Thượng khẩn / Hỏa tốc | Không (mặc định: Thường) |
| `co_quan_chu_quan` | Cơ quan chủ quản: Đại học Quốc gia Hà Nội (đã điền sẵn) | Không (mặc định: ĐHQGHN) |
| `co_quan_ban_hanh` | Cơ quan ban hành: Trường Quốc tế – ĐHQGHN (đã điền sẵn); ghi thêm đơn vị soạn thảo nếu khác | Không (mặc định: Trường Quốc tế – ĐHQGHN) |
| `dia_danh` | Địa danh ghi ở dòng ngày tháng năm (mặc định: Hà Nội) | Không (mặc định: Hà Nội) |
| `so_van_ban` | Số, ký hiệu văn bản đã được cấp (để trống nếu chưa cấp; không tự đặt) | Không |

### Thông tin VNU-IS đã điền sẵn (không hỏi lại)

| Mục | Giá trị mặc định |
|---|---|
| Cơ quan chủ quản; Trường; địa danh | Đại học Quốc gia Hà Nội (ĐHQGHN); Trường Quốc tế – ĐHQGHN (VNU – International School); Hà Nội |
| Đơn vị sử dụng và phối hợp | Phòng Tổ chức và Quản trị; mọi đơn vị cần phát hành công văn |
| Cơ sở | Xuân Thủy (Cầu Giấy); Phan Tây Nhạc (Xuân Phương); Hòa Lạc (tòa HT1, Khu Đô thị ĐHQGHN). Ghi rõ cơ sở khi nội dung gắn địa điểm |
| Ngôn ngữ đầu ra | Tiếng Việt là bản gốc; thêm tiếng Anh cho đối tác, người học quốc tế hoặc khi được yêu cầu |
| Hệ thống nguồn dữ liệu có trên website | E-Office (văn bản điều hành). Skill không kết nối hệ thống, chỉ dùng file xuất/tải lên (C5) |
| Người duyệt và ký | Ghi theo vai trò (Trưởng phòng, Phó Hiệu trưởng phụ trách, Hiệu trưởng); tuyến duyệt và thẩm quyền ký chờ C1, C6 |

Nguồn: website và phiếu CES; đổi theo khảo sát thì sửa tại đây và trong `references/boi-canh-vnuis.md`.

## Quy trình

*⏱ là ước tính ban đầu của bộ gốc, chưa đo tại VNU-IS; hiệu chỉnh sau khảo sát.*

**Bước 1. Xác định loại công văn và yêu cầu đặc thù**
- Làm gì: Đọc `loai_cong_van`, xác định tập yêu cầu riêng của từng loại: Phúc đáp → bắt buộc có công văn đến để trích dẫn; Đề nghị → nêu rõ đề xuất và thời hạn mong hồi âm; Thông báo → nội dung ngắn, rõ đối tượng và thời hạn; Giải trình → nêu rõ vấn đề được yêu cầu giải trình kèm lập luận; Báo cáo → trình bày đúng nội dung được giao, có số liệu.
- Dùng input: `loai_cong_van`, `cong_van_den` (bắt buộc khi loại là Phúc đáp).
- Vai trò: Chuyên viên Phòng TC&QT (văn phòng – văn thư) · AI hỗ trợ: phân tích input, xác định yêu cầu · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Loại công văn quyết định giọng văn và thẩm quyền ký — Giải trình/Báo cáo gửi cấp trên thường do Hiệu trưởng ký; Đề nghị giữa các đơn vị trong trường có thể do Trưởng phòng ký thừa ủy quyền.
- → Kết quả bước: Xác nhận loại công văn + danh sách trường input bắt buộc tương ứng.

**Bước 2. Thu thập và đối chiếu dữ liệu đầu vào**
- Làm gì: Rà soát `noi_dung` — mỗi gạch đầu dòng phải là một ý độc lập, kiểm tra số liệu (ngày tháng, số lượng người, kinh phí) có nhất quán với nhau và khớp với `cong_van_den`; kiểm tra `noi_nhan` có đủ cơ quan nhận chính và các nơi lưu (VT, đơn vị soạn); kiểm tra `nguoi_ky` có thẩm quyền ký loại công văn này theo quy chế phân cấp của trường.
- Dùng input: `noi_dung`, `cong_van_den`, `noi_nhan`, `nguoi_ky`.
- Vai trò: Chuyên viên Phòng TC&QT (văn phòng – văn thư) (Trưởng phòng kiểm tra lại) · AI hỗ trợ: đối chiếu chéo tự động · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: Bẫy thường gặp — chép sai một ký tự trong số/ký hiệu/ngày công văn đến; nơi nhận thiếu dòng "Lưu: VT" khiến văn thư không có bản lưu; mốc thời hạn trong nội dung (vd "trước ngày 20/10/2026") đã qua so với ngày ban hành dự kiến.
- → Kết quả bước: Bảng đối chiếu dữ liệu đầu vào đã kiểm chuẩn, kèm danh sách lỗi cần bổ sung (nếu có).

**Bước 3. Dựng phần đầu văn bản theo thể thức NĐ 30/2020**
- Làm gì: Dùng Mẫu 1.5 Phụ lục III Nghị định 30: bên trái là cơ quan chủ quản trực tiếp (nếu có), cơ quan ban hành; bên phải là quốc hiệu, tiêu ngữ. Dưới cơ quan là số, ký hiệu và trích yếu V/v; dưới tiêu ngữ là địa danh/ngày. Số đã cấp lấy đúng hồ sơ văn thư; chưa cấp để trống. Ký hiệu công văn chỉ gồm mã cơ quan và mã đơn vị soạn/lĩnh vực, không dùng chữ CV. Không đặt phòng soạn thảo thay tên cơ quan ban hành. Nếu có độ khẩn được xác nhận, bố trí dấu ở ô 10a Phụ lục I. Phần đầu văn bản lấy từ `co_quan_chu_quan` (nếu có), `co_quan_ban_hanh`, `dia_danh`, `so_van_ban` (để dòng dấu chấm nếu chưa cấp số).
- Dùng input: `trich_yeu`, `noi_nhan` (xác định đối tượng "Kính gửi"), `do_khan`, `co_quan_chu_quan`, `co_quan_ban_hanh`, `dia_danh`, `so_van_ban`.
- Vai trò: Chuyên viên Phòng TC&QT (văn phòng – văn thư) · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Số văn bản phải lấy từ sổ đăng ký văn bản đi — không tự đặt số trùng; trích yếu viết sau "V/v", không có dấu chấm cuối câu; "Kính gửi" ghi đúng tên cơ quan như trong `noi_nhan`.
- → Kết quả bước: Khung phần đầu văn bản đã lắp đủ các thành phần thể thức.

**Bước 4. Soạn nội dung theo bố cục 3 phần**
- Làm gì: (a) Mở đầu — một đoạn nêu lý do/căn cứ ban hành; nếu là Phúc đáp, mở bằng "Phúc đáp Công văn số ... ngày ... của ... về việc ..."; (b) Nội dung chính — chuyển từng gạch đầu dòng trong `noi_dung` thành các điểm đánh số 1., 2., 3..., mỗi điểm một ý trọn vẹn, câu văn hành chính với động từ chuẩn ("đồng ý", "cử", "đề nghị"); (c) Kết thúc — một câu đề nghị phối hợp/hồi âm kèm lời cảm ơn, kết bằng ký hiệu "./.".
- Dùng input: `loai_cong_van`, `noi_dung`, `cong_van_den`.
- Vai trò: Chuyên viên Phòng TC&QT (văn phòng – văn thư) · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Mỗi điểm đánh số chỉ chứa MỘT ý; viết tắt (vd "TC&QT") phải giải thích đầy đủ ở lần xuất hiện đầu tiên; mốc thời gian trong nội dung thống nhất định dạng ngày/tháng/năm.
- → Kết quả bước: Dự thảo nội dung 3 phần hoàn chỉnh.

**Bước 5. Soạn nơi nhận và khối chữ ký**
- Làm gì: Liệt kê nơi nhận: dòng "- Như trên;" (hoặc "- Như Kính gửi;"), tiếp theo các nơi nhận để biết/lưu, kết thúc bằng "- Lưu: VT, [mã đơn vị]."; khối chữ ký phía bên phải: Phó Hiệu trưởng ký thay → "KT. HIỆU TRƯỞNG" / "PHÓ HIỆU TRƯỞNG"; Trưởng phòng ký thừa ủy quyền → "TUQ. HIỆU TRƯỞNG" / "TRƯỞNG PHÒNG [tên phòng]"; bản trình ký ghi họ tên người dự kiến ký và chừa khoảng trống ký.
- Dùng input: `noi_nhan`, `nguoi_ky`.
- Vai trò: Chuyên viên Phòng TC&QT (văn phòng – văn thư) · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Thừa lệnh (TL.) phải có căn cứ giao ký trong quy chế làm việc/quy chế văn thư; thừa ủy quyền (TUQ.) phải có văn bản ủy quyền giới hạn thời gian và nội dung, không được ủy quyền lại. Kiểm tra căn cứ trước khi chọn ký hiệu; nơi nhận thiếu đơn vị lưu thì văn thư không có bản lưu.
- → Kết quả bước: Phần nơi nhận và khối chữ ký đúng thẩm quyền.

**Bước 6. Kiểm tra theo danh mục kiểm thể thức**
- Làm gì: Đối chiếu từng mục danh mục kiểm: quốc hiệu – tiêu ngữ đúng vị trí, chữ in hoa; đủ số, ký hiệu, ngày tháng, trích yếu; trích dẫn công văn đến (nếu Phúc đáp); nội dung đánh số thứ tự, chính tả, số liệu; nơi nhận đầy đủ; thẩm quyền ký phù hợp; dấu độ khẩn (nếu có).
- Dùng input: toàn bộ input (đối chiếu chéo).
- Vai trò: Chuyên viên Phòng TC&QT (văn phòng – văn thư) (Trưởng phòng kiểm tra lại) · AI hỗ trợ: quét lỗi theo danh mục kiểm · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: Đọc soát chính tả một lượt riêng (tên cơ quan, tên người); kiểm tra lại số/ký hiệu/ngày công văn đến một lần nữa vì đây là lỗi sai phổ biến nhất.
- → Kết quả bước: Kết quả đối chiếu thể thức (giữ nội bộ, không xuất kèm file) + danh sách lỗi cần sửa (nếu có), trả về bước tương ứng để chỉnh.

**Bước 7. Xuất bản văn bản hoàn chỉnh trình ký**
- Làm gì: Ghép phần đầu văn bản + nội dung + nơi nhận + khối chữ ký thành văn bản hoàn chỉnh file theo định dạng đầu ra của skill; thực hiện đối chiếu nội bộ, không xuất kèm danh mục kiểm; chuyển cho chuyên viên soạn xác nhận rồi trình người ký duyệt (human gate).
- Dùng input: toàn bộ.
- Vai trò: Chuyên viên Phòng TC&QT (văn phòng – văn thư) chuẩn bị, người có thẩm quyền ký · AI hỗ trợ: tổng hợp hồ sơ, soạn phiếu trình/tờ trình đầy đủ · ⏱ ~15–30 phút chuẩn bị + chờ duyệt (ước tính)
- Lưu ý nghiệp vụ: Sau khi đã đăng ký số vào sổ văn bản đi thì không tự ý đổi số, ký hiệu.
- → Kết quả bước: Văn bản công văn hoàn chỉnh; phần kiểm tra giữ nội bộ, sẵn sàng trình ký / xuất file Word.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Yêu cầu soạn công văn"/] --> B1["Bước 1: Xác định loại công văn và yêu cầu đặc thù"]
    B1 --> B2["Bước 2: Thu thập và đối chiếu dữ liệu đầu vào"]
    B2 --> DP{"Công văn phúc đáp?"}
    DP -->|Có| B3A["Ghi nhận số, ký hiệu, ngày công văn đến để trích dẫn"]
    DP -->|Không| B3["Bước 3: Dựng phần đầu văn bản theo thể thức"]
    B3A --> B3
    B3 --> B4["Bước 4: Soạn nội dung theo bố cục 3 phần"]
    B4 --> B5["Bước 5: Soạn nơi nhận và khối chữ ký"]
    B5 --> B6["Bước 6: Kiểm tra theo danh mục kiểm thể thức"]
    B6 --> B7["Bước 7: Xuất bản văn bản hoàn chỉnh trình ký"]
    B7 --> HG["👤 Chuyên viên soạn xác nhận, người ký duyệt"]
    HG --> OUT[["Văn bản công văn hoàn chỉnh trình ký"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm danh mục kiểm/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Nội dung và số liệu trong output khớp đúng với Input đã cho (không thêm, bớt hay suy diễn)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức và định dạng theo Nghị định 30/2020/NĐ-CP về công tác văn thư.
- [ ] Căn cứ pháp lý được trích dẫn đầy đủ và còn hiệu lực
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra và duyệt trước khi phát hành; bản soạn chưa được coi là đã ký/đã duyệt
- [ ] Số văn bản phải lấy từ sổ đăng ký văn bản đi — không tự đặt số trùng
- [ ] "Kính gửi" ghi đúng tên cơ quan như trong `noi_nhan`
- [ ] Viết tắt (vd "TC&QT") phải giải thích đầy đủ ở lần xuất hiện đầu tiên

## Căn cứ & lưu ý
- Nghị định 30/2020/NĐ-CP về công tác văn thư.
- Công văn có độ khẩn được xác nhận dùng KHẨN/THƯỢNG KHẨN/HỎA TỐC tại ô 10a theo Phụ lục I.
- Ví dụ trong skill chỉ để minh họa; không đưa dữ liệu cá nhân thật vào ví dụ. Tên Trường, cơ quan chủ quản và địa danh dùng đúng bảng thông tin VNU-IS đã điền sẵn.

## Quản trị phiên bản
- Phiên bản gói VNU-IS `0.4.2` (cập nhật 2026-10-11), dựa trên skill gốc `soan-cong-van` bản `1.3.2`; hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.

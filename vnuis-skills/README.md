# Bộ skill AI cho Trường Quốc tế – ĐHQGHN (VNU-IS) — bản v0.4

Gói do CES GLOBAL xây dựng dựa trên bộ 171 skill cho phòng ban trường đại học (https://github.com/phamtruong91/university-skills-framework), chỉnh cho bối cảnh VNU-IS.

## Trạng thái — đọc trước khi dùng

**Đây là bản v0.4.2 chờ khảo sát, chưa phải bản chính thức.** Nội dung được dựng từ ba nguồn: website công khai của Trường (đọc ngày 10/10/2026), phiếu khảo sát CES (còn trống, chưa có dữ liệu thật của đơn vị) và skill soạn báo cáo/công văn TC&QT do người dùng cung cấp. Chưa có văn bản nội bộ của VNU-IS hay ĐHQGHN. Chưa chạy thử với tài liệu thật của Trường.

Những chỗ chưa biết được ghi `[CẦN XÁC MINH]` hoặc đánh mã C1–C8. Skill hỏi lại thay vì tự điền. Sau mỗi phiên khảo sát, cập nhật skill tương ứng bằng `docs/CAU_HOI_CAN_XAC_NHAN.md`.

**Thay đổi ở v0.4.2 so với v0.4.1** (sau thử nghiệm 3 skill với dữ liệu giả lập 10–20 trang; xem `docs/BAO_CAO_TEST_v0.4.2.md`, dữ liệu thử ở `tests/`):
- Bộ chạy (`runtime/runner.py`): bước tự kiểm tra nay nhận cả dữ liệu gốc (cắt ở 24.000 ký tự) để đối chiếu số, tên, ngày; trước đó chỉ thấy bản soạn nên không bắt được số sai. Dòng "đã qua cổng duyệt" và ghi chú nội bộ không còn lẫn vào file xuất (ghi chú tách sang file riêng).
- Thêm `runtime/tools/likert_stats.py` (tính sẵn thống kê khảo sát: bỏ trùng, ngoài thang, câu đảo, nhóm nhỏ) và `runtime/tools/mask_pii.py` (che số điện thoại, email, số giấy tờ). Model nhỏ không cộng đúng vài trăm dòng dữ liệu thô.
- Bổ sung quy tắc cho 3 skill đã thử: hợp nhất báo cáo đơn vị (không cộng trùng, tính lại tỷ lệ, kỳ báo cáo lệch), phân tích khảo sát (câu đảo, tỷ lệ phản hồi, nhóm nhỏ, ý kiến chứa thông tin cá nhân), soạn biên bản họp (chủ trì đổi ý, việc thuộc thẩm quyền cấp trên, phiếu không khớp, nội dung nhạy cảm).
- **Chưa thử với model thật**: toàn bộ thử nghiệm do trợ lý soạn theo skill, không phải GLM/DeepSeek/Qwen; xem giới hạn trong báo cáo thử nghiệm.

**Thay đổi ở v0.4.1 so với v0.3** (sau đợt rà soát chi tiết 11/10/2026; xem `docs/BAO_CAO_RA_SOAT.md`):
- Thêm thư mục `runtime/` để chạy skill qua API model nhỏ (GLM-5.3-Flash, DeepSeek-V4-Flash, Qwen3.5-Flash): biên dịch skill thành JSON, bộ chọn skill, bộ chạy có tự kiểm tra, xuất Word/Excel. Xem `runtime/README.md`. Chưa chạy với model thật.
- Căn cứ pháp lý: thêm **Luật Giáo dục đại học 125/2025/QH15** (hiệu lực 01/01/2026, thay Luật 2012) và **Thông tư 58/2026/TT-BGDĐT**; bỏ các dẫn Luật GDĐH 2012/2018 trong thân skill. Nguồn là trang tổng hợp, chưa đối chiếu toàn văn chính thức; chưa đọc các nghị định hướng dẫn.
- Hội đồng KH&ĐT chỉ còn tư vấn (Điều 18) và hội đồng trường công lập chấm dứt từ 01/01/2026 (Điều 46): 5 skill hội đồng và các skill nhắc "Hội đồng có thẩm quyền" đã chỉnh; "Hội đồng có thẩm quyền (C6)" đổi thành "cấp có thẩm quyền (C6)".
- Tuyến báo cáo và thẩm quyền mở ngành không còn viết cứng "gửi Bộ GD&ĐT" ở 7 skill; ghi "cơ quan tiếp nhận (ĐHQGHN hoặc Bộ GD&ĐT, chờ C2)". Đây là chỗ chờ khảo sát, không phải kết luận.
- Bỏ dòng "không dùng tên thật của trường/cá nhân" (kế thừa từ bộ mẫu) ở 166 skill vì mâu thuẫn với thông tin Trường đã điền sẵn.
- Chuẩn hóa mục kiểm cổng duyệt ở 19 skill; thay các từ tiếng Anh còn sót (checklist, KPI, brief, ticket, SLA, rubric...) ở các skill liên quan; sửa 167 liên kết `quy-tac-chung.md`; thêm chỉ dẫn chạy qua API (không có công cụ tạo file).

**Thay đổi ở v0.3 so với v0.2:**
- Đặt lại tên cả 167 skill theo quy ước `vnuis-<nhóm>-<việc>` (20 nhóm nghiệp vụ, xem `docs/DANH_MUC_SKILL.md`); bỏ từ tiếng Anh và viết tắt khó hiểu (funnel, triage, PMO, grant, audit, FAQ, executive brief...). Tên cũ lưu trong `references/version.json` (`previous_name`) và cột "Tên cũ" của danh mục.
- Thay tên đơn vị của bộ gốc bằng đơn vị thực tế của VNU-IS: Phòng TCCB, HCTH, TCKT, QTTB, CTSV, Khảo thí & ĐBCL, Thanh tra – Pháp chế nay ghi là các mảng của Phòng TC&QT hoặc Phòng Đào tạo; "Hội đồng trường" ghi là hội đồng có thẩm quyền (chờ C6); ví dụ "Trường Đại học A" đổi thành Trường Quốc tế – ĐHQGHN, tên khoa giả lập đổi sang sáu khoa thật.
- Mỗi skill có bảng "Thông tin VNU-IS đã điền sẵn" (cơ quan chủ quản, tên Trường, địa danh, đơn vị, cơ sở, mô hình đào tạo, ngôn ngữ, hệ thống, người duyệt) và `quy-cach-dau-ra.md` có phần đầu văn bản đã điền; các input đã xác định (cơ quan chủ quản, cơ quan ban hành, địa danh) không còn bắt buộc nhập.
- Chuẩn hóa tiêu đề mục (Đầu vào/Quy trình/Luồng/Human gate/Giới hạn) và ghi rõ thời gian từng bước là ước tính của bộ gốc.

**Khác v0.1:** v0.1 có 41 skill; v0.2 mở rộng lên 167 skill, phủ toàn bộ các skill áp dụng được trong bộ 171, thêm 7 skill mới. 19 skill gốc chưa đưa vào vì chưa có dấu hiệu Trường cần (xem sheet "Trạng thái 171 skill gốc"). 3 skill (`vnuis-phapche-ke-hoach-thanh-tra-nam`, `vnuis-phapche-soan-ket-luan-thanh-tra`, `vnuis-htqt-ke-hoach-doan-ra-vao`) được đưa vào dù ban đầu thuộc nhóm chưa chắc, vì phiếu CES giao chức năng thanh tra – pháp chế và hợp tác quốc tế cho hai phòng; có thể bỏ nếu khảo sát cho thấy Trường không làm.

## Quy ước đặt tên

`vnuis-<nhóm>-<việc>`. Nhóm là lĩnh vực nghiệp vụ, không phải tên phòng, vì một việc có thể do nhiều đơn vị làm. Phần "việc" bắt đầu bằng động từ (soan, lap, bao-cao, ke-hoach, theo-doi, kiem-tra, ra-soat, phan-tich, to-chuc). Muốn tìm việc gì thì gõ nhóm hoặc động từ; ví dụ mọi skill khảo thí bắt đầu bằng `vnuis-khaothi-`. Bảng đầy đủ: `docs/DANH_MUC_SKILL.md` và sheet "Danh mục tra cứu" trong file Excel.

## Nội dung gói

| Thành phần | Số lượng | Ghi chú |
|---|---|---|
| Skill chỉnh sâu từ bộ gốc (tiền tố `vnuis-`) | 152 | Thêm mục "Bối cảnh riêng của VNU-IS": đơn vị dùng, nghiệp vụ trong phiếu, điều chỉnh, điều chờ xác nhận |
| Skill mới | 15 | Các khoảng trống nhìn thấy trong phiếu và website |
| Lớp ngữ cảnh dùng chung | 1 (nằm trong mỗi skill) | `references/boi-canh-vnuis.md`: cơ cấu, chương trình, hệ thống, thuật ngữ, nguyên tắc, danh mục chờ xác nhận |
| Bảng đối chiếu 74 dòng phiếu CES và trạng thái 171 skill gốc | 1 | `docs/BANG_DOI_CHIEU_NGHIEP_VU.xlsx` |
| Tài liệu phân tích | 1 | `docs/PHAN_TICH_VNUIS.md` |
| Câu hỏi cần xác nhận | 1 | `docs/CAU_HOI_CAN_XAC_NHAN.md` |
| Runtime gọi API model | 1 | `runtime/`: compile, router, runner, export, eval, mock |

Mỗi thư mục trong `skills/` là một skill đủ dùng độc lập (SKILL.md, references/, agents/). Skill VNU-IS trỏ tới nhau bằng tên có tiền tố `vnuis-`; tên không có tiền tố là skill gốc ngoài gói.

## Skill theo nhóm nghiệp vụ

**`vp` — Văn phòng – văn bản, họp, lịch, báo cáo điều hành (17):** `vnuis-vp-bao-cao-tong-ket-nam-hoc-toan-truong`, `vnuis-vp-bao-cao-tong-ket-van-phong`, `vnuis-vp-chuan-bi-hop-theo-doi-nhiem-vu`, `vnuis-vp-tom-tat-trinh-lanh-dao`, `vnuis-vp-hop-nhat-bao-cao-don-vi`, `vnuis-vp-ke-hoach-nam-hoc-toan-truong`, `vnuis-vp-lap-lich-cong-tac-tuan`, `vnuis-vp-lap-phieu-trinh-ky`, `vnuis-vp-ra-soat-du-thao-van-ban`, `vnuis-vp-quan-ly-so-van-ban-di-den`, `vnuis-vp-soan-bien-ban-hop`, `vnuis-vp-soan-cong-van`, `vnuis-vp-soan-giay-moi`, `vnuis-vp-soan-ke-hoach-cong-tac`, `vnuis-vp-soan-quyet-dinh-hanh-chinh`, `vnuis-vp-soan-thong-bao`, `vnuis-vp-soan-to-trinh`.

**`nhansu` — Tổ chức cán bộ – nhân sự, thi đua khen thưởng (15):** `vnuis-nhansu-tong-hop-danh-gia-vien-chuc`, `vnuis-nhansu-bao-cao-thi-dua-khen-thuong`, `vnuis-nhansu-bao-cao-thong-ke-nhan-su` (mới), `vnuis-nhansu-de-an-vi-tri-viec-lam`, `vnuis-nhansu-lap-ho-so-de-nghi-khen-thuong`, `vnuis-nhansu-soan-hop-dong-lam-viec`, `vnuis-nhansu-ke-hoach-dao-tao-boi-duong-can-bo`, `vnuis-nhansu-lap-phieu-danh-gia-vien-chuc`, `vnuis-nhansu-quy-trinh-bo-nhiem`, `vnuis-nhansu-quy-trinh-tuyen-dung`, `vnuis-nhansu-soan-quyet-dinh-cu-di-dao-tao`, `vnuis-nhansu-soan-quyet-dinh-dieu-dong`, `vnuis-nhansu-soan-quyet-dinh-khen-thuong-ky-luat-vien-chuc`, `vnuis-nhansu-soan-quyet-dinh-nang-luong`, `vnuis-nhansu-soan-thong-bao-tuyen-dung`.

**`phapche` — Pháp chế – thanh tra (6):** `vnuis-phapche-ke-hoach-thanh-tra-nam`, `vnuis-phapche-soan-ket-luan-thanh-tra`, `vnuis-phapche-soan-quy-che-to-chuc-hoat-dong-don-vi`, `vnuis-phapche-soan-quyet-dinh-giai-quyet-khieu-nai`, `vnuis-phapche-tham-dinh-phap-ly-van-ban`, `vnuis-phapche-theo-doi-thay-doi-van-ban-phap-quy`.

**`taichinh` — Kế hoạch – tài chính (7):** `vnuis-taichinh-bao-cao-cong-khai-tai-chinh`, `vnuis-taichinh-bao-cao-quyet-toan`, `vnuis-taichinh-bao-cao-tai-chinh`, `vnuis-taichinh-kiem-tra-chung-tu-thanh-toan`, `vnuis-taichinh-lap-du-toan-nam`, `vnuis-taichinh-phan-tich-chenh-lech-ngan-sach`, `vnuis-taichinh-soan-thong-bao-muc-thu-hoc-phi`.

**`csvc` — Cơ sở vật chất – mua sắm, tài sản (5):** `vnuis-csvc-lap-bien-ban-kiem-ke-tai-san`, `vnuis-csvc-lap-bien-ban-nghiem-thu-thiet-bi`, `vnuis-csvc-soan-hop-dong-mua-sam`, `vnuis-csvc-ke-hoach-bao-tri`, `vnuis-csvc-ke-hoach-mua-sam`.

**`cntt` — Hạ tầng CNTT, an toàn thông tin, chuyển đổi số (4):** `vnuis-cntt-bao-cao-chuyen-doi-so`, `vnuis-cntt-phan-loai-yeu-cau-ho-tro`, `vnuis-cntt-ke-hoach-phat-trien-cntt`, `vnuis-cntt-soan-quy-che-an-toan-thong-tin`.

**`dt` — Đào tạo (đại học, chương trình, liên kết) (17):** `vnuis-dt-ra-soat-tien-do-tot-nghiep`, `vnuis-dt-bao-cao-3-cong-khai`, `vnuis-dt-bao-cao-dao-tao-dinh-ky`, `vnuis-dt-doi-chieu-cong-nhan-tin-chi` (mới), `vnuis-dt-soan-de-an-mo-nganh`, `vnuis-dt-soan-de-cuong-hoc-phan`, `vnuis-dt-ke-hoach-dao-tao-nam-hoc`, `vnuis-dt-xay-dung-khung-chuong-trinh`, `vnuis-dt-lap-thoi-khoa-bieu`, `vnuis-dt-lap-ma-tran-chuan-dau-ra`, `vnuis-dt-phan-cong-giang-day`, `vnuis-dt-theo-doi-chuong-trinh-lien-ket` (mới), `vnuis-dt-soan-quy-che-dao-tao`, `vnuis-dt-soan-quyet-dinh-xu-ly-hoc-vu`, `vnuis-dt-soan-quyet-dinh-tot-nghiep`, `vnuis-dt-tong-hop-so-lieu-3-cong-khai`, `vnuis-dt-theo-doi-tieng-anh-du-bi` (mới).

**`ctsv` — Công tác sinh viên (10):** `vnuis-ctsv-bao-cao-cong-tac-sinh-vien-nam`, `vnuis-ctsv-ke-hoach-ngay-hoi-viec-lam`, `vnuis-ctsv-ke-hoach-tuan-sinh-hoat-cong-dan`, `vnuis-ctsv-khao-sat-viec-lam-sau-tot-nghiep`, `vnuis-ctsv-lap-phieu-danh-gia-ren-luyen`, `vnuis-ctsv-soan-quyet-dinh-cap-hoc-bong`, `vnuis-ctsv-soan-quyet-dinh-khen-thuong-ky-luat`, `vnuis-ctsv-soan-thong-bao-hoc-bong`, `vnuis-ctsv-tong-hop-diem-ren-luyen`, `vnuis-ctsv-phan-loai-yeu-cau-sinh-vien`.

**`khaothi` — Khảo thí (6):** `vnuis-khaothi-lap-bien-ban-phong-thi`, `vnuis-khaothi-ke-hoach-to-chuc-thi`, `vnuis-khaothi-phan-tich-ket-qua-thi`, `vnuis-khaothi-quy-trinh-ngan-hang-de-thi`, `vnuis-khaothi-soan-quyet-dinh-phan-cong-thi`, `vnuis-khaothi-soan-quyet-dinh-phuc-khao`.

**`dbcl` — Đảm bảo chất lượng, kiểm định (4):** `vnuis-dbcl-bao-cao-dam-bao-chat-luong-nam`, `vnuis-dbcl-bao-cao-tu-danh-gia`, `vnuis-dbcl-lap-danh-muc-minh-chung`, `vnuis-dbcl-ke-hoach-cai-tien-chat-luong`.

**`sdh` — Sau đại học (5):** `vnuis-sdh-bao-cao-dao-tao`, `vnuis-sdh-lap-bien-ban-bao-ve-luan-van`, `vnuis-sdh-ke-hoach-dao-tao`, `vnuis-sdh-soan-quyet-dinh-hoi-dong-bao-ve`, `vnuis-sdh-soan-thong-bao-tuyen-sinh`.

**`ts` — Tuyển sinh (8):** `vnuis-ts-bao-cao-ket-qua-tuyen-sinh`, `vnuis-ts-de-bai-chien-dich-tuyen-sinh`, `vnuis-ts-soan-de-an-tuyen-sinh`, `vnuis-ts-hoi-dap-tuyen-sinh`, `vnuis-ts-theo-doi-pheu-thi-sinh`, `vnuis-ts-kich-ban-tu-van-tuyen-sinh`, `vnuis-ts-ra-soat-nhat-quan-thong-tin` (mới), `vnuis-ts-soan-thong-bao-tuyen-sinh-dai-hoc`.

**`tt` — Truyền thông, thương hiệu, sự kiện (11):** `vnuis-tt-viet-bai-truyen-thong`, `vnuis-tt-lap-lich-noi-dung`, `vnuis-tt-dich-song-ngu-va-thuat-ngu`, `vnuis-tt-ke-hoach-hoat-dong-bao-chi`, `vnuis-tt-ke-hoach-quan-tri-thuong-hieu`, `vnuis-tt-ke-hoach-to-chuc-su-kien`, `vnuis-tt-ke-hoach-truyen-thong-nam`, `vnuis-tt-kich-ban-khanh-tiet`, `vnuis-tt-kich-ban-video`, `vnuis-tt-phan-tich-chi-so-truyen-thong` (mới), `vnuis-tt-bo-tai-lieu-bao-chi-su-kien`.

**`khcn` — Khoa học công nghệ, sở hữu trí tuệ (17):** `vnuis-khcn-bao-cao-khcn-htqt-nam`, `vnuis-khcn-bao-cao-nghiem-thu-de-tai`, `vnuis-khcn-bao-cao-tien-do-de-tai`, `vnuis-khcn-bien-soan-giao-trinh`, `vnuis-khcn-bien-tap-xuat-ban-an-pham`, `vnuis-khcn-lap-cau-truc-bai-bao`, `vnuis-khcn-lap-ho-so-cong-nhan-sang-kien`, `vnuis-khcn-lap-ho-so-so-huu-tri-tue`, `vnuis-khcn-lap-ho-so-quyet-toan-de-tai`, `vnuis-khcn-soan-hop-dong-thuc-hien-de-tai`, `vnuis-khcn-ke-hoach-hoi-thao`, `vnuis-khcn-bien-tap-ky-yeu-hoi-thao`, `vnuis-khcn-quan-tri-tap-chi`, `vnuis-khcn-theo-doi-nguon-tai-tro`, `vnuis-khcn-soan-thong-bao-dang-ky-de-tai`, `vnuis-khcn-soan-thuyet-minh-de-tai`, `vnuis-khcn-tong-quan-tai-lieu`.

**`htqt` — Hợp tác quốc tế (5):** `vnuis-htqt-bao-cao-hop-tac-quoc-te` (mới), `vnuis-htqt-lap-ho-so-doi-tac` (mới), `vnuis-htqt-ke-hoach-doan-ra-vao`, `vnuis-htqt-ke-hoach-trao-doi-nguoi-hoc` (mới), `vnuis-htqt-soan-mou-moa-song-ngu`.

**`thuvien` — Thông tin thư viện (2):** `vnuis-thuvien-bao-cao-cong-tac`, `vnuis-thuvien-ke-hoach-bo-sung-hoc-lieu`.

**`dmst` — Viện ĐMST&CGCN – đổi mới sáng tạo, chuyển giao, đào tạo liên tục (10):** `vnuis-dmst-bao-cao-dich-vu`, `vnuis-dmst-bao-cao-du-an-dinh-ky`, `vnuis-dmst-cap-chung-chi-dao-tao-lien-tuc`, `vnuis-dmst-danh-gia-hieu-qua-chuong-trinh-du-an` (mới), `vnuis-dmst-lap-ho-so-chuyen-giao-cong-nghe`, `vnuis-dmst-lap-ho-so-hop-dong-dich-vu`, `vnuis-dmst-ke-hoach-dao-tao-lien-tuc`, `vnuis-dmst-ke-hoach-uom-tao`, `vnuis-dmst-sang-loc-sang-kien` (mới), `vnuis-dmst-to-chuc-khoa-boi-duong-ngan-han`.

**`hd` — Hội đồng KH&ĐT (5):** `vnuis-hd-soan-bien-ban-hop`, `vnuis-hd-kiem-tra-ho-so-trinh-hoi-dong` (mới), `vnuis-hd-soan-nghi-quyet`, `vnuis-hd-lap-phieu-lay-y-kien`, `vnuis-hd-theo-doi-thuc-hien-ket-luan` (mới).

**`khoa` — Khoa, bộ môn (4):** `vnuis-khoa-bao-cao-tong-ket-nam-hoc`, `vnuis-khoa-ke-hoach-hoat-dong-trung-tam-thuc-hanh`, `vnuis-khoa-ke-hoach-nckh`, `vnuis-khoa-tro-ly-giang-day`.

**`dc` — Dùng chung – dữ liệu, khảo sát, dự án, tri thức (9):** `vnuis-dc-dong-goi-skill-tu-quy-trinh`, `vnuis-dc-hoi-dap-chinh-sach-co-trich-nguon`, `vnuis-dc-lap-danh-muc-kho-tri-thuc` (mới), `vnuis-dc-kiem-tra-chat-luong-du-lieu-bao-cao` (mới), `vnuis-dc-kiem-tra-day-du-ho-so`, `vnuis-dc-phan-tich-ket-qua-khao-sat`, `vnuis-dc-quan-tri-du-an`, `vnuis-dc-quan-ly-phien-ban-tai-lieu`, `vnuis-dc-thiet-ke-phieu-khao-sat`.

## Mức phủ của phiếu khảo sát (74 dòng, gồm 6 dòng trống "nghiệp vụ khác")

- Có skill chỉnh sâu: 47 dòng; chỉnh sâu một phần: 8.
- Có skill mới: 6 dòng; skill mới một phần: 4.
- Chờ khảo sát (chưa có skill riêng hoặc khoa tự đề xuất): 3; dòng trống chờ đơn vị đề xuất: 6.

Đối chiếu dựa trên tên và mô tả skill, chưa kiểm tra nội dung từng skill gốc. Với sáu khoa, phiếu chỉ có tên nhóm nghiệp vụ nên skill của khoa mới là điều chỉnh theo chức năng, chưa theo khảo sát.

## Kiểm tra đã làm

- Bộ kiểm tra cấu trúc của kho gốc (hợp đồng đóng gói, mục bắt buộc, liên kết, dung lượng SKILL.md, quy tắc xuất file): 167/167 skill đạt, 0 lỗi.
- Quét cấu trúc quy trình (bước, đầu vào, sơ đồ): 0 vấn đề.
- Quét tên nhân sự có trong phiếu CES: không có trong gói.

## Chưa làm

- Chưa chạy thử skill với tài liệu thật hoặc giả lập của Trường, nên chưa biết chất lượng đầu ra thực tế.
- Chưa đối chiếu văn bản pháp lý và quy chế của ĐHQGHN, VNU-IS.
- Chưa đọc từng trang con của website; thông tin chương trình, tuyển sinh lấy qua bản tóm tắt trang. Website tự mâu thuẫn về số chương trình (xem mục 3 của bối cảnh).
- Chưa tích hợp với E-Office, LMS hay nền tảng AI tư vấn của Trường; các skill chỉ làm việc với file người dùng cung cấp.
- Phần "Điều chỉnh khi dùng cho VNU-IS" của 119 skill thêm ở v0.2 viết theo chức năng đơn vị và website, mỏng hơn 33 skill ở v0.1 vốn bám từng dòng phiếu.

## Bước tiếp theo đề xuất

1. Dùng `docs/CAU_HOI_CAN_XAC_NHAN.md` trong các phiên khảo sát; xin 01–02 mẫu Input và Output đã ẩn thông tin cá nhân cho mỗi nghiệp vụ ưu tiên.
2. Xin văn bản căn cứ (C1, C2) để bỏ các dấu `[CẦN XÁC MINH]`.
3. Chọn 5–8 skill ưu tiên cao nhất, chạy thử với mẫu thật rồi hoàn thiện lên v1.0. Đừng bàn giao đồng loạt 167 skill: người dùng sẽ không biết bắt đầu từ đâu.
4. Bàn giao từng phòng một: chỉ giao skill của phòng đó.

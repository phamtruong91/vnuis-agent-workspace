# VNU-IS Agent Workspace

Không gian làm việc cho các trợ lý AI (agent) của **Trường Quốc tế – Đại học Quốc gia Hà Nội (VNU-IS)**. Hiện gồm một bộ phận chính: bộ kỹ năng (skill) hỗ trợ công việc hành chính, đào tạo, nghiên cứu và truyền thông của Nhà trường.

> **Trạng thái:** bản đề xuất v0.4.3, **chờ khảo sát và thẩm định**. Chưa kiểm thử với model thật; căn cứ pháp lý cần bộ phận pháp chế xác nhận trước khi dùng chính thức.

## Nội dung

| Thư mục | Mô tả |
|---|---|
| [`vnuis-skills/`](vnuis-skills/) | Bộ 167 skill theo 20 nhóm nghiệp vụ, kèm bộ chạy (`runtime/`), dữ liệu thử (`tests/`) và tài liệu (`docs/`) |

## Bộ skill

Mỗi skill mô tả một việc cụ thể (ví dụ soạn quyết định, lập kế hoạch, tổng hợp báo cáo) với đầu vào, quy trình, đầu ra, kiểm tra nội bộ và điểm cần người có thẩm quyền duyệt.

| Nhóm | Số skill | Nhóm | Số skill |
|---|---|---|---|
| Văn phòng (`vp`) | 17 | Tuyển sinh (`ts`) | 8 |
| Khoa học công nghệ (`khcn`) | 17 | Tài chính (`taichinh`) | 7 |
| Đào tạo (`dt`) | 17 | Pháp chế (`phapche`) | 6 |
| Nhân sự (`nhansu`) | 15 | Khảo thí (`khaothi`) | 6 |
| Truyền thông (`tt`) | 11 | Sau đại học (`sdh`) | 5 |
| Đổi mới sáng tạo (`dmst`) | 10 | Hợp tác quốc tế (`htqt`) | 5 |
| Công tác sinh viên (`ctsv`) | 10 | Hội đồng (`hd`) | 5 |
| Dùng chung (`dc`) | 9 | Cơ sở vật chất (`csvc`) | 5 |
| Khoa (`khoa`) | 4 | Đảm bảo chất lượng (`dbcl`) | 4 |
| Công nghệ thông tin (`cntt`) | 4 | Thư viện (`thuvien`) | 2 |

Định dạng đầu ra mặc định: Word (.docx) cho 139 skill, Excel (.xlsx) cho 27 skill, 1 skill đóng gói (.zip). Danh mục đầy đủ: [`docs/DANH_MUC_SKILL.md`](vnuis-skills/docs/DANH_MUC_SKILL.md).

## Thay đổi ở v0.4.3

- Viết lại mô tả của cả 167 skill theo hướng nêu **tình huống cần dùng**, ngắn gọn (trung bình khoảng 181 ký tự, trước đó khoảng 311), giúp bộ chọn skill nhận diện đúng hơn.
- Đưa mục "Khi nào dùng" lên đầu và thêm mục "Khi nào KHÔNG dùng" cho 36 skill dễ nhầm lẫn.
- Rà soát thể thức theo Nghị định 30/2020/NĐ-CP và căn cứ pháp lý; gắn cảnh báo cập nhật vào 10 skill có văn bản lỗi thời hoặc chưa nhất quán.

Kết quả đo bộ chọn skill bằng từ khóa trên 167 câu kiểm thử (do tác giả bộ skill viết nên có thể lạc quan):

| Chỉ số | v0.4.2 | v0.4.3 |
|---|---|---|
| Đúng ngay kết quả đầu | 0,802 | 0,868 |
| Đúng trong 3 kết quả đầu | 0,946 | 0,964 |
| Độ đúng khi chọn nhanh, không gọi model | 0,927 | 0,976 |

## Tài liệu

- [`docs/GHI_CHU_TOI_UU_MO_TA.md`](vnuis-skills/docs/GHI_CHU_TOI_UU_MO_TA.md): ghi chú tối ưu mô tả.
- [`docs/RA_SOAT_PHAP_LY_THE_THUC.md`](vnuis-skills/docs/RA_SOAT_PHAP_LY_THE_THUC.md): kết quả rà soát pháp lý và thể thức, danh sách việc cần xác nhận.
- [`docs/VNUIS_v0.4.3_doi_chieu_mo_ta_cu_moi.xlsx`](vnuis-skills/docs/VNUIS_v0.4.3_doi_chieu_mo_ta_cu_moi.xlsx): đối chiếu mô tả cũ và mới của từng skill.
- [`docs/VNUIS_v0.4.2_thong_ke_kiem_tra.xlsx`](vnuis-skills/docs/VNUIS_v0.4.2_thong_ke_kiem_tra.xlsx): thống kê và kiểm tra bộ skill.
- [`vnuis-skills/README.md`](vnuis-skills/README.md): hướng dẫn chi tiết và lịch sử các phiên bản trước.

## Giới hạn đã biết

- Chưa so sánh hiệu quả có/không có skill trên model thật; chưa đánh giá chất lượng văn bản đầu ra.
- Căn cứ pháp lý lấy từ nguồn thứ cấp, nhiều văn bản năm 2026 chưa đối chiếu toàn văn.
- Một số thông tin của Nhà trường còn ghi `[CẦN XÁC MINH]` hoặc mã C1–C8, chờ khảo sát.
- Sơ đồ quy trình, ký hiệu thời gian (⏱) và phần nội dung lặp giữa các skill chưa được tối ưu.

## Quy trình sử dụng khuyến nghị

1. Người phụ trách nghiệp vụ chọn skill phù hợp và cung cấp đầu vào.
2. Trợ lý AI soạn bản dự thảo; không tự coi là đã ký hoặc đã duyệt.
3. Người có thẩm quyền kiểm tra, đối chiếu căn cứ pháp lý còn hiệu lực rồi mới phát hành.

## Đơn vị thực hiện

Xây dựng bởi CES GLOBAL, dựa trên [university-skills-framework](https://github.com/phamtruong91/university-skills-framework), điều chỉnh cho bối cảnh VNU-IS. Người duy trì: phamtruong91.

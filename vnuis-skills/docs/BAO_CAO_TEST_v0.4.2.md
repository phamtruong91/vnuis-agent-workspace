# Báo cáo thử nghiệm 3 skill với dữ liệu giả lập (gói v0.4.2, 11/10/2026)

## 1. Thử cái gì, và thử như thế nào (đọc trước)

Ba bộ dữ liệu giả lập dài 12–19 trang, mỗi bộ cài sẵn các "bẫy" (số mâu thuẫn, phiếu lỗi, quyết định đổi ý, thông tin nhạy cảm). Dữ liệu ở `tests/`, đáp án bẫy ở `DAP_AN_CAC_BAY.md` trong từng thư mục.

| Bộ | Skill | Dữ liệu | Quy mô |
|---|---|---|---|
| 1 | `vnuis-vp-hop-nhat-bao-cao-don-vi` | 5 báo cáo đơn vị + mẫu chung + định nghĩa chỉ tiêu (.docx) | 19 trang, 7 file |
| 2 | `vnuis-dc-phan-tich-ket-qua-khao-sat` | phiếu khảo sát + 414 dòng thô + 63 ý kiến mở (.docx, .tsv, .txt) | 16 trang |
| 3 | `vnuis-vp-soan-bien-ban-hop` | gỡ băng cuộc họp giao ban, 170 dòng, nhiều dòng nhiễu | 12 trang |

**Giới hạn quan trọng nhất:**
- **Không có model thật nào chạy.** Không có khóa API tới GLM, DeepSeek hay Qwen trong môi trường này. Phần "model" do chính trợ lý soạn bộ gói (Claude) đóng vai: đọc skill, đọc dữ liệu, soạn đầu ra. Vì vậy:
  - Trợ lý biết trước đáp án bẫy nên tỷ lệ phát hiện dưới đây là **mức trần**, không phải mức mà model flash sẽ đạt. Model nhỏ nhiều khả năng bỏ sót hơn, đặc biệt ở đối chiếu danh sách bài báo và phép tính tỷ lệ.
  - Thử nghiệm chứng minh **skill đủ chỗ để một người làm giỏi đi đúng đường**; không chứng minh model nhỏ làm đúng.
- Đường ống code (đọc file, định tuyến, chạy, xuất docx/xlsx) đã chạy thông trên máy chủ giả cho cả 3 bộ, ở cả chế độ `single` và `steps`. Đó chỉ là kiểm tra code.
- Mới thử 3 trong 167 skill. 164 skill còn lại chưa được thử với dữ liệu.
- Số token là ước lượng thô (ký tự chia 3); tiếng Việt token hóa khác nhau theo model. Hãy đo lại trên nhà cung cấp thật.

## 2. Kết quả theo bộ

### Bộ 1 – Hợp nhất báo cáo: phát hiện 8/8 bẫy kiểm được
Phát hiện: chênh số nhập học (1.120 / 1.087, áp quy tắc nguồn); Viện 22/25 = 88% chứ không phải 92%; "hài lòng 100%" không minh chứng; kỳ báo cáo KHCN lệch ngày; đổi tỷ ra triệu; Khoa thiếu mục kinh phí; bài báo không cộng thẳng (71 sai; 42 hoặc 48 chờ xác nhận); Khoa nói 6 bài đồng tác giả nhưng chỉ khớp 3.
Không kiểm được: "thiếu bao nhiêu đơn vị chưa nộp" — dữ liệu không nêu tổng số đơn vị. Lỗi thiết kế bài thử. Skill đúng khi ghi "chưa xác định được"; đã thêm quy tắc rõ trong v0.4.2.
Nhận xét: bài này khó với model nhỏ ở hai chỗ — đối chiếu 71 tên bài báo giữa ba danh sách, và không cộng thẳng. Nên giao việc đối chiếu tên cho công cụ mã, không cho model (chưa làm trong gói).

### Bộ 2 – Khảo sát: lộ lỗi thiết kế skill rõ nhất
- Skill nhận `du_lieu_tong_hop` (bảng đã tổng hợp) nhưng dữ liệu thực tế là 414 dòng thô. **Model không cộng đúng 400 dòng.** Đã viết `tools/likert_stats.py`; model chỉ diễn giải số công cụ tính.
- Đáp án ban đầu của tôi (382 phiếu hợp lệ) **sai so với chính quy tắc của skill** (skill loại phiếu chọn một đáp án cho mọi câu → 360). Tôi sửa đáp án, không sửa skill; tuy nhiên điều này cho thấy quy tắc loại phiếu thay đổi kết quả (Q10 là 3,86 hay 3,79) và báo cáo phải nêu.
- Công cụ phát hiện đủ: 14 trùng, 10 ngoài thang, 8 bỏ trống, 22 một đáp án; IFI chỉ 20 phiếu nên không kết luận.
- Bẫy "câu đảo": số kỳ trước của Q7 (2,70) không nói đã đảo hay chưa. Công cụ lần đầu so điểm đã đảo với điểm gốc ra chênh +0,78 (sai). Đã sửa (so gốc với gốc) và thêm quy tắc "chưa rõ thì hỏi lại".
- Tỷ lệ phản hồi (skill yêu cầu ≥ 60%) không tính được vì thiếu số phiếu phát ra: skill đúng khi để "chưa tính được".
- Ý kiến mở: công cụ che đúng số điện thoại và email; **không che được** tên tắt ("Thầy T."), hoàn cảnh gia đình; chỉ cảnh báo. Phải có người đọc lại.
- Đếm chủ đề ý kiến mở do trợ lý làm thủ công (63 ý kiến). Model nhỏ sẽ đếm lệch; số đếm phải ghi là sơ bộ.

### Bộ 3 – Biên bản họp: phát hiện 11/11 bẫy
Ngày họp lệch; 10/11 có mặt; biểu quyết 7+2+2 = 11 vượt 10; học bổng "trình Ban Giám hiệu" nhưng chủ trì lại nói "chốt luôn, Hiệu trưởng ký sau" (ghi thận trọng, không ban hành trước); đổi ý về phòng học (ghi quyết định cuối); việc điều hòa không có người phụ trách; số 1.240/1.204; sinh viên có vấn đề sức khỏe không ghi tên; chuyện đá bóng bỏ; hạn "tuần sau" để trống; giao việc cho người vắng ghi "chờ xác nhận".
Skill gốc **không có quy tắc** cho chủ trì đổi ý, phiếu không khớp, việc thuộc thẩm quyền cấp trên, thông tin nhạy cảm; trợ lý làm đúng nhờ suy luận chung, không nhờ skill. Đã thêm 6 quy tắc. Với model nhỏ, đây là chỗ dễ sai nhất (ghi nhầm "đã quyết", ghi tên sinh viên, tự đặt ngày).
Biên bản có chín điểm cần xác nhận; chúng được tách ra "ghi chú nội bộ" để không lọt vào bản trình ký.

## 3. Lỗi đã tìm ra trong gói và đã sửa ở v0.4.2

| # | Lỗi | Nơi | Xử lý |
|---|---|---|---|
| 1 | Bước tự kiểm tra **không có dữ liệu gốc** (chỉ checklist + bản soạn), không thể bắt số bịa hay số sai | `runner.py` | Đưa dữ liệu gốc vào bước kiểm tra, cắt ở 24.000 ký tự |
| 2 | Dòng "Đã qua Human gate…" và giới hạn chung bị đưa **vào file docx/xlsx**, trái quy tắc "không xuất kèm danh mục kiểm" của chính skill | `runner.py` | Trả riêng (`luu_y`), không đưa vào file |
| 3 | Không có chỗ cho ghi chú cần người duyệt xác nhận (mâu thuẫn, thông tin đã loại) | `runner.py` | Dòng tách `=== GHI CHÚ NỘI BỘ ===`, lưu file riêng |
| 4 | **Quy tắc cấm trong mục "Căn cứ & lưu ý" bị bỏ khi skill có mục guardrails** (compile chỉ lấy một trong hai) | `compile.py` | Gộp cả hai; tổng quy tắc cấm nạp vào prompt: 201 |
| 5 | Skill khảo sát nhận bảng đã tổng hợp nhưng thực tế là dữ liệu thô | skill + `tools/` | Công cụ tính sẵn; ghi trong mô tả input |
| 6 | Câu "data gap nhật ký" còn sót từ lần thay chữ trước | skill hợp nhất báo cáo | Đổi thành "bảng thiếu dữ liệu" |
| 7 | Mỗi skill thiếu quy tắc cho các tình huống ở mục 2 | 3 skill | +5, +7, +6 quy tắc |

## 4. Chi phí chạy ước tính (ký tự gửi cho model trong một lần chạy `single` có tự kiểm tra, đo bằng máy chủ giả)

| Bộ | Dữ liệu vào | Tổng gửi/lượt chạy | Ước tính token (chia 3, rất thô) |
|---|---|---|---|
| 1 | khoảng 33.000 ký tự | khoảng 112.000 | khoảng 37.000 |
| 2 | khoảng 34.000 ký tự | khoảng 97.000 | khoảng 32.000 |
| 3 | khoảng 28.000 ký tự | khoảng 102.000 | khoảng 34.000 |

Chế độ `steps` đo ở v0.4.1 tốn khoảng 4,5 lần chế độ `single`. Phần lớn chi phí là gửi lặp dữ liệu (thu thập input, soạn, kiểm tra, sửa). Với tài liệu dài hơn 24.000 ký tự phải chia nhỏ theo đơn vị.

## 5. Chưa làm, nên làm tiếp
1. Chạy 3 bộ này với model flash thật, đo tỷ lệ bắt bẫy; so với mức trần ở trên. Đây là phép thử quyết định.
2. Công cụ mã cho việc đối chiếu danh sách (bài báo, đề tài) và tính lại tỷ lệ; model chỉ viết nhận xét.
3. Thử thêm các skill khác có dữ liệu bảng (tuyển sinh, tài chính, nhân sự) — rủi ro tương tự bộ 2.
4. Thay dữ liệu giả lập bằng 3–5 hồ sơ thật đã che danh tính, vì dữ liệu giả lập do chính người viết skill soạn nên dễ.

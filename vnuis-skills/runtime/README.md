# Runtime chạy bộ skill VNU-IS qua API model

Dành cho ứng dụng tự viết, gọi model qua giao diện kiểu OpenAI (`/chat/completions`). Chỉ cần Python 3.9+ và thư viện chuẩn; xuất Word/Excel cần thêm `pip install python-docx openpyxl`.

## Tình trạng thực tế (đọc trước)
- **Chưa chạy với model thật.** Đã kiểm thử đường ống bằng máy chủ giả (`eval/mock_server.py`): chỉ chứng minh code chạy thông, **không** chứng minh chất lượng văn bản hay độ đúng của model.
- `base_url`, tên model, tham số tắt/bật "suy nghĩ" (thinking) **chưa xác minh**: tên model lấy từ yêu cầu của bạn, thông tin trên các trang tổng hợp không thống nhất. Bạn tự điền theo tài liệu nhà cung cấp trong `models.json`.
- Bộ câu hỏi thử của router (`eval/router_testset.jsonl`, 167 câu, mỗi skill một câu) do người soạn gói viết, nên điểm đo **lạc quan** hơn thực tế. Hãy thay bằng câu hỏi thật của cán bộ.

## Các phần
| File | Việc |
|---|---|
| `compile.py` | Đọc 167 `SKILL.md` thành `compiled/*.json` và `skills-index.json`. Chạy lại mỗi khi sửa skill. |
| `router.py` | Chọn skill: tìm từ khóa (miễn phí, không gọi model); nếu chưa chắc mới nhờ model chọn trong tối đa 8 ứng viên, hoặc hỏi lại người dùng. |
| `runner.py` | Chạy skill: trích input → hỏi lại nếu thiếu input bắt buộc → soạn → tự kiểm tra có đối chiếu dữ liệu gốc (+ sửa một lượt) → tách ghi chú nội bộ → trả giới hạn và ô duyệt riêng (không nằm trong file xuất). |
| `extract.py` | Đọc `.docx` (cả bảng), `.xlsx`, `.pdf`, `.txt/.csv/.tsv/.md/.json` thành chữ để đưa vào `--input` (nhiều tệp một lần). |
| `tools/likert_stats.py` | Tính sẵn thống kê khảo sát (bỏ trùng, ngoài thang, trống, một đáp án, câu đảo, theo nhóm, so kỳ trước). **Model không tự cộng 400 dòng được.** |
| `tools/mask_pii.py` | Che số điện thoại, email, số giấy tờ trước khi gửi ra model; cảnh báo dòng có tên tắt, hoàn cảnh cá nhân (phải người đọc lại). |
| `export.py` | Chuyển Markdown model trả thành `.docx` / `.xlsx`. Model không tạo file. |
| `llm.py`, `models.example.json` | Client gọi API và cấu hình. Khóa API đọc từ biến môi trường, không ghi vào file. |
| `synonyms.json` | Viết tắt và từ khóa thêm cho router; thêm từ cán bộ hay dùng vào đây. |
| `eval/` | Đo router (`eval_router.py`), máy chủ giả (`mock_server.py`). |

## Bắt đầu
```
cp models.example.json models.json     # điền base_url, model; đặt biến môi trường khóa API
python3 compile.py
python3 router.py "soạn thông báo nghỉ lễ"
python3 runner.py "theo dõi thí sinh theo phễu đợt tuyển sinh 2026" --input du_lieu.txt --out ra
```
Nhúng vào ứng dụng: `from runner import roles, run; rl, _ = roles(); kq = run(rl, "tên-skill", văn_bản)`. Nếu `kq["trang_thai"] == "can_hoi"` thì hiển thị `kq["cau_hoi"]` cho người dùng rồi gọi lại với thông tin bổ sung; nếu `"xong"` thì lấy `kq["markdown"]` và gọi `export.export(...)`.

## Gán model theo việc (`vai_tro`)
Bốn vai: `router`, `thu_thap_input`, `soan`, `tu_kiem_tra`. Gợi ý: bắt đầu một model cho cả bốn; sau khi đo thì dùng model rẻ nhất đủ tốt cho `router` và `thu_thap_input` (việc ngắn, cần chính xác), dành model tốt hơn cho `soan`. Nên để model **khác** hoặc cùng model nhưng bật suy nghĩ cho `tu_kiem_tra`; cùng model tự chấm thường dễ dãi.

## Chế độ chạy
- `single` (mặc định): một lượt gọi, rẻ, hợp skill ngắn.
- `steps`: mỗi bước quy trình một lượt rồi tổng hợp; tốn khoảng (số bước + 1) lần gọi nhưng ít sót ý hơn với model nhỏ ở skill dài.
Chưa có số đo chênh lệch chất lượng giữa hai chế độ; hãy thử trên 5–10 tài liệu thật của Trường.

## Cách dùng khi dữ liệu dài (đã thử trên bộ giả lập 12–19 trang)
- Tài liệu 10–20 trang tương đương khoảng 25.000–35.000 ký tự. Chế độ `single` gửi khoảng 100.000–110.000 ký tự cho một lần chạy (thu thập input, soạn, tự kiểm tra có dữ liệu gốc, sửa); đây là ước lượng thô, hãy đo token thật trên nhà cung cấp.
- Chế độ `steps` tốn gấp khoảng 4–5 lần chế độ `single` vì mỗi bước đều nhận lại toàn bộ dữ liệu. Với tài liệu dài chỉ dùng khi `single` bỏ sót rõ ràng.
- Bước tự kiểm tra cắt dữ liệu gốc ở 24.000 ký tự (`SOURCE_CAP` trong `runner.py`). Dữ liệu dài hơn thì phần cuối không được đối chiếu; chia nhỏ theo đơn vị/chương rồi chạy từng phần.
- Dữ liệu dạng bảng dài (khảo sát, danh sách thí sinh, bảng điểm): **tính sẵn bằng mã, rồi mới đưa kết quả cho model**. Ví dụ: `python3 tools/likert_stats.py du_lieu.tsv --items Q1-Q10 --group Khoa --reverse Q7 > so_lieu.md`.
- Dữ liệu có thông tin định danh: `python3 tools/mask_pii.py y_kien.txt > da_che.txt`, đọc lại phần cảnh báo, rồi mới gửi.
- Model được yêu cầu đặt dòng `=== GHI CHÚ NỘI BỘ ===` sau sản phẩm; phần sau dòng này lưu thành `<tên-skill>_ghi_chu_noi_bo.md`, không đưa vào file Word/Excel.

## Giới hạn cần biết
- Model nhỏ dễ bỏ sót phần cuối của cấu trúc đầu ra dài và dễ bịa số liệu; vì vậy có bước tự kiểm tra, nhưng tự kiểm tra **không thay** người duyệt. Mọi sản phẩm kết thúc bằng ô duyệt chưa tích.
- Skill chưa có cơ chế đọc file đính kèm: ứng dụng phải tự trích chữ từ Word/PDF/Excel rồi truyền vào `--input` hoặc tham số `text`. Văn bản dài vượt cửa sổ ngữ cảnh của model sẽ bị cắt; ứng dụng cần tự chia nhỏ.
- Skill chưa gắn chuỗi (soạn → kiểm tra → trình ký), bản rút gọn cho model nhỏ và bộ đánh giá chất lượng đầu ra: chưa làm, nên làm tiếp khi có dữ liệu thật.
- Dữ liệu cá nhân (thí sinh, sinh viên, cán bộ) sẽ đi qua API của nhà cung cấp model; cần quyết định về bảo mật trước khi dùng cho dữ liệu thật.

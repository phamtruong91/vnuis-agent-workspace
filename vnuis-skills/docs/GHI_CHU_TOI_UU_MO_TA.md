# Ghi chú tối ưu mô tả skill (bản đề xuất v0.4.3, chưa kiểm thử với model thật)

## Đã thay đổi
1. Viết lại `description` của 167 skill: mở đầu bằng tình huống kích hoạt ("Dùng khi…" hoặc "Dùng trước/sau/đầu/cuối…"), trung bình ~181 ký tự (trước ~311), phần quan trọng nằm trong 220 ký tự đầu (router cắt ở đó khi gọi model).
2. Bỏ câu "Bản riêng cho…", "Bản VNU-IS" và các câu "Không dùng cho…" khỏi mô tả; chuyển câu loại trừ sang mục mới `## Khi nào KHÔNG dùng` trong thân skill (36 skill dễ nhầm lẫn).
3. Chuyển mục `## Khi nào dùng` lên ngay sau tiêu đề H1 (trước đây ở khoảng dòng 40).
4. Biên dịch lại `runtime/compiled/` và `runtime/skills-index.json` bằng `compile.py`.

## Không thay đổi (cố ý)
Nội dung quy trình, đầu vào/đầu ra, human gate, sơ đồ mermaid, ký hiệu ⏱, phần boilerplate lặp lại, tham chiếu, version (vẫn 0.4.2 trong file). Lý do: thay các phần này cần thử nghiệm hành vi với model thật trước.

## Kết quả đo bộ định tuyến (bộ 167 câu do tác giả viết, nên có thể lạc quan)
| Chỉ số | Trước | Sau |
|---|---|---|
| top1 | 0,802 | 0,868 |
| top3 | 0,946 | 0,964 |
| top5 | 0,982 | 0,982 |
| Đường nhanh (không gọi model): số câu / độ đúng | 123 / 0,927 | 124 / 0,976 |

## Chưa làm
- Chưa chạy so sánh có/không skill trên model thật; chưa kiểm tra chất lượng văn bản đầu ra.
- Mô tả chỉ được viết từ nội dung skill, chưa được người phụ trách nghiệp vụ duyệt.

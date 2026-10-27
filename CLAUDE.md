# Dự án thực hành: Địa chất công trình + Claude Code

Repo luyện tập. Toàn bộ số liệu trong `data/` là **dữ liệu giả lập**, không dùng cho thiết kế thật.

## Quy ước
- Trả lời và comment bằng tiếng Việt; tên biến/hàm giữ không dấu.
- Đơn vị: độ sâu (m), dung trọng (kN/m³), c và áp lực (kPa), góc φ (độ), độ ẩm/giới hạn (%).
- γw = 10 kN/m³. Ký hiệu hố khoan: HK1, HK2, ...
- Phân loại đất dính theo chỉ số dẻo IP (≤7 cát pha, 7–17 sét pha, >17 sét) và trạng thái theo độ sệt IL.
- Tiêu chuẩn tham chiếu thường dùng: TCVN 9362 (thiết kế nền nhà và công trình), TCVN 9351 (SPT), TCVN 4195–4202 (thí nghiệm đất trong phòng), TCVN 9153 (xử lý số liệu thống kê chỉ tiêu cơ lý). Khi trích dẫn công thức/tiêu chuẩn mà không chắc, phải nói rõ là cần kiểm tra lại với bản gốc.
- Không tự sửa file trong `data/` (số liệu gốc); xuất kết quả ra `output/`.

## Lệnh hay dùng
- `python3 scripts/tinh_chi_tieu.py data/lab_samples.csv` — tính γd, e, n, Sr, IP, IL và phân loại.

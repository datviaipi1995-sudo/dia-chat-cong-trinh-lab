# Lộ trình thực hành Claude Code cho khảo sát địa chất công trình

Mở terminal tại thư mục repo, chạy `claude`, rồi lần lượt làm các bài. Mỗi bài có prompt gợi ý — hãy sửa lại theo cách nói của bạn.

## Cấp 1 — Làm quen (đọc và hỏi)
1. `Đọc repo này và giải thích từng file dùng để làm gì.`
2. `Giải thích từng công thức trong scripts/tinh_chi_tieu.py bằng ngôn ngữ của kỹ sư địa chất.`
3. `Trong data/lab_samples.csv, mẫu nào có Sr < 0.9? Điều đó nói lên điều gì về mức độ bão hòa?`

## Cấp 2 — Phân tích số liệu
4. `Gom các mẫu theo hố khoan, lập bảng giá trị trung bình, độ lệch chuẩn, hệ số biến động của w, γ, c, φ cho từng loại đất.`
5. `Phát hiện mẫu bất thường trong lab_samples.csv (ví dụ IL, e lệch hẳn so với lân cận cùng độ sâu) và giải thích vì sao đáng nghi.`
6. `Từ spt.csv, phân loại độ chặt/độ cứng theo N cho từng độ sâu, so sánh giữa 3 hố khoan.`

## Cấp 3 — Viết công cụ
7. `Viết scripts/ve_tru_hk.py vẽ trụ hố khoan (cột N-SPT theo độ sâu, 3 hố cạnh nhau, trục sâu hướng xuống), lưu PNG vào output/.`
8. `Viết scripts/thong_ke_lop.py: gom mẫu thành lớp đất, tính giá trị tiêu chuẩn và giá trị tính toán của c, φ theo TCVN 9153. Có test kèm theo.` (kiểm tra kỹ công thức với tiêu chuẩn gốc)
9. `Viết script đọc file CSV mới do tôi thêm vào data/ và báo lỗi nếu thiếu cột, sai đơn vị, hoặc giá trị phi lý (w > 100%, φ > 45°...).`

## Cấp 4 — Báo cáo
10. `Dựa trên kết quả tính, soạn nháp mục "Điều kiện địa chất công trình" của báo cáo khảo sát, ghi rõ chỗ nào là giả định.`
11. `Đề xuất danh sách lớp đất (lớp 1, 2, 3...) và nhận xét sơ bộ khả năng làm nền cho nhà 5 tầng. Nêu các thông tin còn thiếu.`

## Cấp 5 — Thói quen làm việc với Claude Code
- Dùng `/init` hoặc sửa `CLAUDE.md` để dạy Claude quy ước của bạn.
- Yêu cầu Claude chạy lại script và đối chiếu một mẫu bằng tay trước khi tin kết quả.
- Dùng git: `git diff` xem Claude đã sửa gì, commit từng bước nhỏ.
- Luôn tự kiểm tra: mọi số liệu và công thức phục vụ thiết kế thật phải do kỹ sư có chuyên môn xác nhận.

## Kiểm tra bằng tay mẫu HK1-1 (để biết script đúng)
w=28.5%, γ=18.6, Gs=2.69 → γd = 18.6/1.285 = 14.47; e = 2.69·10/14.47 − 1 = 0.858; Sr = 0.285·2.69/0.858 = 0.89; IP = 34−20.5 = 13.5; IL = (28.5−20.5)/13.5 = 0.59.

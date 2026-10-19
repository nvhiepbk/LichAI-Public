## Lịch AI Excel Translator 1.0.4 · 2026-10-19

## 1.0.4 — 2026-10-10
- Nút sách ở header và phím F1 mở cửa sổ hướng dẫn có cuộn, đóng bằng Escape; không mở trùng cửa sổ.
- Hướng dẫn định dạng/tên file theo mã ngôn ngữ, cột Excel, theo dõi dịch, nghỉ 429, lưu/tiếp tục và cập nhật EXE.

## 1.0.3 — 2026-10-10
- Bảo vệ nguyên cụm | Lịch AI trong khi dịch phần câu.
- Dòng có ngoặc biến chưa cân bằng, lỗi dịch, kết quả rỗng hoặc giống nguồn: giữ nguyên các ô và chuyển dòng tiếp, không gán Có hay dừng lượt.
- Chỉ dòng chỉ có thương hiệu/biến/ký hiệu mới tự gán Có; nhịp nghỉ 429 tiếp tục áp dụng khi gặp giới hạn dịch vụ.
- Thông báo cuối lượt đếm cả các dòng chưa dịch để chạy lại bằng chương trình này hoặc công cụ khác.

## 1.0.2 — 2026-10-10
- Khi dịch vụ thay đổi mã bảo vệ, dịch các đoạn chữ riêng rồi ghép nguyên biến/thẻ/thương hiệu; không dừng chỉ vì mã bị thay đổi.
- Giữ nguyên icon/emoji và ký tự nối trong bản dịch.
- Dòng chỉ có thương hiệu/biến vẫn đánh dấu Có, để trống bản dịch.

## 1.0.1 — 2026-10-10
- Kiểm tra phiên bản GitHub khi mở ứng dụng bằng luồng nền, timeout 8 giây; mất mạng không chặn dịch.
- Phiên bản mới hiển thị bảng so sánh và nút tải EXE qua trình duyệt. Không thay EXE đang chạy.
- Đóng gói VERSION vào EXE; workflow công bố EXE và translator-version.json, giữ các tệp khác ở artifact nội bộ.
- Gồm sửa bỏ qua dòng chỉ có thương hiệu/biến, đánh dấu giữ nguyên Có.

## 2026-10-10 — Bỏ qua dòng chỉ có thương hiệu và biến
- Kiểm tra trước khi gọi dịch; dòng chỉ có Lịch AI/LichAI, biến {…}, số và ký tự phân cách được giữ nguyên.
- Cột bản dịch để trống, cột giữ nguyên chuyển sang Có, preview hiển thị Không dịch.
- Dòng có câu chữ ngoài phần bảo vệ vẫn được dịch như trước.

## Lịch AI Studio 1.0.2 · 2026-10-20

# Lịch AI Studio 1.0.2 — sửa lưu trữ Windows

- Dữ liệu Windows mới dùng application support hoặc LOCALAPPDATA, kiểm tra quyền ghi thực tế trước khi lưu.
- Cho chọn thư mục dữ liệu khác và ghi nhớ lựa chọn; không tự mở dự án trống khi ổ đã chọn không khả dụng.
- Tìm lại dự án và video trong Documents/thư mục cũ; không xóa hay di chuyển media nguồn.
- Có nút Xem video và Mở thư mục đích trên Windows; hủy hoặc lỗi Save As vẫn giữ bản video đã dựng để lưu lại.
- Android giữ application support, SAF và FileProvider hiện có, không thêm quyền lưu trữ rộng.

Bản 1.0.2 tăng build number lên 5 để đưa các sửa lỗi đã merge từ PR #9 qua quy trình kiểm thử và ký riêng. Chỉ coi là đã phát hành khi Public xác minh và cập nhật registry; đây chưa phải xác nhận nghiệm thu trên thiết bị thật.

Giới hạn còn lại: thử Windows tài khoản thường với Documents redirect/Controlled Folder Access, thư mục tiếng Việt/ổ khác và Android arm64 thật; chưa có render nền/resume, kiểm tra dung lượng trước xuất hoặc project bundle portable.

# Lịch AI Studio 0.1.0-alpha.2 — bản kỹ thuật

- Thêm Dựng xem thử 720p: MP4 thực có nhạc, chuyển cảnh, chữ và watermark, mở bằng trình phát hệ điều hành sau khi dựng; cấu hình xuất gốc được giữ nguyên.
- Khôi phục nút xem/chia sẻ video xuất gần nhất khi mở lại ứng dụng.
- Giữ video bằng file staging rồi đổi tên; không nhận file sao chép dở là video đã hoàn tất.
- Dọn job render bỏ lại quá 24 giờ vào lần dựng tiếp theo; khóa file bảo vệ job còn chạy. Không dọn ảnh nguồn hoặc exports.

Android: APK arm64 debug thử nghiệm, Android 8+; giữ ứng dụng ở phía trước khi dựng. Windows: giải nén toàn bộ ZIP rồi chạy lich_ai_studio.exe, giữ engine/data/DLL/sources/notices đi kèm.

Mã nguồn GPL-3.0-or-later, FFmpeg/x264 có GPL; corresponding source và thông báo giấy phép đi kèm bundle. Không cloud, tài khoản hoặc quảng cáo.

Đây chưa phải bản đã nghiệm thu trên máy thật. Xem docs/ACCEPTANCE.md: còn kiểm tra Save/Share/quyền truy cập trên Windows/Android arm64 thật và hiệu năng 4K/60fps. Xem thử cần dựng trước, không phát realtime trong editor. Chưa render nền/resume, preflight dung lượng, project bundle portable hoặc khóa ký release ổn định.

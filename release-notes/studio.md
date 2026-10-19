## Lịch AI Studio 1.0.1 · 2026-10-19

# Lịch AI Studio 0.1.0-alpha.2 — bản kỹ thuật

- Thêm Dựng xem thử 720p: MP4 thực có nhạc, chuyển cảnh, chữ và watermark, mở bằng trình phát hệ điều hành sau khi dựng; cấu hình xuất gốc được giữ nguyên.
- Khôi phục nút xem/chia sẻ video xuất gần nhất khi mở lại ứng dụng.
- Giữ video bằng file staging rồi đổi tên; không nhận file sao chép dở là video đã hoàn tất.
- Dọn job render bỏ lại quá 24 giờ vào lần dựng tiếp theo; khóa file bảo vệ job còn chạy. Không dọn ảnh nguồn hoặc exports.

Android: APK arm64 debug thử nghiệm, Android 8+; giữ ứng dụng ở phía trước khi dựng. Windows: giải nén toàn bộ ZIP rồi chạy lich_ai_studio.exe, giữ engine/data/DLL/sources/notices đi kèm.

Mã nguồn GPL-3.0-or-later, FFmpeg/x264 có GPL; corresponding source và thông báo giấy phép đi kèm bundle. Không cloud, tài khoản hoặc quảng cáo.

Đây chưa phải bản đã nghiệm thu trên máy thật. Xem docs/ACCEPTANCE.md: còn kiểm tra Save/Share/quyền truy cập trên Windows/Android arm64 thật và hiệu năng 4K/60fps. Xem thử cần dựng trước, không phát realtime trong editor. Chưa render nền/resume, preflight dung lượng, project bundle portable hoặc khóa ký release ổn định.

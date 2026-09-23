# Nhật ký cập nhật Lịch AI

Đây là thông tin của phiên bản mới nhất trên từng nền tảng. Bộ cài được tự động cập nhật sau khi quy trình build và kiểm tra hoàn tất; tên file và đường dẫn tải xuống luôn được giữ cố định.

### 📱 Android · 1.8.8

Cập nhật: 22/09/2026

- Hoàn thiện hiển thị sự kiện và ghi chú gần nhất trên Widget.
- Bổ sung các ngày lễ, sự kiện âm lịch quan trọng.
- Tối ưu kiểm tra và tải bản cập nhật qua đường dẫn cố định.


## Reminder Push — 2026-09-21
- Android requests notification permission once on first successful page load (Android 13+).
- Native FCM token can be rebound immediately after the web session is restored/logged in.
- Existing Firebase Messaging service and server-side reminder delivery remain unchanged.


## Android 1.8.8 — 2026-09-22
- Nâng versionCode 18 / versionName 1.8.8 để cài đè bản 1.8.7 và kích hoạt luồng kiểm tra cập nhật hiện có.

[Tải Android](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Android.apk)

### 📺 Android TV · 1.3.2

Cập nhật: 23/09/2026

# TV 1.3.2 — 2026-09-23

- Tăng chiều cao hàng menu phía trên lịch tháng (nút ‹ Hôm nay › Cập nhật) để không bị che khi focus trên TV Box.
- Tăng cỡ chữ khung thông tin ngày bên trái khoảng 2 cỡ; số Dương lịch và dòng Âm lịch nổi bật, lớn hơn (gần phong cách lịch ngày web).
- Giữ nguyên typography và bố cục lưới lịch tháng.
- versionCode 9 / versionName TV 1.3.2 — cài đè được bản 1.3.1 và cũ hơn.


# TV 1.3.0 — 2026-09-17

- Responsive UI theo kích thước khung và độ phân giải TV.
- Chi tiết ngày full-screen ngang 3 cột.
- Tăng cỡ chữ và khả năng đọc sự kiện/văn bản dài.
- Sửa Downloader bằng cách phân giải mã tải sang URL đích trước khi mở ứng dụng Downloader.
- Chuẩn hóa OTA: versionCode 7; manifest TV được phát hành cùng APK và có fallback lich.ai.vn.

- TV 1.2.3: Tự co giao diện theo vùng hiển thị thực tế của TV/TV Box.
- TV 1.2.3: Ngăn cỡ chữ hệ thống làm tràn khung lịch và sự kiện.
- TV 1.2.3: Giữ hướng dẫn remote trong màn hình chính, không cần cuộn trang.
- Hiển thị tên ngày lễ và sự kiện của ngày đang chọn trên màn hình lịch TV.
- Phân biệt rõ sự kiện Âm lịch và Dương lịch.
- Bổ sung sự kiện gần nhất và số ngày đếm ngược.
- Không lặp ngày lễ âm lịch trong tháng nhuận.


# TV Typography — 2026-09-21

- Tách hệ typography của bảng thông tin ngày bên trái khỏi typography của lưới lịch tháng.
- Tăng nhẹ cỡ chữ và line-height riêng cho bảng thông tin TV.
- Bỏ giới hạn line count/line-height nén đối với giờ hoàng đạo, hướng tốt và sự kiện; nội dung dài được tự xuống dòng.
- Giữ nguyên hệ cỡ chữ và bố cục của lưới lịch tháng.


# TV 1.3.1 — 2026-09-22

- Tăng thêm một cỡ chữ riêng cho khung thông tin/diễn giải ngày; giữ nguyên typography của lưới tháng.
- Nâng versionCode 8 / versionName TV 1.3.1 để cài đè bản 1.3.0 và dùng cơ chế kiểm tra cập nhật hiện có.

[Tải Android TV](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.TV.apk)

### 🖥️ Windows · 0.5.1

Cập nhật: 23/09/2026

- Hoàn thiện bộ cài Windows dạng EXE và MSI.
- Giữ đường dẫn tải xuống cố định sau mỗi lần build.
- Cải thiện độ ổn định của ứng dụng Desktop.
- Cập nhật API khay hệ thống Tauri và dọn các cảnh báo Rust không cần thiết.

[Tải EXE](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Desktop.exe) · [Tải MSI](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Desktop.msi)

### 🍎 iOS

Chưa phát hành bản IPA chính thức. Bản iOS sẽ được cập nhật sau khi hoàn thiện chứng chỉ ký Apple và provisioning profile.

---

🌐 [Trang tải xuống chính thức](https://lich.ai.vn/download)

> Repository này chỉ chứa bộ cài đã phát hành, không chứa mã nguồn ứng dụng.

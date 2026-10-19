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

### 🖥️ Windows · 0.6.0

Cập nhật: 19/10/2026

# 0.6.0 — 2026-09-23

- Giao diện click icon tray giống LịchAI TV: chia đôi (chi tiết ngày | lưới tháng).
- Đánh dấu ngày có sự kiện / văn khấn trên lưới; click ngày để xem chi tiết.
- Click sự kiện để đọc mô tả; click văn khấn để xem hướng dẫn chuẩn bị và bài khấn.
- Phóng to icon khay hệ thống (crop padding, tray-icon 256px).
- Cửa sổ lịch tháng 920×560; Cài đặt thu nhỏ gọn.
- Nâng version 0.6.0 / code 600.

# 0.5.1

- Hoàn thiện bộ cài Windows dạng EXE và MSI.
- Giữ đường dẫn tải xuống cố định sau mỗi lần build.
- Cải thiện độ ổn định của ứng dụng Desktop.
- Cập nhật API khay hệ thống Tauri và dọn các cảnh báo Rust không cần thiết.

[Tải EXE](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Desktop.exe) · [Tải MSI](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Desktop.msi)

### 🍎 iOS

Chưa phát hành bản IPA chính thức. Bản iOS sẽ được cập nhật sau khi hoàn thiện chứng chỉ ký Apple và provisioning profile.

### 🎬 Lịch AI Studio · 1.0.1

Cập nhật: 19/10/2026

Lịch AI Studio 1.0.1: Windows EXE và Android APK. Mã nguồn và thông tin giấy phép được quản lý ở dự án Studio; hỗ trợ cung cấp nguồn tương ứng theo GPL-3.0-or-later.

[Giới thiệu Studio](https://lich.ai.vn/lich-ai-studio-tao-video-tu-anh) · [Hướng dẫn](https://lich.ai.vn/huong-dan-lich-ai-studio) · [Download](https://lich.ai.vn/download)

---

🌐 [Trang tải xuống chính thức](https://lich.ai.vn/download)

> Repository phục vụ bộ cài và thông tin phát hành; Studio cung cấp gói nguồn GPL và giấy phép tương ứng trong Assets.

<!-- registry:start -->
# Application release catalogue

## Lịch AI Android 1.8.8 · 2026-10-19

- Hoàn thiện hiển thị sự kiện và ghi chú gần nhất trên Widget.
- Bổ sung các ngày lễ, sự kiện âm lịch quan trọng.
- Tối ưu kiểm tra và tải bản cập nhật qua đường dẫn cố định.


## Reminder Push — 2026-09-21
- Android requests notification permission once on first successful page load (Android 13+).
- Native FCM token can be rebound immediately after the web session is restored/logged in.
- Existing Firebase Messaging service and server-side reminder delivery remain unchanged.


## Android 1.8.8 — 2026-09-22
- Nâng versionCode 18 / versionName 1.8.8 để cài đè bản 1.8.7 và kích hoạt luồng kiểm tra cập nhật hiện có.

## Lịch AI TV 1.3.2 · 2026-10-19

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

## Lịch AI Desktop 0.6.2 · 2026-10-19

# 0.6.2 — Đồng bộ hệ thống phát hành

- Đồng bộ phiên bản trong cấu hình Tauri, Rust và giao diện đóng gói.
- Giao bộ cài EXE/MSI cùng run thành công cho bộ xác minh phát hành tập trung.
- Giữ nguyên URL tải và cơ chế so sánh SemVer của ứng dụng.

# 0.6.0 — 2026-09-23

- Giao diện click icon tray giống LịchAI TV: chia đôi (chi tiết ngày | lưới tháng).
- Đánh dấu ngày có sự kiện / văn khấn trên lưới; click ngày để xem chi tiết.
- Click sự kiện để đọc mô tả; click văn khấn để xem hướng dẫn chuẩn bị và bài khấn.
- Phóng to icon khay hệ thống (crop padding, tray-icon 256px).
- Cửa sổ lịch tháng 920×560; Cài đặt thu nhỏ gọn.
- Nâng version 0.6.0 / code 600.

# 0.5.1

- Hoàn thiện bộ cài Windows dạng EXE và MSI.
- Giữ đường dẫn tải xuống cố định sau mỗi lần build.
- Cải thiện độ ổn định của ứng dụng Desktop.
- Cập nhật API khay hệ thống Tauri và dọn các cảnh báo Rust không cần thiết.


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

## Lịch AI Word Translator 1.0.1 · 2026-10-19

# Lịch AI Word Translator

## v1.0.1 — release candidate

- Windows portable EXE for DOCX translation.
- Two modes: full-document translation and page-interleaved bilingual output (Microsoft Word required for the latter).
- Sentence-level translation log with one-line shortened previews.
- Pause/resume controls and per-sentence checkpoint file.
- Handles HTTP 429 by stopping rather than hammering the translation endpoint.

### Requirements and caveats

- Requires Internet; translation service may rate-limit requests.
- Page interleaving requires Microsoft Word installed on the user's Windows machine.
- Complex formatting, tables, headers/footers, and pagination must be reviewed manually.
- Sensitive documents may be sent to third-party translation endpoints; obtain appropriate authorization before use.

### Publication gate

Do not announce a public release until Windows CI, the downloadable EXE, and the real Word page-pairing acceptance test have passed. The Word release metadata is separate from the Excel translator's assets.

<!-- registry:end -->

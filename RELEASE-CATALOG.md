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

## Lịch AI Studio 1.0.1 · 2026-10-19

# Lịch AI Studio 0.1.0-alpha.2 — bản kỹ thuật

- Thêm Dựng xem thử 720p: MP4 thực có nhạc, chuyển cảnh, chữ và watermark, mở bằng trình phát hệ điều hành sau khi dựng; cấu hình xuất gốc được giữ nguyên.
- Khôi phục nút xem/chia sẻ video xuất gần nhất khi mở lại ứng dụng.
- Giữ video bằng file staging rồi đổi tên; không nhận file sao chép dở là video đã hoàn tất.
- Dọn job render bỏ lại quá 24 giờ vào lần dựng tiếp theo; khóa file bảo vệ job còn chạy. Không dọn ảnh nguồn hoặc exports.

Android: APK arm64 debug thử nghiệm, Android 8+; giữ ứng dụng ở phía trước khi dựng. Windows: giải nén toàn bộ ZIP rồi chạy lich_ai_studio.exe, giữ engine/data/DLL/sources/notices đi kèm.

Mã nguồn GPL-3.0-or-later, FFmpeg/x264 có GPL; corresponding source và thông báo giấy phép đi kèm bundle. Không cloud, tài khoản hoặc quảng cáo.

Đây chưa phải bản đã nghiệm thu trên máy thật. Xem docs/ACCEPTANCE.md: còn kiểm tra Save/Share/quyền truy cập trên Windows/Android arm64 thật và hiệu năng 4K/60fps. Xem thử cần dựng trước, không phát realtime trong editor. Chưa render nền/resume, preflight dung lượng, project bundle portable hoặc khóa ký release ổn định.


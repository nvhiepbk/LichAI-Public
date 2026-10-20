# Lịch AI — Trung tâm tải ứng dụng chính thức

[**🌐 Trang tải xuống**](https://lich.ai.vn/download) · [**📦 Release LichAI-Public**](https://github.com/nvhiepbk/LichAI-Public/releases/tag/LichAI-Public) · [**🏠 Website**](https://lich.ai.vn)

Repository **LichAI-Public** là nơi phát hành bộ cài chính thức của hệ sinh thái **Lịch AI**. Các ứng dụng sử dụng **một Release chung** mang tag `LichAI-Public`; tên tệp và URL tải xuống được giữ cố định khi cập nhật phiên bản.

> Danh mục và trạng thái bộ cài được xác minh trong [registry/applications.json](registry/applications.json); mỗi ứng dụng giữ phiên bản, chữ ký và checksum riêng.

## 📥 Tải nhanh

| Ứng dụng | Nền tảng | Tệp tải trực tiếp |
|---|---|---|
| **Lịch AI Android** | Điện thoại / máy tính bảng Android | [⬇️ LichAI.Android.apk](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Android.apk) |
| **Lịch AI TV** | Android TV | [⬇️ LichAI.TV.apk](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.TV.apk) |
| **Lịch AI Desktop** | Windows · EXE | [⬇️ LichAI.Desktop.exe](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Desktop.exe) |
| **Lịch AI Desktop** | Windows · MSI | [⬇️ LichAI.Desktop.msi](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI.Desktop.msi) |
| **Lịch AI Excel Translator** | Windows x64 | [⬇️ LichAI-Excel-Translater.exe](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Excel-Translater.exe) |
| **Lịch AI Word Translator** | Windows x64 | [⬇️ LichAI-Word-Translator.exe](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Word-Translator.exe) |
| **Lịch AI Studio** | Windows | [⬇️ LichAI-Studio-Windows.exe](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Studio-Windows.exe) |
| **Lịch AI Studio** | Android | [⬇️ LichAI-Studio-Android.apk](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Studio-Android.apk) |
| **Lịch AI Launcher Android** | Màn hình chính Android 8+ | [⬇️ LichAI-Launcher-Android.apk](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Launcher-Android.apk) |
| **Lịch AI Launcher TV** | Màn hình chính Android TV / TV Box 8+ | [⬇️ LichAI-Launcher-TV.apk](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Launcher-TV.apk) |

**Quan trọng:** Các link trên là link tải **bộ cài**, không phải mã nguồn. Không đổi tên asset hoặc tag nếu muốn website và ứng dụng tiếp tục dùng URL cũ.

## 📱 1. Lịch AI Android

- **Nền tảng:** Android (điện thoại, máy tính bảng).
- **Bộ cài:** `LichAI.Android.apk`.
- **Phát hành:** APK được tạo từ workflow Android Release APK + AAB; workflow xác minh chữ ký APK trước khi tải bộ cài lên Release chung.
- **Cài đặt:** Tải APK từ liên kết ở bảng trên, mở tệp trên thiết bị Android và làm theo hướng dẫn cài đặt của hệ thống. Chỉ cho phép cài đặt từ nguồn đáng tin cậy.
- **Lưu ý:** Tệp AAB dùng cho kênh phân phối ứng dụng, không phải bộ cài APK tải trực tiếp tại đây.

## 📺 2. Lịch AI TV

- **Nền tảng:** Android TV tương thích.
- **Bộ cài:** `LichAI.TV.apk`.
- **Phát hành:** Workflow TV tạo APK release và AAB; APK được đưa lên Release chung.
- **Cài đặt:** Tải APK, chuyển sang thiết bị Android TV và cài đặt theo hướng dẫn của thiết bị. Khả năng tương thích phụ thuộc phiên bản Android TV và cấu hình phần cứng.

## 🖥️ 3. Lịch AI Desktop

- **Nền tảng:** Windows.
- **Bộ cài:** `LichAI.Desktop.exe` (trình cài đặt EXE) hoặc `LichAI.Desktop.msi` (gói MSI).
- **Phát hành:** Workflow Windows tạo bộ cài bằng Tauri, sau đó chuẩn hóa tên EXE/MSI và đưa cả hai lên Release chung.
- **Cài đặt:** Chọn **một** trong hai định dạng phù hợp với cách triển khai trên máy Windows; không cần cài cả hai.

## 📊 4. Lịch AI Excel Translator

- **Nền tảng:** Windows x64.
- **Bộ cài:** `LichAI-Excel-Translater.exe` (giữ nguyên cách viết **Translater** trong tên tệp để không làm hỏng link tải).
- **Chức năng:** Dịch nội dung bảng tính Excel, hỗ trợ xem xét nội dung trước khi lưu, theo dõi tiến độ và cố gắng giữ cấu trúc bảng tính trong phạm vi hỗ trợ.
- **Sử dụng:** Tải EXE, mở ứng dụng trên Windows; quá trình dịch cần Internet. Nên giữ bản sao của bảng tính gốc.
- **Giới thiệu / hướng dẫn:** [Phần mềm dịch Excel miễn phí](https://lich.ai.vn/phan-mem-dich-excel-mien-phi).

## 📝 5. Lịch AI Word Translator

- **Nền tảng:** Windows x64.
- **Bộ cài:** `LichAI-Word-Translator.exe`.
- **Chức năng:** Dịch tài liệu DOCX theo từng câu/dòng; hỗ trợ xem trước **Gốc → Dịch**, theo dõi tiến độ và lưu để tiếp tục khi bị gián đoạn.
- **Chế độ:** Dịch toàn văn hoặc song ngữ theo trang (xen kẽ trang gốc và trang dịch).
- **Bố cục:** Cố gắng giữ đoạn văn, bảng và định dạng. Chế độ ghép trang sử dụng khả năng phân trang của Microsoft Word trên Windows; tài liệu phức tạp có thể cần chỉnh sửa thủ công.
- **Phiên bản được ghi nhận trong tài liệu dự án:** 1.0.1; kiểm tra phiên bản thực tế trong ứng dụng.
- **Giới thiệu / hướng dẫn:** [Phần mềm dịch Word song ngữ](https://lich.ai.vn/phan-mem-dich-word-song-ngu).

## 🎬 6. Lịch AI Studio

- **Nền tảng:** Windows và Android.
- **Bộ cài Windows:** `LichAI-Studio-Windows.exe`.
- **Bộ cài Android:** `LichAI-Studio-Android.apk` (bản release có ký).
- **Chức năng:** Công cụ tạo video từ ảnh; thông tin tính năng và hướng dẫn sử dụng được duy trì tại website chính thức.
- **Phiên bản trong metadata phát hành:** 1.0.1; mỗi nền tảng có thể có phiên bản riêng ở các lần cập nhật tiếp theo.
- **Metadata:** [apps/studio.json](apps/studio.json) — thông tin phiên bản, kích thước, SHA-256, trạng thái ký APK và link tải.
- **Giới thiệu:** [Lịch AI Studio — Tạo video từ ảnh](https://lich.ai.vn/lich-ai-studio-tao-video-tu-anh).
- **Hướng dẫn:** [Hướng dẫn Lịch AI Studio](https://lich.ai.vn/huong-dan-lich-ai-studio).

<!-- studio:start -->
<!-- studio:end -->

## 🔄 Cơ chế phát hành và khôi phục tự động

1. Repository nguồn chạy build/kiểm thử và tạo artifact ứng viên; APK phải có chữ ký ổn định.
2. [Coordinator Public](.github/workflows/reconcile-registry.yml) kiểm tra source đã được cho phép, đúng lượt chạy thành công, chữ ký, phiên bản, SHA-256 và kích thước trước khi xuất bản nhóm bộ cài vào Release chung.
3. Registry và metadata chỉ được ghi sau khi xác minh bytes trên Public. Tám tên bộ cài ban đầu được giữ nguyên; các ứng dụng mới như Launcher có asset riêng.
4. Chạy thủ công với `application=launcher-phone` hoặc `application=launcher-tv` để chỉ xét ứng dụng đó. Để trống thì xét toàn danh mục; giao dịch đang dở phải phục hồi trước khi phát hành nhóm khác. Không bỏ kiểm tra cùng phiên bản nhưng khác bytes.
5. Website đồng bộ danh mục đã xác minh. Cập nhật danh mục trong git và triển khai trang SEO là hai bước riêng; kiểm tra cả hai trước khi thông báo trang tải đã cập nhật.

**Quyền truy cập:** Coordinator dùng `RELEASE_SYNC_TOKEN` hoặc `PUBLIC_ARTIFACTS_TOKEN` để đọc source artifacts và ghi Public; chế độ xuất bản yêu cầu `REGISTRY_ENABLED=true` và `apply=true`. Không đưa token, keystore hay mật khẩu vào mã nguồn.

## 🧾 Phiên bản, kiểm tra tệp và an toàn

- **Không có một số phiên bản chung** cho tất cả ứng dụng. Mỗi ứng dụng/nền tảng được cập nhật độc lập. Xem [Release](https://github.com/nvhiepbk/LichAI-Public/releases/tag/LichAI-Public), [CHANGELOG.md](CHANGELOG.md) và metadata tương ứng.
- **Kiểm tra SHA-256** khi có mã băm được công bố. Trên Windows PowerShell có thể chạy:

  ```powershell
  Get-FileHash .\LichAI-Studio-Android.apk -Algorithm SHA256
  ```

- Chỉ tải ứng dụng từ website chính thức hoặc repository này; không cài APK/EXE từ nguồn không xác định.
- Đối với công cụ dịch tài liệu, hãy lưu bản sao tệp gốc và kiểm tra nội dung/bố cục trước khi sử dụng kết quả.
- Nếu link tải báo lỗi, kiểm tra mục **Assets** của [Release chung](https://github.com/nvhiepbk/LichAI-Public/releases/tag/LichAI-Public).

## 🍎 iOS, macOS và Linux

Repository có thể lưu thông tin kế hoạch phát hành cho các nền tảng khác. **Các bộ cài được xác minh hiện gồm Android, Android TV và Windows.** Không xem các nền tảng chưa có tệp phát hành là đã hỗ trợ tải trực tiếp.

## 📬 Hỗ trợ

- **Website:** https://lich.ai.vn
- **Trang tải ứng dụng:** https://lich.ai.vn/download
- **Email:** nvhiepbk@gmail.com

## Bản quyền

© Lịch AI — lich.ai.vn. Các bộ cài và tài liệu phát hành thuộc các dự án tương ứng; vui lòng xem giấy phép và điều khoản sử dụng của từng ứng dụng.

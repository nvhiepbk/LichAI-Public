# Lịch AI Launcher Android

Nguồn riêng: nvhiepbk/LichAI-Launcher. Manifest release-manifests/launcher-phone.json; workflow release-phone.yml; artifact launcher-phone-publication. Asset mới duy nhất LichAI-Launcher-Android.apk trong Release chung LichAI-Public. Không thay đổi tám tên bộ cài hiện có.

Workflow release chạy toàn bộ build/lint/unit/emulator trước khi ký release Android bằng khóa ổn định. Cần bốn repository secrets ANDROID_KEYSTORE_BASE64, ANDROID_KEYSTORE_PASSWORD, ANDROID_KEY_ALIAS và ANDROID_KEY_PASSWORD ở kho Launcher. Không tạo khóa dùng một lần và không publish debug.

Coordinator hiện có chỉ lấy lượt main push/manual thành công, xác minh chữ ký, hash/size, version và nhóm artifact. Khi release chính thức chưa tồn tại, không thêm metadata published hoặc link tải giả. Sau publish, entry launcher-phone tự thêm vào registry/applications.json và metadata/application-registry.json.

Website Lich-AI dùng sync_application_registry.py để cập nhật snapshot Download sau khi xác minh Public. Hai URL SEO: /lich-ai-launcher-android và /huong-dan-lich-ai-launcher-android. Trang SEO đọc trạng thái entry launcher-phone và chỉ hiện nút APK khi is_verified đạt.

Bản TV không thuộc nhóm phát hành Android này.

## Cấu hình khóa ký trên Windows

Thực hiện trong thư mục riêng ngoài mã nguồn. Nếu đã có khóa phát hành Launcher, dùng lại khóa đó; không tạo khóa thay thế cho ứng dụng đã phát hành.

Nếu đây là bản phát hành đầu tiên và chưa có khóa, cài JDK rồi chạy trong PowerShell:

```powershell
keytool -genkeypair -keystore LichAI-Launcher-release.jks -storetype JKS -alias lichai-launcher -keyalg RSA -keysize 3072 -validity 10000
```

Nhập mật khẩu trong lời nhắc của keytool và sao lưu keystore/mật khẩu ở nơi an toàn. Không đưa keystore, mật khẩu hay chuỗi base64 vào mã nguồn hoặc cuộc trò chuyện.

Trong GitHub → nvhiepbk/LichAI-Launcher → Settings → Secrets and variables → Actions, tạo bốn repository secrets:

| Secret | Giá trị |
| --- | --- |
| ANDROID_KEYSTORE_BASE64 | Nội dung keystore mã hóa base64 |
| ANDROID_KEYSTORE_PASSWORD | Mật khẩu kho khóa |
| ANDROID_KEY_ALIAS | lichai-launcher hoặc alias khóa sẵn có |
| ANDROID_KEY_PASSWORD | Mật khẩu của alias; nếu dùng chung thì bằng mật khẩu kho khóa |

Sao chép base64 vào clipboard để dán trực tiếp vào secret GitHub, không ghi ra repository:

```powershell
Set-Clipboard -Value ([Convert]::ToBase64String([IO.File]::ReadAllBytes((Resolve-Path .\LichAI-Launcher-release.jks))))
```

Sau khi đã cấu hình, chạy lại kiểm tra signing-readiness trên PR. Khi mã đã merge vào main, workflow Verify and sign Android Launcher → Run workflow trên main sẽ chạy toàn bộ nghiệm thu, ký và chuẩn bị artifact chính thức. Coordinator Public sẽ chỉ xuất bản khi các điều kiện xác minh đã đạt và chế độ apply của registry được bật theo quy trình hiện có.

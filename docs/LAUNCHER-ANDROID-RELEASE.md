# Lịch AI Launcher Android

Nguồn riêng: nvhiepbk/LichAI-Launcher. Manifest release-manifests/launcher-phone.json; workflow release-phone.yml; artifact launcher-phone-publication. Asset mới duy nhất LichAI-Launcher-Android.apk trong Release chung LichAI-Public. Không thay đổi tám tên bộ cài hiện có.

Workflow release chạy toàn bộ build/lint/unit/emulator trước khi ký release Android bằng khóa ổn định. Cần bốn repository secrets ANDROID_KEYSTORE_BASE64, ANDROID_KEYSTORE_PASSWORD, ANDROID_KEY_ALIAS và ANDROID_KEY_PASSWORD ở kho Launcher. Không tạo khóa dùng một lần và không publish debug.

Coordinator hiện có chỉ lấy lượt main push/manual thành công, xác minh chữ ký, hash/size, version và nhóm artifact. Khi release chính thức chưa tồn tại, không thêm metadata published hoặc link tải giả. Sau publish, entry launcher-phone tự thêm vào registry/applications.json và metadata/application-registry.json.

Website Lich-AI dùng sync_application_registry.py để cập nhật snapshot Download sau khi xác minh Public. Hai URL SEO: /lich-ai-launcher-android và /huong-dan-lich-ai-launcher-android. Trang SEO đọc trạng thái entry launcher-phone và chỉ hiện nút APK khi is_verified đạt.

Bản TV không thuộc nhóm phát hành Android này.

# Lịch AI — Official Releases

Kho phát hành chính thức của **Lịch AI** cho các nền tảng Android, Android TV, iOS và Desktop.

Repository này chỉ chứa thông tin phát hành và liên kết tải ứng dụng. Mã nguồn chính được lưu trong repository riêng tư.

## Tải xuống

Tải ứng dụng từ trang chính thức của Lịch AI:

**https://lich.ai.vn/download**

Trang tải xuống tập hợp các bộ cài đã phát hành và thông tin về các nền tảng:

* Android
* Android TV
* iOS
* Windows
* macOS
* Linux
  
### Android

* Android APK: xem bản phát hành mới nhất trong mục Releases.
* Yêu cầu: Android 8.0 trở lên.

### Android TV

* Android TV APK: xem file có hậu tố `Android.TV` trong Releases.
* Yêu cầu: Android TV tương thích.

### iOS

* Ứng dụng iOS được phát hành qua kênh phân phối chính thức của Apple khi sẵn sàng.

### Desktop

* Windows, macOS và Linux: xem các file tương ứng trong Releases.

### Tiện ích dịch tài liệu Windows Desktop

**Hai tiện ích Excel và Word đã có file EXE trong [bản phát hành LichAI-Public](https://github.com/nvhiepbk/LichAI-Public/releases/tag/LichAI-Public).**

Lịch AI cung cấp hai phần mềm dịch tài liệu độc lập cho **Windows x64**. Người dùng chỉ cần tải **một file EXE** tương ứng, không cần tải kèm JSON phiên bản hoặc cài đặt Python. Quá trình dịch cần kết nối Internet.

#### Lịch AI Excel Translator

- **Ứng dụng:** `LichAI-Excel-Translater.exe`
- **Chức năng:** Dịch nội dung bảng tính Excel, hỗ trợ kiểm tra nội dung trước khi lưu, theo dõi tiến độ và giữ cấu trúc bảng tính trong phạm vi hỗ trợ.
- **Phù hợp:** Bảng biểu, dữ liệu công việc, tài liệu Excel đa ngôn ngữ.
- **Tải EXE:** [LichAI-Excel-Translater.exe](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Excel-Translater.exe)
- **Giới thiệu và hướng dẫn:** https://lich.ai.vn/phan-mem-dich-excel-mien-phi

#### Lịch AI Word Translator

- **Ứng dụng:** `LichAI-Word-Translator.exe`
- **Phiên bản ứng dụng:** 1.0.1 (kiểm tra phiên bản thực tế của EXE trong thông tin ứng dụng khi chạy)
- **Chức năng:** Dịch tài liệu DOCX theo từng câu/dòng, xem trước Gốc → Dịch, theo dõi tiến độ và lưu để tiếp tục khi gián đoạn.
- **Hai chế độ:** Dịch toàn văn; song ngữ theo trang (xen kẽ trang gốc và trang dịch).
- **Bố cục:** Cố gắng giữ đoạn văn, bảng và định dạng; khi bản dịch tràn trang, phần mềm thử điều chỉnh cỡ chữ theo từng đoạn. Chế độ ghép trang sử dụng bộ phân trang Microsoft Word trên Windows và có thể báo lỗi với tài liệu phức tạp.
- **Tải EXE:** [LichAI-Word-Translator.exe](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Word-Translator.exe)
- **Giới thiệu và hướng dẫn:** https://lich.ai.vn/phan-mem-dich-word-song-ngu
- **Khi ghép trang lỗi:** Nếu phiên bản đang dùng có hỗ trợ, chương trình giữ file DOCX đã dịch và thông báo nguyên nhân để người dùng có thể ghép thủ công; cần rà soát bản dịch và bố cục.

> **Lưu ý:** Các liên kết EXE chỉ tải được khi file tương ứng đã được xuất bản trong [Releases](https://github.com/nvhiepbk/LichAI-Public/releases). File JSON phiên bản được lưu trong Releases để phục vụ cập nhật tự động, **không cần tải về máy**. Trước khi dùng với tài liệu quan trọng, nên kiểm tra bản dịch và lưu bản sao của tệp gốc.

## Phiên bản mới nhất

Mỗi nền tảng có số phiên bản riêng, không có một số phiên bản chung cho toàn bộ bộ cài. Xem phiên bản và ngày cập nhật tương ứng trong [Release notes](https://github.com/nvhiepbk/LichAI-Public/releases/tag/LichAI-Public).

## Kiểm tra file tải xuống

Mỗi bản phát hành có thể kèm mã SHA-256 để kiểm tra tính toàn vẹn của file:

```bash
sha256sum LichAI.Android.vX.X.X.apk
```

Đối chiếu kết quả với mã SHA-256 được ghi trong Release notes.

## Lưu ý bảo mật

* Chỉ tải ứng dụng từ repository này hoặc các kênh chính thức của Lịch AI.
* Không tải APK từ liên kết không rõ nguồn gốc.
* Không chia sẻ hoặc tải lên mã nguồn, keystore, file `.env`, token, mật khẩu hoặc thông tin bí mật vào repository này.
* Nếu phát hiện liên kết hoặc file bất thường, vui lòng thông báo cho nhóm Lịch AI.

## Hỗ trợ

Website: https://lich.ai.vn

Email hỗ trợ: `nvhiepbk@gmail.com`

## Bản quyền

© Lịch AI — lich.ai.vn

Các file phát hành trong repository này thuộc về dự án Lịch AI. Vui lòng xem điều khoản sử dụng của từng nền tảng trước khi cài đặt hoặc phân phối lại.

<!-- studio:start -->
## Lịch AI Studio 1.0.1

[Giới thiệu](https://lich.ai.vn/lich-ai-studio-tao-video-tu-anh) · [Hướng dẫn](https://lich.ai.vn/huong-dan-lich-ai-studio)

[Windows portable EXE](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Studio-Windows.exe) · [Android APK](https://github.com/nvhiepbk/LichAI-Public/releases/download/LichAI-Public/LichAI-Studio-Android.apk)
<!-- studio:end -->

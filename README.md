# Đề tài 25: Tấn công từ chối dịch vụ trong mạng IoT và giảm thiểu

## 1. Thành viên nhóm
* Họ và tên: [Họ tên của bạn]
* Mã số sinh viên: [MSSV của bạn]
* Học phần: Bảo mật IoT (INT570) - Trường Đại học Văn Hiến[cite: 1]

## 2. Nguồn GitHub và Công cụ sử dụng
* **Flask**: https://github.com/pallets/flask[cite: 1] (Dùng để dựng API nhận telemetry và lập trình Rate Limiting phòng thủ DoS).
* **OWASP ISVS**: https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS[cite: 1] (Tham khảo tiêu chuẩn kiểm soát bảo mật IoT).
* **OWASP ISTG**: https://github.com/OWASP/owasp-istg[cite: 1] (Phương pháp kiểm thử bảo mật).

## 3. Hướng dẫn chạy Lab cục bộ
1. Cài đặt Python và thư viện Flask:
   ```bash
   pip install Flask

import requests
import time

URL = "http://127.0.0.1:5000/telemetry"
payload = {"device_id": "sensor-01", "temperature": 28.5, "humidity": 75}

print("=== BẮT ĐẦU KIỂM THỬ KỊCH BẢN (NORMAL & FLOODING) ===")

# Kịch bản 1: Gửi request với tần suất bình thường (TC-01)
print("\n--- [TC-01] Gửi request với nhịp độ bình thường (Hợp lệ) ---")
for i in range(3):
    response = requests.post(URL, json=payload)
    print(f"Request {i+1}: Status Code = {response.status_code} | Phản hồi: {response.json()}")
    time.sleep(1) # Nghỉ 1 giây giữa các request

# Kịch bản 2: Gửi request dồn dập liên tiếp (TC-02 - Mô phỏng DoS / Flooding)
print("\n--- [TC-02] Mô phỏng tấn công ngập lụt (Gửi dồn dập vượt ngưỡng 5 lần/10s) ---")
for i in range(7):
    response = requests.post(URL, json=payload)
    print(f"Flood Request {i+1}: Status Code = {response.status_code} | Phản hồi: {response.json()}")

print("\n=== HOÀN TẤT KIỂM THỬ THỰC NGHIỆM ===")
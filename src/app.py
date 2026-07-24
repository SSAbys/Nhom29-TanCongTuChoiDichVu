from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Khởi tạo cơ chế Rate Limiting dựa trên địa chỉ IP của client
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/telemetry', methods=['POST'])
@limiter.limit("5 per 10 seconds")  # Ngưỡng phòng thủ: Tối đa 5 request trong vòng 10 giây cho mỗi IP
def receive_telemetry():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid payload"}), 400
    
    print(f"[+] Nhận dữ liệu hợp lệ từ IP {request.remote_addr}: {data}")
    return jsonify({
        "status": "success", 
        "message": "Đã tiếp nhận dữ liệu cảm biến thành công."
    }), 200

# Tùy chỉnh phản hồi khi vượt quá ngưỡng (Mã lỗi tiêu chuẩn 429 Too Many Requests)
@app.errorhandler(429)
def ratelimit_handler(e):
    print(f"[!] Cảnh báo: Phát hiện lưu lượng vượt ngưỡng từ IP {request.remote_addr} (Dấu hiệu DoS/Flooding)")
    return jsonify({
        "error": "Too Many Requests",
        "message": "Vượt quá giới hạn cho phép. Yêu cầu đã bị từ chối để bảo vệ hệ thống."
    }), 429

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
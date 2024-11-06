# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)  # 打印收到的 Webhook 資料
    return jsonify({'status': 'success'}), 200

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# ルートエンドポイントを定義
@app.route('/')
def index():
    return render_template('index.html')  # トップページのHTMLを返す

# Pingや起動時間を取得するAPIエンドポイント
@app.route('/api/ping')
def get_ping():
    # ダミーデータを返す（後で実際のPingのデータに置き換える）
    return jsonify({
        "ping": random.randint(100, 200),  # ダミーのPing値
        "uptime": "12 hours"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

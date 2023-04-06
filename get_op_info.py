from flask import Flask, jsonify, request

app = Flask(__name__)

# 建立一個 GET 請求的路由


@app.route('/hello', methods=['GET'])
def hello():
    # 回傳一個 JSON 格式的回應
    return jsonify({'message': 'Hello, World!'})

# 建立一個 POST 請求的路由


@app.route('/add', methods=['POST'])
def add():
    # 從 POST 的 request 中取得兩個數字
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    # 將兩個數字相加
    sum = int(num1) + int(num2)
    # 回傳一個 JSON 格式的回應
    return jsonify({'result': sum})


if __name__ == '__main__':
    # 啟動 Flask 伺服器
    app.run(debug=True)

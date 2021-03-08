from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index_page():
    return "Sum API"


@app.route('/sum', methods=["POST"])
def return_sum():
    data = request.get_json()
    result = data["number1"] + data["number2"]
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')

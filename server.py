from flask import Flask,jsonify,request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world!', 200
   

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify(error='Invalid request. Both "first" and "second" numbers are required.'), 400

    first = data['first']
    second = data['second']
    result = first + second
    return jsonify(result=result), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify(error='Invalid request. Both "first" and "second" numbers are required.'), 400

    first = data['first']
    second = data['second']
    result = first - second
    return jsonify(result=result), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
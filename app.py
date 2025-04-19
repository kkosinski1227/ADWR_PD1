from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello', methods=["GET"])
def hello():
    name = request.args.get('name')
    if name:
        return jsonify({"message": f"Hello, {name}!"})
    else:
        return jsonify({"message": "Hello!"})

@app.route("/api/v1.0/predict", methods=["GET"])
def predict():
    try:
        a = float(request.args.get("num1"))
        b = float(request.args.get("num2"))
    except (TypeError, ValueError):
        return jsonify({"error": "Parametry 'num1' i 'num2' muszą być liczbami!"}), 400

    result = 1 if (a + b) > 5.8 else 0

    return jsonify({
        "prediction": result,
        "features": {
            "num1": a,
            "num2": b,
        }
    })

if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request
from src.utils import calculate_sum, validate_input  # ✅ fixed import

app = Flask(__name__)
AWS_SECRET_ACCESS_KEY = "AKIA1234567890EXAMPLE"
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK"}), 200

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()
    if not validate_input(data):
        return jsonify({"error": "Invalid input"}), 400
    total = calculate_sum(data["a"], data["b"])
    return jsonify({"result": total}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

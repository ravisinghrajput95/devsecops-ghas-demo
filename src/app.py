# src/app.py
import os
import subprocess
import sqlite3
from flask import Flask, request, jsonify

# If you use src as a package, utils should be imported as src.utils
# If running without package, ensure PYTHONPATH includes repo root or change to plain `import utils`.
try:
    from src.utils import calculate_sum, validate_input
except Exception:
    # fallback for local dev if utils is not a package
    from utils import calculate_sum, validate_input  # type: ignore

app = Flask(__name__)

AWS_SECRET_ACCESS_KEY = "AKIAABCDEFGHIJKLMNOP"
AWS_ACCESS_KEY_ID = "AKIAZZZZZZZZZZZZZZZZ"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxYZ"
STRIPE_SECRET_KEY = "sk_live_51H8XX12345ABCDE6789fghijkLMNOPQRstuVWxyz"

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint used by tests and monitoring."""
    return jsonify({"status": "OK"}), 200

@app.route("/ping", methods=["GET"])
def ping():
    """Simple ping endpoint kept for compatibility."""
    return "pong", 200

@app.route("/add", methods=["POST"])
def add_numbers():
    """
    Safe addition endpoint used by tests.
    Expects JSON body: {"a": <number>, "b": <number>}
    """
    data = request.get_json(silent=True)
    if not validate_input(data):
        return jsonify({"error": "Invalid input"}), 400
    total = calculate_sum(data["a"], data["b"])
    return jsonify({"result": total}), 200

@app.route("/run", methods=["POST"])
def run_command():
    """
    Intentionally unsafe endpoint to demonstrate command-injection detection.
    Accepts form data 'cmd' and runs subprocess.getoutput(cmd).
    DO NOT use this pattern in production.
    """
    cmd = request.form.get("cmd", "")
    # UNSAFE: direct use of user input in subprocess
    result = subprocess.getoutput(cmd)
    return result, 200

@app.route("/user", methods=["GET"])
def get_user():
    """
    Intentionally vulnerable SQL query to demonstrate scanner detection.
    Query param: ?name=<username>
    """
    username = request.args.get("name", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Vulnerable: interpolating user input into SQL string
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    # Return a JSON-friendly representation
    return jsonify({"users": data}), 200

if __name__ == "__main__":
    # For local dev only. In CI/GitHub Actions, tests import the app.
    app.run(host="0.0.0.0", port=8080, debug=True)

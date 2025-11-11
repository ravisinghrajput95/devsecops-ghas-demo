import os
import subprocess
import flask
from flask import Flask, request

app = Flask(__name__)

# 🚨 1. Hardcoded secret (will trigger Secret Scanning)
AWS_SECRET_KEY = "AKIA1234567890EXAMPLE"

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

# 🚨 2. Command injection vulnerability
@app.route("/run", methods=["POST"])
def run_command():
    cmd = request.form.get("cmd")
    # UNSAFE: direct use of user input in subprocess
    result = subprocess.getoutput(cmd)
    return result

# 🚨 3. SQL Injection example
import sqlite3
@app.route("/user")
def get_user():
    username = request.args.get("name")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # vulnerable
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return {"users": data}

if __name__ == "__main__":
    app.run(debug=True)

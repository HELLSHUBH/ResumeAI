from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "ResumeAI backend is running on Vercel"})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if email == "test@gmail.com" and password == "123456":
        return jsonify({
            "success": True,
            "message": "Login successful"
        }), 200

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    }), 401
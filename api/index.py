import os
import sys

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from database import get_db_connection

# ---------------------------------------------------
# This allows Vercel's api/index.py to access files
# inside your Backend folder.
# ---------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(ROOT_DIR, "Backend")
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

# ---------------------------------------------------
# Imports from your existing backend files
# Same as server.py
# ---------------------------------------------------
import applicant
import recruiter

from login import login_bp
from signup import signup_bp
from profile import profile_bp
from history import history_bp
from recruiter_history import recruiter_history_bp

# ---------------------------------------------------
# Flask app setup
# ---------------------------------------------------
app = Flask(__name__)
CORS(app)

# ---------------------------------------------------
# Register blueprints
# Same structure as your server.py
# ---------------------------------------------------
app.register_blueprint(applicant.analyze_bp, url_prefix="/api")
app.register_blueprint(recruiter.recruiter_bp, url_prefix="/api/recruiter")

app.register_blueprint(login_bp, url_prefix="/api")
app.register_blueprint(signup_bp, url_prefix="/api")
app.register_blueprint(profile_bp, url_prefix="/api")
app.register_blueprint(history_bp, url_prefix="/api")
app.register_blueprint(recruiter_history_bp, url_prefix="/api/recruiter")

# ---------------------------------------------------
# Test routes
# ---------------------------------------------------

@app.route("/api/db-test", methods=["GET"])
def db_test():
    connection = get_db_connection()

    if connection is None:
        return jsonify({
            "success": False,
            "message": "Database connection failed. Check Vercel logs."
        }), 500

    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Database connected successfully",
        "database": result[0]
    }), 200

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({
        "success": True,
        "message": "API test successful"
    })
# ---------------------------------------------------
# Do NOT add app.run() here.
# Vercel runs this Flask app automatically.
# ---------------------------------------------------
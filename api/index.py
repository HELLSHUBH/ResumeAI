import os
import sys

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

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
import os
import sys

from flask import Flask
from flask_cors import CORS

# Add Backend folder to Python path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(ROOT_DIR, "Backend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

import applicant
import recruiter

from login import login_bp
from signup import signup_bp
from profile import profile_bp
from history import history_bp
from recruiter_history import recruiter_history_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(applicant.analyze_bp, url_prefix="/api")
app.register_blueprint(recruiter.recruiter_bp, url_prefix="/api/recruiter")

app.register_blueprint(login_bp, url_prefix="/api")
app.register_blueprint(signup_bp, url_prefix="/api")
app.register_blueprint(profile_bp, url_prefix="/api")
app.register_blueprint(history_bp, url_prefix="/api")
app.register_blueprint(recruiter_history_bp, url_prefix="/api/recruiter")

@app.route("/", methods=["GET"])
def home():
    return "ResumeAI backend is running on Vercel"

@app.route("/api/test", methods=["GET"])
def test():
    return {
        "success": True,
        "message": "API test successful"
    }
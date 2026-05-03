from flask import Flask
from flask_cors import CORS

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
    return "Server is running"


if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)
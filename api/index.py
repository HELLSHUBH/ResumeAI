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
# import applicant
# import recruiter

# from login import login_bp
# from signup import signup_bp
# from profile import profile_bp
# from history import history_bp
# from recruiter_history import recruiter_history_bp

# ---------------------------------------------------
# Flask app setup
# ---------------------------------------------------
app = Flask(__name__)
CORS(app)

# ---------------------------------------------------
# Register blueprints
# Same structure as your server.py
# ---------------------------------------------------
# app.register_blueprint(applicant.analyze_bp, url_prefix="/api")
# app.register_blueprint(recruiter.recruiter_bp, url_prefix="/api/recruiter")

# app.register_blueprint(login_bp, url_prefix="/api")
# app.register_blueprint(signup_bp, url_prefix="/api")
# app.register_blueprint(profile_bp, url_prefix="/api")
# app.register_blueprint(history_bp, url_prefix="/api")
# app.register_blueprint(recruiter_history_bp, url_prefix="/api/recruiter")

# ---------------------------------------------------
# Test routes
# ---------------------------------------------------

@app.route("/api/env-test", methods=["GET"])
def env_test():
    required_vars = ["DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"]

    result = {}

    for var in required_vars:
        value = os.getenv(var)

        if value:
            if var == "DB_PASSWORD":
                result[var] = "Present"
            else:
                result[var] = value
        else:
            result[var] = "Missing"

    return jsonify({
        "success": True,
        "environment_variables": result
    }), 200


@app.route("/api/mysql-import-test", methods=["GET"])
def mysql_import_test():
    try:
        import mysql.connector

        return jsonify({
            "success": True,
            "message": "mysql.connector imported successfully"
        }), 200

    except Exception as error:
        return jsonify({
            "success": False,
            "message": "mysql.connector import failed",
            "error": str(error)
        }), 500


@app.route("/api/db-test", methods=["GET"])
def db_test():
    try:
        import mysql.connector

        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")

        if not host or not port or not user or not password or not database:
            return jsonify({
                "success": False,
                "message": "Missing database environment variables",
                "values": {
                    "DB_HOST": "Present" if host else "Missing",
                    "DB_PORT": "Present" if port else "Missing",
                    "DB_USER": "Present" if user else "Missing",
                    "DB_PASSWORD": "Present" if password else "Missing",
                    "DB_NAME": "Present" if database else "Missing"
                }
            }), 500

        connection = mysql.connector.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
            connection_timeout=5,
            ssl_disabled=False
        )

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

    except Exception as error:
        return jsonify({
            "success": False,
            "message": "Database connection failed",
            "error": str(error)
        }), 500

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
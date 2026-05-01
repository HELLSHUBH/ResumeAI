# history.py

from flask import Blueprint, jsonify
from database import get_db_connection
import json

history_bp = Blueprint("history", __name__)


def save_analysis_history(user_id, resume_file_name, job_description, analysis_result):
    if not user_id:
        return False

    connection = get_db_connection()

    if connection is None:
        print("History save failed: database connection failed")
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO analysis_history
            (
                user_id,
                resume_file_name,
                job_description,
                match_score,
                matched_skills,
                missing_skills,
                feedback,
                suggestions
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (
            int(user_id),
            resume_file_name,
            job_description,
            analysis_result.get("final_match_score", 0),
            json.dumps(analysis_result.get("matched_skills", [])),
            json.dumps(analysis_result.get("missing_skills", [])),
            json.dumps(analysis_result.get("feedback", [])),
            json.dumps(analysis_result.get("suggestions", []))
        ))

        connection.commit()
        return True

    except Exception as error:
        print("History save error:", error)
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()


@history_bp.route("/history/<int:user_id>", methods=["GET"])
def get_user_history(user_id):
    connection = get_db_connection()

    if connection is None:
        return jsonify({
            "message": "Database connection failed"
        }), 500

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                analysis_id,
                resume_file_name,
                job_description,
                match_score,
                matched_skills,
                missing_skills,
                feedback,
                suggestions,
                generated_at
            FROM analysis_history
            WHERE user_id = %s
            ORDER BY generated_at DESC
        """

        cursor.execute(query, (user_id,))
        history = cursor.fetchall()

        for item in history:
            item["generated_at"] = str(item["generated_at"]) if item["generated_at"] else ""

            item["matched_skills"] = parse_json_field(item.get("matched_skills"))
            item["missing_skills"] = parse_json_field(item.get("missing_skills"))
            item["feedback"] = parse_json_field(item.get("feedback"))
            item["suggestions"] = parse_json_field(item.get("suggestions"))

            if item.get("match_score") is not None:
                item["match_score"] = float(item["match_score"])

        return jsonify({
            "message": "History fetched successfully",
            "history": history
        }), 200

    except Exception as error:
        print("History fetch error:", error)

        return jsonify({
            "message": "Could not fetch history"
        }), 500

    finally:
        if cursor:
            cursor.close()
        connection.close()


def parse_json_field(value):
    if not value:
        return []

    try:
        return json.loads(value)
    except Exception:
        return [value]
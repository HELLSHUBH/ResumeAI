# recruiter_history.py

from flask import Blueprint, jsonify
from database import get_db_connection
import json

recruiter_history_bp = Blueprint("recruiter_history", __name__)


def save_recruiter_ranking_history(recruiter_id, job_title, job_description, ranked_results):
    """
    Saves one recruiter screening session.
    One job title can contain many applicant ranking reports.
    """

    if not recruiter_id:
        return None

    connection = get_db_connection()

    if connection is None:
        print("Recruiter history save failed: database connection failed")
        return None

    cursor = None

    try:
        cursor = connection.cursor()

        total_applicants = len(ranked_results)

        top_score = 0
        if ranked_results:
            top_score = ranked_results[0].get("final_match_score", 0)

        job_insert_query = """
            INSERT INTO recruiter_jobs
            (
                recruiter_id,
                job_title,
                job_description,
                total_applicants,
                top_score
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(job_insert_query, (
            int(recruiter_id),
            job_title,
            job_description,
            total_applicants,
            top_score
        ))

        job_id = cursor.lastrowid

        report_insert_query = """
            INSERT INTO recruiter_applicant_reports
            (
                job_id,
                resume_file_name,
                match_score,
                skill_score,
                keyword_score,
                matched_skills,
                missing_skills,
                feedback,
                suggestions,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for applicant in ranked_results:
            cursor.execute(report_insert_query, (
                job_id,
                applicant.get("file_name"),
                applicant.get("final_match_score", 0),
                applicant.get("skill_score", 0),
                applicant.get("keyword_score", 0),
                json.dumps(applicant.get("matched_skills", [])),
                json.dumps(applicant.get("missing_skills", [])),
                json.dumps(applicant.get("feedback", [])),
                json.dumps(applicant.get("suggestions", [])),
                applicant.get("status", "Review")
            ))

        connection.commit()

        return job_id

    except Exception as error:
        print("Recruiter history save error:", error)
        return None

    finally:
        if cursor:
            cursor.close()
        connection.close()


@recruiter_history_bp.route("/history/<int:recruiter_id>", methods=["GET"])
def get_recruiter_jobs(recruiter_id):
    """
    Shows only job titles/screening sessions first.
    Example:
        Front End Developer
        Python Developer
        Data Analyst
    """

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
                job_id,
                job_title,
                total_applicants,
                top_score,
                generated_at
            FROM recruiter_jobs
            WHERE recruiter_id = %s
            ORDER BY generated_at DESC
        """

        cursor.execute(query, (recruiter_id,))
        jobs = cursor.fetchall()

        for job in jobs:
            job["generated_at"] = str(job["generated_at"]) if job["generated_at"] else ""
            job["top_score"] = float(job["top_score"]) if job["top_score"] is not None else 0

        return jsonify({
            "message": "Recruiter jobs fetched successfully",
            "jobs": jobs
        }), 200

    except Exception as error:
        print("Recruiter jobs fetch error:", error)

        return jsonify({
            "message": "Could not fetch recruiter history"
        }), 500

    finally:
        if cursor:
            cursor.close()
        connection.close()


@recruiter_history_bp.route("/history/job/<int:job_id>", methods=["GET"])
def get_recruiter_job_reports(job_id):
    """
    Shows all applicant reports under one selected job title.
    """

    connection = get_db_connection()

    if connection is None:
        return jsonify({
            "message": "Database connection failed"
        }), 500

    cursor = None

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                job_id,
                job_title,
                job_description,
                total_applicants,
                top_score,
                generated_at
            FROM recruiter_jobs
            WHERE job_id = %s
        """, (job_id,))

        job = cursor.fetchone()

        if not job:
            return jsonify({
                "message": "Job history not found"
            }), 404

        cursor.execute("""
            SELECT
                report_id,
                resume_file_name,
                match_score,
                skill_score,
                keyword_score,
                matched_skills,
                missing_skills,
                feedback,
                suggestions,
                status,
                generated_at
            FROM recruiter_applicant_reports
            WHERE job_id = %s
            ORDER BY match_score DESC
        """, (job_id,))

        reports = cursor.fetchall()

        job["generated_at"] = str(job["generated_at"]) if job["generated_at"] else ""
        job["top_score"] = float(job["top_score"]) if job["top_score"] is not None else 0

        for report in reports:
            report["generated_at"] = str(report["generated_at"]) if report["generated_at"] else ""
            report["match_score"] = float(report["match_score"]) if report["match_score"] is not None else 0
            report["skill_score"] = float(report["skill_score"]) if report["skill_score"] is not None else 0
            report["keyword_score"] = float(report["keyword_score"]) if report["keyword_score"] is not None else 0

            report["matched_skills"] = parse_json_field(report.get("matched_skills"))
            report["missing_skills"] = parse_json_field(report.get("missing_skills"))
            report["feedback"] = parse_json_field(report.get("feedback"))
            report["suggestions"] = parse_json_field(report.get("suggestions"))

        return jsonify({
            "message": "Recruiter job reports fetched successfully",
            "job": job,
            "reports": reports
        }), 200

    except Exception as error:
        print("Recruiter job reports fetch error:", error)

        return jsonify({
            "message": "Could not fetch job reports"
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
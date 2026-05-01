from flask import Blueprint, request, jsonify
from pdf_extractor import extract_text_from_pdf
from analyzer import analyze_resume
from history import save_analysis_history

analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.route("/analyze", methods=["POST"])
def collect_data():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    if "jobDescription" not in request.form:
        return jsonify({"error": "No job description provided"}), 400

    resume_file = request.files["resume"]
    job_description = request.form["jobDescription"]
    user_id = request.form.get("user_id")

    if resume_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    resume_text = extract_text_from_pdf(resume_file)

    if not resume_text:
        return jsonify({
            "error": "Could not extract text from PDF"
        }), 400

    analysis_result = analyze_resume(resume_text, job_description)

    history_saved = False

    if user_id:
        history_saved = save_analysis_history(
            user_id=user_id,
            resume_file_name=resume_file.filename,
            job_description=job_description,
            analysis_result=analysis_result
        )

    return jsonify({
        "message": "Resume analyzed successfully",
        "file_name": resume_file.filename,
        "history_saved": history_saved,
        "analysis": analysis_result
    }), 200
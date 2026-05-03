from flask import Blueprint, request, jsonify
from pdf_extractor import extract_text_from_pdf
from analyzer import analyze_resume
from recruiter_history import save_recruiter_ranking_history

recruiter_bp = Blueprint("recruiter", __name__)


@recruiter_bp.route("/rank", methods=["POST"])
def rank_applicants():
    """
    Receives multiple applicant PDF resumes and one job description.
    Each resume is analyzed against the same job description.
    Results are sorted by final match score in descending order.

    Also saves the recruiter screening session in database:
        recruiter_jobs
        recruiter_applicant_reports
    """

    recruiter_id = request.form.get("recruiter_id")
    job_title = request.form.get("jobTitle")
    job_description = request.form.get("jobDescription")

    resumes = request.files.getlist("resumes")

    if not recruiter_id:
        return jsonify({
            "message": "Recruiter ID is required"
        }), 400

    if not job_title:
        return jsonify({
            "message": "Job title is required"
        }), 400

    if not job_description:
        return jsonify({
            "message": "Job description is required"
        }), 400

    if not resumes or len(resumes) == 0:
        return jsonify({
            "message": "At least one applicant resume is required"
        }), 400

    ranked_results = []

    for resume_file in resumes:
        file_name = resume_file.filename

        if not file_name:
            ranked_results.append({
                "file_name": "Unknown file",
                "job_title": job_title,
                "final_match_score": 0,
                "skill_score": 0,
                "keyword_score": 0,
                "matched_skills": [],
                "missing_skills": [],
                "matched_keywords": [],
                "missing_keywords": [],
                "feedback": [],
                "suggestions": [],
                "status": "Invalid file",
                "error": "File name is missing"
            })
            continue

        if not file_name.lower().endswith(".pdf"):
            ranked_results.append({
                "file_name": file_name,
                "job_title": job_title,
                "final_match_score": 0,
                "skill_score": 0,
                "keyword_score": 0,
                "matched_skills": [],
                "missing_skills": [],
                "matched_keywords": [],
                "missing_keywords": [],
                "feedback": [],
                "suggestions": [],
                "status": "Invalid file",
                "error": "Only PDF files are allowed"
            })
            continue

        try:
            resume_file.seek(0)

            resume_text = extract_text_from_pdf(resume_file)

            if not resume_text:
                ranked_results.append({
                    "file_name": file_name,
                    "job_title": job_title,
                    "final_match_score": 0,
                    "skill_score": 0,
                    "keyword_score": 0,
                    "matched_skills": [],
                    "missing_skills": [],
                    "matched_keywords": [],
                    "missing_keywords": [],
                    "feedback": [],
                    "suggestions": [],
                    "status": "Text extraction failed",
                    "error": "Could not extract text from PDF"
                })
                continue

            analysis = analyze_resume(resume_text, job_description)

            score = analysis.get("final_match_score", 0)

            result = {
                "file_name": file_name,
                "job_title": job_title,

                "final_match_score": score,
                "skill_score": analysis.get("skill_score", 0),
                "keyword_score": analysis.get("keyword_score", 0),

                "matched_skills": analysis.get("matched_skills", []),
                "missing_skills": analysis.get("missing_skills", []),

                "matched_keywords": analysis.get("matched_keywords", []),
                "missing_keywords": analysis.get("missing_keywords", []),

                "feedback": analysis.get("feedback", []),
                "suggestions": analysis.get("suggestions", []),

                "status": get_candidate_status(score)
            }

            ranked_results.append(result)

        except Exception as error:
            print(f"Error analyzing {file_name}:", error)

            ranked_results.append({
                "file_name": file_name,
                "job_title": job_title,
                "final_match_score": 0,
                "skill_score": 0,
                "keyword_score": 0,
                "matched_skills": [],
                "missing_skills": [],
                "matched_keywords": [],
                "missing_keywords": [],
                "feedback": [],
                "suggestions": [],
                "status": "Analysis failed",
                "error": str(error)
            })

    ranked_results.sort(
        key=lambda applicant: applicant.get("final_match_score", 0),
        reverse=True
    )

    for index, applicant in enumerate(ranked_results, start=1):
        applicant["rank"] = index

    history_job_id = save_recruiter_ranking_history(
        recruiter_id=recruiter_id,
        job_title=job_title,
        job_description=job_description,
        ranked_results=ranked_results
    )

    history_saved = history_job_id is not None

    return jsonify({
        "message": "Applicants ranked successfully",
        "job_title": job_title,
        "total_applicants": len(ranked_results),
        "history_saved": history_saved,
        "history_job_id": history_job_id,
        "results": ranked_results
    }), 200


def get_candidate_status(score):
    """
    Converts match score into simple recruiter decision status.
    """

    try:
        score = float(score)
    except Exception:
        score = 0

    if score >= 80:
        return "Shortlist"

    if score >= 60:
        return "Review"

    return "Reject"
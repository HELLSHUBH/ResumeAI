# analyzer.py

import re
from collections import Counter
from skills_data import SKILL_CATEGORIES, SKILL_ALIASES


STOPWORDS = {
    "the", "is", "are", "am", "a", "an", "and", "or", "to", "of", "in", "on",
    "for", "with", "as", "by", "at", "from", "this", "that", "these", "those",
    "be", "been", "being", "will", "shall", "can", "could", "should", "would",
    "must", "may", "might", "we", "our", "you", "your", "they", "their",
    "he", "she", "it", "its", "about", "into", "using", "use", "used",
    "work", "working", "experience", "candidate", "job", "role", "required",
    "responsibilities", "skills", "knowledge", "good", "strong", "basic",
    "understanding", "ability", "team", "project"
}


def normalize_text(text):
    """
    Converts text into lowercase and normalizes spacing.
    """
    if not text:
        return ""

    text = text.lower()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def normalize_skill(skill):
    """
    Converts alias skills into standard skill names.
    Example:
        js -> javascript
        ml -> machine learning
    """
    skill = skill.lower().strip()
    return SKILL_ALIASES.get(skill, skill)


def get_all_skills():
    """
    Collects all skills from SKILL_CATEGORIES and SKILL_ALIASES.
    """
    all_skills = []

    for skills in SKILL_CATEGORIES.values():
        all_skills.extend(skills)

    all_skills.extend(SKILL_ALIASES.keys())
    all_skills.extend(SKILL_ALIASES.values())

    return sorted(set(all_skills), key=len, reverse=True)


def extract_skills(text):
    """
    Extracts known skills from resume text or job description text.
    """
    text = normalize_text(text)
    found_skills = set()

    all_skills = get_all_skills()

    for skill in all_skills:
        skill = skill.lower().strip()

        # Avoid false matches for very short skills
        if skill in ["c", "r", "go"]:
            continue

        pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"

        if re.search(pattern, text):
            found_skills.add(normalize_skill(skill))

    # Special handling for short/ambiguous skills
    short_skill_patterns = {
        "c": [r"\bc programming\b", r"\bc language\b"],
        "r": [r"\br programming\b", r"\br language\b"],
        "go": [r"\bgolang\b", r"\bgo programming\b", r"\bgo language\b"]
    }

    for skill, patterns in short_skill_patterns.items():
        for pattern in patterns:
            if re.search(pattern, text):
                found_skills.add(skill)

    return sorted(found_skills)

def extract_keywords(text, limit=20):
    """
    Extracts important repeated words from text.
    This is a simple keyword extraction method without external libraries.
    """
    text = normalize_text(text)

    words = re.findall(r"\b[a-zA-Z][a-zA-Z+#.]{2,}\b", text)

    filtered_words = [
        word for word in words
        if word not in STOPWORDS and len(word) > 2
    ]

    word_frequency = Counter(filtered_words)

    keywords = [word for word, count in word_frequency.most_common(limit)]

    return keywords

def extract_keywords(text, limit=20):
    """
    Extracts important repeated words from text.
    This is a simple keyword extraction method without external libraries.
    """
    text = normalize_text(text)

    words = re.findall(r"\b[a-zA-Z][a-zA-Z+#.]{2,}\b", text)

    filtered_words = [
        word for word in words
        if word not in STOPWORDS and len(word) > 2
    ]

    word_frequency = Counter(filtered_words)

    keywords = [word for word, count in word_frequency.most_common(limit)]

    return keywords

def calculate_match_score(resume_skills, jd_skills, resume_keywords, jd_keywords):
    """
    Calculates overall match score using:
    1. Skill match score
    2. Keyword match score
    """

    resume_skills_set = set(resume_skills)
    jd_skills_set = set(jd_skills)

    resume_keywords_set = set(resume_keywords)
    jd_keywords_set = set(jd_keywords)

    matched_skills = resume_skills_set.intersection(jd_skills_set)
    missing_skills = jd_skills_set.difference(resume_skills_set)

    matched_keywords = resume_keywords_set.intersection(jd_keywords_set)
    missing_keywords = jd_keywords_set.difference(resume_keywords_set)

    if len(jd_skills_set) > 0:
        skill_score = (len(matched_skills) / len(jd_skills_set)) * 100
    else:
        skill_score = 0

    if len(jd_keywords_set) > 0:
        keyword_score = (len(matched_keywords) / len(jd_keywords_set)) * 100
    else:
        keyword_score = 0

    # Final score gives more importance to skills than normal keywords
    final_score = (skill_score * 0.75) + (keyword_score * 0.25)

    return {
        "skill_score": round(skill_score, 2),
        "keyword_score": round(keyword_score, 2),
        "final_score": round(final_score, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "matched_keywords": sorted(matched_keywords),
        "missing_keywords": sorted(missing_keywords)
    }

def generate_feedback(final_score, matched_skills, missing_skills, missing_keywords):
    """
    Generates structured resume improvement feedback.
    """
    feedback = []
    suggestions = []

    if final_score >= 80:
        feedback.append("The resume has a strong match with the job description.")
    elif final_score >= 60:
        feedback.append("The resume has a moderate match with the job description.")
    elif final_score >= 40:
        feedback.append("The resume has a partial match with the job description.")
    else:
        feedback.append("The resume has a low match with the job description.")

    if matched_skills:
        feedback.append(
            f"The resume already contains relevant skills such as {', '.join(matched_skills[:8])}."
        )

    if missing_skills:
        suggestions.append(
            f"Add or improve the following important skills: {', '.join(missing_skills[:10])}."
        )

    if missing_keywords:
        suggestions.append(
            f"Include relevant job-related keywords such as: {', '.join(missing_keywords[:10])}."
        )

    if final_score < 60:
        suggestions.append(
            "Improve the resume by aligning the skills, project descriptions, and experience points with the job description."
        )

    suggestions.append(
        "Use clear project descriptions that show where and how each skill was applied."
    )

    return {
        "feedback": feedback,
        "suggestions": suggestions
    }

def generate_chart_data(matched_skills, missing_skills, resume_skills, jd_skills):
    """
    Creates chart-ready data for frontend Chart.js.
    """

    extra_resume_skills = sorted(set(resume_skills).difference(set(jd_skills)))

    chart_data = {
        "skill_match_chart": {
            "labels": ["Matched Skills", "Missing Skills", "Extra Resume Skills"],
            "values": [
                len(matched_skills),
                len(missing_skills),
                len(extra_resume_skills)
            ]
        }
    }

    return chart_data

def analyze_resume(resume_text, job_description):
    """
    Main function used by Flask backend.

    It analyzes:
    1. Resume skills
    2. Job description skills
    3. Matched skills
    4. Missing skills
    5. Keywords
    6. Match score
    7. Feedback
    8. Chart data
    """

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_description)

    score_result = calculate_match_score(
        resume_skills,
        jd_skills,
        resume_keywords,
        jd_keywords
    )

    feedback_result = generate_feedback(
        score_result["final_score"],
        score_result["matched_skills"],
        score_result["missing_skills"],
        score_result["missing_keywords"]
    )

    chart_data = generate_chart_data(
        score_result["matched_skills"],
        score_result["missing_skills"],
        resume_skills,
        jd_skills
    )

    return {
        "resume_skills": resume_skills,
        "job_description_skills": jd_skills,

        "matched_skills": score_result["matched_skills"],
        "missing_skills": score_result["missing_skills"],

        "resume_keywords": resume_keywords,
        "job_description_keywords": jd_keywords,

        "matched_keywords": score_result["matched_keywords"],
        "missing_keywords": score_result["missing_keywords"],

        "skill_score": score_result["skill_score"],
        "keyword_score": score_result["keyword_score"],
        "final_match_score": score_result["final_score"],

        "feedback": feedback_result["feedback"],
        "suggestions": feedback_result["suggestions"],

        "chart_data": chart_data
    }
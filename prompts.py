"""
prompts.py — HireSense AI | Prompt Engineering Layer
All LLM prompts are centralized here for maintainability and versioning.
"""


def ats_score_prompt(resume_text: str, job_description: str) -> str:
    return f"""
You are an elite ATS engine, senior technical recruiter, and career intelligence system.
Perform deep semantic analysis and return ONLY valid JSON (no markdown, no explanation):

{{
  "ats_score": <integer 0-100>,
  "skills_match_score": <integer 0-100>,
  "keyword_score": <integer 0-100>,
  "experience_score": <integer 0-100>,
  "formatting_score": <integer 0-100>,
  "hiring_probability": <integer 0-100>,
  "resume_grade": "<letter: A+/A/B+/B/C+/C/D>",
  "salary_range": "<e.g. $85,000 - $110,000 / year>",
  "years_of_experience_detected": <integer>,
  "seniority_level": "<Junior/Mid-Level/Senior/Lead>",
  "summary": "<2-3 sentence professional recruiter perspective on fit>"
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""


def missing_skills_prompt(resume_text: str, job_description: str) -> str:
    return f"""
You are a senior technical career coach for AI/ML and software engineering roles.
Return ONLY valid JSON (no markdown):

{{
  "missing_technical_skills": ["skill1", "skill2"],
  "missing_technologies": ["tech1", "tech2"],
  "missing_keywords": ["keyword1", "keyword2"],
  "suggested_certifications": ["cert1", "cert2"],
  "improvement_suggestions": ["suggestion1", "suggestion2"],
  "resume_strengths": ["strength1", "strength2"],
  "quick_wins": ["quick action 1 that can be done in <1 week"]
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""


def interview_questions_prompt(resume_text: str, job_description: str) -> str:
    return f"""
You are an elite technical interviewer. Generate role-specific interview questions.
Return ONLY valid JSON (no markdown):

{{
  "hr_questions": [{{"question": "...", "tip": "..."}}],
  "technical_questions": [{{"question": "...", "tip": "..."}}],
  "project_questions": [{{"question": "...", "tip": "..."}}],
  "behavioral_questions": [{{"question": "...", "tip": "..."}}]
}}

Rules: 4 questions per category (16 total). Tips must be concise answer-strategy hints.

Resume:
{resume_text}

Job Description:
{job_description}
"""


def career_roadmap_prompt(resume_text: str, job_description: str) -> str:
    return f"""
You are a career development strategist. Create a 90-day action plan.
Return ONLY valid JSON (no markdown):

{{
  "week_1_2": ["action1", "action2", "action3"],
  "week_3_4": ["action1", "action2", "action3"],
  "month_2": ["action1", "action2", "action3"],
  "month_3": ["action1", "action2", "action3"],
  "top_resources": ["resource1", "resource2", "resource3"]
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""
def comprehensive_analysis_prompt(resume_text: str, job_description: str) -> str:
    return f"""
You are an expert technical recruiter and ATS (Applicant Tracking System) specialist.
Analyze the following RESUME against the JOB DESCRIPTION.

Output MUST be a single, valid JSON object. Do not include any text before or after the JSON.

### REQUIRED JSON STRUCTURE:
{{
  "ats_data": {{
    "ats_score": <int 0-100>,
    "skills_match_score": <int 0-100>,
    "keyword_score": <int 0-100>,
    "experience_score": <int 0-100>,
    "formatting_score": <int 0-100>,
    "hiring_probability": <int 0-100>,
    "resume_grade": "<A+/A/B+/B/C+/C/D>",
    "salary_range": "<expected range based on level>",
    "years_of_experience_detected": <int>,
    "seniority_level": "<Junior/Mid/Senior/Lead>",
    "summary": "<2-3 sentence expert summary of fit>"
  }},
  "skills_data": {{
    "missing_technical_skills": ["Skill 1", "Skill 2"],
    "missing_technologies": ["Tech 1", "Tech 2"],
    "missing_keywords": ["Keyword 1", "Keyword 2"],
    "suggested_certifications": ["Cert 1", "Cert 2"],
    "improvement_suggestions": ["Action 1", "Action 2"],
    "resume_strengths": ["Strength 1", "Strength 2"],
    "quick_wins": ["Immediate fix 1"]
  }},
  "interview_data": {{
    "hr_questions": [{{"question": "...", "tip": "..."}}],
    "technical_questions": [{{"question": "...", "tip": "..."}}],
    "project_questions": [{{"question": "...", "tip": "..."}}],
    "behavioral_questions": [{{"question": "...", "tip": "..."}}]
  }},
  "roadmap_data": {{
    "week_1_2": ["Topic 1", "Topic 2"],
    "week_3_4": ["Project 1", "Learning 1"],
    "month_2": ["Certification 1", "Networking 1"],
    "month_3": ["Mock Interviews", "Application 1"],
    "top_resources": ["Link/Resource 1", "Link/Resource 2"]
  }}
}}

### ANALYSIS RULES:
1. Be critical. If the resume is missing key JD requirements, reflect this in the scores.
2. The ATS Score should be a weighted average of Skills (40%), Experience (40%), and Keywords (20%).
3. Generate 4 high-impact interview questions per category.
4. The 90-day roadmap should be specific to the gaps identified.

---
### RESUME TEXT:
{resume_text}

---
### JOB DESCRIPTION:
{job_description}
"""

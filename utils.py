import json
import streamlit as st
import re

# ---------------------------------------------------------------------------
# ATS LOGIC HELPERS (DETERMINISTIC)
# ---------------------------------------------------------------------------

def calculate_keyword_match(resume_text: str, jd_text: str) -> dict:
    """
    Calculates a base match score based on keyword overlapping.
    This provides a deterministic 'ground truth' to supplement AI analysis.
    """
    def tokenize(text):
        return set(re.findall(r'\b\w{3,}\b', text.lower()))

    resume_words = tokenize(resume_text)
    jd_words = tokenize(jd_text)
    
    # Common stop words to exclude from keyword matching
    stop_words = {'the', 'and', 'for', 'with', 'from', 'this', 'that', 'your', 'about', 'will'}
    jd_words = jd_words - stop_words
    
    matches = jd_words.intersection(resume_words)
    missing = jd_words - resume_words
    
    score = (len(matches) / len(jd_words)) * 100 if jd_words else 0
    
    return {
        "match_score": int(score),
        "matching_keywords": list(matches)[:15], # Top 15
        "missing_keywords": list(missing)[:15]
    }


# ---------------------------------------------------------------------------
# JSON & DATA HELPERS
# ---------------------------------------------------------------------------

def parse_json_response(raw_response: str) -> dict:
    """
    Safely parses a JSON string returned by the LLM.
    """
    if not raw_response:
        return {}

    cleaned = raw_response.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        cleaned = "\n".join(lines[1:-1]) if lines[-1].strip() == "```" else "\n".join(lines[1:])

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}") + 1
        if start != -1 and end > start:
            try:
                return json.loads(cleaned[start:end])
            except json.JSONDecodeError:
                pass
        return {"raw": raw_response}


# ---------------------------------------------------------------------------
# UI RENDERING HELPERS
# ---------------------------------------------------------------------------

def render_score_card(label: str, score: int, help_text: str = ""):
    """Renders a styled score metric with a color-coded progress bar."""
    if score >= 75: color, rating = "🟢", "Excellent"
    elif score >= 50: color, rating = "🟡", "Good"
    elif score >= 30: color, rating = "🟠", "Fair"
    else: color, rating = "🔴", "Poor"

    st.metric(label=f"{color} {label}", value=f"{score}/100", delta=rating, help=help_text)
    st.progress(score / 100)


def render_bullet_list(items: list, icon: str = "✅"):
    """Renders a clean bullet list of strings with an icon prefix."""
    if not items:
        st.info("No items found.")
        return
    for item in items:
        st.markdown(f"{icon} {item}")



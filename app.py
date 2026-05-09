import os
import streamlit as st
import plotly.graph_objects as go
from dotenv import load_dotenv

# Import Services
from services.ai_service import AIService
from services.pdf_service import PDFService
from utils import calculate_keyword_match, parse_json_response, render_score_card, render_bullet_list
from prompts import comprehensive_analysis_prompt
from style import PREMIUM_CSS
from components import (
    hero_section, landing_features, landing_cta, sidebar_brand, sidebar_stack,
    sidebar_features, kpi_dashboard, section_header, loading_step, status_banner,
    tags_html, question_block, roadmap_block, insight_card, premium_footer
)

# Configuration
load_dotenv()

# Try importing Lottie (graceful fallback if not installed)
try:
    from animations import render_lottie, render_upload_animation
    HAS_LOTTIE = True
except ImportError:
    HAS_LOTTIE = False

st.set_page_config(page_title="HireSense AI", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")
st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

# ── CACHED ANALYSIS ─────────────────────────────────────────────────────────

@st.cache_data(show_spinner=False)
def run_cached_analysis(resume_text, job_description, api_key=None, is_demo=False):
    """
    Performs the heavy lifting of AI analysis with caching to save API credits.
    """
    ai_service = AIService(api_key=api_key)
    
    if is_demo:
        return ai_service.get_mock_data()
        
    # 1. AI Semantic Analysis
    prompt = comprehensive_analysis_prompt(resume_text, job_description)
    raw_response = ai_service.analyze_resume(prompt)
    ai_data = parse_json_response(raw_response)
    
    # 2. Deterministic Keyword Matching (Hybrid Approach)
    keyword_results = calculate_keyword_match(resume_text, job_description)
    
    # 3. Hybrid Score Integration
    if "ats_data" in ai_data:
        # Blend AI score with deterministic keyword match (70/30 weight)
        ai_score = ai_data["ats_data"].get("ats_score", 0)
        deterministic_score = keyword_results["match_score"]
        hybrid_score = int((ai_score * 0.7) + (deterministic_score * 0.3))
        
        ai_data["ats_data"]["ats_score"] = hybrid_score
        ai_data["ats_data"]["keyword_score"] = deterministic_score
        
    return ai_data

# ── Plotly helpers ──────────────────────────────────────────────────────────

PLOT_TRANSPARENT = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

def gauge_chart(score, title):
    color = "#34d399" if score>=75 else "#fbbf24" if score>=50 else "#fb923c" if score>=30 else "#f87171"
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=score,
        title={"text": title, "font": {"color": "#94a3b8", "size": 13, "family": "Inter"}},
        number={"font": {"color": "#f1f5f9", "size": 36, "family": "Inter"}, "suffix": "/100"},
        gauge={
            "axis": {"range": [0,100], "tickcolor": "#475569", "tickfont": {"color":"#475569","size":9}},
            "bar": {"color": color, "thickness": 0.7},
            "bgcolor": "rgba(255,255,255,0.04)",
            "bordercolor": "rgba(255,255,255,0.08)",
            "steps": [
                {"range":[0,30],"color":"rgba(244,63,94,0.08)"},
                {"range":[30,60],"color":"rgba(245,158,11,0.08)"},
                {"range":[60,100],"color":"rgba(16,185,129,0.08)"}
            ],
            "threshold": {"line":{"color":color,"width":3},"thickness":0.8,"value":score}
        }
    ))
    fig.update_layout(**PLOT_TRANSPARENT, margin=dict(t=40,b=10,l=20,r=20), height=210)
    return fig

def bar_chart(labels, values):
    colors = ["#34d399" if v>=75 else "#fbbf24" if v>=50 else "#f87171" for v in values]
    fig = go.Figure(go.Bar(
        x=values, y=labels, orientation="h",
        marker=dict(color=colors, opacity=0.85, line=dict(width=0)),
        text=[f"{v}%" for v in values], textposition="auto",
        textfont=dict(color="#f1f5f9", size=11, family="Inter")
    ))
    fig.update_layout(
        **PLOT_TRANSPARENT,
        xaxis=dict(range=[0,100], gridcolor="rgba(255,255,255,0.05)", tickfont=dict(color="#475569",size=9)),
        yaxis=dict(gridcolor="rgba(0,0,0,0)", tickfont=dict(color="#94a3b8", size=11, family="Inter")),
        margin=dict(t=10,b=10,l=10,r=20), height=200, bargap=0.35
    )
    return fig

def radar_chart(scores):
    cats = list(scores.keys()) + [list(scores.keys())[0]]
    vals = list(scores.values()) + [list(scores.values())[0]]
    fig = go.Figure(go.Scatterpolar(
        r=vals, theta=cats, fill="toself",
        fillcolor="rgba(139,92,246,0.15)",
        line=dict(color="#8b5cf6", width=2),
        marker=dict(color="#a78bfa", size=6)
    ))
    fig.update_layout(
        **PLOT_TRANSPARENT,
        polar=dict(
            bgcolor="rgba(255,255,255,0.02)",
            radialaxis=dict(visible=True, range=[0,100], gridcolor="rgba(255,255,255,0.07)", tickfont=dict(color="#475569",size=8)),
            angularaxis=dict(gridcolor="rgba(255,255,255,0.07)", tickfont=dict(color="#94a3b8",size=10))
        ),
        margin=dict(t=20,b=20,l=40,r=40), height=280
    )
    return fig

def donut_chart(labels, values):
    colors = ["#8b5cf6", "#3b82f6", "#06b6d4", "#10b981"]
    fig = go.Figure(go.Pie(
        labels=labels, values=values, hole=0.65,
        marker=dict(colors=colors, line=dict(color="rgba(0,0,0,0.3)", width=2)),
        textfont=dict(color="#f1f5f9", size=11, family="Inter"),
        textinfo="label+percent", textposition="outside"
    ))
    fig.update_layout(**PLOT_TRANSPARENT, margin=dict(t=20,b=20,l=20,r=20), height=260,
                      showlegend=False)
    return fig

def grade_cls(g):
    if g and g[0]=="A": return "hs-grade-A"
    if g and g[0]=="B": return "hs-grade-B"
    if g and g[0]=="C": return "hs-grade-C"
    return "hs-grade-D"

# ── SIDEBAR ─────────────────────────────────────────────────────────────────

with st.sidebar:
    sidebar_brand()
    st.markdown('<div class="hs-divider" style="margin:.5rem 0 1rem"></div>', unsafe_allow_html=True)

    st.markdown('<div class="hs-sidebar-sec">🚀 Engine Settings</div>', unsafe_allow_html=True)
    is_demo = st.toggle("Demo Mode (No API Key)", value=False)
    
    if not is_demo:
        st.markdown('<div class="hs-sidebar-sec">🔑 Groq API Key</div>', unsafe_allow_html=True)
        groq_api_key = st.text_input("Groq API Key", value=os.getenv("GROQ_API_KEY", ""), type="password", label_visibility="collapsed")
        if not groq_api_key:
            st.warning("⚠️ Enter your Groq API Key to begin.")
    else:
        groq_api_key = None
        st.success("✨ Demo Mode: Using high-quality mock data.")

    st.markdown('<div class="hs-sidebar-sec">📄 Resume Upload</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Resume PDF", type=["pdf"], label_visibility="collapsed")
    if uploaded_file:
        st.markdown(f'<div class="hs-ok">✅ {uploaded_file.name}</div>', unsafe_allow_html=True)

    st.markdown('<div class="hs-sidebar-sec">💼 Target Role</div>', unsafe_allow_html=True)
    job_description = st.text_area("Job Description", height=195,
        placeholder="Paste the job description to match against...",
        label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button("⚡ Run AI Analysis", use_container_width=True)

    st.markdown('<div class="hs-divider" style="margin:.8rem 0"></div>', unsafe_allow_html=True)
    st.markdown('<div class="hs-sidebar-sec">🛠 Stack</div>', unsafe_allow_html=True)
    sidebar_stack()

# ── HERO & LANDING ──────────────────────────────────────────────────────────

if not uploaded_file or not job_description.strip():
    hero_section()
    landing_features()
    st.markdown("<br>", unsafe_allow_html=True)
    if HAS_LOTTIE:
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2: render_upload_animation()
    landing_cta()
    st.stop()

# ── ANALYSIS PIPELINE ────────────────────────────────────────────────────────

if analyze_btn:
    if not is_demo and not groq_api_key:
        st.error("❌ Groq API Key is required. Please enter it in the sidebar."); st.stop()
        
    with st.spinner("Processing PDF..."):
        resume_text = PDFService.extract_text(uploaded_file)
        
    if not PDFService.validate_text(resume_text):
        st.error("❌ Could not extract enough text from the PDF. Please ensure it's a text-based document."); st.stop()

    pb = st.progress(0)
    loader = st.empty()

    loading_step(30, "🧠 Analyzing profile with Llama-3...", pb, loader)
    
    try:
        # Run the cached analysis
        full_data = run_cached_analysis(resume_text, job_description, groq_api_key, is_demo)
        
        loading_step(100, "✅ Analysis complete!", pb, loader)
        
        st.session_state.update({
            "ats_data": full_data.get("ats_data", {}),
            "skills_data": full_data.get("skills_data", {}),
            "interview_data": full_data.get("interview_data", {}),
            "roadmap_data": full_data.get("roadmap_data", {}),
            "analysis_done": True
        })
    except Exception as e:
        st.error(f"❌ Analysis failed: {str(e)}")
        st.info("💡 Tip: If you hit a rate limit, try Demo Mode or wait 60 seconds.")
        st.stop()

    pb.progress(100, "✅ Analysis complete!")
    loader.empty()

# ── RESULTS ──────────────────────────────────────────────────────────────────

if not st.session_state.get("analysis_done"): st.stop()

ad = st.session_state.get("ats_data", {})
sd = st.session_state.get("skills_data", {})
iid = st.session_state.get("interview_data", {})
rd = st.session_state.get("roadmap_data", {})

score = ad.get("ats_score", 0)
grade = ad.get("resume_grade", "B")
prob = ad.get("hiring_probability", 0)
salary = ad.get("salary_range", "N/A")
level = ad.get("seniority_level", "Mid-Level")
yoe = ad.get("years_of_experience_detected", 0)

# ── Display ──────────────────────────────────────────────────────────────────
status_banner(score, prob, ad.get('summary', ''))
kpi_dashboard(score, prob, grade, salary, yoe, level, grade_cls(grade))

t1, t2, t3, t4 = st.tabs(["📊 ATS Analysis", "🔍 Skills Gap", "🎤 Interview Copilot", "🗺️ Roadmap"])

with t1:
    section_header("ATS Compatibility Report", "Hybrid analysis combining keyword matching and AI semantics")
    c1, c2 = st.columns([1, 1.6])
    with c1:
        st.plotly_chart(gauge_chart(score, "ATS Score"), config={"displayModeBar": False})
        st.plotly_chart(gauge_chart(prob, "Hiring Probability"), config={"displayModeBar": False})
    with c2:
        labels = ["Skills Match", "Keyword Density", "Experience Fit", "Formatting"]
        vals = [ad.get("skills_match_score",0), ad.get("keyword_score",0), ad.get("experience_score",0), ad.get("formatting_score",0)]
        st.plotly_chart(bar_chart(labels, vals), config={"displayModeBar": False})
        st.markdown(f"**🤖 Recruiter Perspective:** {ad.get('summary', '')}")

with t2:
    section_header("Skills Gap Analysis", "Detection of missing technical competencies and keywords")
    L, R = st.columns(2)
    with L:
        st.markdown("**❌ Missing Skills**")
        st.markdown(tags_html(sd.get("missing_technical_skills", []), "hs-tag-red"), unsafe_allow_html=True)
        st.markdown("<br>**🔑 Missing Keywords**")
        st.markdown(tags_html(sd.get("missing_keywords", []), "hs-tag-blue"), unsafe_allow_html=True)
    with R:
        st.markdown("**💪 Strengths**")
        for s in sd.get("resume_strengths", []): insight_card("✦", s, "hs-insight-good")

with t3:
    section_header("Interview Copilot", "Role-specific questions and tips")
    it1, it2, it3 = st.tabs(["👔 HR", "⚙️ Tech", "🎯 Behavioral"])
    with it1: question_block(iid.get("hr_questions", []))
    with it2: question_block(iid.get("technical_questions", []))
    with it3: question_block(iid.get("behavioral_questions", []))

with t4:
    section_header("Career Roadmap", "90-day action plan to bridge identified gaps")
    rc1, rc2 = st.columns(2)
    with rc1: roadmap_block("Foundation", "🎯", rd.get("week_1_2", []))
    with rc2: roadmap_block("Accelerate", "🚀", rd.get("month_2", []))

premium_footer()
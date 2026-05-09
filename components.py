# =============================================================================
# components.py — HireSense AI | Premium UI Component Builders
# =============================================================================
# Reusable HTML/CSS component functions for the cinematic UI.
# All components return HTML strings rendered via st.markdown().
# =============================================================================

import streamlit as st


def glass_metric(icon, label, value, delay="0s"):
    """Premium KPI metric card with glass effect."""
    return f'''<div class="hs-kpi" style="animation-delay:{delay}">
        <div style="font-size:1.4rem;margin-bottom:.4rem">{icon}</div>
        <div class="hs-kpi-val">{value}</div>
        <div class="hs-kpi-label">{label}</div>
    </div>'''


def section_header(title, subtitle, icon=""):
    """Cinematic section header with gradient accent."""
    st.markdown(f'''
    <div style="margin-bottom:1.8rem;animation:fadeUp .5s ease both">
        <div class="hs-section-title">{icon} {title}</div>
        <div class="hs-section-sub">{subtitle}</div>
    </div>''', unsafe_allow_html=True)


def status_banner(score, prob, summary):
    """Cinematic status banner based on ATS score."""
    if score >= 75:
        cls, emoji, rating = "hs-status-good", "🎉", "Strong Match"
    elif score >= 50:
        cls, emoji, rating = "hs-status-mid", "⚡", "Moderate Match"
    else:
        cls, emoji, rating = "hs-status-low", "🚨", "Needs Improvement"

    st.markdown(f'''
    <div class="hs-status {cls}">
        <div class="hs-status-icon">{emoji}</div>
        <div>
            <div class="hs-status-title">ATS Score {score}/100 — {rating} &nbsp;|&nbsp; Hiring Probability {prob}%</div>
            <div class="hs-status-sub">{summary}</div>
        </div>
    </div>''', unsafe_allow_html=True)


def kpi_dashboard(score, prob, grade, salary, yoe, level, grade_cls):
    """Premium KPI grid with 6 glass metric cards."""
    st.markdown(f'''
    <div class="hs-kpi-grid">
        <div class="hs-kpi" style="animation-delay:0s">
            <div style="font-size:.7rem;color:var(--t3);margin-bottom:.3rem">📊 SCORE</div>
            <div class="hs-kpi-val">{score}</div>
            <div class="hs-kpi-label">ATS Score</div>
        </div>
        <div class="hs-kpi" style="animation-delay:.05s">
            <div style="font-size:.7rem;color:var(--t3);margin-bottom:.3rem">🎯 PROBABILITY</div>
            <div class="hs-kpi-val">{prob}%</div>
            <div class="hs-kpi-label">Hire Probability</div>
        </div>
        <div class="hs-kpi" style="animation-delay:.1s">
            <div style="font-size:.7rem;color:var(--t3);margin-bottom:.3rem">📋 GRADE</div>
            <div class="hs-kpi-val"><span class="hs-grade-badge {grade_cls}">{grade}</span></div>
            <div class="hs-kpi-label">Resume Grade</div>
        </div>
        <div class="hs-kpi" style="animation-delay:.15s">
            <div style="font-size:.7rem;color:var(--t3);margin-bottom:.3rem">💰 SALARY</div>
            <div class="hs-kpi-val" style="font-size:1.1rem">{salary}</div>
            <div class="hs-kpi-label">Salary Range</div>
        </div>
        <div class="hs-kpi" style="animation-delay:.2s">
            <div style="font-size:.7rem;color:var(--t3);margin-bottom:.3rem">⏱️ EXPERIENCE</div>
            <div class="hs-kpi-val">{yoe}yr</div>
            <div class="hs-kpi-label">Experience Detected</div>
        </div>
        <div class="hs-kpi" style="animation-delay:.25s">
            <div style="font-size:.7rem;color:var(--t3);margin-bottom:.3rem">🏅 LEVEL</div>
            <div class="hs-kpi-val" style="font-size:1rem">{level}</div>
            <div class="hs-kpi-label">Seniority Level</div>
        </div>
    </div>''', unsafe_allow_html=True)


def hero_section():
    """Premium hero section with animated gradient text and floating orbs."""
    st.markdown("""
    <div class="hs-hero">
        <div class="hs-grid-bg"></div>
        <div class="hs-orb hs-orb-1"></div>
        <div class="hs-orb hs-orb-2"></div>
        <div class="hs-orb hs-orb-3"></div>
        <div style="position:relative;z-index:1">
            <div style="display:inline-flex;align-items:center;gap:8px;background:rgba(139,92,246,.1);border:1px solid rgba(139,92,246,.22);border-radius:99px;padding:.35rem 1.1rem;font-size:.7rem;color:#a78bfa;font-weight:600;letter-spacing:.6px;text-transform:uppercase;margin-bottom:1.3rem;backdrop-filter:blur(8px)">
                ⚡ AI-Powered Career Intelligence Platform
            </div>
            <div class="hs-gradient-text">HireSense AI</div>
            <div class="hs-subtitle">Transform your resume into a job-winning asset. Get ATS scores, skill gap analysis, interview prep, and a personalized career roadmap — all powered by Google Gemini.</div>
            <div style="margin-top:1.5rem">
                <span class="hs-badge">🎯 ATS Optimization</span>
                <span class="hs-badge">🧠 LLM Prompt Engineering</span>
                <span class="hs-badge">📊 Semantic NLP</span>
                <span class="hs-badge">🤖 Gemini AI</span>
                <span class="hs-badge">🎤 Interview Copilot</span>
            </div>
            <div class="hs-stat-row">
                <div class="hs-stat"><div class="hs-stat-num">4</div><div class="hs-stat-label">AI Modules</div></div>
                <div class="hs-stat"><div class="hs-stat-num">16+</div><div class="hs-stat-label">Interview Questions</div></div>
                <div class="hs-stat"><div class="hs-stat-num">90</div><div class="hs-stat-label">Day Roadmap</div></div>
                <div class="hs-stat"><div class="hs-stat-num">∞</div><div class="hs-stat-label">Career Insights</div></div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)


def landing_features():
    """Bento-style feature cards for the landing page."""
    feats = [
        ("📊", "ATS Score Engine", "AI compatibility score with dimensional breakdown — skills, keywords, experience & formatting"),
        ("🔍", "Skills Gap Analysis", "NLP detection of missing skills, tools, certifications and ATS keywords with quick-win actions"),
        ("🎤", "Interview Copilot", "16 role-specific questions across HR, technical, project & behavioral with answer strategies"),
        ("🗺️", "Career Roadmap", "Personalized 90-day week-by-week action plan plus salary range and hiring probability"),
    ]
    cols = st.columns(4)
    for i, (col, (icon, title, desc)) in enumerate(zip(cols, feats)):
        with col:
            st.markdown(f'''
            <div class="hs-feature-card" style="animation-delay:{i*0.1}s">
                <span class="hs-feature-icon">{icon}</span>
                <div class="hs-feature-title">{title}</div>
                <div class="hs-feature-desc">{desc}</div>
            </div>''', unsafe_allow_html=True)


def landing_cta():
    """Premium CTA block for empty state."""
    st.markdown("""
    <div class="hs-cta">
        <div style="font-size:2.8rem;margin-bottom:1rem;animation:float 3s ease-in-out infinite">👈</div>
        <div style="font-size:1.2rem;font-weight:800;color:#f1f5f9;margin-bottom:.6rem;font-family:'Plus Jakarta Sans',sans-serif">Get Started in 30 Seconds</div>
        <div style="font-size:.88rem;color:#94a3b8;max-width:420px;margin:0 auto;line-height:1.7">
            Upload your resume PDF and paste a job description in the sidebar,<br>
            then click <strong style="color:#a78bfa">⚡ Run AI Analysis</strong>
        </div>
    </div>""", unsafe_allow_html=True)


def sidebar_brand():
    """Premium sidebar brand header."""
    st.markdown("""
    <div style="padding:1.5rem 1rem 1rem;text-align:center">
        <div class="hs-logo-icon">🧠</div>
        <div class="hs-logo-name">HireSense AI</div>
        <div class="hs-logo-tag">Resume & Interview Intelligence</div>
    </div>""", unsafe_allow_html=True)


def sidebar_stack():
    """Sidebar tech stack pills."""
    st.markdown("""
    <div>
        <span class="hs-pill">🤖 Gemini</span><span class="hs-pill">🐍 Python</span>
        <span class="hs-pill">🎈 Streamlit</span><span class="hs-pill">📊 Plotly</span>
        <span class="hs-pill">📄 PyPDF2</span>
    </div>""", unsafe_allow_html=True)


def sidebar_features():
    """Sidebar feature list."""
    features = ["ATS Scoring Engine", "Hiring Probability", "Skills Gap Analysis",
                 "Interview Copilot", "90-Day Roadmap", "Salary Estimation"]
    for f in features:
        st.markdown(f'<div class="hs-badge" style="margin:.2rem 0;width:100%;justify-content:flex-start">◆ {f}</div>', unsafe_allow_html=True)


def loading_step(pct, msg, pb, loader):
    """Cinematic loading step with animated dots."""
    pb.progress(pct, msg)
    loader.markdown(f'''
    <div class="hs-loader">
        <div class="hs-dot-l"></div><div class="hs-dot-l"></div><div class="hs-dot-l"></div>
        <span style="font-size:.84rem;color:#94a3b8">{msg}</span>
    </div>''', unsafe_allow_html=True)


def tags_html(items, cls):
    """Render skill/keyword tags."""
    return "".join(f'<span class="hs-tag {cls}">{i}</span>' for i in items) if items else ""


def question_block(questions):
    """Render interview question cards."""
    for i, q in enumerate(questions, 1):
        tip = f'<div class="hs-qtip">💡 {q.get("tip","")}</div>' if q.get("tip") else ""
        st.markdown(f'''
        <div class="hs-qcard" style="animation-delay:{i*0.05}s">
            <div style="display:flex;align-items:flex-start;gap:10px">
                <span class="hs-qnum">{i}</span>
                <span style="font-size:.93rem;font-weight:600;color:#f1f5f9;line-height:1.55">{q.get("question","")}</span>
            </div>{tip}
        </div>''', unsafe_allow_html=True)


def roadmap_block(header, icon, items, delay="0s"):
    """Render roadmap phase card with timeline dots."""
    rows = "".join(f'<div class="hs-rmap-item"><div class="hs-dot"></div>{it}</div>' for it in items)
    st.markdown(f'''
    <div class="hs-rmap" style="animation-delay:{delay}">
        <div class="hs-rmap-header">{icon} {header}</div>
        {rows}
    </div>''', unsafe_allow_html=True)


def insight_card(icon, text, cls="hs-insight-info"):
    """Render a single insight card."""
    st.markdown(f'''
    <div class="hs-insight {cls}">
        <span style="margin-right:8px">{icon}</span>
        <span style="font-size:.86rem;color:#cbd5e0;line-height:1.55">{text}</span>
    </div>''', unsafe_allow_html=True)


def premium_footer():
    """Premium footer with aurora glow."""
    st.markdown('''
    <div class="hs-footer">
        <div style="margin-bottom:.5rem;font-size:.85rem">
            Built with 🧠 <strong>HireSense AI</strong>
        </div>
        <div>Streamlit · Google Gemini · Plotly Analytics · LLM-Powered Resume Intelligence</div>
    </div>''', unsafe_allow_html=True)

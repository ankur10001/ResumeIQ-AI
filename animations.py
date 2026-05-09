# =============================================================================
# animations.py — HireSense AI | Lottie Animation Module
# =============================================================================
# Provides Lottie animation loading and rendering helpers.
# All animations are loaded from public LottieFiles CDN URLs.
# =============================================================================

import requests
import streamlit as st
from streamlit_lottie import st_lottie


# ---------------------------------------------------------------------------
# LOTTIE LOADER
# ---------------------------------------------------------------------------

def load_lottie_url(url: str) -> dict:
    """
    Fetches a Lottie animation JSON from a public URL.
    Returns the JSON dict, or None on failure.
    """
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# ANIMATION URLS — Public LottieFiles CDN
# ---------------------------------------------------------------------------

LOTTIE_URLS = {
    "hero_ai":      "https://lottie.host/4db68bbd-31f6-4cd8-84eb-189de081159f/IGmMCqhzpt.json",
    "loading":      "https://lottie.host/f7a149e5-9bbc-4be0-9f5e-35a784e27dc3/1JVvHSiCca.json",
    "success":      "https://lottie.host/2bc21e56-51bf-4e5d-832c-89d014625baa/dS0QUFkhCQ.json",
    "upload":       "https://lottie.host/785a1e04-e498-437e-88b4-398913e0f6b8/M2Cl98GGIN.json",
    "rocket":       "https://lottie.host/f2a6573c-c93e-4a60-8803-b947fea14a77/9KZQO7DxlW.json",
    "analytics":    "https://lottie.host/c3c6ec15-79ed-4a2d-a0d6-3dabe3cb0485/DKPEhNV0Nr.json",
    "scan":         "https://lottie.host/34f0acbf-4e2a-4eeb-8a0e-7e21825e4cbb/RxM4GIBaMk.json",
    "brain":        "https://lottie.host/ca9476cc-5ee0-4c6a-b02c-0bd8b5b8de4e/LOvz9KjIjP.json",
}


# ---------------------------------------------------------------------------
# CACHED LOADERS — avoid re-fetching on each rerun
# ---------------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def get_lottie(name: str) -> dict:
    """Get a cached Lottie animation by name."""
    url = LOTTIE_URLS.get(name, "")
    if url:
        return load_lottie_url(url)
    return None


# ---------------------------------------------------------------------------
# RENDER HELPERS
# ---------------------------------------------------------------------------

def render_lottie(name: str, height: int = 200, key: str = None):
    """Render a named Lottie animation with a given height."""
    anim = get_lottie(name)
    if anim:
        st_lottie(anim, height=height, key=key or f"lottie_{name}")
    else:
        # Graceful fallback — show nothing if CDN is unreachable
        st.markdown(
            f'<div style="height:{height}px;display:flex;align-items:center;'
            f'justify-content:center;opacity:0.3;font-size:2rem">🧠</div>',
            unsafe_allow_html=True
        )


def render_hero_animation():
    """Hero section Lottie — AI brain / neural network."""
    render_lottie("hero_ai", height=280, key="hero_anim")


def render_loading_animation():
    """Loading state Lottie — analysis spinner."""
    render_lottie("loading", height=180, key="loading_anim")


def render_success_animation():
    """Success state Lottie — checkmark celebration."""
    render_lottie("success", height=150, key="success_anim")


def render_upload_animation():
    """Empty/upload state Lottie — upload prompt."""
    render_lottie("upload", height=220, key="upload_anim")


def render_rocket_animation():
    """Roadmap Lottie — rocket launch."""
    render_lottie("rocket", height=160, key="rocket_anim")


def render_analytics_animation():
    """Analytics Lottie — data visualization."""
    render_lottie("analytics", height=160, key="analytics_anim")

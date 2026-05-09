PREMIUM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
:root{--bg:#06060e;--bg2:#0c0c1d;--glass:rgba(255,255,255,0.04);--glass2:rgba(255,255,255,0.08);--border:rgba(255,255,255,0.06);--p:#8b5cf6;--b:#3b82f6;--c:#06b6d4;--g:#10b981;--r:#f43f5e;--y:#f59e0b;--t1:#f1f5f9;--t2:#94a3b8;--t3:#475569;--glow:rgba(139,92,246,0.15);}
*,*::before,*::after{box-sizing:border-box;}
html,body,[class*="css"],.stApp{font-family:'Inter',sans-serif!important;background:var(--bg)!important;color:var(--t1)!important;}
#MainMenu,footer,header{visibility:hidden;}
::-webkit-scrollbar{width:5px;}::-webkit-scrollbar-track{background:var(--bg2);}::-webkit-scrollbar-thumb{background:linear-gradient(var(--p),var(--c));border-radius:3px;}
.stApp{background:var(--bg)!important;}
.stApp::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse 80% 60% at 50% -20%,rgba(124,58,237,0.12),transparent 70%),radial-gradient(ellipse 60% 40% at 80% 60%,rgba(14,165,233,0.06),transparent),radial-gradient(ellipse 40% 30% at 15% 80%,rgba(16,185,129,0.05),transparent);pointer-events:none;z-index:0;}
section[data-testid="stMain"]{background:transparent!important;}
[data-testid="stSidebar"]{background:rgba(8,8,22,0.95)!important;border-right:1px solid var(--border)!important;backdrop-filter:blur(20px)!important;}
[data-testid="stSidebar"]>div{background:transparent!important;}
[data-testid="stFileUploadDropzone"]{background:var(--glass)!important;border:1px dashed rgba(139,92,246,0.35)!important;border-radius:14px!important;transition:all .3s!important;}
[data-testid="stFileUploadDropzone"]:hover{border-color:var(--p)!important;background:rgba(139,92,246,0.08)!important;box-shadow:0 0 30px rgba(139,92,246,0.1)!important;}
.stTextArea textarea{background:var(--glass)!important;border:1px solid var(--border)!important;border-radius:14px!important;color:var(--t1)!important;font-family:'Inter',sans-serif!important;transition:all .3s!important;}
.stTextArea textarea:focus{border-color:var(--p)!important;box-shadow:0 0 0 3px rgba(139,92,246,0.15),0 0 30px rgba(139,92,246,0.08)!important;}
.stButton>button{background:linear-gradient(135deg,#7c3aed,#4f46e5,#0ea5e9)!important;background-size:200% 200%!important;animation:gradShift 4s ease infinite!important;color:#fff!important;border:none!important;border-radius:12px!important;padding:.75rem 1.5rem!important;font-weight:700!important;font-size:.95rem!important;transition:all .3s cubic-bezier(.4,0,.2,1)!important;box-shadow:0 0 25px rgba(124,58,237,.3),0 4px 15px rgba(0,0,0,.3)!important;letter-spacing:.3px!important;}
.stButton>button:hover{transform:translateY(-3px) scale(1.01)!important;box-shadow:0 0 50px rgba(124,58,237,.5),0 8px 30px rgba(0,0,0,.4)!important;}
.stButton>button:active{transform:translateY(-1px)!important;}
.stTabs [data-baseweb="tab-list"]{background:var(--glass)!important;border-radius:14px!important;padding:5px!important;gap:4px!important;border:1px solid var(--border)!important;backdrop-filter:blur(12px)!important;}
.stTabs [data-baseweb="tab"]{border-radius:10px!important;color:var(--t2)!important;font-weight:600!important;transition:all .25s!important;font-size:.85rem!important;}
.stTabs [aria-selected="true"]{background:linear-gradient(135deg,rgba(124,58,237,.25),rgba(14,165,233,.15))!important;color:var(--t1)!important;border:1px solid rgba(139,92,246,.3)!important;box-shadow:0 0 20px rgba(139,92,246,.1)!important;}
[data-testid="stTabsContent"]{background:transparent!important;border:none!important;padding-top:1.5rem!important;}
.stProgress>div>div>div>div{background:linear-gradient(90deg,#7c3aed,#0ea5e9,#10b981)!important;border-radius:99px!important;box-shadow:0 0 15px rgba(124,58,237,.4)!important;}
.stProgress>div>div{background:rgba(255,255,255,0.05)!important;border-radius:99px!important;height:8px!important;}
.stAlert{border-radius:14px!important;backdrop-filter:blur(12px)!important;}
hr{border-color:var(--border)!important;}
.js-plotly-plot .plotly,.js-plotly-plot .plotly div{background:transparent!important;}
@keyframes gradShift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
@keyframes pulse-glow{0%,100%{box-shadow:0 0 20px rgba(124,58,237,.2)}50%{box-shadow:0 0 40px rgba(124,58,237,.5),0 0 80px rgba(14,165,233,.15)}}
@keyframes borderPulse{0%,100%{border-color:rgba(139,92,246,.25)}50%{border-color:rgba(139,92,246,.6)}}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.2}}
@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes aurora{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes borderRotate{0%{--angle:0deg}100%{--angle:360deg}}
@keyframes slideIn{from{opacity:0;transform:translateX(-20px)}to{opacity:1;transform:translateX(0)}}
@keyframes scaleIn{from{opacity:0;transform:scale(0.9)}to{opacity:1;transform:scale(1)}}
.hs-hero{position:relative;overflow:hidden;border-radius:28px;padding:3.5rem 3rem 3rem;margin-bottom:2rem;animation:fadeUp .6s ease both;background:var(--bg2);border:1px solid var(--border);}
.hs-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% -10%,rgba(124,58,237,.18),transparent),radial-gradient(ellipse 50% 50% at 85% 60%,rgba(14,165,233,.1),transparent),radial-gradient(ellipse 40% 40% at 10% 80%,rgba(16,185,129,.07),transparent);pointer-events:none;}
.hs-hero::after{content:'';position:absolute;top:-50%;right:-20%;width:500px;height:500px;background:radial-gradient(circle,rgba(139,92,246,0.08),transparent 60%);border-radius:50%;filter:blur(60px);pointer-events:none;animation:float 8s ease-in-out infinite;}
.hs-grid-bg{position:absolute;inset:0;background-image:linear-gradient(rgba(139,92,246,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(139,92,246,.04) 1px,transparent 1px);background-size:32px 32px;mask-image:radial-gradient(ellipse 70% 70% at 50% 50%,black 30%,transparent 100%);pointer-events:none;}
.hs-gradient-text{background:linear-gradient(135deg,#c4b5fd 0%,#818cf8 25%,#38bdf8 50%,#34d399 75%,#c4b5fd 100%);background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gradShift 6s ease infinite;font-size:3.2rem;font-weight:900;line-height:1.1;letter-spacing:-2px;font-family:'Plus Jakarta Sans','Inter',sans-serif;}
.hs-subtitle{font-size:1.05rem;color:var(--t2);margin-top:1rem;font-weight:400;max-width:560px;line-height:1.7;}
.hs-badge{display:inline-flex;align-items:center;gap:5px;background:rgba(139,92,246,.08);border:1px solid rgba(139,92,246,.2);color:#c4b5fd;padding:.3rem .85rem;border-radius:99px;font-size:.7rem;font-weight:600;letter-spacing:.5px;margin:.3rem .2rem 0 0;text-transform:uppercase;transition:all .25s;backdrop-filter:blur(8px);}
.hs-badge:hover{background:rgba(139,92,246,.18);border-color:rgba(139,92,246,.5);transform:translateY(-2px);box-shadow:0 4px 15px rgba(139,92,246,.15);}
.hs-stat-row{display:flex;gap:2.5rem;margin-top:2rem;}
.hs-stat{text-align:left;}
.hs-stat-num{font-size:1.8rem;font-weight:900;background:linear-gradient(135deg,#a78bfa,#38bdf8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1;font-family:'Plus Jakarta Sans',sans-serif;}
.hs-stat-label{font-size:.68rem;color:var(--t3);text-transform:uppercase;letter-spacing:1px;margin-top:.25rem;}
.glass-card{background:rgba(255,255,255,0.03);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.06);border-radius:20px;padding:1.5rem;transition:all .35s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;}
.glass-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,0.03),transparent 60%);pointer-events:none;border-radius:20px;}
.glass-card:hover{border-color:rgba(139,92,246,.3);background:rgba(255,255,255,0.05);transform:translateY(-4px);box-shadow:0 20px 50px rgba(0,0,0,.3),0 0 30px rgba(139,92,246,.08);}
.bento-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin:1.5rem 0;}
.bento-2x1{grid-column:span 2;}
.bento-1x2{grid-row:span 2;}
.hs-feature-card{background:var(--glass);border:1px solid var(--border);border-radius:20px;padding:2rem 1.5rem;text-align:center;transition:all .35s cubic-bezier(.4,0,.2,1);animation:fadeUp .5s ease both;height:100%;position:relative;overflow:hidden;}
.hs-feature-card::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:60%;height:1px;background:linear-gradient(90deg,transparent,rgba(139,92,246,.4),transparent);}
.hs-feature-card:hover{border-color:rgba(139,92,246,.35);background:rgba(139,92,246,.06);transform:translateY(-6px);box-shadow:0 25px 60px rgba(0,0,0,.35),0 0 40px rgba(139,92,246,.1);}
.hs-feature-icon{font-size:2.6rem;margin-bottom:1rem;display:block;animation:float 4s ease-in-out infinite;filter:drop-shadow(0 0 12px rgba(139,92,246,.3));}
.hs-feature-title{font-size:1rem;font-weight:700;color:var(--t1);margin-bottom:.5rem;font-family:'Plus Jakarta Sans',sans-serif;}
.hs-feature-desc{font-size:.78rem;color:var(--t3);line-height:1.6;}
.hs-kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1rem;margin:1.2rem 0;}
.hs-kpi{background:var(--glass);border:1px solid var(--border);border-radius:16px;padding:1.3rem 1rem;text-align:center;transition:all .3s;animation:fadeUp .4s ease both;position:relative;overflow:hidden;backdrop-filter:blur(12px);}
.hs-kpi::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--p),var(--c));opacity:0;transition:opacity .3s;}
.hs-kpi:hover{border-color:rgba(139,92,246,.3);transform:translateY(-4px);box-shadow:0 15px 40px rgba(0,0,0,.25),0 0 25px rgba(139,92,246,.08);}
.hs-kpi:hover::before{opacity:1;}
.hs-kpi-val{font-size:1.6rem;font-weight:900;background:linear-gradient(135deg,#a78bfa,#38bdf8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1;font-family:'Plus Jakarta Sans',sans-serif;}
.hs-kpi-label{font-size:.65rem;color:var(--t3);text-transform:uppercase;letter-spacing:1px;margin-top:.35rem;}
.hs-grade-badge{display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:14px;font-size:1.4rem;font-weight:900;border:2px solid;animation:pulse-glow 3s ease infinite;}
.hs-grade-A{background:rgba(16,185,129,.1);border-color:rgba(16,185,129,.4);color:#34d399;}
.hs-grade-B{background:rgba(59,130,246,.1);border-color:rgba(59,130,246,.4);color:#60a5fa;}
.hs-grade-C{background:rgba(245,158,11,.1);border-color:rgba(245,158,11,.4);color:#fbbf24;}
.hs-grade-D{background:rgba(244,63,94,.1);border-color:rgba(244,63,94,.4);color:#fb7185;}
.hs-insight{background:var(--glass);border:1px solid var(--border);border-radius:14px;padding:1rem 1.3rem;margin:.6rem 0;transition:all .3s;animation:fadeUp .4s ease both;backdrop-filter:blur(8px);}
.hs-insight:hover{border-color:rgba(139,92,246,.2);background:var(--glass2);transform:translateX(4px);}
.hs-insight-good{border-left:3px solid var(--g);}
.hs-insight-warn{border-left:3px solid var(--y);}
.hs-insight-bad{border-left:3px solid var(--r);}
.hs-insight-info{border-left:3px solid var(--b);}
.hs-insight-purple{border-left:3px solid var(--p);}
.hs-tag{display:inline-block;padding:.3rem .75rem;border-radius:99px;font-size:.72rem;font-weight:600;margin:.25rem;transition:all .25s;backdrop-filter:blur(6px);}
.hs-tag:hover{transform:scale(1.08) translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,.2);}
.hs-tag-red{background:rgba(244,63,94,.1);border:1px solid rgba(244,63,94,.25);color:#fb7185;}
.hs-tag-green{background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.25);color:#34d399;}
.hs-tag-blue{background:rgba(14,165,233,.1);border:1px solid rgba(14,165,233,.25);color:#38bdf8;}
.hs-tag-purple{background:rgba(139,92,246,.1);border:1px solid rgba(139,92,246,.25);color:#a78bfa;}
.hs-tag-yellow{background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.25);color:#fbbf24;}
.hs-qcard{background:var(--glass);border:1px solid var(--border);border-left:3px solid var(--p);border-radius:0 16px 16px 0;padding:1.3rem 1.5rem;margin:.8rem 0;transition:all .3s;animation:fadeUp .4s ease both;backdrop-filter:blur(8px);}
.hs-qcard:hover{background:var(--glass2);border-left-color:var(--c);transform:translateX(6px);box-shadow:0 8px 25px rgba(0,0,0,.2);}
.hs-qnum{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;background:linear-gradient(135deg,rgba(124,58,237,.3),rgba(14,165,233,.2));border:1px solid rgba(139,92,246,.3);border-radius:8px;font-size:.68rem;font-weight:700;color:#a78bfa;flex-shrink:0;}
.hs-qtip{font-size:.79rem;color:var(--t2);margin-top:.6rem;padding:.55rem 1rem;background:rgba(14,165,233,.05);border-radius:10px;border-left:2px solid var(--c);line-height:1.5;}
.hs-rmap{background:var(--glass);border:1px solid var(--border);border-radius:16px;padding:1.4rem 1.5rem;margin:.7rem 0;transition:all .3s;animation:fadeUp .5s ease both;position:relative;backdrop-filter:blur(8px);}
.hs-rmap::before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;background:linear-gradient(180deg,var(--p),var(--c));border-radius:3px 0 0 3px;}
.hs-rmap:hover{border-color:rgba(139,92,246,.3);background:var(--glass2);transform:translateY(-3px);box-shadow:0 12px 35px rgba(0,0,0,.25);}
.hs-rmap-header{font-size:.72rem;font-weight:700;color:var(--p);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:.8rem;display:flex;align-items:center;gap:6px;}
.hs-rmap-item{display:flex;align-items:flex-start;gap:10px;font-size:.84rem;color:var(--t2);margin:.4rem 0;line-height:1.5;}
.hs-dot{width:6px;height:6px;border-radius:50%;background:linear-gradient(135deg,var(--p),var(--c));flex-shrink:0;margin-top:6px;box-shadow:0 0 8px rgba(139,92,246,.4);}
.hs-status{border-radius:18px;padding:1.4rem 1.8rem;display:flex;align-items:center;gap:1.2rem;margin-bottom:1.5rem;animation:fadeUp .5s ease both;backdrop-filter:blur(12px);}
.hs-status-good{background:rgba(16,185,129,.06);border:1px solid rgba(16,185,129,.18);}
.hs-status-mid{background:rgba(245,158,11,.06);border:1px solid rgba(245,158,11,.18);}
.hs-status-low{background:rgba(244,63,94,.06);border:1px solid rgba(244,63,94,.18);}
.hs-status-icon{font-size:2.2rem;flex-shrink:0;animation:float 3s ease infinite;}
.hs-status-title{font-size:1.05rem;font-weight:700;color:var(--t1);}
.hs-status-sub{font-size:.82rem;color:var(--t2);margin-top:.25rem;line-height:1.5;}
.hs-divider{height:1px;background:linear-gradient(90deg,transparent,rgba(139,92,246,.25),rgba(14,165,233,.2),transparent);margin:2rem 0;}
.hs-section-title{font-size:1.6rem;font-weight:800;color:var(--t1);letter-spacing:-.5px;font-family:'Plus Jakarta Sans','Inter',sans-serif;}
.hs-section-sub{font-size:.82rem;color:var(--t3);margin-bottom:1.5rem;margin-top:.2rem;}
.hs-logo-icon{font-size:2.8rem;filter:drop-shadow(0 0 20px rgba(139,92,246,.6));animation:float 4s ease-in-out infinite;}
.hs-logo-name{font-size:1.35rem;font-weight:800;background:linear-gradient(135deg,#a78bfa,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;letter-spacing:-.5px;margin-top:.3rem;font-family:'Plus Jakarta Sans',sans-serif;}
.hs-logo-tag{font-size:.66rem;color:var(--t3);letter-spacing:.6px;margin-top:.15rem;}
.hs-sidebar-sec{font-size:.65rem;font-weight:700;color:var(--t3);text-transform:uppercase;letter-spacing:1.8px;margin:1.3rem 0 .6rem;}
.hs-ok{background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.2);border-radius:10px;padding:.55rem .9rem;font-size:.78rem;color:#34d399;display:flex;align-items:center;gap:6px;}
.hs-pill{display:inline-flex;align-items:center;gap:4px;background:var(--glass);border:1px solid var(--border);border-radius:8px;padding:.28rem .65rem;font-size:.67rem;color:var(--t2);margin:.18rem;font-family:'JetBrains Mono',monospace;transition:all .2s;}
.hs-pill:hover{border-color:rgba(139,92,246,.3);background:var(--glass2);}
.hs-cta{background:radial-gradient(ellipse 80% 80% at 50% 50%,rgba(124,58,237,.08),transparent);border:1px dashed rgba(139,92,246,.22);border-radius:22px;padding:3rem;text-align:center;animation:borderPulse 4s ease infinite;position:relative;overflow:hidden;}
.hs-cta::before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 50% 0%,rgba(139,92,246,.06),transparent 60%);pointer-events:none;}
.hs-loader{display:flex;align-items:center;gap:10px;padding:.9rem 1.3rem;background:var(--glass);border:1px solid var(--border);border-radius:14px;margin:.4rem 0;backdrop-filter:blur(8px);}
.hs-dot-l{width:8px;height:8px;border-radius:50%;background:var(--p);animation:blink 1.2s ease infinite;}
.hs-dot-l:nth-child(2){animation-delay:.2s;background:var(--b);}
.hs-dot-l:nth-child(3){animation-delay:.4s;background:var(--c);}
.hs-footer{text-align:center;padding:3rem 2rem;margin-top:3rem;color:var(--t3);font-size:.75rem;position:relative;overflow:hidden;}
.hs-footer::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(139,92,246,.3),rgba(14,165,233,.2),transparent);}
.hs-footer::after{content:'';position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:300px;height:200px;background:radial-gradient(ellipse,rgba(124,58,237,.06),transparent 70%);pointer-events:none;}
.hs-footer strong{background:linear-gradient(135deg,#a78bfa,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hs-prob-bar-wrap{background:rgba(255,255,255,.04);border-radius:99px;height:10px;margin:.4rem 0;overflow:hidden;}
.hs-prob-bar{height:100%;border-radius:99px;background:linear-gradient(90deg,#7c3aed,#0ea5e9);transition:width 1.2s cubic-bezier(.4,0,.2,1);box-shadow:0 0 12px rgba(124,58,237,.4);}
.hs-orb{position:absolute;border-radius:50%;filter:blur(60px);pointer-events:none;animation:float 6s ease-in-out infinite;}
.hs-orb-1{width:300px;height:300px;background:rgba(139,92,246,0.06);top:-100px;right:-50px;}
.hs-orb-2{width:200px;height:200px;background:rgba(14,165,233,0.05);bottom:-50px;left:-30px;animation-delay:2s;}
.hs-orb-3{width:150px;height:150px;background:rgba(16,185,129,0.04);top:50%;left:60%;animation-delay:4s;}
</style>
"""

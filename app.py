import streamlit as st
import os
from data import (PROFILE, CVS, STATS, PROJECTS, SKILLS, PROFICIENCIES,
                  EXPERIENCE, EDUCATION, CERTIFICATIONS, ACHIEVEMENTS, OPEN_TO)

st.set_page_config(
    page_title="Anudeep Burra | Data Analyst | Data Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
*, *::before, *::after { font-family: 'Inter', sans-serif !important; box-sizing: border-box; }

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebarNav"]     { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
[data-testid="stSidebar"]        { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* TOP BAR */
.topbar {
    background: linear-gradient(90deg,#060d1f 0%,#0d1a3a 100%);
    border-bottom: 1px solid #1e293b;
    padding: 12px 36px;
    display: flex; align-items: center; justify-content: space-between;
}
.topbar-left { display: flex; align-items: center; gap: 14px; }
.topbar-avatar {
    width: 44px; height: 44px; border-radius: 50%;
    background: linear-gradient(135deg,#3b82f6,#8b5cf6);
    display: flex; align-items: center; justify-content: center; font-size: 1.4rem;
}
.topbar-name { font-size: 1rem; font-weight: 800; color: #f1f5f9; }
.topbar-sub  { font-size: 0.75rem; color: #64748b; margin-top: 1px; }
.topbar-badge {
    background: rgba(16,185,129,0.15); color: #34d399;
    border: 1px solid rgba(16,185,129,0.3); border-radius: 20px;
    padding: 5px 16px; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.04em;
}

/* HERO */
.hero-section {
    background: linear-gradient(135deg,#060d1f 0%,#0d1a3a 55%,#130a2e 100%);
    padding: 52px 60px 44px;
    border-bottom: 1px solid #1e293b;
    position: relative; overflow: hidden;
}
.hero-glow-1 {
    position:absolute;top:-80px;right:10%;width:320px;height:320px;border-radius:50%;
    background:radial-gradient(circle,rgba(59,130,246,0.18),transparent 70%);pointer-events:none;
}
.hero-glow-2 {
    position:absolute;bottom:-60px;left:30%;width:260px;height:260px;border-radius:50%;
    background:radial-gradient(circle,rgba(139,92,246,0.14),transparent 70%);pointer-events:none;
}
.hero-name  { font-size:3rem;font-weight:800;color:#f1f5f9;margin:0 0 8px;line-height:1.1;letter-spacing:-1px; }
.hero-title {
    font-size:1.1rem;font-weight:700;
    background:linear-gradient(90deg,#3b82f6,#8b5cf6);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:10px;
}
.hero-sub   { font-size:0.87rem;color:#64748b;margin-bottom:16px; }
.hero-body  { font-size:0.95rem;color:#94a3b8;line-height:1.85;max-width:580px;margin-bottom:24px; }
.chip {
    display:inline-block;background:rgba(59,130,246,0.1);color:#60a5fa;
    border:1px solid rgba(59,130,246,0.25);border-radius:20px;
    padding:4px 14px;font-size:0.74rem;font-weight:600;margin:3px;
}
.chip-g { background:rgba(16,185,129,0.1);color:#34d399;border-color:rgba(16,185,129,0.25); }
.chip-p { background:rgba(139,92,246,0.1);color:#a78bfa;border-color:rgba(139,92,246,0.25); }
.chip-o { background:rgba(249,115,22,0.1);color:#fb923c;border-color:rgba(249,115,22,0.25); }

/* METRIC CARDS */
[data-testid="stMetric"] {
    background:linear-gradient(135deg,#0d1527,#111827) !important;
    border:1px solid #1e293b !important; border-radius:16px !important; padding:22px 20px !important;
    transition:border-color 0.2s,box-shadow 0.2s !important;
}
[data-testid="stMetric"]:hover { border-color:#3b82f6 !important; box-shadow:0 0 20px rgba(59,130,246,0.1) !important; }
[data-testid="stMetricValue"] { font-size:2.4rem !important;font-weight:800 !important;color:#f1f5f9 !important; }
[data-testid="stMetricDelta"] { color:#60a5fa !important;font-size:0.78rem !important;font-weight:600 !important; }
[data-testid="stMetricLabel"] { color:#64748b !important;font-size:0.82rem !important;font-weight:500 !important; }

/* CONTENT CARDS */
[data-testid="stVerticalBlockBorderWrapper"] {
    background:linear-gradient(135deg,#0d1527,#111827) !important;
    border:1px solid #1e293b !important; border-radius:16px !important;
    transition:border-color 0.25s,box-shadow 0.25s !important;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color:#3b82f6 !important; box-shadow:0 0 24px rgba(59,130,246,0.1) !important;
}

/* PROGRESS */
[data-testid="stProgress"] > div > div {
    background:linear-gradient(90deg,#3b82f6,#8b5cf6) !important;
    border-radius:20px !important; height:8px !important;
}
[data-testid="stProgress"] > div {
    background:#1e293b !important; border-radius:20px !important; height:8px !important;
}

/* ALERTS */
[data-testid="stAlert"] { border-radius:12px !important; border:none !important; }

/* EXPANDERS (still used elsewhere, kept for safety) */
[data-testid="stExpander"] {
    background:#0d1527 !important; border:1px solid #1e293b !important;
    border-radius:14px !important; margin-bottom:10px !important;
}
[data-testid="stExpander"]:hover { border-color:#3b82f6 !important; }

/* DOWNLOAD BUTTON */
[data-testid="stDownloadButton"] button {
    background:linear-gradient(135deg,#3b82f6,#8b5cf6) !important;
    color:white !important; border:none !important; border-radius:10px !important;
    font-weight:700 !important; font-size:0.85rem !important;
    box-shadow:0 4px 14px rgba(59,130,246,0.3) !important;
    transition:all 0.2s !important; width:100% !important;
}
[data-testid="stDownloadButton"] button:hover {
    box-shadow:0 6px 20px rgba(59,130,246,0.5) !important;
    transform:translateY(-1px) !important;
}

/* LINK BUTTONS */
[data-testid="stLinkButton"] a { border-radius:8px !important;font-weight:600 !important; }

/* PROJECT TOGGLE BUTTON (replaces buggy st.expander arrow) */
.proj-toggle-btn button {
    background:transparent !important;
    border:1px solid #1e293b !important;
    color:#60a5fa !important;
    font-weight:800 !important;
    font-size:1rem !important;
    border-radius:8px !important;
    transition:all 0.2s ease !important;
    padding:0.25rem 0 !important;
}
.proj-toggle-btn button:hover {
    background:rgba(59,130,246,0.12) !important;
    border-color:#3b82f6 !important;
    box-shadow:0 0 12px rgba(59,130,246,0.25) !important;
    transform:translateY(-1px) !important;
}

hr { border-color:#1e293b !important; }
.page-wrap { padding:1.8rem 3.5rem; }
h1 { font-weight:800 !important; letter-spacing:-0.5px !important; }
h2,h3 { font-weight:700 !important; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if "open_project" not in st.session_state:
    st.session_state.open_project = None

# ── TOP BAR ───────────────────────────────────────────────────────────────────
profile_loc = PROFILE.get('location', 'Sheffield, UK')
profile_phone = PROFILE.get('phone', '+44 7587 975094')

st.markdown(f"""
<div class="topbar">
  <div class="topbar-left">
    <div class="topbar-avatar">👨‍💻</div>
    <div>
      <div class="topbar-name">{PROFILE['name']}</div>
      <div class="topbar-sub">Data Engineer & Data Analyst · {profile_loc} · {profile_phone}</div>
    </div>
  </div>
  <span class="topbar-badge">✅ &nbsp;Open to Work — No Sponsorship Required</span>
</div>
""", unsafe_allow_html=True)

# ── NAV ───────────────────────────────────────────────────────────────────────
pages = ["🏠 Home","👤 About","🚀 Projects","🛠️ Skills",
         "💼 Experience","🎓 Education","🏆 Achievements","📬 Contact"]
nav_cols = st.columns(len(pages))
for i, pg in enumerate(pages):
    with nav_cols[i]:
        if st.button(pg, key=f"nav_{pg}", use_container_width=True,
                     type="primary" if st.session_state.page == pg else "secondary"):
            st.session_state.page = pg
            st.rerun()

st.markdown("<hr style='border:none;border-top:1px solid #1e293b;margin:0;'>", unsafe_allow_html=True)


# ── CV DOWNLOAD BUTTONS ───────────────────────────────────────────────────────
def cv_buttons():
    cols = st.columns(len(CVS))
    for col, cv in zip(cols, CVS):
        with col:
            if os.path.exists(cv["file"]):
                with open(cv["file"], "rb") as f:
                    st.download_button(
                        label=cv["label"],
                        data=f.read(),
                        file_name=cv["file"],
                        mime="application/pdf",
                        use_container_width=True,
                        key=f"cv_{cv['file']}_{st.session_state.page}",
                    )
            else:
                st.caption(f"{cv['label']} — add PDF to folder")


# ── SECTION HEADER ────────────────────────────────────────────────────────────
def section(title, subtitle=""):
    st.markdown(f"""
<div style='margin:0 0 4px;'>
  <span style='font-size:1.5rem;font-weight:800;color:#f1f5f9;'>{title}</span>
</div>
<div style='width:44px;height:3px;background:linear-gradient(90deg,#3b82f6,#8b5cf6);
  border-radius:4px;margin-bottom:{"8px" if subtitle else "14px"};'></div>
{"<p style='color:#64748b;font-size:0.88rem;margin-bottom:18px;'>"+subtitle+"</p>" if subtitle else ""}
""", unsafe_allow_html=True)


# ── PROJECT CARD (custom toggle — replaces buggy st.expander) ────────────────
def project_card(proj, idx):
    is_open = st.session_state.open_project == idx
    with st.container(border=True):
        hc, ac = st.columns([9, 1])
        with hc:
            st.markdown(
                f"**{proj['emoji']}&nbsp;&nbsp;{proj['title']}**&nbsp;&nbsp;·&nbsp;&nbsp;"
                f"_{proj['category']}_&nbsp;&nbsp;·&nbsp;&nbsp;{proj['status']}"
            )
        with ac:
            st.markdown('<div class="proj-toggle-btn">', unsafe_allow_html=True)
            if st.button("▾" if not is_open else "▴", key=f"toggle_{idx}", use_container_width=True):
                st.session_state.open_project = None if is_open else idx
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        if is_open:
            st.divider()
            st.info(f"💡 **Impact:** {proj['impact']}")
            cd, ct = st.columns([3, 2])
            with cd:
                st.write(proj["description"])
                for h in proj["highlights"][:3]:
                    st.write(f"✅  {h}")
            with ct:
                st.markdown("**Stack:**")
                for t in proj["tech"]:
                    st.markdown(f"• `{t}`")
            b1, b2, _ = st.columns([1.3, 1.3, 5])
            with b1:
                if proj["live_url"]:
                    st.link_button("🔗 Live Demo", proj["live_url"], use_container_width=True)
            with b2:
                st.link_button("⬛ GitHub", proj["github_url"], use_container_width=True)


# ════════════════════════════════════════════════════════════════════
#  HOME
# ════════════════════════════════════════════════════════════════════
def page_home():
    st.markdown(f"""
<div class="hero-section">
  <div class="hero-glow-1"></div><div class="hero-glow-2"></div>
  <div style="display:flex;gap:56px;align-items:flex-start;flex-wrap:wrap;">
    <div style="flex:1;min-width:320px;">
      <div class="hero-name">Hi, I'm {PROFILE['name']} 👋</div>
      <div class="hero-title">{PROFILE['title']}</div>
      <div class="hero-sub">{PROFILE['tagline']}</div>
      <div class="hero-body">{PROFILE['summary']}</div>
      <div>
        <span class="chip">📊 Data Engineering</span>
        <span class="chip chip-g">📈 Data Analytics</span>
        <span class="chip chip-p">🧪 QA Automation</span>
        <span class="chip chip-o">☁️ Cloud (AWS)</span>
        <span class="chip chip-g">✅ No Sponsorship</span>
      </div>
    </div>
    <div style="min-width:260px;max-width:300px;">
      <div style="background:rgba(255,255,255,0.04);border:1px solid #1e293b;
        border-radius:16px;padding:20px 22px;margin-bottom:12px;">
        <div style="font-size:0.7rem;color:#475569;font-weight:700;
          text-transform:uppercase;letter-spacing:0.1em;margin-bottom:12px;">🎯 Open To</div>
        {"".join([f'<div style="font-size:0.86rem;color:#e2e8f0;padding:6px 0;border-bottom:1px solid #1e293b;">{e}&nbsp;&nbsp;{r}</div>' for e,r in OPEN_TO])}
      </div>
      <div style="background:rgba(16,185,129,0.07);border:1px solid rgba(16,185,129,0.2);
        border-radius:12px;padding:14px 16px;font-size:0.82rem;color:#94a3b8;line-height:1.9;">
        📍 Sheffield, UK — Remote · Hybrid · On-site<br>
        ✅ Graduate Route Visa<br>
        ✅ No Sponsorship Required<br>
        ⚡ Available immediately
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div class='page-wrap' style='padding-top:1.2rem;'>", unsafe_allow_html=True)

    # Buttons row
    b1,b2,b3,_ = st.columns([1.2,1.2,1.2,3])
    with b1: st.link_button("⬛  GitHub",   PROFILE["github"],                  use_container_width=True)
    with b2: st.link_button("💼  LinkedIn", PROFILE["linkedin"],                use_container_width=True)
    with b3: st.link_button("📧  Email",    f"mailto:{PROFILE['email_gmail']}", use_container_width=True)

    st.markdown("**📄 Download CV — choose version:**")
    cv_buttons()

    st.divider()
    section("📈 At a Glance")
    m1,m2,m3,m4 = st.columns(4)
    for col,(num,label,delta) in zip([m1,m2,m3,m4],STATS):
        col.metric(label.replace("\n"," "), num, delta)

    st.divider()
    section("🚀 Featured Projects","Click a project to expand · Live demos available")
    for idx, proj in enumerate(PROJECTS[:4]):
        project_card(proj, idx)

    _,ctr,_ = st.columns([3,2,3])
    with ctr:
        if st.button(f"🚀  View All {len(PROJECTS)} Projects →", use_container_width=True, type="primary"):
            st.session_state.page = "🚀 Projects"; st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  ABOUT
# ════════════════════════════════════════════════════════════════════
def page_about():
    st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)
    section("👤 About Me")

    col_bio, col_facts = st.columns([3,2], gap="large")
    with col_bio:
        st.markdown(f"""
I'm a Computing graduate — **MSc, Merit at Sheffield Hallam University** — with
**2+ years of enterprise experience at Infosys** delivering QA for CRM and core banking systems,
now transitioning into data engineering with a portfolio of production-deployed projects.

I've deliberately built across the stack: automating tests, monitoring cloud infrastructure,
and engineering data pipelines — because data engineers who understand the full system
are far more valuable than specialists in a silo.

My flagship project — an **Automated Job Market Intelligence Pipeline** — demonstrates
production-thinking: Medallion Architecture, custom circuit breaker validation,
idempotent PostgreSQL upserts, serverless cron scheduling, and CI/CD via GitHub.
Not a tutorial project. A real system.

📍 **Sheffield, UK** — available immediately on **Graduate Route Visa**.
No sponsorship required.
        """)
        st.markdown("---")
        st.markdown("#### 🔧 Core Strengths")
        c1,c2 = st.columns(2)
        strengths = [
            ("📊","Data Engineering","ETL · Medallion Architecture · SQLAlchemy · PostgreSQL · CI/CD"),
            ("📈","Data Analytics","SQL · Pandas · Plotly · Streamlit · 260K+ record analysis"),
            ("☁️","Cloud & Infrastructure","AWS EC2 · CloudWatch · SNS · boto3 · Nginx · Gunicorn"),
            ("🧪","QA & Test Automation","Selenium · pytest · POM · 200+ test cases · Jira · HP ALM"),
        ]
        for i,(icon,title,cap) in enumerate(strengths):
            with (c1 if i%2==0 else c2):
                with st.container(border=True):
                    st.markdown(f"**{icon} {title}**")
                    st.caption(cap)

    with col_facts:
        with st.container(border=True):
            st.markdown("#### 📋 Profile")
            for icon,label,val in [
                ("📍","Location","Sheffield, UK"),
                ("📞","Phone","+44 7587 975094"),
                ("🎓","Degree","MSc Computing (Merit)"),
                ("🏢","University","Sheffield Hallam University"),
                ("💼","Experience","2+ years @ Infosys"),
                ("🏆","Award","Best Performer — Infosys DDO"),
                ("🥉","Hackathon","3rd Place Cloud Computing — SHU"),
                ("✅","Visa","Graduate Route Visa"),
                ("✅","Sponsorship","No Sponsorship Required"),
                ("📧","Gmail","anudeepburra18@gmail.com"),
                ("📧","Outlook","anuburra18@outlook.com"),
            ]:
                st.markdown(f"**{icon} {label}:** {val}")

        st.markdown("**📄 Download CV:**")
        cv_buttons()

    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  PROJECTS
# ════════════════════════════════════════════════════════════════════
def page_projects():
    st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)
    section("🚀 Projects", f"{len(PROJECTS)} production-grade projects — data engineering, analytics, cloud monitoring, QA, and IT support.")

    cats = ["All"] + list(dict.fromkeys(p["category"] for p in PROJECTS))
    selected = st.selectbox("Filter", cats, label_visibility="collapsed")
    filtered = PROJECTS if selected=="All" else [p for p in PROJECTS if p["category"]==selected]

    for proj in filtered:
        with st.container(border=True):
            tc,sc = st.columns([5,2])
            with tc:
                st.markdown(f"### {proj['emoji']}  {proj['title']}")
                st.caption(f"🏷️ {proj['category']}  ·  {proj['status']}")
            with sc:
                st.markdown("<br>", unsafe_allow_html=True)
                st.info(f"💡 {proj['impact']}")
            st.write(proj["description"])
            st.markdown("**Key highlights:**")
            c1,c2 = st.columns(2)
            for i,h in enumerate(proj["highlights"]):
                with (c1 if i%2==0 else c2): st.write(f"✅  {h}")
            st.markdown(f"**Tech Stack:** `{'`  ·  `'.join(proj['tech'])}`")
            b1,b2,_ = st.columns([1.3,1.3,6])
            with b1:
                if proj["live_url"]: st.link_button("🔗 Live Demo", proj["live_url"], use_container_width=True)
                else: st.button("🔗 No Demo", disabled=True, key=f"nd_{proj['title']}", use_container_width=True)
            with b2: st.link_button("⬛ GitHub", proj["github_url"], use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  SKILLS
# ════════════════════════════════════════════════════════════════════
def page_skills():
    st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)
    section("🛠️ Skills","All technologies used across real deployed projects and enterprise work at Infosys.")

    c1,c2 = st.columns(2, gap="medium")
    for i,(group,data) in enumerate(SKILLS.items()):
        with (c1 if i%2==0 else c2):
            with st.container(border=True):
                st.markdown(f"**{group}**")
                st.markdown("  ".join([f"`{s}`" for s in data["items"]]))

    st.divider()
    section("📊 Proficiency Levels","Based on project work, professional experience, and academic study.")
    for skill,pct in PROFICIENCIES:
        lc,bc = st.columns([3,7])
        with lc: st.markdown(f"**{skill}**")
        with bc: st.progress(pct/100, text=f"{pct}%")

    st.divider()
    section("📜 Certifications")
    c1,c2 = st.columns(2)
    for i,(icon,cert,issuer) in enumerate(CERTIFICATIONS):
        with (c1 if i%2==0 else c2):
            with st.container(border=True):
                st.markdown(f"**{icon} {cert}**")
                st.caption(f"Issued by: {issuer}")

    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  EXPERIENCE
# ════════════════════════════════════════════════════════════════════
def page_experience():
    st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)
    section("💼 Experience")

    for exp in EXPERIENCE:
        with st.container(border=True):
            rc,dc = st.columns([4,2])
            with rc:
                st.markdown(f"### {exp['role']}")
                st.markdown(f"**🏢 {exp['company']}**  ·  {exp['location']}")
                st.caption(f"📅 {exp['period']}")
            with dc:
                st.markdown("<br>", unsafe_allow_html=True)
                st.success(f"⏱️ {exp['duration']}  ·  {exp['type']}")
            for pt in exp["points"]: st.write(f"▸  {pt}")

    st.divider()
    section("📋 Right to Work & Availability")
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.success("✅ **Graduate Route Visa**\n\nNo Sponsorship Required")
    with c2: st.success("⚡ **Immediate Start**\n\nAvailable right now")
    with c3: st.info("📍 **Sheffield, UK**\n\nRemote · Hybrid · On-site")
    with c4: st.info("🌍 **Work Rights**\n\nFull UK work authorisation")

    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  EDUCATION
# ════════════════════════════════════════════════════════════════════
def page_education():
    st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)
    section("🎓 Education")

    for edu in EDUCATION:
        with st.container(border=True):
            dc,gc = st.columns([4,2])
            with dc:
                st.markdown(f"### {edu['degree']}")
                st.markdown(f"**🏛️ {edu['institution']}**  ·  {edu['location']}")
                st.caption(f"📅 {edu['period']}")
            with gc:
                st.markdown("<br><br>", unsafe_allow_html=True)
                st.success(f"🏆  **{edu['grade']}**")
            for h in edu["highlights"]: st.write(f"▸  {h}")

    st.divider()
    section("📜 Certifications")
    c1,c2 = st.columns(2)
    for i,(icon,cert,issuer) in enumerate(CERTIFICATIONS):
        with (c1 if i%2==0 else c2):
            with st.container(border=True):
                st.markdown(f"**{icon} {cert}**")
                st.caption(f"Issued by: {issuer}")

    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  ACHIEVEMENTS
# ════════════════════════════════════════════════════════════════════
def page_achievements():
    st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)
    section("🏆 Achievements & Recognition")

    for icon,title,org,desc in ACHIEVEMENTS:
        with st.container(border=True):
            c1,c2 = st.columns([1,6])
            with c1: st.markdown(f"<div style='font-size:2.5rem;text-align:center;padding-top:8px;'>{icon}</div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"**{title}**")
                st.caption(f"🏢 {org}")
                st.write(desc)

    st.divider()
    section("📊 Key Performance Numbers","Quantified impact from professional experience.")
    k1,k2,k3,k4 = st.columns(4)
    k1.metric("🧪 Test Cases Designed", "200+", "per release @ Infosys")
    k2.metric("🐛 Defect Escape Rate", "0%", "3 consecutive releases")
    k3.metric("⚡ Regression Effort", "~30%", "reduction via Selenium")
    k4.metric("🔍 Data Issues Found", "50+", "SQL validation @ Infosys")

    st.divider()
    section("📜 Certifications")
    c1,c2 = st.columns(2)
    for i,(icon,cert,issuer) in enumerate(CERTIFICATIONS):
        with (c1 if i%2==0 else c2):
            with st.container(border=True):
                st.markdown(f"**{icon} {cert}**")
                st.caption(f"Issued by: {issuer}")

    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════
#  CONTACT
# ════════════════════════════════════════════════════════════════════
def page_contact():
    st.markdown("<div class='page-wrap'>", unsafe_allow_html=True)
    section("📬 Get In Touch","Actively looking for data engineering and analytics roles across the UK.")

    cl,cr = st.columns([3,2], gap="large")
    with cl:
        for icon,label,value,url in [
            ("📧","Gmail",          PROFILE["email_gmail"],  f"mailto:{PROFILE['email_gmail']}"),
            ("📧","Outlook",        PROFILE["email_outlook"],f"mailto:{PROFILE['email_outlook']}"),
            ("📞","Phone",          PROFILE["phone"],         f"tel:{PROFILE['phone']}"),
            ("💼","LinkedIn",       "linkedin.com/in/anudeepburra", PROFILE["linkedin"]),
            ("⬛","GitHub",         "github.com/Anudeep151998",     PROFILE["github"]),
        ]:
            with st.container(border=True):
                st.markdown(f"**{icon} {label}**")
                st.code(value, language=None)
                st.link_button(f"Open {label}", url, use_container_width=True)

    with cr:
        st.markdown("#### 🎯 Open To Roles")
        for e,r in OPEN_TO: st.info(f"{e}  {r}")

        st.markdown("#### 📄 Download CV")
        cv_buttons()

        st.markdown("#### 📋 Right to Work")
        st.success("✅ Graduate Route Visa\n\n✅ No Sponsorship Required\n\n📍 Sheffield, UK\n\n⚡ Immediate start")

    st.divider()
    st.success(
        "### 🟢 Ready for My Next Role\n\n"
        "Actively applying for data engineering and analytics positions across the UK. "
        "UK Graduate Route Visa holder — **no sponsorship required**, eligible to start immediately.\n\n"
        f"📧 **{PROFILE['email_gmail']}**  ·  📞 **{PROFILE['phone']}**"
    )
    cc1,cc2,cc3 = st.columns(3)
    with cc1: st.link_button("📧 Email Me",  f"mailto:{PROFILE['email_gmail']}", use_container_width=True)
    with cc2: st.link_button("💼 LinkedIn",  PROFILE["linkedin"],                use_container_width=True)
    with cc3: st.link_button("⬛ GitHub",    PROFILE["github"],                  use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ── ROUTER ────────────────────────────────────────────────────────────────────
PAGE_MAP = {
    "🏠 Home":        page_home,
    "👤 About":       page_about,
    "🚀 Projects":    page_projects,
    "🛠️ Skills":      page_skills,
    "💼 Experience":  page_experience,
    "🎓 Education":   page_education,
    "🏆 Achievements":page_achievements,
    "📬 Contact":     page_contact,
}
PAGE_MAP[st.session_state.page]()
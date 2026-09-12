import re
from datetime import datetime
import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="ResearchForge AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>

/* =========================================================
   GLOBAL
   ========================================================= */

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(99,102,241,.18), transparent 28%),
        radial-gradient(circle at 95% 10%, rgba(14,165,233,.12), transparent 25%),
        #080b12;
    color: #f8fafc;
}

/* Main content text */
.main,
.block-container {
    color: #f8fafc;
}

/* All normal markdown text */
.stMarkdown,
.stMarkdown p,
.stMarkdown li,
.stMarkdown span {
    color: #e2e8f0;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #f8fafc !important;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] {
    background: #0b0f18;
    border-right: 1px solid rgba(255,255,255,.08);
}

[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

[data-testid="stSidebar"] .stCaption {
    color: #94a3b8 !important;
}

/* Text area */
[data-testid="stSidebar"] textarea {
    background: #111827 !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

[data-testid="stSidebar"] textarea::placeholder {
    color: #94a3b8 !important;
}

/* Select box */
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: #111827 !important;
    color: #f8fafc !important;
    border-color: #334155 !important;
}

/* =========================================================
   QUICK TOPIC SELECTBOX — CENTER PANEL
   ========================================================= */

/* Main selectbox */
div[data-testid="stSelectbox"] [data-baseweb="select"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Selectbox visible box */
div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
}

/* Selected value */
div[data-testid="stSelectbox"] [data-baseweb="select"] [role="button"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Selected text */
div[data-testid="stSelectbox"] [data-baseweb="select"] span {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* Nested elements */
div[data-testid="stSelectbox"] [data-baseweb="select"] div {
    color: #000000 !important;
}

/* Input */
div[data-testid="stSelectbox"] input {
    background-color: #ffffff !important;
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    caret-color: #000000 !important;
}

/* Arrow */
div[data-testid="stSelectbox"] [data-baseweb="select"] svg {
    color: #475569 !important;
    fill: #475569 !important;
}


/* =========================================================
   QUICK TOPIC DROPDOWN MENU
   ========================================================= */

div[data-baseweb="popover"] {
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] > div {
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] ul {
    background-color: #ffffff !important;
}

/* Options */
div[data-baseweb="popover"] li,
div[data-baseweb="popover"] [role="option"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Option text */
div[data-baseweb="popover"] li *,
div[data-baseweb="popover"] [role="option"] * {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* Hover */
div[data-baseweb="popover"] li:hover,
div[data-baseweb="popover"] [role="option"]:hover {
    background-color: #e2e8f0 !important;
    color: #000000 !important;
}

/* Selected option */
div[data-baseweb="popover"] [aria-selected="true"] {
    background-color: #e2e8f0 !important;
    color: #000000 !important;
}

/* =========================================================
   QUICK TOPIC DROPDOWN MENU
   ========================================================= */

[data-baseweb="popover"] {
    background-color: #ffffff !important;
}

[data-baseweb="popover"] > div {
    background-color: #ffffff !important;
}

[data-baseweb="popover"] ul {
    background-color: #ffffff !important;
}

/* Dropdown options */
[data-baseweb="popover"] li,
[data-baseweb="popover"] [role="option"] {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Option text */
[data-baseweb="popover"] li *,
[data-baseweb="popover"] [role="option"] * {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

/* Hover */
[data-baseweb="popover"] li:hover,
[data-baseweb="popover"] [role="option"]:hover {
    background-color: #e2e8f0 !important;
    color: #000000 !important;
}

/* Selected option */
[data-baseweb="popover"] [aria-selected="true"] {
    background-color: #e2e8f0 !important;
    color: #000000 !important;
}

/* =========================================================
   HERO
   ========================================================= */

.hero {
    padding: 2.2rem 2.4rem;
    border-radius: 24px;
    background:
        linear-gradient(
            135deg,
            rgba(99,102,241,.34),
            rgba(14,165,233,.18),
            rgba(15,23,42,.75)
        );
    border: 1px solid rgba(255,255,255,.10);
    box-shadow: 0 20px 60px rgba(0,0,0,.28);
    margin-bottom: 1.4rem;
}

.kicker {
    color: #a5b4fc !important;
    font-size: .75rem;
    font-weight: 800;
    letter-spacing: .14em;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 2.5rem;
    margin: .25rem 0;
}

.hero p {
    color: #dbeafe !important;
    max-width: 850px;
    line-height: 1.6;
}

/* =========================================================
   STAGE CARDS
   ========================================================= */

.stage {
    min-height: 125px;
    padding: 1rem;
    border-radius: 16px;
    background: rgba(15,23,42,.72);
    border: 1px solid rgba(255,255,255,.10);
}

.stage-num {
    color: #a5b4fc !important;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: .1em;
}

.stage-title {
    color: #ffffff !important;
    font-weight: 750;
    margin: .3rem 0;
}

.stage-desc {
    color: #cbd5e1 !important;
    font-size: .82rem;
    line-height: 1.45;
}

/* =========================================================
   METRICS
   ========================================================= */

div[data-testid="stMetric"] {
    background: rgba(15,23,42,.72) !important;
    border: 1px solid rgba(255,255,255,.10) !important;
    border-radius: 16px !important;
    padding: 1rem !important;
}

div[data-testid="stMetric"] label {
    color: #94a3b8 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #ffffff !important;
}

div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
    color: #cbd5e1 !important;
}

/* =========================================================
   TABS
   ========================================================= */

button[data-baseweb="tab"] {
    color: #94a3b8 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #ffffff !important;
}

/* =========================================================
   EXPANDERS
   ========================================================= */

div[data-testid="stExpander"] {
    background: rgba(15,23,42,.60) !important;
    border: 1px solid rgba(255,255,255,.10) !important;
    border-radius: 14px !important;
}

div[data-testid="stExpander"] summary {
    color: #f8fafc !important;
}

div[data-testid="stExpander"] p {
    color: #cbd5e1 !important;
}

/* =========================================================
   TEXT INPUTS
   ========================================================= */

input {
    color: #f8fafc !important;
}

input::placeholder {
    color: #94a3b8 !important;
}

/* =========================================================
   TOPIC BADGE
   ========================================================= */

.topic {
    display: inline-block;
    padding: .35rem .7rem;
    border-radius: 999px;
    background: rgba(99,102,241,.15);
    color: #c7d2fe !important;
    border: 1px solid rgba(129,140,248,.25);
    font-size: .76rem;
    font-weight: 700;
}

/* =========================================================
   CODE / RAW OUTPUT
   ========================================================= */

code {
    color: #e2e8f0 !important;
}

/* =========================================================
   ALERTS / INFO
   ========================================================= */

div[data-testid="stAlert"] {
    color: #e2e8f0 !important;
}

/* =========================================================
   BUTTONS
   ========================================================= */

button {
    color: #f8fafc !important;
}

/* Primary button */
button[kind="primary"] {
    font-weight: 700 !important;
}

/* =========================================================
   DOWNLOAD BUTTON
   ========================================================= */

[data-testid="stDownloadButton"] button {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* =========================================================
   HIDE STREAMLIT CHROME
   ========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Center research panel controls */
div[data-testid="stTextArea"] textarea {
    background:#111827 !important;
    color:#f8fafc !important;
    border:1px solid #334155 !important;
    border-radius:14px !important;
}
div[data-testid="stTextArea"] textarea::placeholder { color:#94a3b8 !important; }
div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background:#111827 !important;
    color:#ffffff !important;
    border:1px solid #475569 !important;
    border-radius:12px !important;
}
div[data-testid="stSelectbox"] [data-baseweb="select"] span { color:#ffffff !important; }
div[data-testid="stSelectbox"] [data-baseweb="select"] svg { fill:#cbd5e1 !important; color:#cbd5e1 !important; }
div[data-baseweb="popover"] { background:#111827 !important; }
div[data-baseweb="popover"] li, div[data-baseweb="popover"] [role="option"] { background:#111827 !important; color:#f8fafc !important; }
div[data-baseweb="popover"] li *, div[data-baseweb="popover"] [role="option"] * { color:#f8fafc !important; }


/* Quick topic selectbox - force readable dark field + black text */
div[data-testid="stSelectbox"] [data-baseweb="select"] > div {
    background: #f8fafc !important;
    color: #000000 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] span,
div[data-testid="stSelectbox"] [data-baseweb="select"] div,
div[data-testid="stSelectbox"] [data-baseweb="select"] input {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

div[data-testid="stSelectbox"] [data-baseweb="select"] svg {
    color: #475569 !important;
    fill: #475569 !important;
}

/* Open quick-topic menu */
div[data-baseweb="popover"] {
    background: #ffffff !important;
}

div[data-baseweb="popover"] li,
div[data-baseweb="popover"] [role="option"] {
    background: #ffffff !important;
    color: #000000 !important;
}

div[data-baseweb="popover"] li *,
div[data-baseweb="popover"] [role="option"] * {
    color: #000000 !important;
}

div[data-baseweb="popover"] li:hover,
div[data-baseweb="popover"] [role="option"]:hover {
    background: #e2e8f0 !important;
    color: #000000 !important;
}


/* Empty state */
.empty-state {
    margin-top: 1rem;
    padding: 1.5rem 1.7rem;
    text-align: center;
    border-radius: 16px;
    background: rgba(15,23,42,.72);
    border: 1px solid rgba(255,255,255,.09);
}

.empty-icon {
    font-size: 1.6rem;
    margin-bottom: .3rem;
}

.empty-title {
    color: #f8fafc !important;
    font-size: 1.05rem;
    font-weight: 750;
}

.empty-text {
    color: #94a3b8 !important;
    max-width: 650px;
    margin: .35rem auto 0;
    line-height: 1.5;
}

.empty-flow {
    color: #a5b4fc !important;
    font-size: .78rem;
    margin-top: .9rem;
}

</style>
""", unsafe_allow_html=True)

def text(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    content = getattr(value, "content", None)
    return content if isinstance(content, str) else str(value)


def urls_from(value):
    found = re.findall(r'https?://[^\s<>\]\)"]+', text(value))
    return list(dict.fromkeys(u.rstrip(".,;:") for u in found))


def critic_score(value):
    match = re.search(
        r'(?:score|rating)?\D{0,20}(\d+(?:\.\d+)?)\s*/\s*10',
        text(value),
        re.IGNORECASE
    )

    return float(match.group(1)) if match else None


def export_markdown(topic, state):
    return f"""# Research Report

## Topic
{topic}

## Final Report
{text(state.get("report"))}

## Critic Feedback
{text(state.get("feedback"))}

---

## Search Results
{text(state.get("search_results"))}

## Scraped Content
{text(state.get("scraped_content"))}
"""


if "research_state" not in st.session_state:
    st.session_state.research_state = None
if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""
if "history" not in st.session_state:
    st.session_state.history = []


with st.sidebar:
    st.markdown("## 🔬 ResearchForge AI")
    st.caption("Multi-agent research workspace")
    st.divider()

    # How the system works — moved into the sidebar
    st.markdown("### 🧠 How the system works")

    st.markdown(
        """
        <div style="
            padding:12px;
            margin-bottom:10px;
            border-radius:12px;
            background:rgba(99,102,241,.10);
            border:1px solid rgba(129,140,248,.18);
        ">
            <b style="color:#ffffff;">01 · 🔎 Search Agent</b><br>
            <span style="color:#94a3b8;font-size:.82rem;">
                Uses Groq + Tavily to find recent and relevant sources.
            </span>
        </div>

        <div style="
            padding:12px;
            margin-bottom:10px;
            border-radius:12px;
            background:rgba(14,165,233,.08);
            border:1px solid rgba(56,189,248,.16);
        ">
            <b style="color:#ffffff;">02 · 📖 Reader Agent</b><br>
            <span style="color:#94a3b8;font-size:.82rem;">
                Selects a useful source and extracts deeper page content.
            </span>
        </div>

        <div style="
            padding:12px;
            margin-bottom:10px;
            border-radius:12px;
            background:rgba(16,185,129,.08);
            border:1px solid rgba(52,211,153,.15);
        ">
            <b style="color:#ffffff;">03 · ✍️ Writer Chain</b><br>
            <span style="color:#94a3b8;font-size:.82rem;">
                Uses an LCEL/Runnable pipeline to create the research report.
            </span>
        </div>

        <div style="
            padding:12px;
            margin-bottom:10px;
            border-radius:12px;
            background:rgba(245,158,11,.08);
            border:1px solid rgba(251,191,36,.15);
        ">
            <b style="color:#ffffff;">04 · 🧐 Critic Chain</b><br>
            <span style="color:#94a3b8;font-size:.82rem;">
                Reviews the report and provides a quality score and feedback.
            </span>
        </div>

        <div style="
            text-align:center;
            padding:8px;
            color:#64748b;
            font-size:.75rem;
        ">
            Search → Read → Write → Critique
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### 🛠️ Technology Stack")
    st.caption("🤖 LLM — Groq · openai/gpt-oss-20b")
    st.caption("🌐 Search — Tavily")
    st.caption("🕷️ Scraping — BeautifulSoup")
    st.caption("🔗 Orchestration — pipeline.py")

    if st.session_state.history:
        st.divider()
        st.markdown("### 🕘 Recent research")

        for i, item in enumerate(reversed(st.session_state.history[-8:])):
            if st.button(
                f"📄 {item['topic'][:34]}",
                key=f"history_{i}",
                use_container_width=True,
            ):
                st.session_state.research_topic = item["topic"]
                st.session_state.research_state = item["state"]
                st.rerun()


st.markdown("""
<div class="hero">
    <div class="kicker">MULTI-AGENT INTELLIGENCE</div>
    <h1>ResearchForge AI 🔬</h1>
    <p>
        Turn a research question into a polished report using specialized
        search, reading, writing, and critic components.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CENTER RESEARCH PANEL
# ============================================================
panel_left, panel_center, panel_right = st.columns([1, 5, 1])

with panel_center:
    st.markdown("""
    <div style="text-align:center; margin:1.5rem 0 1rem 0;">
        <div style="color:#a5b4fc; font-size:.74rem; font-weight:800; letter-spacing:.14em;">
            ASK THE RESEARCH AGENT
        </div>
        <div style="color:#ffffff; font-size:1.7rem; font-weight:800; margin-top:.35rem;">
            What do you want to research?
        </div>
        <div style="color:#94a3b8; font-size:.9rem; margin-top:.4rem;">
            Give the agents a topic. They will search, read, write, and critique it.
        </div>
    </div>
    """, unsafe_allow_html=True)

    topic = st.text_area(
        "Research topic",
        value=st.session_state.research_topic,
        placeholder=(
            "Example: Latest advances in AI agents\n"
            "Example: Future of solid-state batteries\n"
            "Example: Impact of generative AI on software engineering"
        ),
        height=115,
        label_visibility="collapsed",
    )

    quick_col, run_col = st.columns([3, 1])

    with quick_col:
        quick_topic = st.selectbox(
            "Quick topic",
            [
                "Choose a quick topic...",
                "Latest advances in AI agents",
                "Future of solid-state batteries",
                "Impact of generative AI on software engineering",
                "Latest developments in quantum computing",
            ],
            label_visibility="collapsed",
        )
        if quick_topic != "Choose a quick topic...":
            topic = quick_topic

    with run_col:
        st.write("")
        run = st.button(
            "🚀 Start Research",
            type="primary",
            use_container_width=True,
        )

    st.markdown(
        '<div style="text-align:center;color:#64748b;font-size:.78rem;margin:.8rem 0 1.2rem 0;">'
        '🔎 Search &nbsp;→&nbsp; 📖 Read &nbsp;→&nbsp; ✍️ Write &nbsp;→&nbsp; 🧐 Critique'
        '</div>',
        unsafe_allow_html=True,
    )

if run:
    clean_topic = topic.strip()
    if not clean_topic:
        st.warning("Please enter a research topic first.")
    else:
        st.session_state.research_topic = clean_topic
        with st.status("🚀 Running research pipeline...", expanded=True) as status:
            status.write("🔎 Search Agent → finding sources")
            status.write("📖 Reader Agent → extracting deeper content")
            status.write("✍️ Writer Chain → generating report")
            status.write("🧐 Critic Chain → reviewing report")
            try:
                result = run_research_pipeline(clean_topic)
                st.session_state.research_state = result
                st.session_state.history.append({
                    "topic": clean_topic,
                    "state": result,
                    "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
                })
                status.update(label="✅ Research completed", state="complete", expanded=False)
            except Exception as exc:
                status.update(label="❌ Pipeline failed", state="error", expanded=True)
                st.exception(exc)


state = st.session_state.research_state

if not state:
    st.markdown(
    """
    <div class="empty-state">
        <div class="empty-icon">🧠</div>
        <div class="empty-title">Ready when you are.</div>
        <div class="empty-text">
            Enter a research question above and let the agents turn
            scattered web information into a structured report.
        </div>
        <div class="empty-flow">
            🔎 Discover sources &nbsp;•&nbsp; 📖 Read deeply &nbsp;•&nbsp;
            ✍️ Build the report &nbsp;•&nbsp; 🧐 Validate the result
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
else:
    topic = st.session_state.research_topic
    report = text(state.get("report"))
    feedback = text(state.get("feedback"))
    search_results = text(state.get("search_results"))
    scraped = text(state.get("scraped_content"))
    urls = urls_from(search_results)
    score = critic_score(feedback)

    st.markdown('<span class="topic">RESEARCH TOPIC</span>', unsafe_allow_html=True)
    st.markdown(f"## {topic}")

    a, b, c, d = st.columns(4)
    a.metric("Pipeline", "Completed")
    b.metric("Sources found", len(urls) if urls else "—")
    c.metric("Critic score", f"{score:g}/10" if score is not None else "—")
    d.metric("Report", "Ready" if report else "—")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📄 Final Report", "🧐 Critic Review", "🔗 Sources", "🧪 Raw Research"]
    )

    with tab1:
        st.markdown("### Final research report")
        st.markdown(report or "No report returned.")
        st.download_button(
            "⬇️ Download complete research (.md)",
            data=export_markdown(topic, state),
            file_name=f"{topic[:50].strip().replace(' ', '_')}_research.md",
            mime="text/markdown",
        )

    with tab2:
        st.markdown("### Critic review")
        if score is not None:
            st.progress(min(max(score / 10, 0.0), 1.0), text=f"Quality score: {score:g}/10")
        st.markdown(feedback or "No critic feedback returned.")

    with tab3:
        st.markdown("### Sources discovered by Search Agent")
        if urls:
            for i, url in enumerate(urls, 1):
                st.markdown(f"**{i}.** {url}")
        else:
            st.info("No URLs detected in the Search Agent output.")
        with st.expander("View Search Agent output"):
            st.write(search_results)

    with tab4:
        with st.expander("🔎 Search Agent output", expanded=True):
            st.write(search_results)
        with st.expander("📖 Reader Agent output"):
            st.write(scraped)

    st.caption("UI layer only — execution remains controlled by pipeline.py.")

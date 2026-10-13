
import streamlit as st
import html

st.set_page_config(
    page_title="Fintel | Finance Knowledge Assistant",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── COLOUR PALETTE ────────────────────────────────────────
NAVY = "#173B67"
BLUE = "#1769F5"
PALE_BLUE = "#E5F0FF"
BACKGROUND = "#F5F9FF"
TEXT = "#17365F"
MUTED = "#526D91"
BORDER = "#C9DCFA"

# ── PAGE STYLING ──────────────────────────────────────────
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background: linear-gradient(140deg, #F7FAFF 0%, #EEF5FF 100%);
        color: {TEXT};
    }}

    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {{
        display: none !important;
    }}

    .block-container {{
        max-width: 1500px;
        padding: 0 2.8rem 2rem 2.8rem;
    }}

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    /* Header */
    .fintel-header {{
        background: linear-gradient(100deg, #173B67, #214D80);
        margin: 0 -2.8rem 2.5rem -2.8rem;
        padding: 1.1rem 4%;
        display: flex;
        align-items: center;
        gap: 1.2rem;
        color: white;
        min-height: 96px;
        box-sizing: border-box;
    }}

    .brand {{
        display: flex;
        align-items: center;
        gap: 0.8rem;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -1.3px;
        color: white;
        white-space: nowrap;
    }}

    .brand-icon {{
        width: 52px;
        height: 52px;
        flex-shrink: 0;
    }}

    .header-divider {{
        height: 48px;
        width: 1px;
        background: rgba(255,255,255,0.4);
        margin: 0 0.6rem;
    }}

    .header-title {{
        color: #FFFFFF;
        font-size: clamp(1.35rem, 2.3vw, 2.15rem);
        font-weight: 700;
        letter-spacing: -0.8px;
        line-height: 1.2;
    }}

    .prototype {{
        margin-left: auto;
        background: #E1EDFF;
        color: #173B67;
        padding: 0.65rem 1.2rem;
        border-radius: 30px;
        font-size: 0.95rem;
        font-weight: 700;
        white-space: nowrap;
    }}

    /* Welcome section */
    .hero {{
        text-align: center;
        padding: 0.8rem 0 2rem;
    }}

    .hero h1 {{
        font-size: clamp(2.5rem, 4.2vw, 4.2rem);
        font-weight: 800;
        line-height: 1.15;
        letter-spacing: -2px;
        color: #102D54;
        margin: 0 0 1rem;
    }}

    .hero p {{
        font-size: clamp(1.05rem, 1.6vw, 1.4rem);
        line-height: 1.7;
        color: {MUTED};
        max-width: 1050px;
        margin: 0 auto;
    }}

    .section-title {{
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.7px;
        color: #102D54;
        margin: 0.7rem 0 0.1rem;
    }}

    .section-subtitle {{
        color: {MUTED};
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }}

    /* Topic cards */
    .topic-card {{
        background: rgba(255,255,255,0.92);
        border: 1.5px solid {BORDER};
        border-radius: 20px;
        padding: 1.3rem 1.15rem 1rem;
        min-height: 190px;
        height: 100%;
        box-sizing: border-box;
        box-shadow: 0 3px 12px rgba(23,59,103,0.025);
    }}

    .topic-top {{
        display: flex;
        align-items: center;
        gap: 0.7rem;
        margin-bottom: 1rem;
    }}

    .topic-icon {{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 58px;
        height: 58px;
        min-width: 58px;
        border-radius: 50%;
        background: {PALE_BLUE};
        color: #0753D8;
    }}

    .topic-number {{
        color: {BLUE};
        font-size: 1.35rem;
        font-weight: 800;
    }}

    .topic-name {{
        color: #102D54;
        font-size: 1.05rem;
        font-weight: 700;
        line-height: 1.35;
    }}

    .topic-description {{
        color: {TEXT};
        font-size: 0.98rem;
        line-height: 1.65;
    }}

    /* Buttons */
    div.stButton > button {{
        border-radius: 12px;
        border: 1px solid {BORDER};
        background: white;
        color: {TEXT};
        font-weight: 600;
        min-height: 46px;
        transition: all 0.2s ease;
    }}

    div.stButton > button:hover {{
        border-color: {BLUE};
        color: {BLUE};
        background: #F1F6FF;
    }}

    /* Chat area */
    .chat-note {{
        text-align: center;
        color: #718BAE;
        font-size: 0.88rem;
        margin-top: 0.5rem;
    }}

    [data-testid="stChatInput"] {{
        border: 1.5px solid {BORDER};
        border-radius: 18px;
        background: white;
        box-shadow: 0 4px 16px rgba(23,59,103,0.035);
    }}

    [data-testid="stChatInput"] textarea {{
        font-size: 1.05rem;
    }}

    [data-testid="stChatMessage"] {{
        border-radius: 16px;
        border: 1px solid #DCE8F8;
        background: rgba(255,255,255,0.8);
        padding: 1rem;
    }}

    .stAlert {{
        border-radius: 12px;
    }}

    @media (max-width: 750px) {{
        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}

        .fintel-header {{
            margin-left: -1rem;
            margin-right: -1rem;
            padding: 1rem;
            gap: 0.6rem;
            flex-wrap: wrap;
        }}

        .brand {{
            font-size: 1.7rem;
        }}

        .brand-icon {{
            width: 40px;
            height: 40px;
        }}

        .header-divider {{
            display: none;
        }}

        .header-title {{
            font-size: 1.05rem;
        }}

        .prototype {{
            font-size: 0.75rem;
            padding: 0.45rem 0.7rem;
        }}

        .hero h1 {{
            letter-spacing: -1px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── FINTEL LOGO AND HEADER ────────────────────────────────
logo_svg = """
<svg class="brand-icon" viewBox="0 0 64 64"
     xmlns="http://www.w3.org/2000/svg" fill="none">
  <defs>
    <linearGradient id="fintelGradient" x1="8" y1="58" x2="54" y2="5">
      <stop offset="0%" stop-color="#56D7F5"/>
      <stop offset="100%" stop-color="#2877FF"/>
    </linearGradient>
  </defs>
  <path d="M9 54V39L25 29V44L9 54Z" fill="url(#fintelGradient)"/>
  <path d="M29 42V23L45 13V32L29 42Z" fill="url(#fintelGradient)"/>
  <path d="M49 30V8L58 3L55 15L49 30Z" fill="#75CFFF"/>
  <path d="M8 33L25 22V12L8 23V33Z" fill="#80DFFF"/>
  <path d="M29 17L45 7V17L29 27V17Z" fill="#B2E9FF"/>
  <path d="M8 58H57" stroke="#9BCBFF" stroke-width="3"
        stroke-linecap="round"/>
</svg>
"""

st.markdown(
    f"""
    <div class="fintel-header">
        <div class="brand">
            {logo_svg}
            <span>Fintel</span>
        </div>
        <div class="header-divider"></div>
        <div class="header-title">Finance Knowledge Assistant</div>
        <div class="prototype">Prototype</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── DEMO RESPONSES ────────────────────────────────────────
# These are temporary examples, not verified Finance guidance.
DEMO_ANSWERS = {
    "revenue": (
        "Revenue recognition guidance would be retrieved from the approved "
        "Rules of Revenue Recognition document once the knowledge base is connected."
    ),
    "billing": (
        "Billing guidance would be retrieved from the approved Billing Guidelines "
        "document once the knowledge base is connected."
    ),
    "procurement": (
        "Procurement guidance would be retrieved from the approved Procurement "
        "Guidelines document once the knowledge base is connected."
    ),
    "pricing": (
        "Pricing guidance would be retrieved from the approved Pricing Guidelines "
        "document once the knowledge base is connected."
    ),
}

def get_demo_response(question):
    q = question.lower()
    for keyword, response in DEMO_ANSWERS.items():
        if keyword in q:
            return response
    return (
        "Your question has been received. Once Fintel is connected to the "
        "Finance knowledge base, it will search the approved internal documents "
        "and provide an answer with source references."
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# ── WELCOME SECTION ───────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <h1>How can I help you today?</h1>
        <p>
            Ask a question about internal Finance policies, procedures or guidance.<br>
            Fintel helps you find the information you need, with references to its sources.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── TOPIC CARDS ───────────────────────────────────────────
st.markdown('<div class="section-title">Explore a topic</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Choose a common Finance topic to get started.</div>',
    unsafe_allow_html=True,
)

topics = [
    {
        "number": "01",
        "name": "Revenue recognition",
        "description": "Where can I find our revenue recognition rules?",
        "key": "revenue",
        "icon": """<svg width="34" height="34" viewBox="0 0 40 40" fill="none">
            <path d="M10 4H24L32 12V35H10V4Z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
            <path d="M24 4V12H32" stroke="currentColor" stroke-width="3"/>
            <path d="M16 28V22M21 28V17M26 28V20" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
        </svg>""",
    },
    {
        "number": "02",
        "name": "Billing guidelines",
        "description": "What do our internal billing guidelines cover?",
        "key": "billing",
        "icon": """<svg width="34" height="34" viewBox="0 0 40 40" fill="none">
            <rect x="4" y="9" width="32" height="23" rx="4" stroke="currentColor" stroke-width="3"/>
            <path d="M5 16H35" stroke="currentColor" stroke-width="3"/>
        </svg>""",
    },
    {
        "number": "03",
        "name": "Procurement",
        "description": "Where can I find our procurement guidelines?",
        "key": "procurement",
        "icon": """<svg width="34" height="34" viewBox="0 0 40 40" fill="none">
            <path d="M3 5H8L13 27H31L36 11H11" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="16" cy="33" r="2.5" stroke="currentColor" stroke-width="3"/>
            <circle cx="29" cy="33" r="2.5" stroke="currentColor" stroke-width="3"/>
        </svg>""",
    },
    {
        "number": "04",
        "name": "Pricing guidelines",
        "description": "What internal guidance is available on pricing?",
        "key": "pricing",
        "icon": """<svg width="34" height="34" viewBox="0 0 40 40" fill="none">
            <path d="M21 4H35V18L17 36L4 23L21 4Z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
            <circle cx="28" cy="11" r="2.5" fill="currentColor"/>
        </svg>""",
    },
]

cols = st.columns(4, gap="medium")

for col, topic in zip(cols, topics):
    with col:
        st.markdown(
            f"""
            <div class="topic-card">
                <div class="topic-top">
                    <div class="topic-icon">{topic["icon"]}</div>
                    <span class="topic-number">{topic["number"]}</span>
                    <div class="topic-name">{topic["name"]}</div>
                </div>
                <div class="topic-description">{topic["description"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(
            "Explore topic  →",
            key=f"topic_{topic['key']}",
            use_container_width=True,
        ):
            st.session_state.messages.append(
                {"role": "user", "content": topic["description"]}
            )
            st.session_state.messages.append(
                {"role": "assistant", "content": get_demo_response(topic["key"])}
            )
            st.rerun()

# ── CHAT HISTORY ──────────────────────────────────────────
st.markdown("<div style='height: 2rem'></div>", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(
        message["role"],
        avatar="💠" if message["role"] == "assistant" else "👤",
    ):
        st.markdown(message["content"])

# ── CHAT INPUT ────────────────────────────────────────────
question = st.chat_input("Ask Fintel a Finance question...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    st.session_state.messages.append(
        {"role": "assistant", "content": get_demo_response(question)}
    )
    st.rerun()

# ── FOOTER NOTE ───────────────────────────────────────────
st.markdown(
    """
    <div class="chat-note">
        ⓘ &nbsp; Answers should be checked against their source documents.
        <br><br>
        <span style="font-size:0.78rem;">
            Prototype interface · Responses are illustrative until the Finance knowledge base is connected.
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

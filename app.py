
import streamlit as st

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Fintel | Finance Assistant",
    page_icon="F",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Agreed Fintel colour palette
NAVY = "#173B67"
BLUE = "#3478F6"
PALE_BLUE = "#F3F7FC"
BORDER = "#DCE6F2"
MUTED = "#53657A"
WHITE = "#FFFFFF"

# --------------------------------------------------
# Enterprise-style design
# --------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {PALE_BLUE};
    }}

    [data-testid="stHeader"] {{
        background-color: {PALE_BLUE};
    }}

    .block-container {{
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 2.5rem;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: {NAVY};
        border-right: none;
    }}

    section[data-testid="stSidebar"] * {{
        color: #FFFFFF;
    }}

    section[data-testid="stSidebar"] .stButton button {{
        background: rgba(255,255,255,0.08);
        color: #FFFFFF;
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 9px;
        text-align: left;
        min-height: 42px;
    }}

    section[data-testid="stSidebar"] .stButton button:hover {{
        background: rgba(255,255,255,0.16);
        border-color: #FFFFFF;
    }}

    .sidebar-brand {{
        font-size: 1.65rem;
        font-weight: 750;
        letter-spacing: -0.5px;
        color: #FFFFFF;
        margin-bottom: 0.2rem;
    }}

    .sidebar-subtitle {{
        color: #DCE8F7;
        font-size: 0.82rem;
        line-height: 1.5;
    }}

    .sidebar-label {{
        color: #C9D9EE;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-top: 1.2rem;
        margin-bottom: 0.45rem;
    }}

    .sidebar-note {{
        color: #DCE8F7;
        font-size: 0.82rem;
        line-height: 1.6;
    }}

    /* Main header */
    .topbar {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 14px;
        padding: 1rem 1.4rem;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
    }}

    .topbar-title {{
        color: {NAVY};
        font-size: 1.05rem;
        font-weight: 700;
    }}

    .topbar-subtitle {{
        color: {MUTED};
        font-size: 0.82rem;
        margin-top: 0.2rem;
    }}

    .status-pill {{
        color: {NAVY};
        background: #EAF1FC;
        border: 1px solid #D6E4FA;
        border-radius: 20px;
        padding: 0.35rem 0.7rem;
        font-size: 0.76rem;
        white-space: nowrap;
    }}

    /* Typography */
    .eyebrow {{
        color: {BLUE};
        font-size: 0.75rem;
        font-weight: 750;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 0.45rem;
    }}

    .welcome-title {{
        color: {NAVY};
        font-size: clamp(2rem, 4vw, 2.8rem);
        line-height: 1.15;
        font-weight: 750;
        letter-spacing: -1.1px;
        margin: 0 0 0.7rem 0;
    }}

    .welcome-copy {{
        color: {MUTED};
        font-size: 1rem;
        line-height: 1.7;
        max-width: 650px;
        margin-bottom: 1.8rem;
    }}

    .section-heading {{
        color: {NAVY};
        font-size: 1rem;
        font-weight: 700;
        margin-top: 0.5rem;
        margin-bottom: 0.3rem;
    }}

    .section-description {{
        color: {MUTED};
        font-size: 0.86rem;
        margin-bottom: 1rem;
    }}

    /* Suggestion cards */
    div.stButton > button {{
        background: {WHITE};
        color: {NAVY};
        border: 1px solid {BORDER};
        border-radius: 12px;
        min-height: 105px;
        padding: 0.85rem 1rem;
        text-align: left;
        white-space: pre-wrap;
        font-size: 0.91rem;
        line-height: 1.5;
        transition: border-color 0.15s ease;
    }}

    div.stButton > button:hover {{
        border-color: {BLUE};
        color: {NAVY};
    }}

    /* Chat area */
    div[data-testid="stChatMessage"] {{
        background: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 13px;
        padding: 1rem;
        margin-bottom: 0.75rem;
    }}

    div[data-testid="stChatInput"] {{
        border-color: {BORDER};
    }}

    .footer-note {{
        color: #718198;
        font-size: 0.77rem;
        text-align: center;
        margin-top: 2.5rem;
    }}

    @media (max-width: 700px) {{
        .block-container {{
            padding-top: 1rem;
        }}
        .topbar {{
            padding: 0.9rem;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Demo content (not connected to Dify yet)
# --------------------------------------------------
SUGGESTIONS = [
    (
        "01",
        "Revenue recognition",
        "Where can I find our revenue recognition rules?",
        "revenue",
    ),
    (
        "02",
        "Billing guidelines",
        "What do our internal billing guidelines cover?",
        "billing",
    ),
    (
        "03",
        "Procurement",
        "Where can I find our procurement guidelines?",
        "procurement",
    ),
    (
        "04",
        "Pricing guidelines",
        "What internal guidance is available on pricing?",
        "pricing",
    ),
]

DEMO_ANSWERS = {
    "revenue": (
        "This is a demonstration response. In the connected version, "
        "Fintel will search the internal Finance knowledge base for "
        "the relevant revenue recognition rules and supporting evidence."
    ),
    "billing": (
        "This is a demonstration response. The live assistant will "
        "retrieve the applicable billing guidelines and cite the "
        "relevant source passages."
    ),
    "procurement": (
        "This is a demonstration response. The live assistant will "
        "search the internal procurement guidelines before answering."
    ),
    "pricing": (
        "This is a demonstration response. The live assistant will "
        "retrieve the relevant internal pricing guidance."
    ),
}

SOURCE_NAMES = {
    "revenue": "Rules of Revenue Recognition",
    "billing": "Billing Guidelines",
    "procurement": "Procurement Guidelines",
    "pricing": "Pricing Guidelines",
}


def get_demo_response(question):
    q = question.lower()

    if "revenue" in q or "recognition" in q:
        key = "revenue"
    elif "bill" in q or "invoice" in q:
        key = "billing"
    elif "procure" in q or "purchas" in q or "supplier" in q:
        key = "procurement"
    elif "pric" in q or "margin" in q or "rate" in q:
        key = "pricing"
    else:
        return (
            "This is a demonstration of Fintel's response area. "
            "When connected to Dify, I will search the available "
            "Finance documents. If there is not enough evidence, "
            "I should say so rather than guess.",
            None,
        )

    return DEMO_ANSWERS[key], key


def ask_question(question):
    question = question.strip()
    if not question:
        return

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    answer, source_key = get_demo_response(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "source_key": source_key,
            "demo": True,
        }
    )


# --------------------------------------------------
# Session state
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation_count" not in st.session_state:
    st.session_state.conversation_count = 0

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:
    st.markdown(
        '<div class="sidebar-brand">Fintel</div>'
        '<div class="sidebar-subtitle">'
        'Internal Finance Knowledge Assistant'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    if st.button(
        "＋  New conversation",
        use_container_width=True,
        key="new_conversation",
    ):
        if st.session_state.messages:
            st.session_state.conversation_count += 1
        st.session_state.messages = []
        st.rerun()

    st.markdown(
        '<div class="sidebar-label">Workspace</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-note">'
        'Finance knowledge assistant<br>'
        'Policy and procedure guidance<br>'
        'Source-backed answers'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        '<div class="sidebar-label">Conversation history</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-note">'
        'Conversation history is not saved yet. '
        'Previous chats will not be available after a session ends.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown(
        '<div class="sidebar-label">About Fintel</div>'
        '<div class="sidebar-note">'
        'Find answers in internal Finance documents. '
        'The connected assistant will provide source references '
        'and indicate when evidence is insufficient.'
        '</div>',
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# Main header
# --------------------------------------------------
st.markdown(
    """
    <div class="topbar">
        <div>
            <div class="topbar-title">Finance knowledge workspace</div>
            <div class="topbar-subtitle">
                Your central place for internal Finance guidance
            </div>
        </div>
        <div class="status-pill">Prototype</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Welcome screen
# --------------------------------------------------
if not st.session_state.messages:
    st.markdown(
        '<div class="eyebrow">Finance knowledge assistant</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="welcome-title">How can I help you today?</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="welcome-copy">'
        'Ask a question about internal Finance policies, procedures '
        'or guidance. Fintel is designed to help you find the '
        'information you need, with references to its sources.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-heading">Explore a topic</div>'
        '<div class="section-description">'
        'Choose a common Finance topic to get started.'
        '</div>',
        unsafe_allow_html=True,
    )

    for start in (0, 2):
        columns = st.columns(2, gap="medium")

        for column, item in zip(
            columns, SUGGESTIONS[start:start + 2]
        ):
            number, title, question, key = item

            with column:
                if st.button(
                    f"{number}  |  {title}\n\n{question}",
                    key=f"suggestion_{key}",
                    use_container_width=True,
                ):
                    ask_question(question)
                    st.rerun()

    st.markdown(
        """
        <div class="footer-note">
            Answers should be checked against their source documents.
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# Conversation screen
# --------------------------------------------------
else:
    st.markdown(
        '<div class="section-heading">Your conversation</div>',
        unsafe_allow_html=True,
    )

    for message in st.session_state.messages:
        avatar = "U" if message["role"] == "user" else "F"

        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

            if message["role"] == "assistant":
                st.caption(
                    "Demo response · Not verified against Finance documents"
                )

                source_key = message.get("source_key")

                if source_key:
                    with st.expander("View example source reference"):
                        st.markdown(
                            f"**Document:** {SOURCE_NAMES[source_key]}"
                        )
                        st.caption(
                            "Example only. This source has not been "
                            "verified against your actual documents."
                        )

question = st.chat_input("Ask Fintel a Finance question...")

if question:
    ask_question(question)
    st.rerun()

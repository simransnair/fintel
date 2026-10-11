
import streamlit as st

st.set_page_config(
    page_title="Fintel | Finance Assistant",
    page_icon="💬",
    layout="centered",
)

NAVY = "#173B67"
BLUE = "#3478F6"
PALE_BLUE = "#F3F7FC"
BORDER = "#DCE6F2"
MUTED = "#53657A"

st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {PALE_BLUE}; }}
    .block-container {{
        max-width: 900px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }}
    .fintel-header {{
        background: {NAVY};
        padding: 1.25rem 1.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        color: white;
    }}
    .fintel-brand {{
        font-size: 1.8rem;
        font-weight: 750;
        margin: 0;
    }}
    .fintel-subtitle {{
        color: #DCE8F7;
        font-size: 0.92rem;
        margin-top: 0.25rem;
    }}
    .eyebrow {{
        color: {BLUE};
        font-weight: 700;
        font-size: 0.8rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    .welcome-title {{
        color: {NAVY};
        font-size: 2.25rem;
        font-weight: 750;
        margin: 0.25rem 0 0.5rem 0;
    }}
    .welcome-copy {{
        color: {MUTED};
        font-size: 1rem;
        margin-bottom: 1.4rem;
    }}
    div.stButton > button {{
        border: 1px solid {BORDER};
        background: white;
        color: {NAVY};
        border-radius: 12px;
        min-height: 90px;
        text-align: left;
        white-space: normal;
        padding: 0.8rem 1rem;
    }}
    div.stButton > button:hover {{
        border-color: {BLUE};
        color: {NAVY};
    }}
    div[data-testid="stChatMessage"] {{
        background: white;
        border: 1px solid {BORDER};
        border-radius: 14px;
        padding: 0.75rem;
    }}
    .footer-note {{
        color: {MUTED};
        font-size: 0.78rem;
        text-align: center;
        padding-top: 1rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Demo responses only. Dify will be connected later.
DEMO_ANSWERS = {
    "revenue": (
        "This is a demonstration response. In the live version, "
        "Fintel will search your internal revenue recognition documents "
        "and cite the relevant evidence."
    ),
    "billing": (
        "This is a demonstration response. The live version will retrieve "
        "your internal billing guidance and reference the relevant source."
    ),
    "procurement": (
        "This is a demonstration response. The live version will search "
        "your internal procurement guidelines before answering."
    ),
    "pricing": (
        "This is a demonstration response. The live version will search "
        "your internal pricing guidance before answering."
    ),
}

SUGGESTIONS = [
    ("📘", "Revenue recognition",
     "Where can I find our revenue recognition rules?", "revenue"),
    ("🧾", "Billing guidelines",
     "What do our internal billing guidelines cover?", "billing"),
    ("🛒", "Procurement",
     "Where can I find our procurement guidelines?", "procurement"),
    ("🧮", "Pricing guidelines",
     "What internal guidance is available on pricing?", "pricing"),
]


def get_response(question):
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
            "Once connected to Dify, I will search the available Finance "
            "documents. If there is not enough evidence, I should say so "
            "rather than guess."
        ), None

    return DEMO_ANSWERS[key], key


def ask_question(question):
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )
    answer, source_key = get_response(question)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "source_key": source_key,
            "demo": True,
        }
    )


if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown(
    """
    <div class="fintel-header">
        <div class="fintel-brand">💬 Fintel</div>
        <div class="fintel-subtitle">
            Internal Finance Knowledge Assistant
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if not st.session_state.messages:
    st.markdown(
        '<div class="eyebrow">Your Finance knowledge hub</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="welcome-title">How can I help you?</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="welcome-copy">'
        'Ask about internal Finance policies, procedures or guidance.'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown("**Explore a topic**")

    for start in (0, 2):
        columns = st.columns(2)
        for column, item in zip(
            columns, SUGGESTIONS[start:start + 2]
        ):
            emoji, title, question, key = item
            with column:
                if st.button(
                    f"{emoji}  {title}\n\n{question}",
                    key=f"suggestion_{key}",
                    use_container_width=True,
                ):
                    ask_question(question)
                    st.rerun()

else:
    if st.button("← Start a new conversation"):
        st.session_state.messages = []
        st.rerun()

    for message in st.session_state.messages:
        avatar = "🧑" if message["role"] == "user" else "💬"

        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

            if message["role"] == "assistant":
                st.caption(
                    "Demo response · Not verified against Finance documents"
                )

                source_key = message.get("source_key")
                if source_key:
                    source_names = {
                        "revenue": "Rules of Revenue Recognition",
                        "billing": "Billing Guidelines",
                        "procurement": "Procurement Guidelines",
                        "pricing": "Pricing Guidelines",
                    }
                    with st.expander("📄 Example source reference"):
                        st.markdown(
                            f"**Document:** {source_names[source_key]}"
                        )
                        st.caption(
                            "Example only. This source has not been "
                            "verified against your actual documents."
                        )

question = st.chat_input("Ask Fintel a Finance question...")

if question:
    ask_question(question)
    st.rerun()

st.markdown(
    '<div class="footer-note">'
    'Fintel · Prototype mode: responses are examples, '
    'not verified Finance answers'
    '</div>',
    unsafe_allow_html=True,
)

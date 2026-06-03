import time
import streamlit as st

from datetime import datetime
from chatbot import chatbot, detect_guided_flow
from guided_flow import (
    CONTEXT_RESPONSES,GUIDED_FLOWS
)
from eligibility_checker import (
    init_eligibility_state,
    start_eligibility_wizard,
    render_eligibility_wizard
)

init_eligibility_state()


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="PMAY-U 2.0 Assistant",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================================
# LOAD CSS
# ==========================================

def load_css():

    with open(
        "styles/style.css",
        encoding="utf-8"
    ) as f:

        st.markdown(
            f"""
            <style>
            {f.read()}
            </style>
            """,
            unsafe_allow_html=True
        )


load_css()

# ==========================================
# SESSION STATE
# ==========================================

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_suggestions" not in st.session_state:
    st.session_state.pending_suggestions = None

if "quick_query" not in st.session_state:
    st.session_state.quick_query = None

# NEW
if "pending_query" not in st.session_state:
    st.session_state.pending_query = None


if "guided_context" not in st.session_state:
    st.session_state.guided_context = None


# ==========================================
# QUICK QUERY SUPPORT
# ==========================================

user_query = None

if st.session_state.quick_query:

    # Hide welcome instantly
    st.session_state.chat_started = True

    user_query = (
        st.session_state.quick_query
    )

    st.session_state.quick_query = None

# ==========================================
# PMAY BANNER
# ==========================================

st.image(
    "assests/pmay_logo_2.png",
    use_container_width=True
)

# # ==========================================
# # SMALL CLEAR CHAT BUTTON
# # ==========================================

# top_col1, top_col2 = st.columns(
#     [10, 1]
# )

# with top_col2:

#     if st.button(
#         "🗑",
#         help="Clear Chat"
#     ):

        
#         st.session_state.messages = []

#         st.session_state.pending_suggestions = None

#         st.session_state.pending_query = None

#         st.session_state.quick_query = None

#         st.session_state.chat_started = False

#         st.rerun()

# ==========================================
# HOME BUTTON
# ==========================================

top_col1, top_col2 = st.columns([10, 1])



with top_col2:

    if st.button(
    "🏠 Home",
    use_container_width=True
):

        st.session_state.messages = []
        st.session_state.pending_suggestions = None
        st.session_state.pending_query = None
        st.session_state.quick_query = None
        st.session_state.guided_context = None

        st.session_state.chat_started = False

        st.rerun()


# ==========================================
# WELCOME SCREEN
# ==========================================

if not st.session_state.chat_started:

    st.markdown("""
    <div class="welcome-card">

    <h1>
    PMAY-U 2.0 Assistant
    </h1>

    <p>
    Ask me anything about
    PMAY-U 2.0, BLC, AHP, ARH,
    ISS, Eligibility,
    Subsidy, Documents
    and Application Process.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "### Popular Questions"
    )

    col1, col2, col3 = st.columns(3)

    examples = [

        "Documents",

        "Eligibility",

        "Apply",

        "No Income proof",

        "How to apply for PMAY?",

        "Who can apply for PMAY?"
    ]

    cols = [
        col1, col2, col3,
        col1, col2, col3
    ]

    for col, question in zip(
        cols,
        examples
    ):

        with col:

            if st.button(
                question,
                use_container_width=True
            ):
                st.session_state.chat_started = True
                st.session_state.quick_query = (
                    question
                )

                st.rerun()


# ==========================================
# ELIGIBILITY CHECKER
# ==========================================

if not st.session_state.chat_started:

    st.markdown("""
    <div class='eligibility-box'>
    <h4>🏠 Check Your PMAY-U 2.0 Eligibility</h4>
    Get a quick eligibility estimate in less than 1 minute.
    </div>
    """,
    unsafe_allow_html=True)

    if st.button(
        "🏠 Check Your Eligibility",
        use_container_width=True
    ):
        start_eligibility_wizard()

# Show wizard only when active
if st.session_state.eligibility_wizard["active"]:

    render_eligibility_wizard()


# ==========================================
# GUIDED FLOW BUTTONS
# ==========================================

def render_guided_flow():

    if (
        st.session_state
        .guided_context
        is None
    ):
        return

    context = (
        st.session_state
        .guided_context
    )

    for label, key in (
        context.items()
    ):

        if st.button(
            label,
            key=f"guided_{key}",
            use_container_width=True
        ):

            response = (
                CONTEXT_RESPONSES[key]
            )

            # ---------------------------------
            # REMOVE LAST ASSISTANT
            # CLARIFICATION MESSAGE
            # ---------------------------------

            if (
                st.session_state.messages
            ):

                last_message = (
                    st.session_state
                    .messages[-1]
                )

                if (
                    last_message["role"]
                    == "assistant"
                ):

                    st.session_state.messages.pop()

            # ---------------------------------
            # SINGLE CLEAN RESPONSE
            # ---------------------------------

            final_response = (
                f"**You selected:** "
                f"{label}\n\n"
                f"{response}"
            )

            st.session_state.messages.append({

                "role":
                    "assistant",

                "content":
                    final_response,

                "time":
                    datetime.now()
                    .strftime(
                        "%I:%M %p"
                    )
            })

            # ---------------------------------
            # CLEAR GUIDED FLOW
            # ---------------------------------

            st.session_state.guided_context = None

            st.rerun()

# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    # USER MESSAGE
    if message["role"] == "user":

        cols = st.columns([9, 1])

        with cols[0]:

            st.markdown(
                f"""
                <div class="user-message">

                {message['content']}

                <div class="timestamp">
                    {message.get('time','')}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with cols[1]:

            st.markdown(
                """
                <div class="avatar user-avatar">
                    👤
                </div>
                """,
                unsafe_allow_html=True
            )

    # BOT MESSAGE
    else:

        cols = st.columns([1, 9])

        with cols[0]:

            st.markdown(
                """
                <div class="avatar bot-avatar">
                    🤖
                </div>
                """,
                unsafe_allow_html=True
            )

        with cols[1]:

            # Convert newlines safely
            bot_content = (
                message["content"]
                .replace("\n", "<br>")
            )

            st.markdown(
                f"""
                <div class="bot-message">

                {bot_content}

                <div class="timestamp">
                    {message.get('time','')}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ==========================================
# CLICKABLE ANSWER SUGGESTIONS
# ==========================================

def render_suggestions():

    suggestions = (
        st.session_state
        .pending_suggestions
    )

    if not suggestions:
        return

    st.markdown("""
    <div class="suggestion-box">

    <b>
    "Please select the answer you mean."
    </b>

    <br><br>

    Select the answer you mean
    or type 1 / 2

    </div>
    """, unsafe_allow_html=True)

    for idx, item in enumerate(
        suggestions,
        start=1
    ):

        preview = item[
            "preview"
        ]

        button_text = (
            f"{idx}. {preview}"
        )

        if st.button(
            button_text,
            key=f"option_{idx}",
            use_container_width=True
        ):

            answer = item[
                "answer"
            ]

            # ==================================
            # CHECK IF ANSWER MATCHES
            # GUIDED FLOW MESSAGE
            # ==================================

            guided_result = detect_guided_flow(
                answer
            )

            if guided_result["found"]:

                from guided_flow import (
                    GUIDED_FLOWS
                )

                flow_key = (
                    guided_result[
                        "flow_key"
                    ]
                )

                flow = (
                    GUIDED_FLOWS[
                        flow_key
                    ]
                )

                st.session_state.guided_context = (
                    flow["options"]
                )

                st.session_state.messages.append({

                    "role":
                        "assistant",

                    "content":
                        flow["message"],

                    "time":
                        datetime.now()
                        .strftime(
                            "%I:%M %p"
                        )
                })

            else:

                st.session_state.messages.append({

                    "role":
                        "assistant",

                    "content":
                        answer,

                    "time":
                        datetime.now()
                        .strftime(
                            "%I:%M %p"
                        )
                })

            st.session_state.pending_suggestions = None
            st.session_state.pending_query = None
            st.rerun()

render_suggestions()
render_guided_flow()

# ==========================================
# CHAT INPUT
# ==========================================

typed_query = st.chat_input(
    "Ask your PMAY question..."
)

if typed_query:
    user_query = typed_query

# # ==========================================
# # QUICK QUERY SUPPORT
# # ==========================================

# if (
#     st.session_state.quick_query
# ):

#     user_query = (
#         st.session_state
#         .quick_query
#     )

#     st.session_state.quick_query = None


# ==========================================
# HANDLE QUERY
# ==========================================

if user_query:

    st.session_state.chat_started = True
    if "eligibility_wizard" in st.session_state:

        st.session_state.eligibility_wizard["active"] = False

    # --------------------------------------
    # MANUAL OPTION SELECTION
    # --------------------------------------

    if st.session_state.pending_suggestions:

        if user_query in ["1", "2"]:

            selected_idx = (
                int(user_query) - 1
            )

            suggestions = (
                st.session_state
                .pending_suggestions
            )

            answer = (
                suggestions[
                    selected_idx
                ]["answer"]
            )

            # Save typed selection
            st.session_state.messages.append({

                "role":
                    "user",

                "content":
                    user_query,

                "time":
                    datetime.now()
                    .strftime(
                        "%I:%M %p"
                    )
            })

            # ==================================
            # CHECK GUIDED FLOW MATCH
            # ==================================

            guided_result = (
                detect_guided_flow(
                    answer
                )
            )

            # ==================================
            # GUIDED FLOW FOUND
            # ==================================

            if guided_result["found"]:

                flow_key = (
                    guided_result[
                        "flow_key"
                    ]
                )

                flow = (
                    GUIDED_FLOWS[
                        flow_key
                    ]
                )

                st.session_state.guided_context = (
                    flow["options"]
                )

                st.session_state.messages.append({

                    "role":
                        "assistant",

                    "content":
                        flow["message"],

                    "time":
                        datetime.now()
                        .strftime(
                            "%I:%M %p"
                        )
                })

            # ==================================
            # NORMAL ANSWER
            # ==================================

            else:

                st.session_state.messages.append({

                    "role":
                        "assistant",

                    "content":
                        answer,

                    "time":
                        datetime.now()
                        .strftime(
                            "%I:%M %p"
                        )
                })

            # ----------------------------------
            # CLEAR STATES
            # ----------------------------------

            st.session_state.pending_suggestions = None
            st.session_state.pending_query = None

            st.rerun()

        else:

            # User typed a NEW query
            # instead of selecting 1/2

            st.session_state.pending_suggestions = None

    # --------------------------------------
    # NORMAL QUERY
    # --------------------------------------

    st.session_state.messages.append({

        "role":
            "user",

        "content":
            user_query,

        "time":
            datetime.now()
            .strftime(
                "%I:%M %p"
            )
    })

    st.session_state.pending_query = (
        user_query
    )

    st.rerun()

# ==========================================
# PROCESS PENDING QUERY
# ==========================================

if st.session_state.pending_query:

    user_query = (
        st.session_state
        .pending_query
    )

    # Reset pending query
    st.session_state.pending_query = None

    # --------------------------------------
    # TYPING ANIMATION
    # --------------------------------------

    typing_placeholder = st.empty()

    typing_placeholder.markdown("""
    <div class="typing">
    <span></span>
    <span></span>
    <span></span>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.8)

    # --------------------------------------
    # CHATBOT RESPONSE
    # --------------------------------------

    result = chatbot(
        user_query
    )

    typing_placeholder.empty()

    # ======================================
    # DIRECT ANSWER / GREETING / UNKNOWN
    # ======================================

    if result["type"] in [

        "direct_answer",
        "greeting",
        "unknown"

    ]:

        st.session_state.messages.append({

            "role":
                "assistant",

            "content":
                result["response"],

            "time":
                datetime.now()
                .strftime(
                    "%I:%M %p"
                )
        })

    # ======================================
    # TOP-2 ANSWER SUGGESTIONS
    # ======================================

    elif (
        result["type"]
        == "suggestions"
    ):

        st.session_state.pending_suggestions = (
            result["suggestions"]
        )

    # ======================================
    # GUIDED FLOW
    # ======================================

    elif (
        result["type"]
        == "guided_flow"
    ):

        # Only store buttons
        # No extra bot message
        st.session_state.guided_context = (
            result["options"]
        )

        # Show assistant question
        st.session_state.messages.append({

            "role":
                "assistant",

            "content":
                result["response"],

            "time":
                datetime.now()
                .strftime(
                    "%I:%M %p"
                )
        })

    # --------------------------------------
    # REFRESH UI
    # --------------------------------------

    st.rerun()
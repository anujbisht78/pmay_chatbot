import time
import streamlit as st

from datetime import datetime
from chatbot import chatbot
from guided_flow import (
    CONTEXT_RESPONSES
)



# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="PMAY Assistant",
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
    "assests\pmay_logo_2.png",
    use_container_width=True
)

# ==========================================
# SMALL CLEAR CHAT BUTTON
# ==========================================

top_col1, top_col2 = st.columns(
    [10, 1]
)

with top_col2:

    if st.button(
        "🗑",
        help="Clear Chat"
    ):

        
        st.session_state.messages = []

        st.session_state.pending_suggestions = None

        st.session_state.pending_query = None

        st.session_state.quick_query = None

        st.session_state.chat_started = False

        st.rerun()


# ==========================================
# WELCOME SCREEN
# ==========================================

if not st.session_state.chat_started:

    st.markdown("""
    <div class="welcome-card">

    <h1>
    PMAY Assistant
    </h1>

    <p>
    Ask me anything about
    PMAY, BLC, AHP, ARH,
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

        "What is BLC?",

        "Eligibility for PMAY",

        "Documents Required for ISS",

        "What is AHP?",

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

            # Add assistant response
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

    # --------------------------------------
    # MANUAL OPTION SELECTION
    # --------------------------------------
    st.session_state.chat_started = True

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

            # Save answer
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

            st.rerun()

        else:
            # user typed new query
            st.session_state.pending_suggestions = None

    # --------------------------------------
    # SAVE USER MESSAGE
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

    # Save query for processing
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



# CHATBOT RESPONSE
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# from utils import greet_response
from guided_flow import (
    GUIDED_FLOWS
)

from model_loader import (
    model,
    questions,
    answers,
    question_embeddings
)

#greet function
def greet_response(query):

    query = query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "helo",
        "hy",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    how_are_you = [
        "how are you",
        "how are you?",
        "how r u",
        "how are u",
        "kaise ho"
    ]

    thanks = [
        "thanks",
        "thank you",
        "thx"
    ]

    if query in greetings:

        return (
            "Hello! 👋\n\n"
            "I am your PMAY Assistant.\n\n"
            "I can help you with:\n"
            "• BLC\n"
            "• AHP\n"
            "• ARH\n"
            "• ISS\n"
            "• Eligibility\n"
            "• Documents Required\n"
            "• Subsidy\n"
            "• Application Process"
        )

    elif query in how_are_you:

        return (
            "I'm doing great 😊\n\n"
            "How can I help you "
            "regarding PMAY?"
        )

    elif query in thanks:

        return (
            "You're welcome 😊"
        )

    return None



# CONFIG
HIGH_THRESHOLD = 0.90
MID_THRESHOLD = 0.70
# LOW_THRESHOLD = 0.70


# CHATBOT FUNCTION

def chatbot(user_query):

    # ---------------------------------
    # Greeting Check
    # ---------------------------------

    greet = greet_response(
        user_query
    )

    if greet:

        return {
            "type": "greeting",
            "response": greet
        }

    user_query = (
        user_query
        .lower()
        .strip()
    )

    # ---------------------------------
    # Query Embedding
    # ---------------------------------

    query_embedding = model.encode(
        [user_query],
        convert_to_numpy=True
    )

    # ---------------------------------
    # Similarity
    # ---------------------------------

    similarities = cosine_similarity(
        query_embedding,
        question_embeddings
    )[0]

    # Top 3 indices
    top_3_idx = np.argsort(
        similarities
    )[-3:][::-1]

    best_index = top_3_idx[0]

    best_score = similarities[
        best_index
    ]

    print(
        f"Best Score: "
        f"{best_score:.2f}"
    )

    print(
        "Matched Question:",
        questions[best_index]
    )

    # CASE 1:
    # HIGH CONFIDENCE

    if best_score >= HIGH_THRESHOLD:

        matched_query = (
            questions[
                best_index
            ]
            .lower()
            .strip()
        )

        # ==================================
        # GUIDED FLOW
        # ==================================

        if matched_query in GUIDED_FLOWS:

            flow = (
                GUIDED_FLOWS[
                    matched_query
                ]
            )

            return {

                "type":
                    "guided_flow",

                "response":
                    flow["message"],

                "options":
                    flow["options"]
            }

        # ==================================
        # NORMAL ANSWER
        # ==================================

        return {
            "type":
                "direct_answer",

            "response":
                answers[
                    best_index
                ]
        }

# CASE 2:
# TOP 2 ANSWERS
# =====================================

    elif (
        MID_THRESHOLD
        <= best_score
        < HIGH_THRESHOLD
    ):

        suggestions = []

        # Top 2 only
        for idx in top_3_idx[:2]:

            answer_preview = (
                answers[idx][:180]
                + "..."
                if len(
                    answers[idx]
                ) > 180
                else answers[idx]
            )

            suggestions.append({

                "question":
                    questions[idx],

                "answer":
                    answers[idx],

                "preview":
                    answer_preview,

                "score":
                    round(
                        similarities[idx],
                        2
                    )
            })

        return {

            "type":
                "suggestions",

            "response":
                (
                    "I found similar answers."
                ),

            "suggestions":
                suggestions
        }

        suggestions = []

        for idx in top_3_idx:

            suggestions.append({
                "question":
                    questions[idx],

                "answer":
                    answers[idx],

                "score":
                    round(
                        similarities[idx],
                        2
                    )
            })

        return {
            "type":
                "suggestions",

            "response":
                "Did you mean "
                "one of these?",

            "suggestions":
                suggestions
        }

    # CASE 3:
    # UNKNOWN QUERY

    else:

        return {
            "type":
                "unknown",

            "response":
                (
                    "Sorry, I don't "
                    "know about this.\n\n"
                    "You can ask me about:\n"
                    "• BLC\n"
                    "• AHP\n"
                    "• ARH\n"
                    "• ISS\n"
                    "• Eligibility\n"
                    "• Steps to Apply\n"
                    "• Documents Required"
                )
        }
    


    # APP.py

    import time
import streamlit as st

from datetime import datetime
from chatbot import chatbot, detect_guided_flow
from guided_flow import (
    CONTEXT_RESPONSES,GUIDED_FLOWS
)



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



    # CHATBOT.py

    import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# from utils import greet_response
from guided_flow import (
    GUIDED_FLOWS
)

from model_loader import (
    model,
    questions,
    answers,
    question_embeddings
)

# ==================================
# GUIDED FLOW EMBEDDINGS
# ==================================

guided_messages = []
guided_keys = []

for flow_key, flow_data in GUIDED_FLOWS.items():

    guided_messages.append(
        flow_data["message"].lower()
    )

    guided_keys.append(
        flow_key
    )

guided_embeddings = model.encode(
    guided_messages,
    convert_to_numpy=True
)


#greet function
def greet_response(query):

    query = query.lower().strip()

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "helo",
        "hy",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    how_are_you = [
        "how are you",
        "how are you?",
        "how r u",
        "how are u",
        "kaise ho"
    ]

    thanks = [
        "thanks",
        "thank you",
        "thx"
    ]

    if query in greetings:

        return (
            "Hello! 👋\n\n"
            "I am your PMAY Assistant.\n\n"
            "I can help you with:\n"
            "• BLC\n"
            "• AHP\n"
            "• ARH\n"
            "• ISS\n"
            "• Eligibility\n"
            "• Documents Required\n"
            "• Subsidy\n"
            "• Application Process"
        )

    elif query in how_are_you:

        return (
            "I'm doing great 😊\n\n"
            "How can I help you "
            "regarding PMAY?"
        )

    elif query in thanks:

        return (
            "You're welcome 😊"
        )

    return None

# CONFIG
HIGH_THRESHOLD = 0.90
MID_THRESHOLD = 0.70
# LOW_THRESHOLD = 0.70

# ==================================
# DETECT GUIDED FLOW
# ==================================

def detect_guided_flow(answer_text):

    answer_embedding = model.encode(
        [answer_text.lower()],
        convert_to_numpy=True
    )

    similarities = cosine_similarity(
        answer_embedding,
        guided_embeddings
    )[0]

    best_idx = np.argmax(
        similarities
    )

    best_score = similarities[
        best_idx
    ]

    print(
        f"Guided Flow Score: "
        f"{best_score:.2f}"
    )

    if best_score >= 0.95:

        return {

            "found": True,

            "flow_key":
                guided_keys[
                    best_idx
                ],

            "score":
                best_score
        }

    return {
        "found": False
    }


# CHATBOT FUNCTION

def chatbot(user_query):

    # ---------------------------------
    # Greeting Check
    # ---------------------------------

    greet = greet_response(
        user_query
    )

    if greet:

        return {
            "type": "greeting",
            "response": greet
        }

    user_query = (
        user_query
        .lower()
        .strip()
    )

    # ---------------------------------
    # Query Embedding
    # ---------------------------------

    query_embedding = model.encode(
        [user_query],
        convert_to_numpy=True
    )

    # ---------------------------------
    # Similarity
    # ---------------------------------

    similarities = cosine_similarity(
        query_embedding,
        question_embeddings
    )[0]

    # Top 3 indices
    top_3_idx = np.argsort(
        similarities
    )[-3:][::-1]

    best_index = top_3_idx[0]

    best_score = similarities[
        best_index
    ]

    print(
        f"Best Score: "
        f"{best_score:.2f}"
    )

    print(
        "Matched Question:",
        questions[best_index]
    )

    # CASE 1:
    # HIGH CONFIDENCE

    if best_score >= HIGH_THRESHOLD:

        matched_query = (
            questions[
                best_index
            ]
            .lower()
            .strip()
        )

        # ==================================
        # GUIDED FLOW
        # ==================================

        if matched_query in GUIDED_FLOWS:

            flow = (
                GUIDED_FLOWS[
                    matched_query
                ]
            )

            return {

                "type":
                    "guided_flow",

                "response":
                    flow["message"],

                "options":
                    flow["options"]
            }

        # ==================================
        # NORMAL ANSWER
        # ==================================

        return {
            "type":
                "direct_answer",

            "response":
                answers[
                    best_index
                ]
        }

# CASE 2:
# TOP 2 ANSWERS
# =====================================

    elif (
        MID_THRESHOLD
        <= best_score
        < HIGH_THRESHOLD
    ):

        suggestions = []

        # Top 2 only
        for idx in top_3_idx[:2]:

            answer_preview = (
                answers[idx][:180]
                + "..."
                if len(
                    answers[idx]
                ) > 180
                else answers[idx]
            )

            suggestions.append({

                "question":
                    questions[idx],

                "answer":
                    answers[idx],

                "preview":
                    answer_preview,

                "score":
                    round(
                        similarities[idx],
                        2
                    )
            })

        return {

            "type":
                "suggestions",

            "response":
                (
                    "I found similar answers."
                ),

            "suggestions":
                suggestions
        }

        suggestions = []

        for idx in top_3_idx:

            suggestions.append({
                "question":
                    questions[idx],

                "answer":
                    answers[idx],

                "score":
                    round(
                        similarities[idx],
                        2
                    )
            })

        return {
            "type":
                "suggestions",

            "response":
                "Did you mean "
                "one of these?",

            "suggestions":
                suggestions
        }

    # CASE 3:
    # UNKNOWN QUERY

    else:

        return {
            "type":
                "unknown",

            "response":
                (
                    "Sorry, I don't "
                    "know about this.\n\n"
                    "You can ask me about:\n"
                    "• BLC\n"
                    "• AHP\n"
                    "• ARH\n"
                    "• ISS\n"
                    "• Eligibility\n"
                    "• Steps to Apply\n"
                    "• Documents Required"
                )
        }
    

    # ELIGIBILITY CHECKER
    def calculate_eligibility():

    data = st.session_state.eligibility_wizard

    income = data["income"]
    house = data["house"]
    previous_benefit = data["previous_benefit"]
    need = data["housing_need"]
    urban = data["urban"]
  


    # --------------------------------------
    # PREVIOUS BENEFIT CHECK
    # --------------------------------------

    if previous_benefit == "yes":

        return {

            "category":
                "Further Review Required",

            "vertical":
                "Benefit Verification",

            "message":
                (
                    "Based on the information provided, "
                    "you indicated that housing-related benefits "
                    "may have been received under a Central or "
                    "State Government housing scheme during the "
                    "last 20 years.\n\n"

                    "Previous housing assistance may affect "
                    "eligibility under PMAY-U 2.0 depending on "
                    "the nature of the benefit received and "
                    "applicable scheme conditions.\n\n"

                    "A detailed review of the earlier benefit "
                    "would be required before estimating "
                    "possible eligibility.\n\n"

                    "Final eligibility depends on authority "
                    "verification and scheme guidelines."
                )
        }

    # --------------------------------------
    # OWN HOUSE
    # --------------------------------------

    if house == "yes":

        return {
            "category": "Ownership Review Required",

            "vertical": "Further Verification",

            "message":
                (
                    "Based on the information provided, "
                    "house ownership conditions may affect "
                    "PMAY-U 2.0 eligibility.\n\n"

                    "Ownership of a pucca house by any "
                    "beneficiary-family member may impact "
                    "scheme eligibility.\n\n"

                    "A detailed review of ownership, "
                    "family status and housing conditions "
                    "would be required.\n\n"

                    "Final eligibility depends on "
                    "authority verification."
                )
        }

    # --------------------------------------
    # EWS
    # --------------------------------------

    if income == "ews":

        vertical = "BLC"

        if need == "rent":
            vertical = "ARH"

        return {

            "category": "EWS",

            "vertical": vertical,

            "message":
                (
                    "Based on the information provided, "
                    "you may fall under the Economically "
                    "Weaker Section (EWS) category.\n\n"

                    "Your responses suggest that PMAY-U 2.0 "
                    "housing assistance may be relevant "
                    "for your situation.\n\n"

                    f"Possible PMAY-U 2.0 Area: {vertical}\n\n"

                    "Final eligibility depends on "
                    "income verification, ownership "
                    "conditions and authority approval."
                )
        }

    # --------------------------------------
    # LIG
    # --------------------------------------

    if income == "lig":

        vertical = "AHP"

        if need == "loan":
            vertical = "ISS"

        return {

            "category": "LIG",

            "vertical": vertical,

            "message":
                (
                    "Based on the information provided, "
                    "you may fall under the Low Income "
                    "Group (LIG) category.\n\n"

                    "Your responses indicate that PMAY-U 2.0 "
                    "housing support options may be relevant.\n\n"

                    f"Possible PMAY-U 2.0 Area: {vertical}\n\n"

                    "Final eligibility depends on "
                    "verification and scheme conditions."
                )
        }

    # --------------------------------------
    # MIG
    # --------------------------------------

    if income == "mig":

        return {

            "category": "MIG",

            "vertical": "ISS",

            "message":
                (
                    "Based on the information provided, "
                    "you may fall under the Middle Income "
                    "Group (MIG) category.\n\n"

                    "Certain PMAY-U 2.0 housing support "
                    "options may be relevant.\n\n"

                    "Possible PMAY-U 2.0 Area: ISS\n\n"

                    "Final eligibility depends on "
                    "verification and applicable conditions."
                )
        }

    return {

        "category": "Unknown",

        "vertical": "Review Required",

        "message":
            (
                "There is not enough information to "
                "estimate possible eligibility.\n\n"

                "Please provide more details regarding "
                "income, ownership and housing need."
            )
    }



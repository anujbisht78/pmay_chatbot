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
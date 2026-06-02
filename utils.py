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
            "Hello! 👋\n"
            "I am your PMAY Assistant."
            "I can help you with:"
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
            "I'm doing great 😊"
            "How can I help you "
            "regarding PMAY?"
        )

    elif query in thanks:

        return (
            "You're welcome 😊"
        )

    return None
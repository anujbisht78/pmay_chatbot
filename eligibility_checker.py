import streamlit as st


# ==========================================
# INITIALIZE
# ==========================================

def init_eligibility_state():

    if "eligibility_wizard" not in st.session_state:

        st.session_state.eligibility_wizard = {

            "active": False,

            "step": 0,

            "income": None,

            "house": None,

            "previous_benefit": None,

            "housing_need": None,

            "urban": None,

            "result": None
        }


# ==========================================
# START WIZARD
# ==========================================

def start_eligibility_wizard():

    st.session_state.eligibility_wizard = {

        "active": True,

        "step": 1,

        "income": None,

        "house": None,

        "previous_benefit": None,

        "housing_need": None,

        "urban": None,

        "result": None
    }


# ==========================================
# RESET
# ==========================================

def reset_eligibility_wizard():

    st.session_state.eligibility_wizard = {

        "active": False,

        "step": 0,

        "income": None,

        "house": None,

        "previous_benefit": None,

        "housing_need": None,

        "urban": None,

        "result": None
    }


# ==========================================
# ELIGIBILITY LOGIC
# ==========================================

def calculate_eligibility():

    data = st.session_state.eligibility_wizard

    income = data["income"]
    house = data["house"]
    previous_benefit = data["previous_benefit"]
    need = data["housing_need"]
    urban = data["urban"]

    reasoning = []
    concerns = []

    confidence = "High"

    # =====================================
    # CONFIDENCE
    # =====================================

    if income == "unknown":
        confidence = "Low"

    elif urban == "no":
        confidence = "Medium"

    # =====================================
    # INCOME UNKNOWN
    # =====================================

    if income == "unknown":

        return {

            "category":
                "Unable to Assess",

            "vertical":
                "Income Clarification Required",

            "confidence":
                "Low",

            "reasoning": [

                "Income information was not provided."
            ],

            "concerns": [

                "Income category is required for PMAY-U 2.0 assessment."
            ],

            "message":
                (
                    "A preliminary PMAY-U 2.0 eligibility assessment "
                    "cannot be completed without knowing the approximate "
                    "annual household income.\n\n"

                    "You may wish to check salary records, income certificates, "
                    "family income details or other supporting information "
                    "before using the eligibility checker again.\n\n"

                    "Once the income category is known, a more reliable "
                    "assessment can be generated."
                )
        }
    
    # =====================================
    # ABOVE 9 LAKH
    # =====================================

    if income == "above_mig":

        return {

            "category":
                "Not Eligible",

            "vertical":
                "Income Exceeds Assessment Range",

            "confidence":
                "Low",

            "reasoning": [

                "Annual household income reported above ₹9 lakh."
            ],

            "concerns": [

                "Income exceeds the eligibility assessment range used by this checker."
            ],

            "message":
                (
                    "Based on the information provided, your annual household "
                    "income appears to be above ₹9 lakh.\n\n"

                    "Under the assumptions used by this PMAY-U 2.0 eligibility "
                    "checker, applicants above this income range are unlikely "
                    "to qualify through the assessed income categories.\n\n"

                    "Therefore, you are currently assessed as Not Eligible "
                    "through this eligibility pathway.\n\n"

                    "Final determination always depends on applicable "
                    "government guidelines and authority verification."
                )
        }

    # =====================================
    # PREVIOUS BENEFIT REVIEW
    # =====================================

    if previous_benefit == "yes":

        return {

            "category":
                "Not Eligible",

            "vertical":
                "Previous Housing Benefit",

            "confidence":
                "Low",

            "reasoning": [

                "Previous government housing benefit reported."
            ],

            "concerns": [

                "Previous housing assistance may affect PMAY-U 2.0 eligibility."
            ],

            "message":
                (
                    "You indicated that you or a beneficiary-family member "
                    "may have received housing assistance under a Central or "
                    "State Government housing scheme during the last 20 years.\n\n"

                    "Previous housing benefits are an important PMAY-U 2.0 "
                    "screening condition.\n\n"

                    "Based on the information provided, the application "
                    "is currently assessed as Not Eligible through this pathway.\n\n"

                    "Final determination depends on verification of the "
                    "previous benefit and applicable scheme guidelines."
                )
        }

    # =====================================
    # HOUSE OWNERSHIP REVIEW
    # =====================================

    if house == "yes":

        return {

            "category":
                "Not Eligible",

            "vertical":
                "Pucca House Ownership",

            "confidence":
                "Low",

            "reasoning": [

                "Pucca house ownership reported."
            ],

            "concerns": [

                "House ownership may conflict with PMAY-U 2.0 eligibility conditions."
            ],

            "message":
                (
                    "You indicated that a beneficiary-family member "
                    "owns a pucca house.\n\n"

                    "House ownership is one of the most important "
                    "PMAY-U 2.0 eligibility conditions.\n\n"

                    "Based on the information provided, the application "
                    "is currently assessed as Not Eligible through this pathway.\n\n"

                    "If ownership details are unclear or disputed, "
                    "further verification may still be required."
                )
        }

    # =====================================
    # CATEGORY
    # =====================================

    category = "Unknown"

    if income == "ews":

        category = "EWS"

        reasoning.append(
            "Income appears consistent with EWS category."
        )

    elif income == "lig":

        category = "LIG"

        reasoning.append(
            "Income appears consistent with LIG category."
        )

    elif income == "mig":

        category = "MIG"

        reasoning.append(
            "Income appears consistent with MIG category."
        )

    else:

        concerns.append(
            "Income category could not be determined."
        )

    # =====================================
    # SCHEME MAPPING
    # =====================================

    vertical = "Review Required"

    if need == "construction":

        reasoning.append(
            "Construction-related housing need identified."
        )

        if category == "EWS":

            vertical = "BLC"

        elif category == "LIG":

            vertical = "BLC / Review"

            concerns.append(
                "Construction support may require additional scheme review."
            )

        elif category == "MIG":

            vertical = "Review Required"

            concerns.append(
                "Construction requirement identified but MIG applicants may require detailed scheme review."
            )

    elif need == "purchase":

        reasoning.append(
            "Affordable housing purchase requirement identified."
        )

        if category in ["EWS", "LIG"]:

            vertical = "AHP"

        elif category == "MIG":

            vertical = "ISS"

    elif need == "rent":

        reasoning.append(
            "Rental housing requirement identified."
        )

        vertical = "ARH"

    elif need == "loan":

        reasoning.append(
            "Housing loan support requirement identified."
        )

        vertical = "ISS"

    # =====================================
    # URBAN CHECK
    # =====================================

    if urban == "yes":

        reasoning.append(
            "Urban housing requirement reported."
        )

    else:

        concerns.append(
            "Urban area requirement may require verification."
        )

    # =====================================
    # GENERAL REASONING
    # =====================================

    reasoning.append(
        "No pucca house reported."
    )

    reasoning.append(
        "No previous housing benefit reported."
    )

    # =====================================
    # SCHEME EXPLANATION
    # =====================================

    scheme_explanation = ""

    if vertical == "BLC":

        scheme_explanation = (
            "BLC may be relevant because your primary housing need "
            "involves construction or enhancement of a house."
        )

    elif vertical == "AHP":

        scheme_explanation = (
            "AHP may be relevant because your primary need involves "
            "obtaining an affordable housing unit."
        )

    elif vertical == "ARH":

        scheme_explanation = (
            "ARH may be relevant because your primary need involves "
            "affordable rental accommodation."
        )

    elif vertical == "ISS":

        scheme_explanation = (
            "ISS may be relevant because your primary need involves "
            "housing loan-related support."
        )

    else:

        scheme_explanation = (
            "A detailed PMAY-U 2.0 review may be required to identify "
            "the most suitable housing support pathway."
        )

    # =====================================
    # FINAL MESSAGE
    # =====================================

    message = (
        f"Based on the information provided, you may fall under the "
        f"{category} category.\n\n"

        f"Suggested PMAY-U 2.0 Vertical: {vertical}\n\n"

        f"{scheme_explanation}\n\n"

        "This assessment is preliminary and based only on the "
        "information provided through the eligibility wizard.\n\n"

        "Final eligibility depends on income verification, "
        "ownership conditions, beneficiary-family rules, "
        "scheme requirements and authority approval."
    )

    return {

        "category":
            category,

        "vertical":
            vertical,

        "confidence":
            confidence,

        "reasoning":
            reasoning,

        "concerns":
            concerns,

        "message":
            message
    }


# ==========================================
# RENDER WIZARD
# ==========================================

def render_eligibility_wizard():

    wizard = st.session_state.eligibility_wizard

    if not wizard["active"]:
        return

    st.markdown("---")

    st.markdown(
        """
        ## 🏠 PMAY-U 2.0 Eligibility Checker

        Answer a few simple questions to get
        a preliminary eligibility estimate.
        """
    )

    # =====================================
    # STEP 1
    # =====================================

    if wizard["step"] == 1:

        st.info(
            "What is your approximate annual family income?"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button("Up to ₹3 Lakh"):

                wizard["income"] = "ews"
                wizard["step"] = 2
                st.rerun()

            if st.button("₹3–6 Lakh"):

                wizard["income"] = "lig"
                wizard["step"] = 2
                st.rerun()

        with col2:

            if st.button("₹6–9 Lakh"):

                wizard["income"] = "mig"
                wizard["step"] = 2
                st.rerun()

            if st.button("Above ₹9 Lakh"):

                wizard["income"] = "above_mig"
                wizard["step"] = 2
                st.rerun()

        with col3:

            if st.button("Not Sure"):

                wizard["income"] = "unknown"
                wizard["step"] = 2
                st.rerun()

    # =====================================
    # STEP 2
    # =====================================

    elif wizard["step"] == 2:

        st.info(
            "Does any beneficiary-family member own a pucca house anywhere in India?"
        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button("Yes"):

                wizard["house"] = "yes"
                wizard["step"] = 3
                st.rerun()

        with c2:

            if st.button("No"):

                wizard["house"] = "no"
                wizard["step"] = 3
                st.rerun()

    # =====================================
    # STEP 3
    # =====================================

    elif wizard["step"] == 3:

        st.info(
            "Have you availed benefits under any Central or State Government Housing Scheme during the last 20 years?"
        )

        st.markdown(
            """
            Examples may include housing assistance,
            subsidy support, government housing units,
            or other housing-related benefits.
            """
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            if st.button("Yes"):

                wizard["previous_benefit"] = "yes"

                wizard["step"] = 4

                st.rerun()

        with c2:

            if st.button("No"):

                wizard["previous_benefit"] = "no"

                wizard["step"] = 4

                st.rerun()

        with c3:

            if st.button("Not Sure"):

                wizard["previous_benefit"] = "unknown"

                wizard["step"] = 4

                st.rerun()

    # =====================================
    # STEP 4
    # =====================================

    elif wizard["step"] == 4:

        st.info(
            "Which option best describes your housing need?"
        )

        if st.button("Need House Construction"):

            wizard["housing_need"] = "construction"
            wizard["step"] = 5
            st.rerun()

        if st.button("Need Affordable House"):

            wizard["housing_need"] = "purchase"
            wizard["step"] = 5
            st.rerun()

        if st.button("Need Rental Housing"):

            wizard["housing_need"] = "rent"
            wizard["step"] = 5
            st.rerun()

        if st.button("Need Loan Support"):

            wizard["housing_need"] = "loan"
            wizard["step"] = 5
            st.rerun()

    # =====================================
    # STEP 5
    # =====================================

    elif wizard["step"] == 5:

        st.info(
            "Is your housing requirement in an urban area?"
        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button("Yes Urban"):

                wizard["urban"] = "yes"

                wizard["result"] = (
                    calculate_eligibility()
                )

                wizard["step"] = 6

                st.rerun()

        with c2:

            if st.button("No / Not Sure"):

                wizard["urban"] = "no"

                wizard["result"] = (
                    calculate_eligibility()
                )

                wizard["step"] = 6

                st.rerun()

    # =====================================
    # RESULT
    # =====================================

    elif wizard["step"] == 6:

        result = wizard["result"]

        # =====================================
        # RESULT STATUS
        # =====================================

        if result["category"] == "Not Eligible":

            st.error(
                "❌ Preliminary Assessment: Not Eligible"
            )

        elif result["category"] == "Unable to Assess":

            st.warning(
                "⚠️ More Information Required"
            )

        else:

            st.success(
                f"✅ Possible Category: {result['category']}"
            )

        # =====================================
        # VERTICAL
        # =====================================

        st.info(
            f"🏠 Suggested PMAY-U 2.0 Vertical: {result['vertical']}"
        )

        # =====================================
        # CONFIDENCE
        # =====================================

        st.warning(
            f"Assessment Confidence: {result['confidence']}"
        )

        # =====================================
        # REASONING
        # =====================================

        st.markdown("### Why This Assessment?")

        for item in result["reasoning"]:

            st.markdown(
                f"✅ {item}"
            )

        # =====================================
        # CONCERNS
        # =====================================

        if result["concerns"]:

            st.markdown(
                "### Possible Concerns"
            )

            for item in result["concerns"]:

                st.markdown(
                    f"⚠️ {item}"
                )

        # =====================================
        # DETAILED RESULT
        # =====================================

        st.markdown(
            "### Detailed Assessment"
        )

        st.markdown(
            result["message"]
        )

        # =====================================
        # RESTART
        # =====================================

        if st.button(
            "🔄 Check Again"
        ):

            start_eligibility_wizard()

            st.rerun()
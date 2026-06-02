# ==========================================
# GUIDED CONTEXT FLOWS
# ==========================================

GUIDED_FLOWS = {

    "eligibility": {

        "message":
            (
                "Are you asking about income eligibility, house ownership condition, family eligibility, or scheme eligibility under PMAY?"
            ),

        "options": {

            "Income Eligibility":
                "income_eligibility",

            "House Ownership":
                "house_ownership",

            "Family Eligibility":
                "family_eligibility",

            "Scheme Eligibility":
                "scheme_eligibility"
        }
    },

    "privacy": {

        "message":
            (
                "Are you asking about personal data privacy, Aadhaar/bank safety, beneficiary confidentiality, or application security?"
            ),

        "options": {

            "Personal Data Privacy":
                "personal_data_privacy",

            "Aadhaar / Bank Safety":
                "aadhaar_bank_safety",

            "Beneficiary Confidentiality":
                "beneficiary_confidentiality",

            "Application Security":
                "application_security"
        }
    },

    "subsidy": {

        "message":
            (
                "Do you want to know about subsidy eligibility, subsidy amount, approval process, or subsidy delay issues?"
            ),

        "options": {

            "Subsidy Eligibility":
                "subsidy_eligibility",

            "Subsidy Amount":
                "subsidy_amount",

            "Approval Process":
                "subsidy_approval",

            "Subsidy Delay Issues":
                "subsidy_delay"
        }
    },

    "ownership": {

        "message":
            (
                "Are you asking about pucca house ownership, land ownership, family property, or eligibility impact?"
            ),

        "options": {

            "Pucca House Ownership":
                "pucca_house_ownership",

            "Land Ownership":
                "land_ownership",

            "Family Property":
                "family_property",

            "Eligibility Impact":
                "ownership_eligibility_impact"
        }
    },

    "verification": {

        "message":
            (
                "Are you asking about document verification, beneficiary verification, field verification, or approval verification?"
            ),

        "options": {

            "Document Verification":
                "document_verification",

            "Beneficiary Verification":
                "beneficiary_verification",

            "Field Verification":
                "field_verification",

            "Approval Verification":
                "approval_verification"
        }
    },

    "blc": {

        "message":
            (
                "Are you asking about BLC eligibility,"
                "required documents, construction process," 
                "or application steps?"
            ),

        "options": {

            "BLC Eligibility":
                "blc_eligibility",

            "Required Documents":
                "blc_documents",

            "Construction Process":
                "blc_construction",

            "Application Steps":
                "blc_application"
        }
    },

    "arh": {

        "message":
            (
                "Are you asking about ARH eligibility, rental housing, beneficiary conditions, or application process?"
            ),

        "options": {

            "ARH Eligibility":
                "arh_eligibility",

            "Rental Housing":
                "arh_rental_housing",

            "Beneficiary Conditions":
                "arh_conditions",

            "Application Process":
                "arh_application"
        }
    },

    "ahp": {

        "message":
            (
                "Do you want information about AHP eligibility, affordable housing projects, documents, or approval process?"
            ),

        "options": {

            "AHP Eligibility":
                "ahp_eligibility",

            "Affordable Housing Projects":
                "ahp_projects",

            "Required Documents":
                "ahp_documents",

            "Approval Process":
                "ahp_approval"
        }
    },

    "iss": {

        "message":
            (
                "Are you asking about ISS subsidy, loan benefits, eligibility, or approval conditions?"
            ),

        "options": {

            "ISS Subsidy":
                "iss_subsidy",

            "Loan Benefits":
                "iss_loan_benefits",

            "Eligibility":
                "iss_eligibility",

            "Approval Conditions":
                "iss_approval_conditions"
        }
    },

    "approval": {

        "message":
            (
                "Are you asking about application approval, subsidy approval, sanction process, or status tracking?"
            ),

        "options": {

            "Application Approval":
                "application_approval",

            "Subsidy Approval":
                "subsidy_approval_process",

            "Sanction Process":
                "sanction_process",

            "Status Tracking":
                "approval_status_tracking"
        }
    },

    "fraud": {

        "message":
            (
                "Are you asking about fake documents, scam calls, payment fraud, or identity misuse?"
            ),

        "options": {

            "Fake Documents":
                "fake_documents",

            "Scam Calls":
                "scam_calls",

            "Payment Fraud":
                "payment_fraud",

            "Identity Misuse":
                "identity_misuse"
        }
    },

    "document issue": {

        "message":
            (
                "Do you want to know about required documents, missing documents, verification issues, or correction process?"
            ),

        "options": {

            "Required Documents":
                "required_documents",

            "Missing Documents":
                "missing_documents",

            "Verification Issues":
                "document_verification_issues",

            "Correction Process":
                "document_correction_process"
        }
    },

    "rejection": {

        "message":
            (
                "Are you asking about why rejection happens, reapplication, correction, or appeal options?"
            ),

        "options": {

            "Why Rejection Happens":
                "rejection_reason",

            "Reapplication":
                "reapplication",

            "Correction":
                "rejection_correction",

            "Appeal Options":
                "appeal_options"
        }
    },

    "csmc": {

        "message":
            (
                "Do you want to know CSMC full form, role, approval function, or monitoring responsibility?"
            ),

        "options": {

            "CSMC Full Form":
                "csmc_full_form",

            "Role":
                "csmc_role",

            "Approval Function":
                "csmc_approval",

            "Monitoring Responsibility":
                "csmc_monitoring"
        }
    },

    "ews": {

        "message":
            (
                "Are you asking about EWS eligibility, income criteria, documents, or PMAY benefits?"
            ),

        "options": {

            "EWS Eligibility":
                "ews_eligibility",

            "Income Criteria":
                "ews_income",

            "Required Documents":
                "ews_documents",

            "PMAY-U 2.0 Benefits":
                "ews_benefits"
        }
    },

    "lig": {

        "message":
            (
                "Do you want information on LIG eligibility, income range, subsidy, or PMAY benefits?"
            ),

        "options": {

            "LIG Eligibility":
                "lig_eligibility",

            "Income Range":
                "lig_income",

            "Subsidy":
                "lig_subsidy",

            "PMAY-U 2.0 Benefits":
                "lig_benefits"
        }
    },

    "mig": {

        "message":
            (
                "Are you asking about MIG eligibility, subsidy benefits, income category, or loan assistance?"
            ),

        "options": {

            "MIG Eligibility":
                "mig_eligibility",

            "Subsidy Benefits":
                "mig_subsidy",

            "Income Category":
                "mig_income",

            "Loan Assistance":
                "mig_loan_assistance"
        }
    },

    "grievance": {

        "message":
            (
                "Are you asking about complaint process, delayed application, rejection issue, or authority escalation?"
            ),

        "options": {

            "Complaint Process":
                "complaint_process",

            "Delayed Application":
                "delayed_application",

            "Rejection Issue":
                "grievance_rejection",

            "Authority Escalation":
                "authority_escalation"
        }
    },

    "sanction": {

        "message":
            (
                "Do you want to know about sanction meaning, sanction process, approval stage, or pending sanction issue?"
            ),

        "options": {

            "Sanction Meaning":
                "sanction_meaning",

            "Sanction Process":
                "sanction_process_detail",

            "Approval Stage":
                "sanction_approval_stage",

            "Pending Sanction Issue":
                "pending_sanction"
        }
    },

    "status": {

        "message":
            (
                "Are you asking about application status, subsidy status, verification stage, or approval progress?"
            ),

        "options": {

            "Application Status":
                "application_status",

            "Subsidy Status":
                "subsidy_status",

            "Verification Stage":
                "verification_stage",

            "Approval Progress":
                "approval_progress"
        }
    },

    "pucca": {

        "message":
            (
                "Are you asking about pucca house meaning, ownership eligibility, damaged house condition, or PMAY disqualification?"
            ),

        "options": {

            "Pucca House Meaning":
                "pucca_house_meaning",

            "Ownership Eligibility":
                "pucca_ownership",

            "Damaged House Condition":
                "damaged_house",

            "PMAY-U 2.0 Disqualification":
                "pucca_disqualification"
        }
    },

    "aadhaar": {

        "message":
            (
                "Are you asking about Aadhaar requirement, mismatch issue, update problem, or verification process?"
            ),

        "options": {

            "Aadhaar Requirement":
                "aadhaar_requirement",

            "Mismatch Issue":
                "aadhaar_mismatch",

            "Update Problem":
                "aadhaar_update",

            "Verification Process":
                "aadhaar_verification"
        }
    },

    "can i apply?": {

        "message":
            (
                "To check PMAY-U 2.0 "
                "eligibility, please tell "
                "me about:"
            ),

        "options": {

            "Income Category":
                "check_income",

            "House Ownership":
                "check_house",

            "Family Situation":
                "check_family",

            "Location / Urban Area":
                "check_location"
        }
    },

    "pmay for me?": {

        "message":
            (
                "To check whether "
                "PMAY-U 2.0 may apply "
                "to you, please select:"
            ),

        "options": {

            "Income Category":
                "check_income",

            "House Ownership":
                "check_house",

            "Family Situation":
                "check_family",

            "Location / Urban Area":
                "check_location"
        }
    },

    "no house": {

        "message":
            (
                "Do you currently own any pucca house anywhere in India, or live on rent/slum/chawl?"
            ),

        "options": {

            "No Pucca House":
                "no_pucca_house",

            "Living on Rent":
                "living_on_rent",

            "Living in Slum / Chawl":
                "living_slum_chawl",

            "House Ownership Check":
                "house_ownership_check"
        }
    },

    "rent house": {

        "message":
            (
                "Are you asking about rental housing (ARH) or eligibility for buying/building a house under PMAY?"
            ),

        "options": {

            "Rental Housing (ARH)":
                "rental_housing_arh",

            "Eligibility for Buying House":
                "buy_house_eligibility",

            "Eligibility for Building House":
                "build_house_eligibility",

            "Rent House & PMAY-U 2.0 Eligibility":
                "rent_house_eligibility"
        }
    },

    "documents": {

        "message":
            (
                "Are you asking for general PMAY-U 2.0 documents or for BLC, AHP, ARH, or ISS specifically?"
            ),

        "options": {

            "General PMAY-U 2.0 Documents":
                "general_documents",

            "BLC Documents":
                "blc_documents",

            "AHP Documents":
                "ahp_documents",

            "ARH Documents":
                "arh_documents",

            "ISS Documents":
                "iss_documents"
        }
    },

    "no income proof": {

        "message":
            (
                "Do you have any self-declaration, local certificate, or alternate verification document?"
            ),

        "options": {

            "Self-Declaration":
                "no_income_self_declaration",

            "Local Certificate":
                "no_income_local_certificate",

            "Alternate Verification Document":
                "no_income_alternate_document",

            "No Supporting Document":
                "no_income_no_document"
        }
    },

    "widow": {

        "message":
            (
                "Are you asking about eligibility as widow, ownership rules, or priority benefits?"
            ),

        "options": {

            "Eligibility as Widow":
                "widow_eligibility",

            "Ownership Rules":
                "widow_ownership",

            "Priority Benefits":
                "widow_priority"
        }
    },

    "transgender": {

        "message":
            (
                "Are you asking about PMAY eligibility or ownership rules for transgender applicants?"
            ),

        "options": {

            "PMAY-U 2.0 Eligibility":
                "transgender_eligibility",

            "Ownership Rules":
                "transgender_ownership"
        }
    },

    "senior citizen": {

        "message":
            (
                "Are you asking about priority benefits, eligibility, or housing allotment rules?"
            ),

        "options": {

            "Priority Benefits":
                "senior_priority",

            "Eligibility":
                "senior_eligibility",

            "Housing Allotment Rules":
                "senior_allotment"
        }
    },

    "slum": {

        "message":
            (
                "Are you asking about PMAY eligibility, redevelopment, or better housing options?"
            ),

        "options": {

            "PMAY-U 2.0 Eligibility":
                "slum_eligibility",

            "Redevelopment":
                "slum_redevelopment",

            "Better Housing Options":
                "slum_housing_option"
        }
    },

    "chawl": {

        "message":
            (
                "Are you asking about eligibility while living in chawl or redevelopment-related housing?"
            ),

        "options": {

            "Eligibility While Living in Chawl":
                "chawl_eligibility",

            "Redevelopment Related Housing":
                "chawl_redevelopment"
        }
    },

    "own land": {

        "message":
            (
                "Are you asking whether you can build house under BLC on your own land?"
            ),

        "options": {

            "Build House under BLC":
                "own_land_blc",

            "Eligibility on Own Land":
                "own_land_eligibility",

            "Required Documents":
                "own_land_documents",

            "Construction Assistance":
                "own_land_construction"
        }
    },

    "loan": {

        "message":
            (
                "Are you asking about home loan subsidy under ISS or loan eligibility?"
            ),

        "options": {

            "Home Loan Subsidy under ISS":
                "loan_subsidy",

            "Loan Eligibility":
                "loan_eligibility",

            "Loan Approval":
                "loan_approval",

            "Loan Documents":
                "loan_documents"
        }
    },

    "apply": {

        "message":
            (
                "Which PMAY scheme are you asking about — BLC, AHP, ARH, or ISS?"
            ),

        "options": {

            "BLC":
                "apply_blc",

            "AHP":
                "apply_ahp",

            "ARH":
                "apply_arh",

            "ISS":
                "apply_iss"
        }
    },

    "no documents": {

        "message":
            (
                "Which documents are missing — Aadhaar, income proof, land papers, or address proof?"
            ),

        "options": {

            "Aadhaar":
                "missing_aadhaar",

            "Income Proof":
                "missing_income_proof",

            "Land Papers":
                "missing_land_papers",

            "Address Proof":
                "missing_address_proof"
        }
    },

    "family house": {

        "message":
            (
                "Please select "
                "your situation:"
            ),

        "options": {

            "Family Owns Pucca House":
                "family_pucca_house",

            "House in Parents Name":
                "parents_house",

            "Joint Family Property":
                "joint_family_property",

            "Eligibility Impact":
                "family_house_eligibility"
        }
    },

    "confused": {

        "message":
            (
                "No problem — are you trying to buy, build, rent, or check eligibility under PMAY?"
            ),

        "options": {

            "Buy a House":
                "confused_buy",

            "Build a House":
                "confused_build",

            "Rent a House":
                "confused_rent",

            "Check Eligibility":
                "confused_eligibility"
        }
    },

    "i dont know if i should even apply": {

        "message":
            (
                "No problem — could you share whether you own any pucca house, your income situation, and if you live on rent/slum/chawl?matches your situation:"
            ),

        "options": {

            "No Pucca House":
                "hesitant_no_house",

            "Low Income":
                "hesitant_income",

            "Living on Rent / Slum / Chawl":
                "hesitant_rent_slum",

            "Not Sure About Eligibility":
                "hesitant_unsure"
        }
    },

    "house problem": {

        "message":
            (
                "Are you asking about house ownership, damaged house, rental issue, or PMAY eligibility?"
            ),

        "options": {

            "House Ownership":
                "house_problem_ownership",

            "Damaged House":
                "house_problem_damage",

            "Rental Issue":
                "house_problem_rent",

            "PMAY-U 2.0 Eligibility":
                "house_problem_eligibility"
        }
    },

    "my case complicated": {

        "message":
            (
                "That’s okay — is the complication related to family, ownership, documents, income, or rejection?"
            ),

        "options": {

            "Family Situation":
                "complicated_family",

            "Ownership Issue":
                "complicated_ownership",

            "Documents":
                "complicated_documents",

            "Income":
                "complicated_income",

            "Application Rejection":
                "complicated_rejection"
        }
    },

    "family house but not my house but also kind of my house": {

        "message":
            (
                "Could you clarify whether your name appears in ownership records or if the house belongs to another family member?"
            ),

        "options": {

            "House in My Name":
                "ownership_my_name",

            "House in Parent's Name":
                "ownership_parents",

            "Joint Family Property":
                "ownership_joint_family",

            "Not Sure About Ownership":
                "ownership_unsure"
        }
    },

    "i rent but family has something somewhere i think": {

        "message":
            (
                "Do you know whether you or your beneficiary family own any pucca house anywhere in India?"
            ),

        "options": {

            "Yes":
                "family_house_yes",

            "No":
                "family_house_no",

            "Not Sure":
                "family_house_unsure",

            "House in Relative's Name":
                "family_relative_house"
        }
    },

    "aadhaar problem maybe": {

        "message":
            (
                "Are you facing an address mismatch, missing Aadhaar, wrong details, or verification issue?"
            ),

        "options": {

            "Address Mismatch":
                "aadhaar_address_issue",

            "Missing Aadhaar":
                "aadhaar_missing",

            "Wrong Details":
                "aadhaar_wrong_details",

            "Verification Issue":
                "aadhaar_verification_issue"
        }
    },

    "widow but also documents issue and money issue": {

        "message":
            (
                "Possibly yes, but could you share whether the main concern is eligibility, documents, or income proof?"
            ),

        "options": {

            "Eligibility as Widow":
                "widow_money_eligibility",

            "Documents Issue":
                "widow_document_issue",

            "Income / Money Problem":
                "widow_income_issue",

            "Not Sure":
                "widow_unsure"
        }
    },

    "landlord threatening because i asked about scheme": {

        "message":
            (
                "That sounds stressful. Are you asking about eligibility while renting or document/address concerns?"
            ),

        "options": {

            "Eligibility While Renting":
                "renting_eligibility",

            "Address / Document Concern":
                "rent_document_issue",

            "Housing Safety Concern":
                "housing_safety",

            "Not Sure":
                "rent_unsure"
        }
    },

    "maybe pmay not for people like me": {

        "message":
            (
                "PMAY may still be worth checking. Could you share your housing, income, and ownership situation?"
            ),

        "options": {

            "Housing Problem":
                "pmay_people_housing",

            "Low Income":
                "pmay_people_income",

            "No Pucca House":
                "pmay_people_no_house",

            "Not Sure About Eligibility":
                "pmay_people_unsure"
        }
    },

    "my papers all weird honestly": {

        "message":
            (
                "Are the issues related to name mismatch, address mismatch, missing proof, or ownership documents?"
            ),

        "options": {

            "Name Mismatch":
                "paper_name_mismatch",

            "Address Mismatch":
                "paper_address_mismatch",

            "Missing Documents":
                "paper_missing_documents",

            "Ownership Documents":
                "paper_ownership_issue"
        }
    },

    "dont have house but family situation messy": {

        "message":
            (
                "Could you share whether the issue is related to family ownership, separation, inheritance, or documents?"
            ),

        "options": {

            "Family Ownership Issue":
                "messy_family_ownership",

            "Separation / Family Conflict":
                "messy_family_separation",

            "Inheritance Issue":
                "messy_family_inheritance",

            "Document Confusion":
                "messy_family_documents"
        }
    },

    "slum but not fully slum temporary type": {

        "message":
            (
                "Are you asking whether your housing condition counts for PMAY eligibility?"
            ),

        "options": {

            "Temporary Housing":
                "temporary_housing",

            "Unsafe / Damaged Housing":
                "unsafe_housing",

            "Informal Settlement":
                "informal_settlement",

            "Not Sure":
                "temporary_unsure"
        }
    },

    "i think someone maybe used my details": {

        "message":
            (
                "Are you worried about Aadhaar misuse, duplicate beneficiary issue, or fake application concerns?"
            ),

        "options": {

            "Aadhaar Misuse":
                "details_aadhaar_misuse",

            "Duplicate Beneficiary Issue":
                "details_duplicate_issue",

            "Fake PMAY-U 2.0 Application":
                "details_fake_application",

            "Not Sure":
                "details_unsure"
        }
    },

    "my marriage situation very weird honestly": {

        "message":
            (
                "Is the concern related to separation, spouse ownership, divorce, or eligibility after marriage?"
            ),

        "options": {

            "Separation":
                "marriage_separation",

            "Spouse Owns House":
                "marriage_spouse_house",

            "Divorce Situation":
                "marriage_divorce",

            "Eligibility After Marriage":
                "marriage_after"
        }
    },

    "i dont know which scheme even": {

        "message":
            (
                "Are you trying to buy, build, rent, or get subsidy support for housing?"
            ),

        "options": {

            "Buy a House":
                "scheme_buy",

            "Build a House":
                "scheme_build",

            "Rent a House":
                "scheme_rent",

            "Need Subsidy / Loan Support":
                "scheme_subsidy"
        }
    },

    "rejection but maybe wrong rejection maybe": {

        "message":
            (
                "Do you know whether the rejection was due to ownership, income, documents, or duplicate beneficiary issue?"
            ),

        "options": {

            "Ownership Issue":
                "wrong_rejection_ownership",

            "Income Issue":
                "wrong_rejection_income",

            "Documents Issue":
                "wrong_rejection_documents",

            "Duplicate Beneficiary Issue":
                "wrong_rejection_duplicate"
        }
    },

    "family says dont apply waste of time": {

        "message":
            (
                "PMAY eligibility depends on your situation. Could you share ownership, income, and housing condition?"
            ),

        "options": {

            "No Pucca House":
                "family_doubt_no_house",

            "Low Income":
                "family_doubt_income",

            "Housing Problem":
                "family_doubt_housing",

            "Not Sure About Eligibility":
                "family_doubt_unsure"
        }
    },

    "honestly i dont even understand these terms": {

        "message":
            (
                "No problem — are you trying to understand eligibility, documents, subsidy, or PMAY schemes first?"
            ),

        "options": {

            "Eligibility":
                "understand_eligibility",

            "Documents":
                "understand_documents",

            "Subsidy":
                "understand_subsidy",

            "PMAY-U 2.0 Schemes":
                "understand_schemes"
        }
    },

    "bank issue and document issue and no fixed place": {

        "message":
            (
                "Could you share whether the main issue is DBT/bank account, address proof, or eligibility while renting/migrating?"
            ),

        "options": {

            "Bank / DBT Issue":
                "bank_document_dbt",

            "Address Proof Problem":
                "bank_document_address",

            "Eligibility While Renting / Migrating":
                "bank_document_rent_migration",

            "Not Sure":
                "bank_document_unsure"
        }
    },

    "i honestly dont know what counts as house anymore": {

        "message":
            (
                "Are you asking whether your existing structure qualifies as pucca house for PMAY eligibility?"
            ),

        "options": {

            "Temporary Structure":
                "house_temporary",

            "Semi-Pucca / Weak House":
                "house_semi_pucca",

            "Family-Owned House":
                "house_family_owned",

            "Not Sure":
                "house_unsure"
        }
    },

    "too many problems together idk where start": {

        "message":
            (
                "No problem — let us "
                "start with the biggest "
                "issue first."
            ),

        "options": {

            "House Problem":
                "many_problem_house",

            "Income Problem":
                "many_problem_income",

            "Documents Problem":
                "many_problem_documents",

            "Family Situation":
                "many_problem_family",

            "Rejection Issue":
                "many_problem_rejection"
        }
    },

    "feels like chatbot also cant understand my case": {

        "message":
            (
                "That’s okay — we can check it step by step. Is your main concern house ownership, income, family situation, or documents?"
            ),

        "options": {

            "House Ownership":
                "chatbot_house",

            "Income":
                "chatbot_income",

            "Family Situation":
                "chatbot_family",

            "Documents":
                "chatbot_documents"
        }
    },

    "bank issue too now": {

        "message":
            (
                "Is the issue related to DBT delay, inactive account, wrong account details, or mismatch?"
            ),

        "options": {

            "DBT Delay":
                "bank_dbt_delay",

            "Inactive Account":
                "bank_inactive_account",

            "Wrong Account Details":
                "bank_wrong_account",

            "Bank Mismatch":
                "bank_mismatch"
        }
    },

    "idk which scheme bro": {

        "message":
            (
                "No problem — are you trying to build, buy, rent, or reduce housing loan burden?"
            ),

        "options": {

            "Build a House":
                "scheme_bro_build",

            "Buy a House":
                "scheme_bro_buy",

            "Rent a House":
                "scheme_bro_rent",

            "Reduce Loan Burden":
                "scheme_bro_loan"
        }
    },

    "honestly embarrassed to ask": {

        "message":
            (
                "No problem — what feels like the biggest issue: house, income, documents, family, or rejection?"
            ),

        "options": {

            "House Problem":
                "embarrassed_house",

            "Income Problem":
                "embarrassed_income",

            "Documents Problem":
                "embarrassed_documents",

            "Family Situation":
                "embarrassed_family",

            "Rejection":
                "embarrassed_rejection"
        }
    },

    "too many issues together": {

        "message":
            (
                "We can check step by step — is the biggest concern ownership, documents, family, income, or application status?"
            ),

        "options": {

            "Ownership":
                "many_issue_ownership",

            "Documents":
                "many_issue_documents",

            "Family":
                "many_issue_family",

            "Income":
                "many_issue_income",

            "Application Status":
                "many_issue_status"
        }
    },

    "name mismatch": {

        "message":
            (
                "Is the mismatch between Aadhaar, bank, PAN, application form, or property documents?"
            ),

        "options": {

            "Aadhaar":
                "mismatch_aadhaar",

            "Bank Details":
                "mismatch_bank",

            "PAN":
                "mismatch_pan",

            "Application Form":
                "mismatch_application",

            "Property Documents":
                "mismatch_property"
        }
    },

    "rejected because mismatch but not sure which mismatch": {

        "message":
            (
                "Do you know whether the mismatch involved Aadhaar, income proof, bank details, address, or ownership documents?"
            ),

        "options": {

            "Aadhaar":
                "reject_mismatch_aadhaar",

            "Income Proof":
                "reject_mismatch_income",

            "Bank Details":
                "reject_mismatch_bank",

            "Address":
                "reject_mismatch_address",

            "Ownership Documents":
                "reject_mismatch_ownership"
        }
    },

    "which scheme for me?": {

        "message":
            (
                "No problem — what are "
                "you mainly trying to do "
                "under PMAY-U 2.0?"
            ),

        "options": {

            "Build a House":
                "scheme_for_me_build",

            "Buy a House":
                "scheme_for_me_buy",

            "Rent a House":
                "scheme_for_me_rent",

            "Get Subsidy / Loan Help":
                "scheme_for_me_subsidy"
        }
    },

    "idk if eligible honestly": {

        "message":
            (
                "No problem — do you own any pucca house, live on rent, or know your income category?"
            ),

        "options": {

            "No Pucca House":
                "eligible_no_house",

            "Living on Rent":
                "eligible_rent",

            "Know Income Category":
                "eligible_income",

            "Not Sure":
                "eligible_unsure"
        }
    },

    "house not mine but kinda mine": {

        "message":
            (
                "Could you clarify whether your name appears in ownership documents or belongs to family member?"
            ),

        "options": {

            "House in My Name":
                "house_kind_my_name",

            "Family Member's House":
                "house_kind_family",

            "Joint Family Property":
                "house_kind_joint",

            "Not Sure":
                "house_kind_unsure"
        }
    },

    "maybe rejected maybe pending": {

        "message":
            (
                "Do you see pending, rejected, under review, or no update in your PMAY status?"
            ),

        "options": {

            "Pending":
                "status_pending",

            "Rejected":
                "status_rejected",

            "Under Review":
                "status_under_review",

            "No Update":
                "status_no_update"
        }
    },

    "pending": {

        "message":
            (
                "What kind of pending "
                "issue are you worried about?"
            ),

        "options": {

            "Document Verification":
                "pending_documents",

            "Approval Delay":
                "pending_approval",

            "Subsidy / DBT Delay":
                "pending_subsidy",

            "Not Sure":
                "pending_unsure"
        }
    },

    "papers all messed up": {

        "message":
            (
                "Are the issues related to Aadhaar, bank details, name mismatch, address, or ownership proof?"
            ),

        "options": {

            "Aadhaar Issue":
                "papers_aadhaar",

            "Bank Details":
                "papers_bank",

            "Name Mismatch":
                "papers_name",

            "Address Problem":
                "papers_address",

            "Ownership Proof":
                "papers_ownership"
        }
    },

    "rent room no house no clue": {

        "message":
            (
                "No problem — are you looking for rental housing help or permanent house ownership support?"
            ),

        "options": {

            "Rental Housing Help":
                "rent_room_rental",

            "Permanent House Ownership":
                "rent_room_ownership",

            "Eligibility Check":
                "rent_room_eligibility",

            "Not Sure":
                "rent_room_unsure"
        }
    },

        "family thing complicated": {

        "message":
            (
                "Is the complication related to ownership, separation, inheritance, or family housing?"
            ),

        "options": {

            "Ownership":
                "family_comp_ownership",

            "Separation":
                "family_comp_separation",

            "Inheritance":
                "family_comp_inheritance",

            "Family Housing":
                "family_comp_housing"
        }
    },

    "scared to apply honestly": {

        "message":
            (
                "That’s understandable — could you share whether your concern is about eligibility, rejection, documents, or ownership?"
            ),

        "options": {

            "Eligibility":
                "scared_eligibility",

            "Rejection":
                "scared_rejection",

            "Documents":
                "scared_documents",

            "Ownership":
                "scared_ownership"
        }
    },

    "they say im not eligible": {

        "message":
            (
                "Could you share why they think that — ownership, income, family house, or rejection history?"
            ),

        "options": {

            "Ownership":
                "not_eligible_ownership",

            "Income":
                "not_eligible_income",

            "Family House":
                "not_eligible_family_house",

            "Previous Rejection":
                "not_eligible_rejection"
        }
    },

    "no idea whats wrong in app": {

        "message":
            (
                "Do you know whether the issue relates to documents, verification, rejection, or pending status?"
            ),

        "options": {

            "Documents":
                "app_issue_documents",

            "Verification":
                "app_issue_verification",

            "Rejection":
                "app_issue_rejection",

            "Pending Status":
                "app_issue_pending"
        }
    },

    "feels impossible ngl": {

        "message":
            (
                "Difficult situations are not automatically disqualified. Could you share your housing, family, and income situation?"
            ),

        "options": {

            "Housing":
                "impossible_housing",

            "Family":
                "impossible_family",

            "Income":
                "impossible_income",

            "Not Sure":
                "impossible_unsure"
        }
    },

    "maybe fraud happened idk": {

        "message":
            (
                "Are you worried about Aadhaar misuse, fake approval, duplicate beneficiary, or suspicious calls?"
            ),

        "options": {

            "Aadhaar Misuse":
                "fraud_aadhaar",

            "Fake Approval":
                "fraud_fake_approval",

            "Duplicate Beneficiary":
                "fraud_duplicate",

            "Suspicious Calls":
                "fraud_calls"
        }
    },

    "family owns stuff somewhere maybe": {

        "message":
            (
                "Let's try to understand the "
                "ownership situation better. "
                "Do you know which of these is true?"
            ),

        "options": {

            "Beneficiary Family Owns House":
                "family_stuff_family_house",

            "Parents Own House":
                "family_stuff_parents_house",

            "Relative Owns House":
                "family_stuff_relative_house",

            "Not Sure":
                "family_stuff_unsure"
        }
    },

    "broke af no house": {

        "message":
            (
                "Could you share whether you live on rent, slum, chawl, or temporary housing?"
            ),

        "options": {

            "Living on Rent":
                "broke_rent",

            "Living in Slum":
                "broke_slum",

            "Living in Chawl":
                "broke_chawl",

            "Temporary Housing":
                "broke_temporary"
        }
    },

    "applied long ago nothing happening": {

        "message":
            (
                "Do you know whether the status shows pending, under review, sanction, or verification stage?"
            ),

        "options": {

            "Pending":
                "old_application_pending",

            "Under Review":
                "old_application_review",

            "Sanctioned":
                "old_application_sanction",

            "Verification Stage":
                "old_application_verification"
        }
    },

    "weird marriage situation": {

        "message":
            (
                "Is the concern related to separation, spouse ownership, divorce, or eligibility after marriage?"
            ),

        "options": {

            "Separation":
                "marriage_weird_separation",

            "Spouse Owns House":
                "marriage_weird_spouse_house",

            "Divorce":
                "marriage_weird_divorce",

            "Eligibility After Marriage":
                "marriage_weird_after"
        }
    },

    "bank issue too now": {

        "message":
            (
                "Is the issue related to DBT delay, inactive account, wrong account details, or mismatch?"
            ),

        "options": {

            "DBT Delay":
                "bank_issue_dbt",

            "Inactive Account":
                "bank_issue_inactive",

            "Wrong Account Details":
                "bank_issue_wrong_account",

            "Bank Mismatch":
                "bank_issue_mismatch"
        }
    },

    "idk which scheme bro": {

        "message":
            (
                "No problem — are you trying to build, "
                "buy, rent, or reduce housing loan burden?"
            ),

        "options": {

            "Build a House":
                "scheme_build",

            "Buy a House":
                "scheme_buy",

            "Rent a House":
                "scheme_rent",

            "Reduce Housing Loan Burden":
                "scheme_loan"
        }
    },

    "honestly embarrassed to ask": {

        "message":
            (
                "No problem — what feels like the biggest "
                "issue: house, income, documents, family, "
                "or rejection?"
            ),

        "options": {

            "House":
                "embarrassed_house",

            "Income":
                "embarrassed_income",

            "Documents":
                "embarrassed_documents",

            "Family":
                "embarrassed_family",

            "Rejection":
                "embarrassed_rejection"
        }
    },

    "too many issues together": {

        "message":
            (
                "We can check step by step — is the "
                "biggest concern ownership, documents, "
                "family, income, or application status?"
            ),

        "options": {

            "Ownership":
                "many_ownership",

            "Documents":
                "many_documents",

            "Family":
                "many_family",

            "Income":
                "many_income",

            "Application Status":
                "many_status"
        }
    },

    "honestly rules feel confusing": {

        "message":
            (
                "No problem — is your confusion about "
                "house ownership, income, family rules, "
                "or PMAY eligibility?"
            ),

        "options": {

            "House Ownership":
                "rules_ownership",

            "Income Rules":
                "rules_income",

            "Family Rules":
                "rules_family",

            "PMAY-U 2.0 Eligibility":
                "rules_eligibility"
        }
    },

    "honestly dont understand workflow": {

        "message":
            (
                "No problem — are you trying to understand "
                "verification, approvals, subsidy flow, "
                "or implementation process?"
            ),

        "options": {

            "Verification":
                "workflow_verification",

            "Approvals":
                "workflow_approval",

            "Subsidy Flow":
                "workflow_subsidy",

            "Implementation Process":
                "workflow_implementation"
        }
    },

    "honestly dont understand process": {

        "message":
            (
                "No problem — are you trying to understand "
                "verification, subsidy release, approvals, "
                "or construction monitoring?"
            ),

        "options": {

            "Verification":
                "process_verification",

            "Subsidy Release":
                "process_subsidy",

            "Approvals":
                "process_approval",

            "Construction Monitoring":
                "process_monitoring"
        }
    },

    "village house issue?": {

        "message":
            (
                "Are you asking whether a house in a village "
                "affects PMAY-U 2.0 eligibility?"
            ),

        "options": {

            "Village House in My Name":
                "village_my_house",

            "Village House in Family Name":
                "village_family_house",

            "Ancestral Village House":
                "village_ancestral_house",

            "Not Sure":
                "village_unsure"
        }
    },

    "family house problem?": {

        "message":
            (
                "Could you clarify whether the concern is "
                "about family ownership affecting eligibility?"
            ),

        "options": {

            "Parents Own House":
                "family_problem_parents",

            "Joint Family House":
                "family_problem_joint",

            "Inherited House":
                "family_problem_inherited",

            "Ownership Not Clear":
                "family_problem_unclear"
        }
    },

    "no salary proof?": {

        "message":
            (
                "Do you have any alternate income-related "
                "supporting proof or declaration?"
            ),

        "options": {

            "Self Declaration":
                "income_self_declaration",

            "Local Authority Certificate":
                "income_local_certificate",

            "Informal Income":
                "income_informal",

            "No Proof Available":
                "income_no_proof"
        }
    },

    "rejected why?": {

        "message":
            (
                "Do you know whether the issue involved "
                "ownership, income, documents, or "
                "verification mismatch?"
            ),

        "options": {

            "Ownership":
                "reject_ownership",

            "Income":
                "reject_income",

            "Documents":
                "reject_documents",

            "Verification Mismatch":
                "reject_verification"
        }
    },

    "pending too long": {

        "message":
            (
                "Do you know whether the application is "
                "at verification, ULB, approval, or "
                "DBT stage?"
            ),

        "options": {

            "Verification Stage":
                "pending_verification",

            "ULB Stage":
                "pending_ulb",

            "Approval Stage":
                "pending_approval",

            "DBT Stage":
                "pending_dbt"
        }
    },

    "bank issue": {

        "message":
            (
                "Is the concern related to DBT delay, "
                "inactive account, wrong details, or mismatch?"
            ),

        "options": {

            "DBT Delay":
                "bank_dbt_delay",

            "Inactive Account":
                "bank_inactive_account",

            "Wrong Account Details":
                "bank_wrong_details",

            "Bank Mismatch":
                "bank_mismatch"
        }
    },

    "aadhaar issue": {

        "message":
            (
                "Is the issue related to wrong details, "
                "address mismatch, missing Aadhaar, or verification?"
            ),

        "options": {

            "Wrong Aadhaar Details":
                "aadhaar_wrong_details",

            "Address Mismatch":
                "aadhaar_address_mismatch",

            "Missing Aadhaar":
                "aadhaar_missing",

            "Verification Issue":
                "aadhaar_verification"
        }
    },

    "rent house okay?": {

        "message":
            (
                "Are you asking about rental housing support "
                "or PMAY-U 2.0 eligibility while renting?"
            ),

        "options": {

            "Rental Housing Support":
                "rent_support",

            "Eligibility While Renting":
                "rent_eligibility"
        }
    },

    "no land now?": {

        "message":
            (
                "Are you asking about housing options "
                "without owning land?"
            ),

        "options": {

            "Want to Build House":
                "no_land_build",

            "Want to Buy House":
                "no_land_buy",

            "Looking for Rental Housing":
                "no_land_rent",

            "Not Sure":
                "no_land_unsure"
        }
    },

    "documents needed?": {

        "message":
            (
                "Are you asking for general PMAY-U 2.0 "
                "documents or a specific scheme like "
                "BLC, AHP, ARH, or ISS?"
            ),

        "options": {

            "General Documents":
                "docs_general",

            "BLC Documents":
                "docs_blc",

            "AHP Documents":
                "docs_ahp",

            "ARH Documents":
                "docs_arh",

            "ISS Documents":
                "docs_iss"
        }
    },

    "house damaged issue?": {

        "message":
            (
                "Are you asking whether a damaged house "
                "affects PMAY-U 2.0 eligibility?"
            ),

        "options": {

            "Partially Damaged House":
                "damage_partial",

            "Severely Damaged House":
                "damage_severe",

            "Unsafe to Live In":
                "damage_unsafe",

            "Need House Improvement":
                "damage_improvement"
        }
    },

    "family issue pmay?": {

        "message":
            (
                "Is the concern related to ownership, "
                "separation, inheritance, or family eligibility?"
            ),

        "options": {

            "Ownership":
                "family_issue_ownership",

            "Separation":
                "family_issue_separation",

            "Inheritance":
                "family_issue_inheritance",

            "Family Eligibility":
                "family_issue_eligibility"
        }
    },

    "too confusing": {

        "message":
            (
                "No problem — is your biggest concern "
                "eligibility, documents, subsidy, or "
                "application status?"
            ),

        "options": {

            "Eligibility":
                "confusing_eligibility",

            "Documents":
                "confusing_documents",

            "Subsidy":
                "confusing_subsidy",

            "Application Status":
                "confusing_status"
        }
    },

    "no update": {

        "message":
            (
                "Do you know whether the application is "
                "pending, under review, verification, or "
                "approval stage?"
            ),

        "options": {

            "Pending":
                "update_pending",

            "Under Review":
                "update_review",

            "Verification":
                "update_verification",

            "Approval Stage":
                "update_approval"
        }
    },

    "fraud fear": {

        "message":
            (
                "Are you worried about OTP scams, fake approval, "
                "identity misuse, or suspicious calls?"
            ),

        "options": {

            "OTP Scam":
                "fraud_otp",

            "Fake Approval":
                "fraud_fake_approval",

            "Identity Misuse":
                "fraud_identity",

            "Suspicious Calls":
                "fraud_calls"
        }
    },

    "honestly scared apply": {

        "message":
            (
                "That's understandable — is the worry about "
                "eligibility, rejection, documents, or fraud concerns?"
            ),

        "options": {

            "Eligibility":
                "scared_apply_eligibility",

            "Rejection":
                "scared_apply_rejection",

            "Documents":
                "scared_apply_documents",

            "Fraud Concerns":
                "scared_apply_fraud"
        }
    },

    "idk what to do": {

        "message":
            (
                "No problem — what feels like the biggest "
                "issue first: house, income, documents, "
                "family, or rejection?"
            ),

        "options": {

            "House":
                "idk_house",

            "Income":
                "idk_income",

            "Documents":
                "idk_documents",

            "Family":
                "idk_family",

            "Rejection":
                "idk_rejection"
        }
    },

    "Honestly I can’t tell if issue is fraud, rejection, documents, or ownership anymore.": {

        "message":
            (
                "No problem — what feels like the biggest "
                "issue first: rejection, ownership, "
                "verification, or fraud concern?"
            ),

        "options": {

            "Rejection":
                "mixed_rejection",

            "Ownership":
                "mixed_ownership",

            "Verification":
                "mixed_verification",

            "Fraud Concern":
                "mixed_fraud"
        }
    },

    "I feel eligible and ineligible at same time honestly": {

        "message":
            (
                "No problem — is the biggest confusion "
                "related to house ownership, family, "
                "income, or rejection?"
            ),

        "options": {

            "House Ownership":
                "eligible_confused_ownership",

            "Family":
                "eligible_confused_family",

            "Income":
                "eligible_confused_income",

            "Rejection":
                "eligible_confused_rejection"
        }
    },

    "Everything says “possibly” and now I am more confused": {

        "message":
            (
                "That's understandable — what feels like "
                "the biggest issue first: house, family, "
                "income, or documents?"
            ),

        "options": {

            "House":
                "possibly_house",

            "Family":
                "possibly_family",

            "Income":
                "possibly_income",

            "Documents":
                "possibly_documents"
        }
    },

    "I feel eligible and ineligible at same time honestly": {

        "message":
            (
                "No problem — is the biggest confusion "
                "related to house ownership, family, "
                "income, or rejection?"
            ),

        "options": {

            "House Ownership":
                "confused_ownership",

            "Family Situation":
                "confused_family",

            "Income":
                "confused_income",

            "Rejection Concern":
                "confused_rejection"
        }
    },

    "Everything says possibly and now I am more confused": {

        "message":
            (
                "That's understandable — what feels like "
                "the biggest issue first: house, family, "
                "income, or documents?"
            ),

        "options": {

            "House":
                "possibly_house",

            "Family":
                "possibly_family",

            "Income":
                "possibly_income",

            "Documents":
                "possibly_documents"
        }
    },

    "I keep opening the PMAY page and closing it because I honestly feel my case is too messy": {

        "message":
            (
                "That's understandable — what feels like "
                "the biggest concern: house ownership, "
                "family situation, documents, or rejection fear?"
            ),

        "options": {

            "House Ownership":
                "messy_ownership",

            "Family Situation":
                "messy_family",

            "Documents":
                "messy_documents",

            "Rejection Fear":
                "messy_rejection"
        }
    },

    "Everyone around me says just apply but nobody actually understands my situation": {

        "message":
            (
                "Could you share whether your biggest concern "
                "is eligibility, family ownership, documents, "
                "or housing situation?"
            ),

        "options": {

            "Eligibility":
                "situation_eligibility",

            "Family Ownership":
                "situation_family",

            "Documents":
                "situation_documents",

            "Housing Situation":
                "situation_housing"
        }
    },

    "I don’t even know what question I’m supposed to ask anymore": {

        "message":
            (
                "No problem — what feels most confusing right now: "
                "house, income, family, documents, or application status?"
            ),

            "options": {

            "House":
                "dontknow_house",

            "Income":
                "dontknow_income",

            "Family":
                "dontknow_family",

            "Documents":
                "dontknow_documents",

            "Application Status":
                "dontknow_status"
        }
    },

    "My situation sounds fake even when I explain it to people": {

        "message":
            (
                "Complex situations happen more often than "
                "you think. Is the biggest issue related to "
                "ownership, family, documents, or housing?"
            ),

        "options": {

            "Ownership":
                "fake_ownership",

            "Family":
                "fake_family",

            "Documents":
                "fake_documents",

            "Housing":
                "fake_housing"
        }
    },

    "Honestly I m scared someone will laugh if I explain how complicated my life situation is": {

        "message":
            (
                "No judgment here — what part feels hardest: "
                "housing, family conflict, unstable income, "
                "or documents?"
            ),

        "options": {

            "Housing":
                "laugh_housing",

            "Family Conflict":
                "laugh_family",

            "Unstable Income":
                "laugh_income",

            "Documents":
                "laugh_documents"
        }
    },

    "Every time I think I understand PMAY, someone tells me a completely different thing": {

        "message":
            (
                "Conflicting advice can feel frustrating. "
                "Could you share whether the confusion is "
                "about eligibility, ownership, subsidy, "
                "or application process?"
            ),

        "options": {

            "Eligibility":
                "advice_eligibility",

            "Ownership":
                "advice_ownership",

            "Subsidy":
                "advice_subsidy",

            "Application Process":
                "advice_process"
        }
    },

    "I genuinely don’t know if I’m confused or just exhausted from trying to understand rules": {

        "message":
            (
                "That’s understandable — would it help to "
                "start with just one thing: eligibility, "
                "documents, subsidy, or status?"
            ),

        "options": {

            "Eligibility":
                "exhausted_eligibility",

            "Documents":
                "exhausted_documents",

            "Subsidy":
                "exhausted_subsidy",

            "Application Status":
                "exhausted_status"
        }
    },

    "My family situation is the kind where every answer creates three more problems": {

        "message":
            (
                "Complex family situations may still be checked "
                "step by step. Is the main issue ownership, "
                "separation, inheritance, or dependency?"
            ),

        "options": {

            "Ownership":
                "family_complex_ownership",

            "Separation":
                "family_complex_separation",

            "Inheritance":
                "family_complex_inheritance",

            "Dependency":
                "family_complex_dependency"
        }
    },

    "I honestly don’t know whether to ask about my house issue or family issue first": {

        "message":
            (
                "No problem — which one feels more urgent "
                "right now: housing situation or family-related concern?"
            ),

        "options": {

            "Housing Situation":
                "house_or_family_house",

            "Family Concern":
                "house_or_family_family"
        }
    },

    "My life is basically paperwork problems mixed with family drama": {

        "message":
            (
                "That sounds stressful. Is the bigger issue "
                "currently documents, ownership, or family conflict?"
            ),

        "options": {

            "Documents":
                "drama_documents",

            "Ownership":
                "drama_ownership",

            "Family Conflict":
                "drama_family"
        }
    },

    "I honestly don’t know how to explain my situation without sounding confusing": {

        "message":
            (
                "No problem — we can go one step at a time. "
                "Is the issue mainly housing, documents, "
                "family, or application status?"
            ),

        "options": {

            "Housing":
                "explain_housing",

            "Documents":
                "explain_documents",

            "Family":
                "explain_family",

            "Application Status":
                "explain_status"
        }
    },

    "I don’t know if I need cheaper rent or future ownership more": {

        "message":
            (
                "Would you prefer immediate housing stability "
                "or long-term ownership support first?"
            ),

        "options": {

            "Immediate Housing Stability":
                "rent_stability",

            "Long-Term Ownership":
                "future_ownership"
        }
    },

    "Honestly all schemes sound useful and useless at same time": {

        "message":
            (
                "No problem — are you trying to build, buy, "
                "rent, or reduce loan-related housing pressure first?"
            ),

        "options": {

            "Build":
                "allschemes_build",

            "Buy":
                "allschemes_buy",

            "Rent":
                "allschemes_rent",

            "Reduce Loan Burden":
                "allschemes_loan"
        }
    },

    "BLC, AHP, ARH, ISS all somehow partially fit my situation": {

        "message":
            (
                "That happens sometimes — what feels most urgent "
                "first: land, housing purchase, rental stability, "
                "or loan burden?"
            ),

        "options": {

            "Land / Construction":
                "partial_blc",

            "Housing Purchase":
                "partial_ahp",

            "Rental Stability":
                "partial_arh",

            "Loan Burden":
                "partial_iss"
        }
    },

    "I shared PMAY papers with someone helping me and now regret it": {

        "message":
            (
                "Sensitive documents should generally be handled carefully. "
                "Are you worried about identity misuse, fake application, "
                "or document misuse?"
            ),

        "options": {

            "Identity Misuse":
                "regret_identity",

            "Fake Application":
                "regret_fake_application",

            "Document Misuse":
                "regret_document_misuse"
        }
    },

    "Honestly I don’t know who to trust anymore in PMAY process": {

        "message":
            (
                "That’s understandable — is your biggest concern "
                "documents, fraud, privacy, or approval-related confusion?"
            ),

        "options": {

            "Documents":
                "trust_documents",

            "Fraud":
                "trust_fraud",

            "Privacy":
                "trust_privacy",

            "Approval Confusion":
                "trust_approval"
        }
    },

    "Honestly I don’t even know who my family counts as legally anymore": {

        "message":
            (
                "No problem — is the biggest confusion related to "
                "marriage, parents, ownership, or dependency?"
            ),

        "options": {

            "Marriage":
                "family_legal_marriage",

            "Parents":
                "family_legal_parents",

            "Ownership":
                "family_legal_ownership",

            "Dependency":
                "family_legal_dependency"
        }
    },

    "I honestly can’t tell if my biggest issue is rejection, documents, ownership, or just exhaustion": {

        "message":
            (
                "That’s understandable — which feels most urgent right now: "
                "ownership, verification, rejection, or housing stability?"
            ),

        "options": {

            "Ownership":
                "exhaustion_ownership",

            "Verification":
                "exhaustion_verification",

            "Rejection":
                "exhaustion_rejection",

            "Housing Stability":
                "exhaustion_housing"
        }
    },

    "I trust nobody anymore because every PMAY answer feels different": {

        "message":
            (
                "That’s understandable — is your biggest concern "
                "eligibility, privacy, ownership, or approval-related confusion?"
            ),

        "options": {

            "Eligibility":
                "trustnone_eligibility",

            "Privacy":
                "trustnone_privacy",

            "Ownership":
                "trustnone_ownership",

            "Approval Confusion":
                "trustnone_approval"
        }
    },

    "Honestly I don’t even know whether I need housing help or just clarity anymore": {

        "message":
            (
                "That’s understandable — what feels most urgent: "
                "housing stability, eligibility, documents, or application confusion?"
            ),

        "options": {

            "Housing Stability":
                "clarity_housing",

            "Eligibility":
                "clarity_eligibility",

            "Documents":
                "clarity_documents",

            "Application Confusion":
                "clarity_application"
        }
    },

    "honestly not sure if i count as eligible person": {

        "message":
            (
                "No problem — do you own any house, "
                "live on rent, or know your current housing situation?"
            ),

        "options": {

            "I Own a House":
                "eligible_own_house",

            "I Live on Rent":
                "eligible_rent",

            "Housing Situation Not Clear":
                "eligible_unclear"
        }
    },

    "arh or ownership better?": {

        "message":
            (
                "Would you prefer temporary affordable rental "
                "housing or long-term ownership support?"
            ),

        "options": {

            "Affordable Rental Housing":
                "arh_better",

            "Long-Term Ownership":
                "ownership_better"
        }
    },

    "no clue difference between all schemes": {

        "message":
            (
                "No problem — are you trying to build, buy, "
                "rent, or reduce housing loan burden?"
            ),

        "options": {

            "Build":
                "difference_blc",

            "Buy":
                "difference_ahp",

            "Rent":
                "difference_arh",

            "Reduce Loan Burden":
                "difference_iss"
        }
    },

    "i feel none of schemes fit me exactly": {

        "message":
            (
                "That happens sometimes — what feels most urgent: "
                "land, rent, ownership, or loan-related stress?"
            ),

        "options": {

            "Land / Construction":
                "fit_blc",

            "Rent":
                "fit_arh",

            "Ownership":
                "fit_ahp",

            "Loan Stress":
                "fit_iss"
        }
    },

    "before applying i just want right scheme for my situation": {

        "message":
            (
                "No problem — are you mainly trying to build, "
                "buy, rent, or reduce housing loan burden?"
            ),

        "options": {

            "Build":
                "rightscheme_blc",

            "Buy":
                "rightscheme_ahp",

            "Rent":
                "rightscheme_arh",

            "Reduce Loan Burden":
                "rightscheme_iss"
        }
    },

    "rejection fear + delay + no answers all together": {

        "message":
            (
                "That sounds stressful. Is the biggest concern "
                "approval delay, rejection worry, or missing status updates?"
            ),

        "options": {

            "Approval Delay":
                "stress_delay",

            "Rejection Worry":
                "stress_rejection",

            "Missing Updates":
                "stress_updates"
        }
    },

    "honestly i dont even know where to start": {

        "message":
            (
                "No problem — what feels like the biggest issue first: "
                "house, documents, money, family, or status?"
            ),

        "options": {

            "House":
                "start_house",

            "Documents":
                "start_documents",

            "Money":
                "start_money",

            "Family":
                "start_family",

            "Status":
                "start_status"
        }
    },
    "i think i messed something up while applying": {

        "message":
            (
                "Possibly manageable. Do you think the issue "
                "is related to documents, details, bank, or "
                "scheme selection?"
            ),

        "options": {

            "Documents":
                "messed_documents",

            "Application Details":
                "messed_details",

            "Bank Information":
                "messed_bank",

            "Scheme Selection":
                "messed_scheme"
        }
    },

    "maybe i shouldnt even apply": {

        "message":
            (
                "That depends — is the hesitation about "
                "eligibility, rejection fear, documents, "
                "or housing situation?"
            ),

        "options": {

            "Eligibility":
                "hesitate_eligibility",

            "Rejection Fear":
                "hesitate_rejection",

            "Documents":
                "hesitate_documents",

            "Housing Situation":
                "hesitate_housing"
        }
    },

    "if i explain my situation people usually get confused": {

        "message":
            (
                "That’s okay — we can go one step at a time. "
                "Is the biggest issue house, family, documents, "
                "or income?"
            ),

        "options": {

            "House":
                "confuse_house",

            "Family":
                "confuse_family",

            "Documents":
                "confuse_documents",

            "Income":
                "confuse_income"
        }
    },

    "feels like every answer creates new confusion": {

        "message":
            (
                "That can happen. What feels most confusing "
                "right now: eligibility, subsidy, documents, "
                "or application status?"
            ),

        "options": {

            "Eligibility":
                "newconfusion_eligibility",

            "Subsidy":
                "newconfusion_subsidy",

            "Documents":
                "newconfusion_documents",

            "Application Status":
                "newconfusion_status"
        }
    },

    "my situation sounds fake when i say it out loud": {

        "message":
            (
                "Unusual situations happen more often than people think. "
                "Is the biggest concern ownership, family, or housing stability?"
            ),

        "options": {

            "Ownership":
                "fakecase_ownership",

            "Family":
                "fakecase_family",

            "Housing Stability":
                "fakecase_housing"
        }
    },

    "no house but still feel ineligible somehow": {

        "message":
            (
                "That uncertainty is understandable. "
                "Do you own any land or have family property-related concerns?"
            ),

        "options": {

            "Own Land":
                "nohouse_land",

            "Family Property":
                "nohouse_family_property",

            "Not Sure":
                "nohouse_unsure"
        }
    },

    "family situation too messy to explain quickly": {

        "message":
            (
                "No problem — is the issue mainly marriage, "
                "separation, inheritance, or dependency?"
            ),

        "options": {

            "Marriage":
                "messyfamily_marriage",

            "Separation":
                "messyfamily_separation",

            "Inheritance":
                "messyfamily_inheritance",

            "Dependency":
                "messyfamily_dependency"
        }
    },

    "i feel embarrassed asking basic questions": {

        "message":
            (
                "No worries — what feels most confusing: "
                "eligibility, subsidy, status, or documents?"
            ),

        "options": {

            "Eligibility":
                "embarrassed_eligibility",

            "Subsidy":
                "embarrassed_subsidy",

            "Application Status":
                "embarrassed_status",

            "Documents":
                "embarrassed_documents"
        }
    },

    "feels like everybody else understands pmay except me": {

        "message":
            (
                "PMAY-U 2.0 can feel confusing at first. "
                "Would it help to start with eligibility, "
                "documents, subsidy, or scheme choice?"
            ),

        "options": {

            "Eligibility":
                "everyone_eligibility",

            "Documents":
                "everyone_documents",

            "Subsidy":
                "everyone_subsidy",

            "Scheme Choice":
                "everyone_scheme"
        }
    },

    "i honestly dont know if i qualify or just desperate": {

        "message":
            (
                "That’s understandable — do you own any house, "
                "live on rent, or have housing instability concerns?"
            ),

        "options": {

            "Own House":
                "desperate_house",

            "Live on Rent":
                "desperate_rent",

            "Housing Instability":
                "desperate_instability"
        }
    },

    "i think im overthinking this maybe": {

        "message":
            (
                "That happens sometimes. What feels like the "
                "main concern: eligibility, money, documents, or delays?"
            ),

        "options": {

            "Eligibility":
                "overthink_eligibility",

            "Money":
                "overthink_money",

            "Documents":
                "overthink_documents",

            "Delays":
                "overthink_delays"
        }
    },

    "honestly just want stable place to live": {

        "message":
            (
                "Housing stability matters. Are you looking for "
                "rental support, ownership, or construction-related help?"
            ),

        "options": {

            "Rental Support":
                "stable_rental",

            "Home Ownership":
                "stable_ownership",

            "Construction Help":
                "stable_construction"
        }
    },
    "before i give up tell me": {

        "message":
            (
                "That depends on your situation — do you own any "
                "house, live on rent, or face housing instability?"
            ),

        "options": {

            "Own House":
                "giveup_house",

            "Live on Rent":
                "giveup_rent",

            "Housing Instability":
                "giveup_instability"
        }
    },

    "honestly should i even try": {

        "message":
            (
                "Before deciding, what feels like the biggest concern: "
                "eligibility, documents, rejection fear, or housing situation?"
            ),

        "options": {

            "Eligibility":
                "shouldtry_eligibility",

            "Documents":
                "shouldtry_documents",

            "Rejection Fear":
                "shouldtry_rejection",

            "Housing Situation":
                "shouldtry_housing"
        }
    },

    "my situation is confusing emotional financial and unstable all at once": {

        "message":
            (
                "That sounds overwhelming. We can go step by step — "
                "what feels biggest first: house, family, money, or documents?"
            ),

        "options": {

            "House":
                "overwhelmed_house",

            "Family":
                "overwhelmed_family",

            "Money":
                "overwhelmed_money",

            "Documents":
                "overwhelmed_documents"
        }
    },

    "i dont understand pmay honestly": {

        "message":
            (
                "No problem — what feels most confusing: "
                "eligibility, documents, subsidy, or scheme choice?"
            ),

        "options": {

            "Eligibility":
                "understand_eligibility",

            "Documents":
                "understand_documents",

            "Subsidy":
                "understand_subsidy",

            "Scheme Choice":
                "understand_scheme"
        }
    },

    "what if i dont know my category": {

        "message":
            (
                "No problem — are you trying to build, buy, rent, "
                "or reduce loan-related housing pressure?"
            ),

        "options": {

            "Build":
                "category_build",

            "Buy":
                "category_buy",

            "Rent":
                "category_rent",

            "Reduce Loan Burden":
                "category_loan"
        }
    },

    "pmay worth trying?": {

        "message":
            (
                "That may depend on your housing situation — do you "
                "own any house or face housing difficulties?"
            ),

        "options": {

            "Own House":
                "worth_house",

            "No House":
                "worth_nohouse",

            "Housing Difficulties":
                "worth_difficulties"
        }
    },

    "honestly feels confusing for normal people": {

        "message":
            (
                "PMAY-U 2.0 can feel confusing initially. "
                "Would it help to start with eligibility, "
                "documents, subsidy, or status?"
            ),

        "options": {

            "Eligibility":
                "normal_eligibility",

            "Documents":
                "normal_documents",

            "Subsidy":
                "normal_subsidy",

            "Application Status":
                "normal_status"
        }
    },
    "before applying just tell me if worth checking": {

        "message":
            (
                "Could you share whether you own any house, "
                "live on rent, or face housing-related difficulty?"
            ),

        "options": {

            "Own House":
                "worthcheck_house",

            "Live on Rent":
                "worthcheck_rent",

            "Housing Difficulty":
                "worthcheck_difficulty"
        }
    },

    "I think three different PMAY rules may conflict in my case": {

        "message":
            (
                "That can happen — is the biggest concern "
                "ownership, income, family, or housing situation?"
            ),

        "options": {

            "Ownership":
                "conflict_ownership",

            "Income":
                "conflict_income",

            "Family":
                "conflict_family",

            "Housing Situation":
                "conflict_housing"
        }
    },

    "Honestly feels like I qualify and disqualify myself at same time": {

        "message":
            (
                "That uncertainty is understandable — is the main "
                "concern house ownership, family, or income-related situation?"
            ),

        "options": {

            "House Ownership":
                "qualify_ownership",

            "Family Situation":
                "qualify_family",

            "Income Situation":
                "qualify_income"
        }
    },

    "honestly portal scares me more than eligibility": {

        "message":
            (
                "That’s understandable — is the biggest issue "
                "login, tracking, status, or technical error?"
            ),

        "options": {

            "Login Problem":
                "portal_login",

            "Application Tracking":
                "portal_tracking",

            "Status Confusion":
                "portal_status",

            "Technical Error":
                "portal_error"
        }
    },

    "no clue if issue is portal or my mistake": {

        "message":
            (
                "That happens — is the biggest issue login, "
                "tracking, document upload, or status visibility?"
            ),

        "options": {

            "Login":
                "mistake_login",

            "Tracking":
                "mistake_tracking",

            "Document Upload":
                "mistake_upload",

            "Status Visibility":
                "mistake_status"
        }
    },
    "honestly technology making pmay harder for me": {

        "message":
            (
                "That’s understandable. What feels hardest right now: "
                "login, tracking, updates, or document upload?"
            ),

        "options": {

            "Login":
                "tech_login",

            "Tracking":
                "tech_tracking",

            "Updates":
                "tech_updates",

            "Document Upload":
                "tech_upload"
        }
    },

    "Honestly paperwork feels more complicated than eligibility": {

        "message":
            (
                "That’s understandable — is the biggest issue "
                "identity mismatch, ownership proof, or address-related confusion?"
            ),

        "options": {

            "Identity Mismatch":
                "paper_identity",

            "Ownership Proof":
                "paper_ownership",

            "Address Confusion":
                "paper_address"
        }
    },

    "Feels like every document tells different story about me": {

        "message":
            (
                "That can feel stressful. Is the biggest issue "
                "name, address, ownership, or family-related mismatch?"
            ),

        "options": {

            "Name Mismatch":
                "docs_name",

            "Address Mismatch":
                "docs_address",

            "Ownership Mismatch":
                "docs_ownership",

            "Family Information":
                "docs_family"
        }
    },

    "dbt sounds confusing honestly": {

        "message":
            (
                "No problem — is the biggest confusion about "
                "bank account, subsidy timing, or payment tracking?"
            ),

        "options": {

            "Bank Account":
                "dbt_bank",

            "Subsidy Timing":
                "dbt_timing",

            "Payment Tracking":
                "dbt_tracking"
        }
    },

    "nobody explained dbt clearly to me": {

        "message":
            (
                "No problem — is the biggest confusion about "
                "where money goes, timing, or bank linking?"
            ),

        "options": {

            "Where Money Goes":
                "dbt_money",

            "Payment Timing":
                "dbt_payment",

            "Bank Linking":
                "dbt_linking"
        }
    },

    "housing loan stressful enough already": {

        "message":
            (
                "That’s understandable — is the biggest concern "
                "EMI, subsidy timing, or approval uncertainty?"
            ),

        "options": {

            "EMI Burden":
                "loan_emi",

            "Subsidy Timing":
                "loan_subsidy",

            "Approval Uncertainty":
                "loan_approval"
        }
    },
    "feels like finance language too complicated": {

        "message":
            (
                "Financial terms can feel confusing initially. "
                "Would it help to start with loan, subsidy, or DBT basics?"
            ),

        "options": {

            "Loan Basics":
                "finance_loan",

            "Subsidy Basics":
                "finance_subsidy",

            "DBT Basics":
                "finance_dbt"
        }
    },

    "all schemes sound useful and impossible together": {

        "message":
            (
                "No problem — are you mainly trying to build, "
                "buy, rent, or reduce loan burden?"
            ),

        "options": {

            "Build":
                "alluseful_blc",

            "Buy":
                "alluseful_ahp",

            "Rent":
                "alluseful_arh",

            "Reduce Loan Burden":
                "alluseful_iss"
        }
    },

    "honestly no clue which scheme actually matches life": {

        "message":
            (
                "No problem — what matters most right now: "
                "rent, ownership, construction, or loan pressure?"
            ),

        "options": {

            "Rental Housing":
                "life_arh",

            "Home Ownership":
                "life_ahp",

            "Construction":
                "life_blc",

            "Loan Pressure":
                "life_iss"
        }
    },

    "feels like my situation half fits every scheme": {

        "message":
            (
                "That can happen — what feels most urgent first: "
                "house, rent, land, or loan-related pressure?"
            ),

        "options": {

            "Need a House":
                "halffit_house",

            "Need Rental Support":
                "halffit_rent",

            "Own Land":
                "halffit_land",

            "Loan Pressure":
                "halffit_loan"
        }
    },

    "before applying just want right path not confusion": {

        "message":
            (
                "No problem — are you mainly trying to build, "
                "buy, rent, or manage housing loan burden?"
            ),

        "options": {

            "Build":
                "rightpath_blc",

            "Buy":
                "rightpath_ahp",

            "Rent":
                "rightpath_arh",

            "Manage Loan Burden":
                "rightpath_iss"
        }
    },

    "honestly dont know whether to wait or complain": {

        "message":
            (
                "That depends — is the biggest concern approval delay, "
                "missing update, or unresolved issue?"
            ),

        "options": {

            "Approval Delay":
                "wait_delay",

            "Missing Update":
                "wait_update",

            "Unresolved Issue":
                "wait_issue"
        }
    },
    "honestly dont know who safe to trust anymore": {

        "message":
            (
                "That’s understandable — is the biggest concern "
                "privacy, fake agents, documents, or approval-related pressure?"
            ),

        "options": {

            "Privacy":
                "trust_privacy",

            "Fake Agents":
                "trust_agents",

            "Documents":
                "trust_documents",

            "Approval Pressure":
                "trust_approval"
        }
    },

    "honestly biggest fear not rejection but fraud": {

        "message":
            (
                "That concern is understandable — is the biggest worry "
                "OTP scams, fake approval, or identity misuse?"
            ),

        "options": {

            "OTP Scams":
                "fraud_otp",

            "Fake Approval":
                "fraud_fakeapproval",

            "Identity Misuse":
                "fraud_identity"
        }
    },

    "everything just feels stuck honestly": {

        "message":
            (
                "That sounds frustrating. Is the biggest issue "
                "status, approval, documents, or money-related delay?"
            ),

        "options": {

            "Application Status":
                "stuck_status",

            "Approval":
                "stuck_approval",

            "Documents":
                "stuck_documents",

            "Money Delay":
                "stuck_money"
        }
    },

    "i dont even know what problem first": {

        "message":
            (
                "No worries — what feels biggest right now: "
                "house, money, documents, family, or application status?"
            ),

        "options": {

            "House":
                "problem_house",

            "Money":
                "problem_money",

            "Documents":
                "problem_documents",

            "Family":
                "problem_family",

            "Application Status":
                "problem_status"
        }
    },

    "maybe i applied wrong maybe not": {

        "message":
            (
                "Possibly manageable. Is the concern about "
                "scheme selection, details, or documents?"
            ),

        "options": {

            "Scheme Selection":
                "wrong_scheme",

            "Application Details":
                "wrong_details",

            "Documents":
                "wrong_documents"
        }
    },

    "nothing making sense anymore with pmay": {

        "message":
            (
                "PMAY-U 2.0 can feel confusing sometimes. "
                "What feels most unclear: eligibility, status, subsidy, or paperwork?"
            ),

        "options": {

            "Eligibility":
                "sense_eligibility",

            "Application Status":
                "sense_status",

            "Subsidy":
                "sense_subsidy",

            "Paperwork":
                "sense_paperwork"
        }
    },
    "i think something messed up but cant explain": {

        "message":
            (
                "That’s okay — does it feel more like documents, "
                "money, approval, or family situation?"
            ),

        "options": {

            "Documents":
                "messedup_documents",

            "Money":
                "messedup_money",

            "Approval":
                "messedup_approval",

            "Family Situation":
                "messedup_family"
        }
    },

    "too much waiting making me angry honestly": {

        "message":
            (
                "Waiting can feel exhausting. Is the biggest concern "
                "approval, status, or missing updates?"
            ),

        "options": {

            "Approval":
                "waiting_approval",

            "Application Status":
                "waiting_status",

            "Missing Updates":
                "waiting_updates"
        }
    },

    "house problem money problem everything problem": {

        "message":
            (
                "That sounds overwhelming. What feels biggest first: "
                "housing, finances, or application-related concern?"
            ),

        "options": {

            "Housing":
                "everything_housing",

            "Finances":
                "everything_finance",

            "Application Concern":
                "everything_application"
        }
    },

    "honestly scared open portal now": {

        "message":
            (
                "That concern is understandable. Is the worry about "
                "status changes, rejection, or technical issues?"
            ),

        "options": {

            "Status Changes":
                "portalfear_status",

            "Rejection":
                "portalfear_rejection",

            "Technical Issues":
                "portalfear_technical"
        }
    },

    "everybody asking documents im tired": {

        "message":
            (
                "Paperwork can feel exhausting. Is the biggest issue "
                "missing papers, mismatch, or repeated requests?"
            ),

        "options": {

            "Missing Papers":
                "tireddocs_missing",

            "Document Mismatch":
                "tireddocs_mismatch",

            "Repeated Requests":
                "tireddocs_repeat"
        }
    },

    "family situation too weird for forms": {

        "message":
            (
                "That happens sometimes — is the biggest issue "
                "marriage, separation, inheritance, or dependency?"
            ),

        "options": {

            "Marriage":
                "weirdfamily_marriage",

            "Separation":
                "weirdfamily_separation",

            "Inheritance":
                "weirdfamily_inheritance",

            "Dependency":
                "weirdfamily_dependency"
        }
    },
    "maybe i should stop trying honestly": {

        "message":
            (
                "That depends — is the biggest concern rejection, "
                "delay, money, or housing instability?"
            ),

        "options": {

            "Rejection":
                "stoptrying_rejection",

            "Delay":
                "stoptrying_delay",

            "Money":
                "stoptrying_money",

            "Housing Instability":
                "stoptrying_housing"
        }
    },

    "i feel lost in this whole thing": {

        "message":
            (
                "That’s understandable. What feels most confusing: "
                "eligibility, documents, money, or approval stage?"
            ),

        "options": {

            "Eligibility":
                "lost_eligibility",

            "Documents":
                "lost_documents",

            "Money":
                "lost_money",

            "Approval Stage":
                "lost_approval"
        }
    },

    "dont know if im scared or confused more": {

        "message":
            (
                "That’s understandable — is the biggest worry fraud, "
                "rejection, money, or eligibility confusion?"
            ),

        "options": {

            "Fraud":
                "scared_fraud",

            "Rejection":
                "scared_rejection",

            "Money":
                "scared_money",

            "Eligibility Confusion":
                "scared_eligibility"
        }
    },

    "just want stable place not stress honestly": {

        "message":
            (
                "Housing stability matters. Are you looking for "
                "rental support, ownership, or construction-related help?"
            ),

        "options": {

            "Rental Support":
                "stability_rental",

            "Home Ownership":
                "stability_ownership",

            "Construction Help":
                "stability_construction"
        }
    },

    "i dont know if i messed up application or life": {

        "message":
            (
                "That sounds overwhelming. Is the biggest concern "
                "application issue or housing-related situation?"
            ),

        "options": {

            "Application Issue":
                "lifemess_application",

            "Housing Situation":
                "lifemess_housing"
        }
    },

    "honestly exhausted repeating same story": {

        "message":
            (
                "That sounds tiring. What feels most unresolved "
                "right now: approval, eligibility, or paperwork?"
            ),

        "options": {

            "Approval":
                "repeat_approval",

            "Eligibility":
                "repeat_eligibility",

            "Paperwork":
                "repeat_paperwork"
        }
    },
    "portal confusing office confusing": {

        "message":
            (
                "That can feel exhausting. Which feels hardest: "
                "portal updates, approval stage, or mixed advice?"
            ),

        "options": {

            "Portal Updates":
                "confusing_portal",

            "Approval Stage":
                "confusing_approval",

            "Mixed Advice":
                "confusing_advice"
        }
    },

    "i think im overcomplicating maybe": {

        "message":
            (
                "That happens sometimes. What feels like the main concern: "
                "housing, documents, money, or approval?"
            ),

        "options": {

            "Housing":
                "overcomplicate_housing",

            "Documents":
                "overcomplicate_documents",

            "Money":
                "overcomplicate_money",

            "Approval":
                "overcomplicate_approval"
        }
    },

    "feels like nobody understands my situation": {

        "message":
            (
                "That can feel isolating. Is the biggest issue "
                "family, ownership, housing, or finances?"
            ),

        "options": {

            "Family":
                "understood_family",

            "Ownership":
                "understood_ownership",

            "Housing":
                "understood_housing",

            "Finances":
                "understood_finances"
        }
    },

    "scared to hope honestly": {

        "message":
            (
                "That feeling is understandable. Is the biggest uncertainty "
                "approval, eligibility, or financial support?"
            ),

        "options": {

            "Approval":
                "hope_approval",

            "Eligibility":
                "hope_eligibility",

            "Financial Support":
                "hope_financial"
        }
    },

    "life messy application messy brain messy honestly": {

        "message":
            (
                "That sounds overwhelming. We can go step by step — "
                "what feels biggest first: house, money, documents, or family situation?"
            ),

        "options": {

            "House":
                "messy_house",

            "Money":
                "messy_money",

            "Documents":
                "messy_documents",

            "Family Situation":
                "messy_family"
        }
    },

    "Honestly not sure who even counts as my family legally": {

        "message":
            (
                "No problem — is the biggest confusion related to "
                "parents, marriage, separation, or dependency?"
            ),

        "options": {

            "Parents":
                "familylegal_parents",

            "Marriage":
                "familylegal_marriage",

            "Separation":
                "familylegal_separation",

            "Dependency":
                "familylegal_dependency"
        }
    },

    "Too many family issues mixed with property confusion": {

        "message":
            (
                "That sounds stressful. Is the biggest concern "
                "inheritance, separation, or ownership-related conflict?"
            ),

        "options": {

            "Inheritance":
                "property_inheritance",

            "Separation":
                "property_separation",

            "Ownership Conflict":
                "property_ownership"
        }
    },

    "Application pending, landlord pressuring me, and family says stop trying": {

        "message":
            (
                "That sounds stressful. Is the biggest concern "
                "approval delay, housing pressure, or family-related stress?"
            ),

        "options": {

            "Approval Delay":
                "pendinglandlord_approval",

            "Housing Pressure":
                "pendinglandlord_housing",

            "Family Stress":
                "pendinglandlord_family"
        }
    },

    "Feels like my case is eligibility plus family drama plus technical problems": {

        "message":
            (
                "That sounds overwhelming. Which feels biggest first: "
                "eligibility, family, or portal-related issue?"
            ),

        "options": {

            "Eligibility":
                "threethings_eligibility",

            "Family":
                "threethings_family",

            "Portal Issue":
                "threethings_portal"
        }
    },

    "Subsidy delay causing loan stress and family arguments": {

        "message":
            (
                "Financial delays can feel stressful. Is the biggest concern "
                "subsidy timing, EMI, or approval stage?"
            ),

        "options": {

            "Subsidy Timing":
                "subsidyloan_timing",

            "EMI Pressure":
                "subsidyloan_emi",

            "Approval Stage":
                "subsidyloan_approval"
        }
    },

    "I think three PMAY rules and two life problems collided in my case": {

        "message":
            (
                "That can happen — is the biggest concern "
                "ownership, housing, family, or finances?"
            ),

        "options": {

            "Ownership":
                "collision_ownership",

            "Housing":
                "collision_housing",

            "Family":
                "collision_family",

            "Finances":
                "collision_finances"
        }
    },

    "Honestly dont know if system slow or my case difficult": {

        "message":
            (
                "That uncertainty is understandable. Is the biggest concern "
                "approval delay, eligibility, or missing updates?"
            ),

        "options": {

            "Approval Delay":
                "systemslow_delay",

            "Eligibility":
                "systemslow_eligibility",

            "Missing Updates":
                "systemslow_updates"
        }
    },

    "Family pressure, rent pressure, and no PMAY clarity together": {

        "message":
            (
                "That sounds overwhelming. What feels biggest first: "
                "housing, family, or application-related stress?"
            ),

        "options": {

            "Housing":
                "pressure_housing",

            "Family":
                "pressure_family",

            "Application Stress":
                "pressure_application"
        }
    },
        
    "Honestly biggest problem is I cant explain situation clearly": {

        "message":
            (
                "That’s okay — we can go step by step. "
                "Is the biggest concern house, money, family, or documents?"
            ),

        "options": {

            "House":
                "cant_explain_house",

            "Money":
                "cant_explain_money",

            "Family":
                "cant_explain_family",

            "Documents":
                "cant_explain_documents"
        }
    },

    "PMAY stress affecting sleep honestly": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "approval delay, money, or eligibility uncertainty?"
            ),

        "options": {

            "Approval Delay":
                "sleep_approval",

            "Money":
                "sleep_money",

            "Eligibility":
                "sleep_eligibility"
        }
    },

    "blc rules feel confusing honestly": {

        "message":
            (
                "That’s understandable — is the biggest confusion about "
                "land, eligibility, or verification?"
            ),

        "options": {

            "Land Requirement":
                "blc_land",

            "Eligibility":
                "blc_eligibility",

            "Verification":
                "blc_verification"
        }
    },

    "honestly dont know if ahp fits me": {

        "message":
            (
                "No problem — are you trying to buy an affordable "
                "housing unit or flat?"
            ),

        "options": {

            "Yes, Looking to Buy":
                "ahp_buy",

            "Not Sure":
                "ahp_unsure"
        }
    },

    "ahp rules feel confusing": {

        "message":
            (
                "That’s understandable — is the biggest confusion about "
                "eligibility, housing purchase, or verification?"
            ),

        "options": {

            "Eligibility":
                "ahp_eligibility",

            "Housing Purchase":
                "ahp_purchase",

            "Verification":
                "ahp_verification"
        }
    },

    "before applying tell me if ahp worth checking": {

        "message":
            (
                "Could you share whether you want an affordable "
                "flat or housing purchase support?"
            ),

        "options": {

            "Affordable Flat":
                "ahp_flat",

            "Housing Purchase Support":
                "ahp_support"
        }
    },
    
    "honestly dont know if arh fits me": {

        "message":
            (
                "No problem — are you looking for temporary affordable "
                "rental housing support under PMAY-U 2.0?"
            ),

        "options": {

            "Yes, Need Rental Housing":
                "arh_rental",

            "Not Sure":
                "arh_unsure"
        }
    },

    "arh rules feel confusing": {

        "message":
            (
                "That’s understandable — is the biggest confusion about "
                "rental housing, eligibility, or verification?"
            ),

        "options": {

            "Rental Housing":
                "arh_housing",

            "Eligibility":
                "arh_eligibility",

            "Verification":
                "arh_verification"
        }
    },

    "honestly dont know if iss fits me": {

        "message":
            (
                "No problem — are you trying to reduce housing "
                "loan-related burden under PMAY-U 2.0?"
            ),

        "options": {

            "Yes, I Have Housing Loan":
                "iss_loan",

            "Not Sure":
                "iss_unsure"
        }
    },

    "iss rules feel confusing": {

        "message":
            (
                "That’s understandable — is the biggest confusion about "
                "loan, eligibility, or verification?"
            ),

        "options": {

            "Loan Benefits":
                "iss_loan_confusion",

            "Eligibility":
                "iss_eligibility",

            "Verification":
                "iss_verification"
        }
    },

    "before applying tell me if iss worth checking": {

        "message":
            (
                "Could you share whether you have a housing loan "
                "or need loan-related housing support?"
            ),

        "options": {

            "Have Housing Loan":
                "iss_have_loan",

            "Need Loan Support":
                "iss_need_support"
        }
    },

    "honestly not sure income fits ahp": {

        "message":
            (
                "No problem — could you share whether your concern "
                "is about income category, eligibility, or scheme selection?"
            ),

        "options": {

            "Income Category":
                "incomefit_category",

            "Eligibility":
                "incomefit_eligibility",

            "Scheme Selection":
                "incomefit_scheme"
        }
    },

    "income confusion before applying ahp": {

        "message":
            (
                "No problem — are you unsure about income eligibility "
                "or verification-related requirements for AHP under PMAY-U 2.0?"
            ),

        "options": {

            "Income Eligibility":
                "ahp_income_eligibility",

            "Verification Requirements":
                "ahp_income_verification"
        }
    },

    "honestly confused about arh income criteria": {

        "message":
            (
                "No problem — is the confusion mainly about income "
                "eligibility, rental housing eligibility, or verification?"
            ),

        "options": {

            "Income Eligibility":
                "arh_income_eligibility",

            "Rental Housing Eligibility":
                "arh_rental_eligibility",

            "Verification":
                "arh_income_verification"
        }
    },

    "before applying arh income okay or not": {

        "message":
            (
                "Could you share whether your main concern is income "
                "eligibility, rental housing need, or verification requirements?"
            ),

        "options": {

            "Income Eligibility":
                "arh_before_income",

            "Rental Housing Need":
                "arh_before_rental",

            "Verification":
                "arh_before_verification"
        }
    },

    "honestly confused if income fits iss": {

        "message":
            (
                "No problem — is the confusion mainly about income "
                "eligibility, housing loan eligibility, or verification?"
            ),

        "options": {

            "Income Eligibility":
                "iss_income_eligibility",

            "Housing Loan Eligibility":
                "iss_loan_eligibility",

            "Verification":
                "iss_income_verification"
        }
    },

    "before applying iss income okay or not": {

        "message":
            (
                "Could you share whether your main concern is income "
                "eligibility, housing loan support, or verification requirements?"
            ),

        "options": {

            "Income Eligibility":
                "iss_before_income",

            "Housing Loan Support":
                "iss_before_loan",

            "Verification":
                "iss_before_verification"
        }
    },

    "honestly portal feels broken": {

        "message":
            (
                "That’s understandable — is the biggest issue tracking, "
                "missing application, or status mismatch?"
            ),

        "options": {

            "Tracking Issue":
                "portal_tracking",

            "Missing Application":
                "portal_missing",

            "Status Mismatch":
                "portal_mismatch"
        }
    },

    "status everywhere different confusing me": {

        "message":
            (
                "Conflicting updates can feel stressful. Which source "
                "are you checking: portal, SMS, or office update?"
            ),

        "options": {

            "Portal":
                "status_portal",

            "SMS":
                "status_sms",

            "Office Update":
                "status_office"
        }
    },

    "portal issue or my mistake no idea": {

        "message":
            (
                "That happens sometimes — is the biggest issue "
                "tracking, status visibility, or login-related?"
            ),

        "options": {

            "Tracking":
                "portalmistake_tracking",

            "Status Visibility":
                "portalmistake_visibility",

            "Login Issue":
                "portalmistake_login"
        }
    },

    "honestly no clue what verification stage means": {

        "message":
            (
                "No problem — what is most confusing about verification: "
                "verification purpose, current status, or next step?"
            ),

        "options": {

            "Verification Purpose":
                "verification_purpose",

            "Current Status":
                "verification_status",

            "Next Step":
                "verification_nextstep"
        }
    },

    "geo tagging confusing me honestly": {

        "message":
            (
                "That’s understandable — are you confused about "
                "status, location verification, or next step?"
            ),

        "options": {

            "Status":
                "geotag_status",

            "Location Verification":
                "geotag_verification",

            "Next Step":
                "geotag_nextstep"
        }
    },

    "feels like status lying honestly": {

        "message":
            (
                "Conflicting or delayed updates can feel confusing. "
                "Which source are you checking: portal, SMS, or office update?"
            ),

        "options": {

            "Portal":
                "lyingstatus_portal",

            "SMS":
                "lyingstatus_sms",

            "Office Update":
                "lyingstatus_office"
        }
    },

    "honestly dont know wait complain or give up": {

        "message":
            (
                "That depends — is the biggest concern delay, "
                "contradictory status, or missing updates?"
            ),

        "options": {

            "Delay":
                "wait_delay",

            "Contradictory Status":
                "wait_status",

            "Missing Updates":
                "wait_updates"
        }
    },

    "pmay status stressing me mentally now": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "approval delay, verification, or unclear updates?"
            ),

        "options": {

            "Approval Delay":
                "stressstatus_delay",

            "Verification":
                "stressstatus_verification",

            "Unclear Updates":
                "stressstatus_updates"
        }
    },

    "family says eligible i feel not eligible": {

        "message":
            (
                "That uncertainty is understandable. Is the biggest concern "
                "house, income, or ownership-related?"
            ),

        "options": {

            "House":
                "familyeligible_house",

            "Income":
                "familyeligible_income",

            "Ownership":
                "familyeligible_ownership"
        }
    },

    "feels eligible emotionally not legally maybe": {

        "message":
            (
                "That uncertainty is understandable. Is the biggest concern "
                "ownership, family, or documentation?"
            ),

        "options": {

            "Ownership":
                "emotioneligible_ownership",

            "Family":
                "emotioneligible_family",

            "Documentation":
                "emotioneligible_documents"
        }
    },

    "honestly feels requirements endless": {

        "message":
            (
                "Requirements can feel overwhelming. What feels hardest: "
                "documents, eligibility, or verification?"
            ),

        "options": {

            "Documents":
                "requirements_documents",

            "Eligibility":
                "requirements_eligibility",

            "Verification":
                "requirements_verification"
        }
    },

    "dont know if my documents enough": {

        "message":
            (
                "No problem — is the biggest concern identity, "
                "address, ownership, or income proof?"
            ),

        "options": {

            "Identity Proof":
                "docenough_identity",

            "Address Proof":
                "docenough_address",

            "Ownership Proof":
                "docenough_ownership",

            "Income Proof":
                "docenough_income"
        }
    },

    "honestly no clue what category i fit": {

        "message":
            (
                "No problem — is the confusion mainly about "
                "income category, eligibility, or scheme selection?"
            ),

        "options": {

            "Income Category":
                "category_income",

            "Eligibility":
                "category_eligibility",

            "Scheme Selection":
                "category_scheme"
        }
    },

    "family income confusing me mentally": {

        "message":
            (
                "Combined income rules can feel confusing. "
                "Is the concern about spouse, parents, or joint family income?"
            ),

        "options": {

            "Spouse Income":
                "familyincome_spouse",

            "Parents Income":
                "familyincome_parents",

            "Joint Family Income":
                "familyincome_joint"
        }
    },

    "dont understand income rules honestly": {

        "message":
            (
                "That’s understandable — is the biggest confusion about "
                "category, proof, or family income?"
            ),

        "options": {

            "Income Category":
                "incomerules_category",

            "Income Proof":
                "incomerules_proof",

            "Family Income":
                "incomerules_family"
        }
    },

    "honestly rules feel hidden sometimes": {

        "message":
            (
                "That’s understandable — is the biggest confusion about "
                "family, ownership, or housing rules?"
            ),

        "options": {

            "Family Rules":
                "hiddenrules_family",

            "Ownership Rules":
                "hiddenrules_ownership",

            "Housing Rules":
                "hiddenrules_housing"
        }
    },

    "dont understand ownership rules at all": {

        "message":
            (
                "No problem — is the concern about land, house, spouse, "
                "or inheritance-related ownership?"
            ),

        "options": {

            "Land Ownership":
                "ownership_land",

            "House Ownership":
                "ownership_house",

            "Spouse Ownership":
                "ownership_spouse",

            "Inheritance":
                "ownership_inheritance"
        }
    },

    "beneficiary validation confusing honestly": {

        "message":
            (
                "That’s understandable — are you confused about "
                "status, meaning, or next step?"
            ),

        "options": {

            "Status":
                "beneficiary_status",

            "Meaning":
                "beneficiary_meaning",

            "Next Step":
                "beneficiary_nextstep"
        }
    },

    "geo tagging sounds scary honestly": {

        "message":
            (
                "That’s understandable — are you worried about "
                "location check or status impact?"
            ),

        "options": {

            "Location Check":
                "geoscary_location",

            "Status Impact":
                "geoscary_status"
        }
    },

    "dont know if approved or still verifying": {

        "message":
            (
                "No problem — could you share what feels most unclear: "
                "status wording, verification stage, or approval stage?"
            ),

        "options": {

            "Status Wording":
                "approved_statusword",

            "Verification Stage":
                "approved_verification",

            "Approval Stage":
                "approved_approval"
        }
    },

    "honestly no clue who approving what": {

        "message":
            (
                "No problem — is the biggest confusion about "
                "ULB, verification, or approval stages?"
            ),

        "options": {

            "ULB":
                "approving_ulb",

            "Verification":
                "approving_verification",

            "Approval Stages":
                "approving_approval"
        }
    },

    "before giving up tell me delayed verification still chance": {

        "message":
            (
                "Verification delays do not automatically mean rejection. "
                "Is your concern delayed verification, missing updates, or approval uncertainty?"
            ),

        "options": {

            "Delayed Verification":
                "chance_verification",

            "Missing Updates":
                "chance_updates",

            "Approval Uncertainty":
                "chance_approval"
        }
    },

    "honestly portal feels emotionally exhausting": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, unclear wording, or missing updates?"
            ),

        "options": {

            "Delay":
                "portalstress_delay",

            "Unclear Wording":
                "portalstress_wording",

            "Missing Updates":
                "portalstress_updates"
        }
    },

    "dont know trust portal or office": {

        "message":
            (
                "Conflicting updates can feel confusing. "
                "Which source feels more inconsistent right now?"
            ),

        "options": {

            "Portal":
                "trustsource_portal",

            "Office":
                "trustsource_office",

            "Both":
                "trustsource_both"
        }
    },

    "honestly cant tell if problem income documents or status": {

        "message":
            (
                "That’s understandable — what feels biggest right now: "
                "income, documents, or tracking-related concern?"
            ),

        "options": {

            "Income":
                "mixedproblem_income",

            "Documents":
                "mixedproblem_documents",

            "Tracking / Status":
                "mixedproblem_status"
        }
    },

    "officer positive portal negative dont know trust": {

        "message":
            (
                "Conflicting updates can feel stressful. Which feels most concerning: "
                "status mismatch or verification delay?"
            ),

        "options": {

            "Status Mismatch":
                "trust_status_mismatch",

            "Verification Delay":
                "trust_verification_delay"
        }
    },

    "status confusing and mentally exhausted honestly": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, rejection fear, or unclear wording?"
            ),

        "options": {

            "Delay":
                "mental_delay",

            "Rejection Fear":
                "mental_rejection",

            "Unclear Wording":
                "mental_wording"
        }
    },

    "feels like application became bigger stress than housing": {

        "message":
            (
                "That sounds overwhelming. Is the biggest concern "
                "status, eligibility, or verification-related stress?"
            ),

        "options": {

            "Status":
                "applicationstress_status",

            "Eligibility":
                "applicationstress_eligibility",

            "Verification":
                "applicationstress_verification"
        }
    },

    "i no understand pmay": {

        "message":
            (
                "No worries — are you confused about house, eligibility, "
                "or application process?"
            ),

        "options": {

            "House":
                "basic_house",

            "Eligibility":
                "basic_eligibility",

            "Application Process":
                "basic_process"
        }
    },

    "pmay i try or waste time": {

        "message":
            (
                "That depends — is the biggest concern house, income, "
                "or eligibility-related?"
            ),

        "options": {

            "House":
                "worth_house",

            "Income":
                "worth_income",

            "Eligibility":
                "worth_eligibility"
        }
    },

    "pmay no understand rule": {

        "message":
            (
                "No worries — is the confusion about house, income, "
                "or family eligibility?"
            ),

        "options": {

            "House":
                "rule_house",

            "Income":
                "rule_income",

            "Family Eligibility":
                "rule_family"
        }
    },

    "pmay many rules scary": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "eligibility, documents, or status?"
            ),

        "options": {

            "Eligibility":
                "scary_eligibility",

            "Documents":
                "scary_documents",

            "Status":
                "scary_status"
        }
    },

    "pmay worth trying maybe": {

        "message":
            (
                "That depends — is the biggest concern "
                "house, income, or eligibility-related?"
            ),

        "options": {

            "House Situation":
                "worthmaybe_house",

            "Income":
                "worthmaybe_income",

            "Eligibility":
                "worthmaybe_eligibility"
        }
    },

    "family saying eligible i thinking no": {

        "message":
            (
                "That uncertainty is understandable. Is the biggest concern "
                "house, ownership, or income-related?"
            ),

        "options": {

            "House Situation":
                "familysays_house",

            "Ownership":
                "familysays_ownership",

            "Income":
                "familysays_income"
        }
    },

    "hidden pmay rule scary honestly": {

        "message":
            (
                "That’s understandable. Is the biggest concern "
                "house, family, or ownership-related rules?"
            ),

        "options": {

            "House Rules":
                "hiddenfear_house",

            "Family Rules":
                "hiddenfear_family",

            "Ownership Rules":
                "hiddenfear_ownership"
        }
    },

    "feel eligible but some hidden problem maybe": {

        "message":
            (
                "That uncertainty is understandable. Is the biggest concern "
                "house, income, or ownership-related?"
            ),

        "options": {

            "House":
                "hiddenproblem_house",

            "Income":
                "hiddenproblem_income",

            "Ownership":
                "hiddenproblem_ownership"
        }
    },

    "i no understand beneficiary family": {

        "message":
            (
                "No worries — is the confusion about "
                "parents, spouse, or living separately?"
            ),

        "options": {

            "Parents":
                "beneficiary_parents",

            "Spouse":
                "beneficiary_spouse",

            "Living Separately":
                "beneficiary_separate"
        }
    },

    "honestly rules too much confusing": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "house, family, or ownership-related rules?"
            ),

        "options": {

            "House Rules":
                "toomanyrules_house",

            "Family Rules":
                "toomanyrules_family",

            "Ownership Rules":
                "toomanyrules_ownership"
        }
    },

    "feel no eligible but family say yes": {

        "message":
            (
                "That uncertainty is understandable. What feels biggest concern: "
                "house, income, or ownership-related?"
            ),

        "options": {

            "House":
                "familyyes_house",

            "Income":
                "familyyes_income",

            "Ownership":
                "familyyes_ownership"
        }
    },

    "too much full form brain confused": {

        "message":
            (
                "That’s understandable — which full form feels confusing: "
                "BLC, AHP, ARH, ISS, or PMAY?"
            ),

        "options": {

            "BLC":
                "fullform_blc",

            "AHP":
                "fullform_ahp",

            "ARH":
                "fullform_arh",

            "ISS":
                "fullform_iss"
        }
    },

    "pmay many scheme confusing": {

        "message":
            (
                "That’s understandable — are you trying to "
                "build, rent, buy, or take housing loan support?"
            ),

        "options": {

            "Build":
                "scheme_build",

            "Rent":
                "scheme_rent",

            "Buy":
                "scheme_buy",

            "Housing Loan":
                "scheme_loan"
        }
    },

    "wife say ahp i think blc": {

        "message":
            (
                "That uncertainty is understandable. Is the housing need "
                "about building or ready housing?"
            ),

        "options": {

            "Building House":
                "wife_blc",

            "Ready Housing":
                "wife_ahp"
        }
    },

    "pmay scheme no understand honestly": {

        "message":
            (
                "No worries — are you confused about "
                "building, renting, buying, or loan support?"
            ),

        "options": {

            "Building":
                "understand_build",

            "Renting":
                "understand_rent",

            "Buying":
                "understand_buy",

            "Loan Support":
                "understand_loan"
        }
    },

    "all scheme head pain honestly": {

        "message":
            (
                "That’s understandable — which feels hardest: "
                "BLC, AHP, ARH, or ISS?"
            ),

        "options": {

            "BLC":
                "headpain_blc",

            "AHP":
                "headpain_ahp",

            "ARH":
                "headpain_arh",

            "ISS":
                "headpain_iss"
        }
    },

    "no clue which vertical mine": {

        "message":
            (
                "No worries — what is your housing need: "
                "build, rent, buy, or loan-related?"
            ),

        "options": {

            "Build":
                "vertical_build",

            "Rent":
                "vertical_rent",

            "Buy":
                "vertical_buy",

            "Loan Related":
                "vertical_loan"
        }
    },

    "no clue blc eligible me or no": {

        "message":
            (
                "No worries — is the biggest concern "
                "land, house, or family-related eligibility?"
            ),

        "options": {

            "Land":
                "blceligible_land",

            "House":
                "blceligible_house",

            "Family Eligibility":
                "blceligible_family"
        }
    },

    "blc paper confusion brain gone": {

        "message":
            (
                "No worries — is the biggest concern "
                "land paper, Aadhaar, or income proof?"
            ),

        "options": {

            "Land Paper":
                "blcpaper_land",

            "Aadhaar":
                "blcpaper_aadhaar",

            "Income Proof":
                "blcpaper_income"
        }
    },

    "honestly blc rules head pain": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "land, family, or ownership-related rule?"
            ),

        "options": {

            "Land Rules":
                "blcrules_land",

            "Family Rules":
                "blcrules_family",

            "Ownership Rules":
                "blcrules_ownership"
        }
    },

    "honestly blc process brain tired": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "status, delay, or verification-related?"
            ),

        "options": {

            "Status":
                "blcprocess_status",

            "Delay":
                "blcprocess_delay",

            "Verification":
                "blcprocess_verification"
        }
    },

    "no clue blc status what meaning": {

        "message":
            (
                "No worries — what is most confusing about the status: "
                "status meaning, current stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "blcstatus_meaning",

            "Current Stage":
                "blcstatus_stage",

            "Next Step":
                "blcstatus_next"
        }
    },

    "no clue ahp eligible me or no": {

        "message":
            (
                "No worries — is the biggest concern "
                "house, family, or ownership-related eligibility?"
            ),

        "options": {

            "House":
                "ahpeligible_house",

            "Family":
                "ahpeligible_family",

            "Ownership":
                "ahpeligible_ownership"
        }
    },

    "feel eligible but hidden problem maybe": {

        "message":
            (
                "That uncertainty is understandable. Is the biggest concern "
                "house, family, or ownership-related?"
            ),

        "options": {

            "House":
                "hiddenahp_house",

            "Family":
                "hiddenahp_family",

            "Ownership":
                "hiddenahp_ownership"
        }
    },

    "honestly ahp eligibility head pain": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "house, ownership, or family-related eligibility?"
            ),

        "options": {

            "House":
                "ahppain_house",

            "Ownership":
                "ahppain_ownership",

            "Family Eligibility":
                "ahppain_family"
        }
    },

    "ahp paper confusion brain tired": {

        "message":
            (
                "No worries — is the biggest concern "
                "Aadhaar, income proof, or address-related document?"
            ),

        "options": {

            "Aadhaar":
                "ahppaper_aadhaar",

            "Income Proof":
                "ahppaper_income",

            "Address Document":
                "ahppaper_address"
        }
    },

    "honestly ahp verification scary": {

        "message":
            (
                "That’s understandable — are you worried about "
                "documents, officer checks, or approval delay?"
            ),

        "options": {

            "Documents":
                "ahpverify_documents",

            "Officer Checks":
                "ahpverify_officer",

            "Approval Delay":
                "ahpverify_delay"
        }
    },

    "beneficiary family no understand ahp": {

        "message":
            (
                "No worries — is the confusion about "
                "parents, spouse, or separate living situation?"
            ),

        "options": {

            "Parents":
                "ahpfamily_parents",

            "Spouse":
                "ahpfamily_spouse",

            "Separate Living":
                "ahpfamily_separate"
        }
    },

    "honestly ahp rules head pain": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "family, ownership, or housing-related rule?"
            ),

        "options": {

            "Family Rules":
                "ahprules_family",

            "Ownership Rules":
                "ahprules_ownership",

            "Housing Rules":
                "ahprules_housing"
        }
    },

    "honestly ahp process brain tired": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "status, delay, or verification-related?"
            ),

        "options": {

            "Status":
                "ahpprocess_status",

            "Delay":
                "ahpprocess_delay",

            "Verification":
                "ahpprocess_verification"
        }
    },

    "no clue ahp status what meaning": {

        "message":
            (
                "No worries — what is most confusing about the status: "
                "status meaning, current stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "ahpstatus_meaning",

            "Current Stage":
                "ahpstatus_stage",

            "Next Step":
                "ahpstatus_next"
        }
    },

    "wife want ahp me confused": {

        "message":
            (
                "No worries — is the biggest concern "
                "eligibility, house, or ownership-related?"
            ),

        "options": {

            "Eligibility":
                "wifeahp_eligibility",

            "House":
                "wifeahp_house",

            "Ownership":
                "wifeahp_ownership"
        }
    },

    "honestly ahp making mental stress": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, eligibility, or family-related confusion?"
            ),

        "options": {

            "Delay":
                "ahpstress_delay",

            "Eligibility":
                "ahpstress_eligibility",

            "Family Confusion":
                "ahpstress_family"
        }
    },

    "family say eligible my mind say no": {

        "message":
            (
                "That uncertainty is understandable. What feels biggest concern: "
                "house, income, or ownership-related?"
            ),

        "options": {

            "House":
                "mindno_house",

            "Income":
                "mindno_income",

            "Ownership":
                "mindno_ownership"
        }
    },

    "honestly no clue if ahp for me": {

        "message":
            (
                "No worries — is the biggest concern "
                "house, income, or ownership-related eligibility?"
            ),

        "options": {

            "House":
                "ahpforme_house",

            "Income":
                "ahpforme_income",

            "Ownership":
                "ahpforme_ownership"
        }
    },

    "i no understand arh eligible me or no": {

        "message":
            (
                "No worries — is your biggest concern about "
                "rent house, worker situation, or family-related housing?"
            ),

        "options": {

            "Rental Housing":
                "arheligible_rent",

            "Worker Situation":
                "arheligible_worker",

            "Family Housing":
                "arheligible_family"
        }
    },

    "honestly arh rules brain confused": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "rent rule, worker situation, or eligibility-related confusion?"
            ),

        "options": {

            "Rental Rules":
                "arhrules_rent",

            "Worker Situation":
                "arhrules_worker",

            "Eligibility":
                "arhrules_eligibility"
        }
    },

    "honestly arh paper brain tired": {

        "message":
            (
                "No worries — is the biggest concern "
                "Aadhaar, rental proof, or address-related document?"
            ),

        "options": {

            "Aadhaar":
                "arhpaper_aadhaar",

            "Rental Proof":
                "arhpaper_rentproof",

            "Address Document":
                "arhpaper_address"
        }
    },

    "honestly income confusing arh": {

        "message":
            (
                "No worries — could you share whether the confusion is about "
                "income eligibility, income proof, or rental situation?"
            ),

        "options": {

            "Income Eligibility":
                "arhincome_eligibility",

            "Income Proof":
                "arhincome_proof",

            "Rental Situation":
                "arhincome_rent"
        }
    },

    "no clue family income count arh": {

        "message":
            (
                "No worries — is the concern about "
                "spouse income, parents, or joint household income?"
            ),

        "options": {

            "Spouse Income":
                "arhfamilyincome_spouse",

            "Parents":
                "arhfamilyincome_parents",

            "Joint Household Income":
                "arhfamilyincome_joint"
        }
    },

    "honestly salary no fixed brain stress arh": {

        "message":
            (
                "That sounds stressful. Is the biggest concern "
                "unstable income, rental proof, or eligibility-related confusion?"
            ),

        "options": {

            "Unstable Income":
                "arhsalary_unstable",

            "Rental Proof":
                "arhsalary_rentproof",

            "Eligibility":
                "arhsalary_eligibility"
        }
    },

    "beneficiary family no understand arh": {

        "message":
            (
                "No worries — is the confusion about "
                "parents, spouse, or separate living situation?"
            ),

        "options": {

            "Parents":
                "arhfamily_parents",

            "Spouse":
                "arhfamily_spouse",

            "Separate Living":
                "arhfamily_separate"
        }
    },

    "honestly arh rules head pain": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "rent rule, family condition, or ownership-related confusion?"
            ),

        "options": {

            "Rental Rules":
                "arhheadpain_rent",

            "Family Condition":
                "arhheadpain_family",

            "Ownership Confusion":
                "arhheadpain_ownership"
        }
    },

    "honestly arh process brain tired": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, tracking, or approval-related confusion?"
            ),

        "options": {

            "Delay":
                "arhprocess_delay",

            "Tracking":
                "arhprocess_tracking",

            "Approval":
                "arhprocess_approval"
        }
    },

    "no clue arh status what meaning": {

        "message":
            (
                "No worries — what is most confusing about the status: "
                "status meaning, current stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "arhstatus_meaning",

            "Current Stage":
                "arhstatus_stage",

            "Next Step":
                "arhstatus_next"
        }
    },

    "honestly no clue arh for me": {

        "message":
            (
                "No worries — is the biggest concern about "
                "rent situation, worker condition, or family-related housing?"
            ),

        "options": {

            "Rent Situation":
                "arhforme_rent",

            "Worker Condition":
                "arhforme_worker",

            "Family Housing":
                "arhforme_family"
        }
    },

    "honestly arh making too stress": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "rent issue, delay, or eligibility-related confusion?"
            ),

        "options": {

            "Rent Issue":
                "arhstress_rent",

            "Delay":
                "arhstress_delay",

            "Eligibility":
                "arhstress_eligibility"
        }
    },

    "family say eligible my brain say no arh": {

        "message":
            (
                "That uncertainty is understandable. What feels biggest concern: "
                "rent situation, family issue, or ownership-related confusion?"
            ),

        "options": {

            "Rent Situation":
                "arhmindno_rent",

            "Family Issue":
                "arhmindno_family",

            "Ownership":
                "arhmindno_ownership"
        }
    },

    "honestly no idea if arh right for me": {

        "message":
            (
                "No worries — what feels most unclear about your situation: "
                "rent situation, work/living condition, or housing need?"
            ),

        "options": {

            "Rent Situation":
                "arhright_rent",

            "Work/Living Condition":
                "arhright_worker",

            "Housing Need":
                "arhright_housing"
        }
    },

    "no clue iss eligible me or no": {

        "message":
            (
                "No worries — is the biggest concern about "
                "loan, house ownership, or family-related property?"
            ),

        "options": {

            "Housing Loan":
                "isseligible_loan",

            "House Ownership":
                "isseligible_house",

            "Family Property":
                "isseligible_family"
        }
    },

    "honestly iss brain confused": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "loan, ownership, or eligibility-related confusion?"
            ),

        "options": {

            "Loan":
                "issconfused_loan",

            "Ownership":
                "issconfused_ownership",

            "Eligibility":
                "issconfused_eligibility"
        }
    },

    "honestly iss paper brain tired": {

        "message":
            (
                "No worries — is the biggest concern "
                "loan paper, Aadhaar, or bank-related document?"
            ),

        "options": {

            "Loan Documents":
                "isspaper_loan",

            "Aadhaar":
                "isspaper_aadhaar",

            "Bank Documents":
                "isspaper_bank"
        }
    },

    "honestly bank process scary iss": {

        "message":
            (
                "That sounds stressful. Is the biggest concern "
                "loan verification, subsidy delay, or document-related issue?"
            ),

        "options": {

            "Loan Verification":
                "issbank_verify",

            "Subsidy Delay":
                "issbank_subsidy",

            "Documents":
                "issbank_documents"
        }
    },

    "no clue family income count iss": {

        "message":
            (
                "No worries — is the concern about "
                "spouse income, parents, or joint household income?"
            ),

        "options": {

            "Spouse Income":
                "issincome_spouse",

            "Parents":
                "issincome_parents",

            "Joint Household Income":
                "issincome_joint"
        }
    },

    "beneficiary family no understand iss": {

        "message":
            (
                "No worries — is the confusion about "
                "parents, spouse, or separate living situation?"
            ),

        "options": {

            "Parents":
                "issfamily_parents",

            "Spouse":
                "issfamily_spouse",

            "Separate Living":
                "issfamily_separate"
        }
    },

    "honestly iss rules head pain": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "loan rule, ownership, or family-related confusion?"
            ),

        "options": {

            "Loan Rules":
                "issrules_loan",

            "Ownership":
                "issrules_ownership",

            "Family Situation":
                "issrules_family"
        }
    },

    "honestly iss process brain tired": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "subsidy, bank process, or status-related confusion?"
            ),

        "options": {

            "Subsidy":
                "issprocess_subsidy",

            "Bank Process":
                "issprocess_bank",

            "Status":
                "issprocess_status"
        }
    },

    "wife saying apply iss me confused": {

        "message":
            (
                "No worries — is the biggest concern about "
                "loan, ownership, or subsidy-related eligibility?"
            ),

        "options": {

            "Loan":
                "isswife_loan",

            "Ownership":
                "isswife_ownership",

            "Subsidy Eligibility":
                "isswife_subsidy"
        }
    },

    "honestly iss making mental stress": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "loan, subsidy, or rejection-related fear?"
            ),

        "options": {

            "Loan":
                "issstress_loan",

            "Subsidy":
                "issstress_subsidy",

            "Rejection Fear":
                "issstress_rejection"
        }
    },

    "honestly no clue if iss for me": {

        "message":
            (
                "No worries — is the biggest concern about "
                "loan, income, or house ownership-related eligibility?"
            ),

        "options": {

            "Housing Loan":
                "issforme_loan",

            "Income":
                "issforme_income",

            "House Ownership":
                "issforme_ownership"
        }
    },

    "honestly everything confusing in iss": {

        "message":
            (
                "That’s understandable. What feels hardest right now: "
                "loan, subsidy, bank process, or eligibility-related confusion?"
            ),

        "options": {

            "Loan":
                "isseverything_loan",

            "Subsidy":
                "isseverything_subsidy",

            "Bank Process":
                "isseverything_bank",

            "Eligibility":
                "isseverything_eligibility"
        }
    },

    "honestly income confusion pmay": {

        "message":
            (
                "No worries — is the income confusion mainly about "
                "income category, income proof, or family income calculation?"
            ),

        "options": {

            "Income Category":
                "pmayincome_category",

            "Income Proof":
                "pmayincome_proof",

            "Family Income":
                "pmayincome_family"
        }
    },

    "honestly income confusion blc": {

        "message":
            (
                "No worries — is the income confusion mainly about "
                "income category, income proof, or self-employed income?"
            ),

        "options": {

            "Income Category":
                "blcincome_category",

            "Income Proof":
                "blcincome_proof",

            "Self-Employed Income":
                "blcincome_self"
        }
    },

    "honestly income confusion ahp": {

        "message":
            (
                "No worries — is the income confusion mainly about "
                "income category, income proof, or family income calculation?"
            ),

        "options": {

            "Income Category":
                "ahpincome_category",

            "Income Proof":
                "ahpincome_proof",

            "Family Income":
                "ahpincome_family"
        }
    },

    "honestly income confusion arh": {

        "message":
            (
                "No worries — is the income confusion mainly about "
                "income category, rental situation, or family income?"
            ),

        "options": {

            "Income Category":
                "arhincome_category",

            "Rental Situation":
                "arhincome_rentalsituation",

            "Family Income":
                "arhincome_family"
        }
    },

    "honestly income confusion iss": {

        "message":
            (
                "No worries — is the income confusion mainly about "
                "income category, loan eligibility, or family income?"
            ),

        "options": {

            "Income Category":
                "issincome_category",

            "Loan Eligibility":
                "issincome_loan",

            "Family Income":
                "issincome_family"
        }
    },

    "honestly no clue pmay for woman": {

        "message":
            (
                "No worries — is the biggest concern "
                "income, ownership, or family-related eligibility?"
            ),

        "options": {

            "Income":
                "woman_income",

            "Ownership":
                "woman_ownership",

            "Family Eligibility":
                "woman_family"
        }
    },

    "honestly paper confusion woman pmay": {

        "message":
            (
                "No worries — is the biggest concern "
                "identity proof, family document, or income-related proof?"
            ),

        "options": {

            "Identity Proof":
                "womanpaper_identity",

            "Family Document":
                "womanpaper_family",

            "Income Proof":
                "womanpaper_income"
        }
    },

    "honestly verification scary pmay": {

        "message":
            (
                "That concern is understandable. Is the biggest worry "
                "documents, officer check, or approval-related delay?"
            ),

        "options": {

            "Documents":
                "womanverify_documents",

            "Officer Check":
                "womanverify_officer",

            "Approval Delay":
                "womanverify_delay"
        }
    },

    "honestly income confusing woman pmay": {

        "message":
            (
                "No worries — is the income confusion mainly about "
                "income category, income proof, or family income calculation?"
            ),

        "options": {

            "Income Category":
                "womanincome_category",

            "Income Proof":
                "womanincome_proof",

            "Family Income":
                "womanincome_family"
        }
    },

    "honestly pmay rules confusing widow": {

        "message":
            (
                "That’s understandable — what feels hardest: "
                "ownership, family-related rule, or vulnerable-category confusion?"
            ),

        "options": {

            "Ownership":
                "widowrules_ownership",

            "Family Rules":
                "widowrules_family",

            "Category Benefits":
                "widowrules_category"
        }
    },

    "honestly process brain tired pmay widow": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, verification, or approval-related confusion?"
            ),

        "options": {

            "Delay":
                "widowprocess_delay",

            "Verification":
                "widowprocess_verification",

            "Approval":
                "widowprocess_approval"
        }
    },

    "senior citizen no clue status meaning": {

        "message":
            (
                "No worries — what is most confusing about the status: "
                "status meaning, current stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "seniorstatus_meaning",

            "Current Stage":
                "seniorstatus_stage",

            "Next Step":
                "seniorstatus_next"
        }
    },

    "honestly officer check scary pmay": {

        "message":
            (
                "That feeling is understandable. Is the biggest concern "
                "documents, verification, or approval-related issue?"
            ),

        "options": {

            "Documents":
                "officercheck_documents",

            "Verification":
                "officercheck_verification",

            "Approval Issue":
                "officercheck_approval"
        }
    },

    "honestly life difficult pmay confusion": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "income, house, or family-related eligibility?"
            ),

        "options": {

            "Income":
                "lifedifficult_income",

            "Housing":
                "lifedifficult_housing",

            "Family Situation":
                "lifedifficult_family"
        }
    },

    "honestly pmay making mental stress": {

        "message":
            (
                "That sounds overwhelming. Is the biggest concern "
                "documents, income, or approval-related confusion?"
            ),

        "options": {

            "Documents":
                "mentalstress_documents",

            "Income":
                "mentalstress_income",

            "Approval Confusion":
                "mentalstress_approval"
        }
    },

    "honestly login making stress pmay": {

        "message":
            (
                "That sounds frustrating. Is the biggest concern "
                "OTP, password, or account-related access?"
            ),

        "options": {

            "OTP":
                "loginstress_otp",

            "Password":
                "loginstress_password",

            "Account Access":
                "loginstress_account"
        }
    },

    "honestly portal no work brain tired": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "login, OTP, or password-related issue?"
            ),

        "options": {

            "Login":
                "portalnotwork_login",

            "OTP":
                "portalnotwork_otp",

            "Password":
                "portalnotwork_password"
        }
    },

    "honestly website making stress pmay": {

        "message":
            (
                "That sounds frustrating. Is the biggest concern "
                "upload, captcha, or website-related error?"
            ),

        "options": {

            "Upload Issue":
                "website_upload",

            "Captcha Issue":
                "website_captcha",

            "Website Error":
                "website_error"
        }
    },

    "honestly no clue portal problem pmay": {

        "message":
            (
                "No worries — is the biggest concern "
                "website opening, upload, or captcha-related issue?"
            ),

        "options": {

            "Website Opening":
                "portalproblem_opening",

            "Upload":
                "portalproblem_upload",

            "Captcha":
                "portalproblem_captcha"
        }
    },

    "honestly portal confusing pmay": {

        "message":
            (
                "That sounds frustrating. Is the biggest concern "
                "tracking, wrong details, or missing application-related issue?"
            ),

        "options": {

            "Tracking":
                "portalconfusing_tracking",

            "Wrong Details":
                "portalconfusing_details",

            "Missing Application":
                "portalconfusing_missing"
        }
    },

    "honestly portal making headache pmay": {

        "message":
            (
                "That sounds frustrating. Is the biggest concern "
                "login, status, or technical-related issue?"
            ),

        "options": {

            "Login":
                "portalheadache_login",

            "Status":
                "portalheadache_status",

            "Technical Issue":
                "portalheadache_technical"
        }
    },

    "honestly mental stress because pmay portal": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "login, tracking, or technical-related failure?"
            ),

        "options": {

            "Login":
                "portalstress_login",

            "Tracking":
                "portalstress_tracking",

            "Technical Failure":
                "portalstress_technical"
        }
    },

    "honestly status confusing pmay": {

        "message":
            (
                "No worries — what is most confusing about the status: "
                "status meaning, current stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "statusconfusion_meaning",

            "Current Stage":
                "statusconfusion_stage",

            "Next Step":
                "statusconfusion_next"
        }
    },

    "honestly brain tired checking pmay": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, status wording, or tracking-related confusion?"
            ),

        "options": {

            "Delay":
                "checkingtired_delay",

            "Status Wording":
                "checkingtired_wording",

            "Tracking":
                "checkingtired_tracking"
        }
    },

    "honestly tracking stress pmay": {

        "message":
            (
                "That sounds frustrating. Is the biggest concern "
                "missing status, tracking issue, or delay-related confusion?"
            ),

        "options": {

            "Missing Status":
                "trackingstress_missing",

            "Tracking Issue":
                "trackingstress_issue",

            "Delay":
                "trackingstress_delay"
        }
    },

    "honestly status no understand pmay": {

        "message":
            (
                "No worries — what is most confusing about the status: "
                "status meaning, current stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "statusunderstand_meaning",

            "Current Stage":
                "statusunderstand_stage",

            "Next Step":
                "statusunderstand_next"
        }
    },

    "honestly brain tired checking pmay": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, rejection fear, or status-related confusion?"
            ),

        "options": {

            "Delay":
                "braintired_delay",

            "Rejection Fear":
                "braintired_rejection",

            "Status Confusion":
                "braintired_status"
        }
    },

    "honestly frustrated pmay no update": {

        "message":
            (
                "That sounds frustrating. Is the biggest concern "
                "delay, no response, or status-related confusion?"
            ),

        "options": {

            "Delay":
                "noupdate_delay",

            "No Response":
                "noupdate_response",

            "Status Confusion":
                "noupdate_status"
        }
    },

    "no clue complaint process pmay": {

        "message":
            (
                "No worries — is the biggest concern "
                "delay, officer issue, or no update-related frustration?"
            ),

        "options": {

            "Delay":
                "complaint_delay",

            "Officer Issue":
                "complaint_officer",

            "No Update":
                "complaint_noupdate"
        }
    },

    "honestly angry pmay delay": {

        "message":
            (
                "Frustration after long delays is understandable. "
                "Is the biggest concern status, officer, or no update-related issue?"
            ),

        "options": {

            "Status":
                "angrydelay_status",

            "Officer":
                "angrydelay_officer",

            "No Updates":
                "angrydelay_updates"
        }
    },

    "honestly angry officer pmay": {

        "message":
            (
                "Frustration after repeated issues is understandable. "
                "Is the biggest concern delay, rejection, or communication-related issue?"
            ),

        "options": {

            "Delay":
                "angryofficer_delay",

            "Rejection":
                "angryofficer_rejection",

            "Communication":
                "angryofficer_communication"
        }
    },

    "honestly tired office going pmay": {

        "message":
            (
                "That sounds exhausting. Is the biggest concern "
                "delay, approval, or no update-related frustration?"
            ),

        "options": {

            "Delay":
                "officefatigue_delay",

            "Approval":
                "officefatigue_approval",

            "No Updates":
                "officefatigue_noupdate"
        }
    },

    "honestly angry no subsidy pmay": {

        "message":
            (
                "Frustration after long waiting is understandable. "
                "Is the biggest concern delay, approval, or subsidy-related issue?"
            ),

        "options": {

            "Delay":
                "nosubsidy_delay",

            "Approval":
                "nosubsidy_approval",

            "Subsidy Issue":
                "nosubsidy_issue"
        }
    },

    "honestly helpless pmay": {

        "message":
            (
                "Feeling helpless after delays is understandable. "
                "Is the biggest concern status, complaint, or approval-related issue?"
            ),

        "options": {

            "Status":
                "helpless_status",

            "Complaint":
                "helpless_complaint",

            "Approval":
                "helpless_approval"
        }
    },

    "honestly crying because pmay delay": {

        "message":
            (
                "Long delays can feel emotionally exhausting. "
                "Is the biggest concern delay, complaint, or no update-related issue?"
            ),

        "options": {

            "Delay":
                "crying_delay",

            "Complaint":
                "crying_complaint",

            "No Updates":
                "crying_noupdate"
        }
    },

    "honestly confused subsidy pmay": {

        "message":
            (
                "No worries — is the biggest concern "
                "amount, delay, or no money-related issue?"
            ),

        "options": {

            "Subsidy Amount":
                "subsidyconfused_amount",

            "Delay":
                "subsidyconfused_delay",

            "No Money Received":
                "subsidyconfused_nomoney"
        }
    },

    "subsidy status no understanding pmay": {

        "message":
            (
                "No worries — what is most confusing about the subsidy status: "
                "status meaning, current stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "subsidystatus_meaning",

            "Current Stage":
                "subsidystatus_stage",

            "Next Step":
                "subsidystatus_next"
        }
    },

    "honestly angry subsidy delay pmay": {

        "message":
            (
                "Frustration after financial delays is understandable. "
                "Is the biggest concern amount, delay, or no money-related issue?"
            ),

        "options": {

            "Amount":
                "angrysubsidy_amount",

            "Delay":
                "angrysubsidy_delay",

            "No Money Received":
                "angrysubsidy_nomoney"
        }
    },

    "honestly money stress pmay loan": {

        "message":
            (
                "Financial pressure can feel overwhelming. Is the biggest concern "
                "loan, EMI, or bank-related issue?"
            ),

        "options": {

            "Loan":
                "moneystress_loan",

            "EMI":
                "moneystress_emi",

            "Bank Issue":
                "moneystress_bank"
        }
    },

    "dbt status no understanding pmay": {

        "message":
            (
                "No worries — what is most confusing about the DBT status: "
                "status meaning, money credit stage, or next step?"
            ),

        "options": {

            "Status Meaning":
                "dbtstatus_meaning",

            "Money Credit Stage":
                "dbtstatus_credit",

            "Next Step":
                "dbtstatus_next"
        }
    },

    "honestly no clue dbt pmay": {

        "message":
            (
                "No worries — is the biggest concern "
                "money credit, Aadhaar link, or bank-related issue?"
            ),

        "options": {

            "Money Credit":
                "dbtconfused_credit",

            "Aadhaar Link":
                "dbtconfused_aadhaar",

            "Bank Issue":
                "dbtconfused_bank"
        }
    },

    "honestly mentally tired money pmay": {

        "message":
            (
                "Financial uncertainty can feel exhausting. Is the biggest concern "
                "subsidy, EMI, or bank-related issue?"
            ),

        "options": {

            "Subsidy":
                "moneytired_subsidy",

            "EMI":
                "moneytired_emi",

            "Bank Issue":
                "moneytired_bank"
        }
    },

    "honestly crying money problem pmay": {

        "message":
            (
                "Financial pressure can feel emotionally exhausting. "
                "Is the biggest concern loan, subsidy, or bank-related issue?"
            ),

        "options": {

            "Loan":
                "moneycry_loan",

            "Subsidy":
                "moneycry_subsidy",

            "Bank Issue":
                "moneycry_bank"
        }
    },

    "honestly scared share aadhaar pmay": {

        "message":
            (
                "Sharing identity-related details can feel stressful. "
                "Is the biggest concern Aadhaar, OTP, or bank-related safety?"
            ),

        "options": {

            "Aadhaar Safety":
                "aadhaarsafety_aadhaar",

            "OTP Safety":
                "aadhaarsafety_otp",

            "Bank Safety":
                "aadhaarsafety_bank"
        }
    },

    "honestly scared personal info pmay": {

        "message":
            (
                "Concern about personal information is understandable. "
                "Is the biggest concern Aadhaar, mobile, or bank-related privacy?"
            ),

        "options": {

            "Aadhaar Privacy":
                "privacy_aadhaar",

            "Mobile Privacy":
                "privacy_mobile",

            "Bank Privacy":
                "privacy_bank"
        }
    },

    "honestly scared scam pmay": {

        "message":
            (
                "Scam-related fear is understandable. Is the biggest concern "
                "call, money, or OTP-related issue?"
            ),

        "options": {

            "Suspicious Call":
                "scam_call",

            "Money Concern":
                "scam_money",

            "OTP Concern":
                "scam_otp"
        }
    },

    "honestly fear cheated pmay": {

        "message":
            (
                "Feeling worried about fraud-related concern is understandable. "
                "Is the biggest concern money, call, or personal detail-related issue?"
            ),

        "options": {

            "Money":
                "cheated_money",

            "Call":
                "cheated_call",

            "Personal Details":
                "cheated_details"
        }
    },

    "honestly confused real fake pmay": {

        "message":
            (
                "No worries — is the biggest concern "
                "call, message, or money-related communication?"
            ),

        "options": {

            "Call":
                "realfake_call",

            "Message":
                "realfake_message",

            "Money Request":
                "realfake_money"
        }
    },

    "honestly scared hacked pmay": {

        "message":
            (
                "Security-related fear is understandable. "
                "Is the biggest concern login, OTP, or account-related change?"
            ),

        "options": {

            "Login":
                "hacked_login",

            "OTP":
                "hacked_otp",

            "Account Changes":
                "hacked_account"
        }
    },

    "honestly panic account pmay": {

        "message":
            (
                "Security-related confusion can feel overwhelming. "
                "Is the biggest concern login, OTP, or changed details-related issue?"
            ),

        "options": {

            "Login":
                "panicaccount_login",

            "OTP":
                "panicaccount_otp",

            "Changed Details":
                "panicaccount_details"
        }
    },

    "honestly panic money issue pmay": {

        "message":
            (
                "Financial uncertainty can feel overwhelming. "
                "Is the biggest concern money, bank, or subsidy-related issue?"
            ),

        "options": {

            "Money":
                "panicmoney_money",

            "Bank":
                "panicmoney_bank",

            "Subsidy":
                "panicmoney_subsidy"
        }
    },

    "honestly crying money fear pmay": {

        "message":
            (
                "Financial uncertainty can feel emotionally exhausting. "
                "Is the biggest concern money, bank, or suspicious activity-related issue?"
            ),

        "options": {

            "Money Concern":
                "moneyfear_money",

            "Bank Concern":
                "moneyfear_bank",

            "Suspicious Activity":
                "moneyfear_suspicious"
        }
    },

    "honestly no clue house owner pmay": {

        "message":
            (
                "No worries — is the biggest concern "
                "family ownership, inherited property, or separation-related issue?"
            ),

        "options": {

            "Family Ownership":
                "houseowner_family",

            "Inherited Property":
                "houseowner_inheritance",

            "Separation Related":
                "houseowner_separation"
        }
    },

    "honestly family house stress pmay": {

        "message":
            (
                "Family-related ownership confusion can feel overwhelming. "
                "Is the biggest concern father, sibling, or inherited property-related issue?"
            ),

        "options": {

            "Father's Property":
                "familyhouse_father",

            "Sibling Property":
                "familyhouse_sibling",

            "Inherited Property":
                "familyhouse_inheritance"
        }
    },
    "bank": {

        "message":
            (
                "Are you asking about bank account requirement, subsidy transfer, "
                "account mismatch, or inactive account issue?"
            ),

        "options": {

            "Bank Account Requirement":
                "bank_requirement",

            "Subsidy Transfer":
                "bank_subsidy",

            "Account Mismatch":
                "bank_mismatch",

            "Inactive Account":
                "bank_inactive"
        }
    },

    "family": {

        "message":
            (
                "Are you asking about family eligibility, separate family rules, "
                "spouse ownership, or inherited property?"
            ),

        "options": {

            "Family Eligibility":
                "family_eligibility",

            "Separate Family Rules":
                "family_separate",

            "Spouse Ownership":
                "family_spouse",

            "Inherited Property":
                "family_inherited"
        }
    },

    "income": {

        "message":
            (
                "Are you asking about income eligibility, income proof, "
                "category confusion, or changing income situation?"
            ),

        "options": {

            "Income Eligibility":
                "income_eligibility",

            "Income Proof":
                "income_proof",

            "Category Confusion":
                "income_category",

            "Changing Income":
                "income_change"
        }
    },

    "subsidy loan": {

        "message":
            (
                "Are you asking about loan subsidy under ISS or "
                "general PMAY-U 2.0 financial assistance?"
            ),

        "options": {

            "ISS Loan Subsidy":
                "loan_iss",

            "General Financial Assistance":
                "loan_financial"
        }
    }

}


# ==========================================
# CONTEXT RESPONSES
# ==========================================

CONTEXT_RESPONSES = {

    # ==========================================
    # ELIGIBILITY
    # ==========================================

    "income_eligibility":
        (
            "PMAY-U 2.0 eligibility "
            "depends on annual family "
            "income.\n\n"

            "• EWS (Economically Weaker "
            "Section): up to ₹3 lakh/year\n"

            "• LIG (Low Income Group): "
            "₹3 lakh to ₹6 lakh/year\n"

            "• MIG (Middle Income Group): "
            "₹6 lakh to ₹9 lakh/year\n\n"

            "Your eligibility also depends "
            "on the scheme component such "
            "as BLC, AHP, ARH or ISS."
        ),

    "house_ownership":
        (
            "To apply under PMAY-U 2.0, "
            "you or any member of your "
            "family should NOT own a "
            "pucca (permanent) house "
            "anywhere in India.\n\n"

            "Family includes husband, "
            "wife and unmarried children.\n\n"

            "If any family member already "
            "owns a pucca house, you may "
            "not be eligible for PMAY benefits."
        ),

    "family_eligibility":
        (
            "Under PMAY-U 2.0, a "
            "beneficiary family includes:\n\n"

            "• Husband\n"
            "• Wife\n"
            "• Unmarried sons\n"
            "• Unmarried daughters\n\n"

            "The family should not own a "
            "pucca house anywhere in India "
            "to become eligible under PMAY."
        ),

    "scheme_eligibility":
        (
            "Eligibility depends on the "
            "PMAY scheme type:\n\n"

            "• BLC: For EWS families who "
            "have their own land and want "
            "to build a new house.\n\n"

            "• AHP: For EWS families who "
            "want to purchase a house in "
            "government/private housing projects.\n\n"

            "• ARH: For rental housing, "
            "mainly for migrants, workers "
            "and urban poor.\n\n"

            "• ISS: For EWS/LIG/MIG families "
            "taking a home loan to buy or "
            "construct a house."
        ),

    # ==========================================
    # PRIVACY
    # ==========================================

    "personal_data_privacy":
        (
            "Under PMAY-U 2.0, personal "
            "information such as Aadhaar, "
            "bank account details, income "
            "proof and address details are "
            "collected mainly for beneficiary "
            "verification and eligibility checking.\n\n"

            "This information is generally "
            "used only by authorized government "
            "departments and implementing agencies "
            "to process applications, verify "
            "eligibility and release benefits.\n\n"

            "Applicants should always provide "
            "correct information and avoid "
            "sharing sensitive details with "
            "unauthorized persons."
        ),

    "aadhaar_bank_safety":
        (
            "Aadhaar and bank account details "
            "are important for PMAY verification "
            "and Direct Benefit Transfer (DBT), "
            "through which eligible benefits "
            "or subsidy are transferred.\n\n"

            "Make sure Aadhaar and bank details "
            "entered in the application are correct "
            "to avoid delays or rejection.\n\n"

            "Never share OTP, bank PIN or personal "
            "documents with unknown persons, agents "
            "or unofficial websites."
        ),

    "beneficiary_confidentiality":
        (
            "Beneficiary details are generally "
            "used only for PMAY application "
            "processing, verification and subsidy "
            "or housing benefit approval.\n\n"

            "Application details are normally "
            "handled by authorized authorities "
            "and implementing agencies involved "
            "in PMAY.\n\n"

            "Applicants should apply only through "
            "official channels to keep their "
            "information secure."
        ),

    "application_security":
        (
            "To keep your PMAY application safe, "
            "always apply through official "
            "government portals, ULB offices "
            "or authorized centers.\n\n"

            "Avoid fake websites or unauthorized "
            "agents claiming guaranteed approval "
            "or asking for money.\n\n"

            "Before submitting, carefully verify "
            "your Aadhaar, bank account and other "
            "documents to avoid issues later."
        ),


    # =====================================
    # SUBSIDY
    # =====================================

    "subsidy_eligibility":
        (
            "PMAY-U 2.0 subsidy eligibility depends on "
            "factors such as annual family income, "
            "house ownership status and the PMAY "
            "scheme component.\n\n"

            "Generally, the beneficiary family "
            "should not own a pucca house anywhere "
            "in India and should satisfy the "
            "eligibility rules of schemes like "
            "BLC, AHP, ARH or ISS.\n\n"

            "Income category such as EWS, LIG "
            "or MIG may also affect eligibility."
        ),

    "subsidy_amount":
        (
            "Subsidy amount depends on the "
            "PMAY-U 2.0 scheme and eligibility category.\n\n"

            "In ISS (Interest Subsidy Scheme), "
            "eligible beneficiaries may receive "
            "interest subsidy on home loans as "
            "per PMAY-U 2.0 rules.\n\n"

            "The final benefit amount depends on "
            "loan eligibility, scheme guidelines "
            "and approval by concerned authorities."
        ),

    "subsidy_approval":
        (
            "After applying, your documents and "
            "eligibility details are verified by "
            "local authorities and implementing "
            "agencies.\n\n"

            "Verification may include Aadhaar, "
            "income proof, ownership details and "
            "family eligibility checks.\n\n"

            "If approved, subsidy or housing "
            "benefits are processed according "
            "to PMAY guidelines."
        ),

    "subsidy_delay":
        (
            "Subsidy delays can happen for "
            "several reasons such as incorrect "
            "documents, Aadhaar mismatch, bank "
            "account issues, pending verification "
            "or approval delays.\n\n"

            "Applicants should ensure all details "
            "are correct and regularly check "
            "application status through concerned "
            "authorities or official PMAY channels."
        ),


    # =====================================
    # OWNERSHIP
    # =====================================

    "pucca_house_ownership":
        (
            "Under PMAY-U 2.0, the applicant "
            "or beneficiary family should not "
            "own a pucca (permanent) house "
            "anywhere in India.\n\n"

            "A beneficiary family includes "
            "husband, wife and unmarried children.\n\n"

            "If any family member already owns "
            "a pucca house, the applicant may "
            "not be eligible for PMAY benefits."
        ),

    "land_ownership":
        (
            "Land ownership is important in "
            "certain PMAY schemes, especially "
            "BLC (Beneficiary Led Construction).\n\n"

            "In BLC, the applicant generally "
            "needs ownership or legal possession "
            "of land to construct or enhance a house.\n\n"

            "Applicants may need documents such "
            "as ownership proof, land records or "
            "other legal documents."
        ),

    "family_property":
        (
            "PMAY considers family property while "
            "checking eligibility.\n\n"

            "If husband, wife or unmarried children "
            "already own a pucca house anywhere "
            "in India, PMAY eligibility may be affected.\n\n"

            "The scheme checks ownership at the "
            "beneficiary family level, not only "
            "the individual applicant."
        ),

    "ownership_eligibility_impact":
        (
            "Property ownership can directly affect "
            "PMAY eligibility.\n\n"

            "If the beneficiary family already "
            "owns a pucca house anywhere in India, "
            "they may not qualify for PMAY-U 2.0 benefits.\n\n"

            "However, eligibility may also depend "
            "on scheme type, land ownership and "
            "other conditions."
        ),

    # =====================================
    # VERIFICATION
    # =====================================

    "document_verification":
        (
            "In PMAY-U 2.0, document "
            "verification is done to confirm "
            "that the applicant meets scheme "
            "eligibility conditions and to "
            "avoid incorrect or duplicate claims.\n\n"

            "Authorities may verify documents "
            "such as Aadhaar, income proof, "
            "bank details, land or house ownership "
            "records, identity proof and other "
            "supporting documents.\n\n"

            "If documents are incorrect, missing "
            "or mismatched, approval may be delayed "
            "or the application may be rejected. "
            "Applicants should ensure all details "
            "match official records."
        ),

    "beneficiary_verification":
        (
            "Beneficiary verification in "
            "PMAY-U 2.0 is done to check whether "
            "the applicant and family meet the "
            "required eligibility conditions.\n\n"

            "Authorities may verify family income, "
            "ownership status, Aadhaar details, "
            "bank information and whether the "
            "beneficiary family already owns a "
            "pucca house anywhere in India.\n\n"

            "This process helps ensure that "
            "housing benefits reach genuine "
            "eligible beneficiaries only."
        ),

    "field_verification":
        (
            "Field verification in PMAY-U 2.0 "
            "may be conducted by officials to "
            "physically confirm information "
            "provided in the application.\n\n"

            "This may include checking land "
            "ownership, house condition, site "
            "location or construction progress, "
            "especially under schemes like BLC.\n\n"

            "Field verification helps authorities "
            "ensure that benefits are being used "
            "for genuine housing purposes."
        ),

    "approval_verification":
        (
            "Before approval in PMAY-U 2.0, "
            "authorities review documents, "
            "beneficiary eligibility and scheme "
            "conditions carefully.\n\n"

            "Verification may include checking "
            "income category, Aadhaar details, "
            "ownership condition, bank account "
            "details and supporting documents.\n\n"

            "Once verification is completed "
            "successfully, subsidy or housing "
            "benefits may be approved as per "
            "scheme guidelines."
        ),


    # =====================================
    # BLC
    # =====================================

    "blc_eligibility":
        (
            "BLC (Beneficiary Led Construction) "
            "under PMAY-U 2.0 is mainly meant "
            "for EWS (Economically Weaker Section) "
            "families who want to construct a "
            "new house or improve an existing "
            "house on their own land.\n\n"

            "The beneficiary family should not "
            "own a pucca house anywhere in India "
            "and generally should have legal "
            "ownership or possession of land.\n\n"

            "Eligibility may also depend on "
            "local authority verification and "
            "scheme-specific conditions."
        ),

    "blc_documents":
        (
            "Documents commonly required for "
            "BLC under PMAY-U 2.0 may include:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Land ownership or possession proof\n"
            "• Bank account details\n"
            "• Identity and address proof\n"
            "• Property related documents\n\n"

            "Local authorities may ask for "
            "additional documents depending "
            "on city or state requirements."
        ),

    "blc_construction":
        (
            "Under BLC in PMAY-U 2.0, eligible "
            "beneficiaries can construct a new "
            "house or enhance an existing house "
            "on their own land.\n\n"

            "Construction work is generally "
            "verified in stages, and financial "
            "assistance may be released after "
            "progress verification.\n\n"

            "Beneficiaries should ensure that "
            "construction follows approved "
            "guidelines and verification process."
        ),

    "blc_application":
        (
            "To apply for BLC under PMAY-U 2.0, "
            "beneficiaries generally need to "
            "submit an application along with "
            "required documents and land proof.\n\n"

            "After submission, authorities verify "
            "eligibility, ownership details and "
            "documents before approval.\n\n"

            "Once approved, financial assistance "
            "may be released according to "
            "construction stages."
        ),


    # =====================================
    # ARH
    # =====================================

    "arh_eligibility":
        (
            "ARH (Affordable Rental Housing) "
            "under PMAY-U 2.0 is mainly meant "
            "for urban migrants, workers, "
            "students, industrial laborers "
            "and economically weaker sections "
            "who need affordable rental housing.\n\n"

            "Unlike ownership-based schemes, "
            "ARH focuses on affordable rent-based "
            "accommodation near workplaces or cities.\n\n"

            "Eligibility conditions may vary "
            "depending on local implementation."
        ),

    "arh_rental_housing":
        (
            "ARH in PMAY-U 2.0 focuses on "
            "providing affordable rental housing "
            "instead of home ownership.\n\n"

            "The scheme helps migrant workers, "
            "urban poor and other eligible groups "
            "access safe and affordable houses "
            "near employment areas.\n\n"

            "Rental housing may be provided "
            "through government or private "
            "participating agencies."
        ),

    "arh_conditions":
        (
            "Beneficiary conditions under "
            "ARH in PMAY-U 2.0 may depend on "
            "income level, occupation, migration "
            "status and housing need.\n\n"

            "Since ARH is meant for rental "
            "accommodation, ownership-related "
            "conditions may differ from other "
            "PMAY-U 2.0 schemes."
        ),

    "arh_application":
        (
            "To apply under ARH in PMAY-U 2.0, "
            "beneficiaries may need to register "
            "through approved rental housing "
            "providers or concerned authorities.\n\n"

            "Required documents and eligibility "
            "checks may vary depending on city "
            "guidelines and implementation."
        ),


    # =====================================
    # AHP
    # =====================================

    "ahp_eligibility":
        (
            "AHP (Affordable Housing in Partnership) "
            "under PMAY-U 2.0 is mainly for "
            "EWS families seeking affordable "
            "houses in approved housing projects.\n\n"

            "The beneficiary family should "
            "generally not own a pucca house "
            "anywhere in India.\n\n"

            "Eligibility also depends on income "
            "category, document verification and "
            "availability in approved projects."
        ),

    "ahp_projects":
        (
            "AHP in PMAY-U 2.0 supports affordable "
            "housing projects developed through "
            "government and private partnerships.\n\n"

            "Eligible beneficiaries may purchase "
            "houses in approved projects at "
            "affordable rates.\n\n"

            "Project availability depends on "
            "local authority approval and city planning."
        ),

    "ahp_documents":
        (
            "Common documents required for "
            "AHP under PMAY-U 2.0 may include:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Identity/address proof\n"
            "• Bank account details\n"
            "• Family related documents\n\n"

            "Additional documents may be requested "
            "depending on project and authority requirements."
        ),

    "ahp_approval":
        (
            "Approval under AHP in PMAY-U 2.0 "
            "depends on beneficiary eligibility, "
            "document verification and project availability.\n\n"

            "Authorities review applicant details "
            "before allotting affordable housing benefits."
        ),


    # =====================================
    # ISS
    # =====================================

    "iss_subsidy":
        (
            "ISS (Interest Subsidy Scheme) "
            "under PMAY-U 2.0 provides eligible "
            "beneficiaries with interest subsidy "
            "on home loans.\n\n"

            "The subsidy helps reduce the overall "
            "loan burden, making home ownership "
            "more affordable for eligible families.\n\n"

            "Final subsidy benefit depends on "
            "loan approval, eligibility and "
            "scheme conditions."
        ),

    "iss_loan_benefits":
        (
            "Under ISS in PMAY-U 2.0, eligible "
            "families may receive support through "
            "interest subsidy on housing loans.\n\n"

            "This helps reduce EMI burden and "
            "makes home purchase or construction "
            "more affordable.\n\n"

            "Loan-related benefits depend on "
            "income category, eligibility and "
            "approved lending institutions."
        ),

    "iss_eligibility":
        (
            "Eligibility for ISS under PMAY-U 2.0 "
            "depends on annual family income, "
            "ownership condition and home loan eligibility.\n\n"

            "The beneficiary family should "
            "generally not own a pucca house "
            "anywhere in India.\n\n"

            "Income category such as EWS, LIG "
            "or MIG may affect eligibility."
        ),

    "iss_approval_conditions":
        (
            "Approval under ISS in PMAY-U 2.0 "
            "depends on successful loan approval, "
            "document verification and beneficiary eligibility.\n\n"

            "Correct Aadhaar, bank account and "
            "income details help avoid delays "
            "or rejection during approval."
        ),

    # =====================================
    # APPROVAL
    # =====================================

    "application_approval":
        (
            "Application approval in "
            "PMAY-U 2.0 depends on successful "
            "verification of eligibility, "
            "documents and beneficiary details.\n\n"

            "Authorities may review Aadhaar, "
            "income proof, ownership condition, "
            "family details and other required "
            "documents before approval.\n\n"

            "If all conditions are satisfied, "
            "the application may be approved "
            "for housing or subsidy benefits."
        ),

    "subsidy_approval_process":
        (
            "Subsidy approval under PMAY-U 2.0 "
            "depends on scheme eligibility, "
            "document verification and successful "
            "beneficiary validation.\n\n"

            "Authorities may check income "
            "category, house ownership status, "
            "loan details (if applicable) and "
            "bank information before subsidy approval.\n\n"

            "Incorrect details or pending "
            "verification may delay approval."
        ),

    "sanction_process":
        (
            "In PMAY-U 2.0, the sanction process "
            "refers to official approval of "
            "beneficiary assistance or housing support.\n\n"

            "After verification, concerned "
            "authorities review applications "
            "before sanctioning financial "
            "assistance, subsidy or housing benefits.\n\n"

            "The process may vary depending "
            "on scheme type and local authority."
        ),

    "approval_status_tracking":
        (
            "Applicants under PMAY-U 2.0 may "
            "track their approval or application "
            "status through official channels "
            "or local authorities.\n\n"

            "Status updates may include stages "
            "such as verification pending, "
            "under review, approved or rejected.\n\n"

            "Keeping Aadhaar and application "
            "details correct helps avoid delays."
        ),


    # =====================================
    # FRAUD
    # =====================================

    "fake_documents":
        (
            "Submitting fake or incorrect "
            "documents in PMAY-U 2.0 may lead "
            "to application rejection, cancellation "
            "of benefits or legal action.\n\n"

            "Applicants should always provide "
            "genuine Aadhaar, income proof, "
            "bank details and ownership documents.\n\n"

            "Incorrect information may also "
            "delay approval."
        ),

    "scam_calls":
        (
            "Be careful of scam calls claiming "
            "guaranteed approval or asking for "
            "money in exchange for PMAY-U 2.0 benefits.\n\n"

            "Government authorities generally "
            "do not ask for OTP, bank PIN or "
            "private passwords over calls.\n\n"

            "Always verify information through "
            "official PMAY-U 2.0 channels."
        ),

    "payment_fraud":
        (
            "Applicants should be cautious of "
            "payment fraud related to PMAY-U 2.0.\n\n"

            "Avoid making payments to unauthorized "
            "agents claiming guaranteed approval "
            "or faster subsidy processing.\n\n"

            "Always use official channels and "
            "verify requests before making payments."
        ),

    "identity_misuse":
        (
            "Identity misuse happens when someone "
            "uses Aadhaar, bank details or personal "
            "documents without permission.\n\n"

            "To stay safe in PMAY-U 2.0, avoid "
            "sharing OTP, Aadhaar copies or "
            "sensitive information with unknown persons.\n\n"

            "Apply only through authorized "
            "government channels."
        ),


    # =====================================
    # DOCUMENTS
    # =====================================

    "required_documents":
        (
            "Documents required under PMAY-U 2.0 "
            "may vary depending on scheme type, "
            "but commonly include:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Identity/address proof\n"
            "• Bank account details\n"
            "• Land or ownership documents "
            "(if applicable)\n\n"

            "Local authorities may ask for "
            "additional documents based on scheme requirements."
        ),

    "missing_documents":
        (
            "Missing documents in PMAY-U 2.0 "
            "may delay verification or approval "
            "of your application.\n\n"

            "Applicants should carefully check "
            "whether Aadhaar, income proof, "
            "bank details and required supporting "
            "documents have been submitted correctly.\n\n"

            "You may need to resubmit or update "
            "missing documents."
        ),

    "document_verification_issues":
        (
            "Document verification issues in "
            "PMAY-U 2.0 may happen due to name mismatch, "
            "incorrect Aadhaar details, missing "
            "documents or invalid proofs.\n\n"

            "Applicants should ensure that all "
            "information matches official records "
            "to avoid rejection or delays."
        ),

    "document_correction_process":
        (
            "If there is an error in submitted "
            "documents under PMAY-U 2.0, applicants "
            "may need to update or correct details "
            "through concerned authorities.\n\n"

            "Common corrections include Aadhaar, "
            "bank account, income proof or "
            "ownership-related details."
        ),


    # =====================================
    # REJECTION
    # =====================================

    "rejection_reason":
        (
            "Applications under PMAY-U 2.0 may "
            "be rejected for reasons such as "
            "incorrect documents, eligibility issues, "
            "income mismatch or ownership conditions.\n\n"

            "If the beneficiary family already "
            "owns a pucca house anywhere in India, "
            "the application may become ineligible.\n\n"

            "Incomplete or mismatched information "
            "may also lead to rejection."
        ),

    "reapplication":
        (
            "In some cases, applicants may be "
            "able to reapply for PMAY-U 2.0 after "
            "correcting issues that caused rejection.\n\n"

            "Before reapplying, applicants should "
            "carefully verify documents, eligibility "
            "conditions and required details."
        ),

    "rejection_correction":
        (
            "If an application is rejected under "
            "PMAY-U 2.0 due to incorrect details "
            "or missing documents, corrections "
            "may be possible depending on local rules.\n\n"

            "Applicants should contact concerned "
            "authorities and update the required information."
        ),

    "appeal_options":
        (
            "If an applicant believes rejection "
            "under PMAY-U 2.0 was incorrect, they "
            "may contact concerned authorities "
            "or local implementing agencies for clarification.\n\n"

            "Supporting documents and correct "
            "information may help during review "
            "or appeal discussions."
        ),

    # =====================================
    # CSMC
    # =====================================

    "csmc_full_form":
        (
            "CSMC stands for "
            "'Central Sanctioning and "
            "Monitoring Committee'.\n\n"

            "It is an important committee "
            "under PMAY-U 2.0 responsible for "
            "reviewing and approving housing "
            "proposals submitted by States "
            "and Union Territories.\n\n"

            "CSMC helps ensure that eligible "
            "housing projects and beneficiaries "
            "receive approval according to "
            "PMAY-U 2.0 guidelines."
        ),

    "csmc_role":
        (
            "The role of CSMC in PMAY-U 2.0 "
            "is to review housing proposals, "
            "check compliance with scheme "
            "guidelines and support proper "
            "implementation.\n\n"

            "The committee helps ensure that "
            "housing benefits reach eligible "
            "beneficiaries and approved projects "
            "are processed correctly."
        ),

    "csmc_approval":
        (
            "Under PMAY-U 2.0, CSMC plays an "
            "important approval function by "
            "examining proposals submitted "
            "by States and Union Territories.\n\n"

            "After reviewing eligibility, "
            "housing demand and scheme "
            "conditions, the committee may "
            "recommend approval for projects "
            "or beneficiaries."
        ),

    "csmc_monitoring":
        (
            "CSMC also has a monitoring role "
            "under PMAY-U 2.0.\n\n"

            "It helps track implementation "
            "progress, beneficiary coverage "
            "and proper utilization of scheme "
            "benefits.\n\n"

            "Monitoring helps ensure transparency "
            "and smooth implementation of "
            "housing projects."
        ),


    # =====================================
    # EWS
    # =====================================

    "ews_eligibility":
        (
            "EWS (Economically Weaker Section) "
            "under PMAY-U 2.0 mainly includes "
            "families with lower annual income "
            "who need housing support.\n\n"

            "To become eligible, the beneficiary "
            "family should generally not own "
            "a pucca house anywhere in India "
            "and should satisfy PMAY-U 2.0 "
            "scheme conditions.\n\n"

            "Eligibility may also depend on "
            "income verification and scheme type."
        ),

    "ews_income":
        (
            "Under PMAY-U 2.0, EWS category "
            "generally includes families with "
            "annual income up to ₹3 lakh.\n\n"

            "Income may be verified using "
            "documents such as income certificate "
            "or other accepted proofs.\n\n"

            "Income category is important for "
            "determining scheme eligibility "
            "and available benefits."
        ),

    "ews_documents":
        (
            "Common documents for EWS applicants "
            "under PMAY-U 2.0 may include:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Bank account details\n"
            "• Identity/address proof\n"
            "• Property or land documents "
            "(if required)\n\n"

            "Additional documents may vary "
            "depending on scheme type and "
            "local authority requirements."
        ),

    "ews_benefits":
        (
            "Eligible EWS families under "
            "PMAY-U 2.0 may receive benefits "
            "such as affordable housing support, "
            "financial assistance or subsidy "
            "depending on scheme type.\n\n"

            "Benefits may vary under BLC, AHP, "
            "ARH or ISS based on eligibility "
            "conditions."
        ),


    # =====================================
    # LIG
    # =====================================

    "lig_eligibility":
        (
            "LIG (Low Income Group) under "
            "PMAY-U 2.0 generally includes "
            "families falling under specified "
            "income limits who need affordable housing.\n\n"

            "The beneficiary family should "
            "generally not own a pucca house "
            "anywhere in India and should "
            "meet scheme conditions."
        ),

    "lig_income":
        (
            "Under PMAY-U 2.0, LIG category "
            "generally includes families with "
            "annual income between ₹3 lakh "
            "and ₹6 lakh.\n\n"

            "Income proof may be required "
            "during verification.\n\n"

            "Income category helps determine "
            "housing eligibility and benefits."
        ),

    "lig_subsidy":
        (
            "Eligible LIG beneficiaries under "
            "PMAY-U 2.0 may receive subsidy "
            "benefits depending on the selected "
            "scheme component and eligibility.\n\n"

            "In ISS, eligible families may "
            "receive interest subsidy on "
            "housing loans."
        ),

    "lig_benefits":
        (
            "LIG beneficiaries under PMAY-U 2.0 "
            "may receive housing support, "
            "interest subsidy or affordable "
            "housing opportunities depending "
            "on eligibility and scheme type.\n\n"

            "Benefits vary under BLC, AHP, "
            "ARH and ISS."
        ),


    # =====================================
    # MIG
    # =====================================

    "mig_eligibility":
        (
            "MIG (Middle Income Group) under "
            "PMAY-U 2.0 generally includes "
            "families within approved income "
            "limits seeking housing assistance.\n\n"

            "Eligibility may depend on income, "
            "ownership condition and scheme-specific rules."
        ),

    "mig_subsidy":
        (
            "Eligible MIG families under "
            "PMAY-U 2.0 may receive subsidy "
            "benefits mainly through ISS "
            "(Interest Subsidy Scheme).\n\n"

            "Subsidy may help reduce the "
            "financial burden of housing loans."
        ),

    "mig_income":
        (
            "Under PMAY-U 2.0, MIG category "
            "generally includes families with "
            "annual income between ₹6 lakh "
            "and ₹9 lakh.\n\n"

            "Income proof may be required "
            "during beneficiary verification."
        ),

    "mig_loan_assistance":
        (
            "MIG beneficiaries under PMAY-U 2.0 "
            "may receive support through "
            "interest subsidy on eligible "
            "housing loans.\n\n"

            "Loan-related benefits depend on "
            "income eligibility, lender approval "
            "and PMAY-U 2.0 conditions."
        ),

    # =====================================
    # GRIEVANCE
    # =====================================

    "complaint_process":
        (
            "If applicants face issues in "
            "PMAY-U 2.0 such as delays, wrong "
            "information or benefit-related problems, "
            "they may raise a grievance or complaint.\n\n"

            "Complaints may generally be submitted "
            "through local authorities, Urban Local "
            "Bodies (ULBs) or official PMAY-U 2.0 "
            "channels.\n\n"

            "Applicants should keep application "
            "details and supporting documents ready "
            "while reporting issues."
        ),

    "delayed_application":
        (
            "Delays in PMAY-U 2.0 applications "
            "may happen due to pending verification, "
            "missing documents, Aadhaar mismatch "
            "or approval backlog.\n\n"

            "Applicants should check whether all "
            "documents and bank details are correct.\n\n"

            "For long delays, concerned local "
            "authorities or PMAY-U 2.0 offices "
            "may be contacted for clarification."
        ),

    "grievance_rejection":
        (
            "If an application under PMAY-U 2.0 "
            "is rejected and the applicant believes "
            "there is an issue, a grievance may "
            "be raised with concerned authorities.\n\n"

            "Applicants should verify rejection "
            "reasons such as eligibility mismatch, "
            "document issues or ownership conditions.\n\n"

            "Correct supporting documents may "
            "help resolve the issue."
        ),

    "authority_escalation":
        (
            "If a PMAY-U 2.0 issue remains unresolved, "
            "applicants may escalate the matter "
            "to higher authorities or concerned "
            "implementing agencies.\n\n"

            "Keeping application ID, Aadhaar and "
            "document details ready may help in "
            "faster resolution."
        ),


    # =====================================
    # SANCTION
    # =====================================

    "sanction_meaning":
        (
            "In PMAY-U 2.0, sanction generally "
            "means official approval of housing "
            "benefits, financial assistance or "
            "subsidy after successful verification.\n\n"

            "Once sanctioned, eligible beneficiaries "
            "may move to the next stage of receiving "
            "scheme support."
        ),

    "sanction_process_detail":
        (
            "The sanction process in PMAY-U 2.0 "
            "usually starts after document and "
            "eligibility verification.\n\n"

            "Authorities review beneficiary details, "
            "income category, ownership condition "
            "and scheme eligibility before granting sanction.\n\n"

            "Sanction timing may vary depending "
            "on city and approval stage."
        ),

    "sanction_approval_stage":
        (
            "The approval stage in PMAY-U 2.0 "
            "comes after verification of documents "
            "and beneficiary eligibility.\n\n"

            "At this stage, authorities review "
            "whether the applicant qualifies for "
            "scheme benefits before sanction approval."
        ),

    "pending_sanction":
        (
            "Pending sanction in PMAY-U 2.0 may "
            "happen due to incomplete verification, "
            "document mismatch, approval backlog "
            "or eligibility clarification.\n\n"

            "Applicants should regularly check "
            "their status and ensure submitted "
            "details are correct."
        ),


    # =====================================
    # STATUS
    # =====================================

    "application_status":
        (
            "Applicants can track PMAY-U 2.0 "
            "application status to understand "
            "whether the application is under "
            "review, approved, rejected or pending.\n\n"

            "Status may depend on document "
            "verification and authority approval."
        ),

    "subsidy_status":
        (
            "Subsidy status under PMAY-U 2.0 "
            "helps applicants know whether "
            "subsidy approval or release is pending, "
            "approved or completed.\n\n"

            "Bank details and successful verification "
            "play an important role in subsidy release."
        ),

    "verification_stage":
        (
            "Verification stage in PMAY-U 2.0 "
            "indicates whether applicant details "
            "and documents are still being checked.\n\n"

            "This may include Aadhaar verification, "
            "income proof checking, ownership review "
            "and eligibility confirmation."
        ),

    "approval_progress":
        (
            "Approval progress in PMAY-U 2.0 "
            "shows how far the application has "
            "moved in the approval process.\n\n"

            "Progress may include stages such as "
            "submitted, under verification, "
            "under review, sanctioned or approved."
        ),


    # =====================================
    # PUCCA
    # =====================================

    "pucca_house_meaning":
        (
            "A pucca house in PMAY-U 2.0 generally "
            "means a permanent house built with "
            "durable materials such as cement, "
            "brick, concrete or RCC roof.\n\n"

            "Pucca house ownership is important "
            "because applicants or beneficiary "
            "families already owning one may "
            "not qualify for certain PMAY-U 2.0 benefits."
        ),

    "pucca_ownership":
        (
            "Under PMAY-U 2.0, beneficiary families "
            "should generally not own a pucca house "
            "anywhere in India.\n\n"

            "Family includes husband, wife and "
            "unmarried children.\n\n"

            "Existing pucca house ownership may "
            "affect eligibility."
        ),

    "damaged_house":
        (
            "In some situations under PMAY-U 2.0, "
            "housing assistance may depend on "
            "whether the house is damaged, unsafe "
            "or requires improvement.\n\n"

            "Eligibility may vary depending on "
            "scheme type, local verification and "
            "house condition."
        ),

    "pucca_disqualification":
        (
            "Applicants under PMAY-U 2.0 may "
            "become ineligible if the beneficiary "
            "family already owns a pucca house "
            "anywhere in India.\n\n"

            "Ownership condition is one of the "
            "important eligibility checks during verification."
        ),

    # =====================================
    # AADHAAR
    # =====================================

    "aadhaar_requirement":
        (
            "Aadhaar is generally an important "
            "document in PMAY-U 2.0 for identity "
            "verification and beneficiary authentication.\n\n"

            "Applicants may need Aadhaar during "
            "application, verification and subsidy processing."
        ),

    "aadhaar_mismatch":
        (
            "Aadhaar mismatch issues in PMAY-U 2.0 "
            "may happen if name, date of birth "
            "or other details do not match "
            "official records.\n\n"

            "Mismatch may delay verification "
            "or approval, so applicants should "
            "correct details as early as possible."
        ),

    "aadhaar_update":
        (
            "If Aadhaar details are incorrect, "
            "applicants may need to update them "
            "before or during PMAY-U 2.0 verification.\n\n"

            "Correct Aadhaar details help avoid "
            "delays in approval or subsidy processing."
        ),

    "aadhaar_verification":
        (
            "Aadhaar verification in PMAY-U 2.0 "
            "helps confirm beneficiary identity "
            "and reduce duplicate or incorrect claims.\n\n"

            "Correct Aadhaar details are important "
            "for smooth application and verification."
        ),

    # ===================================== 
    # INCOME 
    # =====================================

    "check_income":
        (
            "PMAY-U 2.0 eligibility "
            "depends on annual family income.\n\n"

            "• Up to ₹3 lakh → EWS\n"
            "• ₹3–6 lakh → LIG\n"
            "• ₹6–9 lakh → MIG\n\n"

            "Please check which category "
            "matches your annual family income."
        ),

    "check_house":
        (
            "To become eligible under "
            "PMAY-U 2.0, the beneficiary "
            "family should generally not "
            "own a pucca house anywhere "
            "in India.\n\n"

            "Family includes husband, wife "
            "and unmarried children."
        ),

    "check_family":
        (
            "PMAY-U 2.0 checks eligibility "
            "at family level.\n\n"

            "A beneficiary family generally "
            "includes husband, wife and "
            "unmarried children.\n\n"

            "If any family member already "
            "owns a pucca house, eligibility "
            "may be affected."
        ),

    "check_location":
        (
            "PMAY-U 2.0 mainly applies "
            "to eligible beneficiaries "
            "living in urban areas.\n\n"

            "Eligibility and implementation "
            "may vary depending on city "
            "and local authority guidelines."
        ),

    # =====================================
    # NO HOUSE
    # =====================================

    "no_pucca_house":
        (
            "If you or your beneficiary family "
            "do not own a pucca house anywhere "
            "in India, you may become eligible "
            "for PMAY-U 2.0 benefits depending "
            "on other eligibility conditions.\n\n"

            "PMAY-U 2.0 generally gives priority "
            "to families without permanent housing.\n\n"

            "Eligibility also depends on annual "
            "family income, scheme type and "
            "document verification."
        ),

    "living_on_rent":
        (
            "People living on rent may also "
            "be eligible under PMAY-U 2.0 "
            "depending on income category, "
            "house ownership status and scheme type.\n\n"

            "If your family does not own a "
            "pucca house anywhere in India, "
            "you may qualify for certain "
            "PMAY-U 2.0 benefits.\n\n"

            "Rental housing support may also "
            "be available under ARH "
            "(Affordable Rental Housing)."
        ),

    "living_slum_chawl":
        (
            "Families living in slums, chawls "
            "or inadequate housing conditions "
            "may become eligible for support "
            "under PMAY-U 2.0 depending on "
            "local implementation and eligibility.\n\n"

            "Authorities may verify housing "
            "condition, ownership status and "
            "income category during evaluation."
        ),

    "house_ownership_check":
        (
            "Under PMAY-U 2.0, eligibility "
            "generally depends on whether the "
            "beneficiary family owns a pucca "
            "house anywhere in India.\n\n"

            "Family includes husband, wife "
            "and unmarried children.\n\n"

            "If no family member owns a pucca "
            "house, eligibility chances may improve."
        ),


    # =====================================
    # RENT HOUSE
    # =====================================

    "rental_housing_arh":
        (
            "ARH (Affordable Rental Housing) "
            "under PMAY-U 2.0 is designed for "
            "urban migrants, workers, students "
            "and economically weaker groups "
            "who need affordable rental housing.\n\n"

            "Instead of ownership, ARH focuses "
            "on providing safe and affordable "
            "houses on rent near workplaces or cities."
        ),

    "buy_house_eligibility":
        (
            "If you are living on rent and want "
            "to buy a house, you may become eligible "
            "under PMAY-U 2.0 depending on income, "
            "ownership condition and scheme eligibility.\n\n"

            "Families without a pucca house may "
            "benefit under schemes such as ISS "
            "or AHP depending on eligibility."
        ),

    "build_house_eligibility":
        (
            "If you want to build a house under "
            "PMAY-U 2.0, eligibility may depend "
            "on whether you own land and belong "
            "to an eligible income category.\n\n"

            "BLC (Beneficiary Led Construction) "
            "is generally meant for eligible "
            "families building houses on their own land."
        ),

    "rent_house_eligibility":
        (
            "Living in a rented house does not "
            "automatically make someone ineligible "
            "for PMAY-U 2.0.\n\n"

            "If your beneficiary family does not "
            "own a pucca house anywhere in India "
            "and meets income eligibility, you "
            "may qualify depending on scheme conditions."
        ),


    # =====================================
    # DOCUMENTS
    # =====================================

    "general_documents":
        (
            "General documents commonly required "
            "under PMAY-U 2.0 may include:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Identity/address proof\n"
            "• Bank account details\n"
            "• Family related details\n\n"

            "Additional documents may vary "
            "depending on scheme type and local authority."
        ),

    "arh_documents":
        (
            "Documents required for ARH under "
            "PMAY-U 2.0 may vary depending on "
            "city and implementation agency.\n\n"

            "Commonly required documents may include:\n\n"

            "• Aadhaar Card\n"
            "• Identity proof\n"
            "• Address details\n"
            "• Employment or migration proof "
            "(if applicable)"
        ),

    "iss_documents":
        (
            "For ISS under PMAY-U 2.0, applicants "
            "may generally require:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Bank account details\n"
            "• Home loan related documents\n"
            "• Identity/address proof\n\n"

            "Loan approval and verification "
            "are important for subsidy eligibility."
        ),

    # =====================================
    # NO INCOME PROOF
    # =====================================

    "no_income_self_declaration":
        (
            "If you do not have formal income proof, "
            "PMAY-U 2.0 may sometimes allow "
            "self-declaration of income depending "
            "on scheme type and local authority rules.\n\n"

            "This is especially helpful for "
            "informal workers, daily wage earners "
            "or self-employed applicants without "
            "regular salary documents.\n\n"

            "Applicants should provide accurate "
            "income details to avoid verification issues."
        ),

    "no_income_local_certificate":
        (
            "In some PMAY-U 2.0 cases, local "
            "authority certificates or income-related "
            "certificates may be considered for "
            "verification when formal salary proof "
            "is unavailable.\n\n"

            "Acceptance may depend on city guidelines "
            "and implementing authority rules.\n\n"

            "Applicants may check with concerned "
            "local authorities regarding accepted documents."
        ),

    "no_income_alternate_document":
        (
            "If formal income proof is unavailable, "
            "PMAY-U 2.0 may sometimes consider "
            "alternative verification documents.\n\n"

            "Examples may include:\n\n"

            "• Bank statements\n"
            "• Occupation proof\n"
            "• Self-employment records\n"
            "• Affidavit or declaration\n"
            "• Local authority certificate\n\n"

            "Accepted proof may vary depending "
            "on scheme type and local implementation."
        ),

    "no_income_no_document":
        (
            "If you currently do not have any "
            "income proof or supporting documents, "
            "eligibility under PMAY-U 2.0 may "
            "still depend on local authority rules.\n\n"

            "In some cases, self-declaration or "
            "other local verification methods may "
            "be accepted.\n\n"

            "You may contact concerned authorities "
            "to understand acceptable alternatives "
            "for income verification."
        ),

    # =====================================
    # WIDOW
    # =====================================

    "widow_eligibility":
        (
            "Widows may become eligible under "
            "PMAY-U 2.0 if they satisfy scheme "
            "conditions such as income eligibility, "
            "house ownership rules and beneficiary criteria.\n\n"

            "The beneficiary family should generally "
            "not own a pucca house anywhere in India.\n\n"

            "Widows may also receive priority "
            "consideration in some housing schemes "
            "depending on local implementation."
        ),

    "widow_ownership":
        (
            "Ownership rules for widows under "
            "PMAY-U 2.0 generally follow the "
            "same eligibility conditions applied "
            "to other beneficiaries.\n\n"

            "If the beneficiary family already "
            "owns a pucca house anywhere in India, "
            "eligibility may be affected.\n\n"

            "Ownership and family condition are "
            "verified during application review."
        ),

    "widow_priority":
        (
            "Widows are considered among priority "
            "groups in PMAY-U 2.0.\n\n"

            "Depending on local implementation, "
            "widows may receive preference during "
            "housing allotment or beneficiary selection.\n\n"

            "Final benefits depend on eligibility "
            "verification and authority approval."
        ),


    # =====================================
    # TRANSGENDER
    # =====================================

    "transgender_eligibility":
        (
            "Transgender applicants may also "
            "be eligible under PMAY-U 2.0 if "
            "they meet income, ownership and "
            "scheme eligibility conditions.\n\n"

            "The applicant or beneficiary family "
            "should generally not own a pucca "
            "house anywhere in India.\n\n"

            "Eligibility depends on beneficiary "
            "verification and applicable scheme rules."
        ),

    "transgender_ownership":
        (
            "Ownership rules for transgender "
            "beneficiaries under PMAY-U 2.0 "
            "follow the same house ownership "
            "conditions as other applicants.\n\n"

            "Applicants generally should not own "
            "a pucca house anywhere in India "
            "to qualify for benefits.\n\n"

            "Verification is done during "
            "application processing."
        ),


    # =====================================
    # SENIOR CITIZEN
    # =====================================

    "senior_priority":
        (
            "Senior citizens are considered "
            "priority beneficiaries under "
            "PMAY-U 2.0 in certain situations.\n\n"

            "Preference may be provided during "
            "housing allotment depending on "
            "scheme type and local authority rules.\n\n"

            "Final allotment depends on "
            "eligibility and project availability."
        ),

    "senior_eligibility":
        (
            "Senior citizens may become eligible "
            "under PMAY-U 2.0 if they satisfy "
            "income eligibility, ownership condition "
            "and scheme requirements.\n\n"

            "The beneficiary family generally "
            "should not own a pucca house "
            "anywhere in India."
        ),

    "senior_allotment":
        (
            "In PMAY-U 2.0, senior citizens may "
            "receive preference during housing "
            "allotment depending on project and "
            "local implementation.\n\n"

            "In some cases, accessible or "
            "ground-floor preference may also "
            "be considered."
        ),


    # =====================================
    # SLUM
    # =====================================

    "slum_eligibility":
        (
            "Families living in slums may "
            "become eligible under PMAY-U 2.0 "
            "depending on income category, "
            "house ownership condition and "
            "local implementation.\n\n"

            "Authorities may verify housing "
            "condition and beneficiary details "
            "during eligibility checking."
        ),

    "slum_redevelopment":
        (
            "PMAY-U 2.0 supports better housing "
            "and redevelopment opportunities "
            "for eligible slum households in "
            "certain situations.\n\n"

            "Redevelopment depends on city plans, "
            "local authority implementation and "
            "beneficiary eligibility."
        ),

    "slum_housing_option":
        (
            "Eligible slum residents under "
            "PMAY-U 2.0 may receive support "
            "through affordable housing schemes, "
            "redevelopment projects or housing assistance.\n\n"

            "Benefits depend on eligibility, "
            "income category and local implementation."
        ),


    # =====================================
    # CHAWL
    # =====================================

    "chawl_eligibility":
        (
            "Families living in chawls may "
            "become eligible under PMAY-U 2.0 "
            "depending on housing condition, "
            "income category and ownership rules.\n\n"

            "If the beneficiary family does not "
            "own a pucca house and satisfies "
            "scheme conditions, eligibility "
            "may be possible."
        ),

    "chawl_redevelopment":
        (
            "In some cities, chawl residents "
            "may benefit from redevelopment or "
            "better housing opportunities under "
            "PMAY-U 2.0-related initiatives.\n\n"

            "Eligibility depends on local plans, "
            "beneficiary verification and "
            "authority approval."
        ),
    
    # =====================================
    # OWN LAND
    # =====================================

    "own_land_blc":
        (
            "If you own land, you may become "
            "eligible to build a house under "
            "BLC (Beneficiary Led Construction) "
            "in PMAY-U 2.0.\n\n"

            "BLC is mainly meant for eligible "
            "EWS families who want to construct "
            "a new house or improve an existing "
            "house on their own land.\n\n"

            "Final eligibility depends on income "
            "category, ownership verification and "
            "other PMAY-U 2.0 conditions."
        ),

    "own_land_eligibility":
        (
            "Owning land may improve eligibility "
            "under BLC in PMAY-U 2.0, but land "
            "ownership alone does not guarantee approval.\n\n"

            "The beneficiary family generally "
            "should not own a pucca house anywhere "
            "in India and should satisfy income "
            "and scheme conditions.\n\n"

            "Authorities may verify land ownership "
            "during application review."
        ),

    "own_land_documents":
        (
            "If you own land and want benefits "
            "under PMAY-U 2.0, commonly required "
            "documents may include:\n\n"

            "• Aadhaar Card\n"
            "• Land ownership proof\n"
            "• Income proof\n"
            "• Identity/address proof\n"
            "• Bank account details\n\n"

            "Additional documents may vary "
            "depending on city and authority rules."
        ),

    "own_land_construction":
        (
            "Under BLC in PMAY-U 2.0, eligible "
            "beneficiaries may receive assistance "
            "for house construction or enhancement "
            "on their own land.\n\n"

            "Financial assistance is generally "
            "released in stages after construction "
            "progress verification."
        ),


    # =====================================
    # LOAN
    # =====================================

    "loan_subsidy":
        (
            "PMAY-U 2.0 offers home loan subsidy "
            "mainly through ISS (Interest Subsidy Scheme).\n\n"

            "Eligible beneficiaries may receive "
            "interest subsidy on housing loans, "
            "helping reduce EMI burden and making "
            "home ownership more affordable.\n\n"

            "Eligibility depends on income category, "
            "ownership condition and loan approval."
        ),

    "loan_eligibility":
        (
            "Loan eligibility under PMAY-U 2.0 "
            "depends on income category, house "
            "ownership condition and lender approval.\n\n"

            "The beneficiary family generally "
            "should not own a pucca house anywhere "
            "in India.\n\n"

            "Eligibility may vary depending on "
            "scheme type and bank conditions."
        ),

    "loan_approval":
        (
            "Loan approval under PMAY-U 2.0 "
            "depends on income verification, "
            "document checking, repayment ability "
            "and lender approval.\n\n"

            "Successful loan approval may be "
            "required before receiving ISS "
            "interest subsidy benefits."
        ),

    "loan_documents":
        (
            "Common documents required for "
            "PMAY-U 2.0 housing loan processing "
            "may include:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Bank statements\n"
            "• Address proof\n"
            "• Property or house-related documents\n\n"

            "Additional requirements may vary "
            "depending on the lender."
        ),


    # =====================================
    # APPLY
    # =====================================

    "apply_blc":
        (
            "To apply for BLC under PMAY-U 2.0, "
            "eligible beneficiaries generally need "
            "land ownership or possession proof "
            "along with required documents.\n\n"

            "After document and eligibility "
            "verification, authorities review "
            "applications before approval."
        ),

    "apply_ahp":
        (
            "To apply under AHP in PMAY-U 2.0, "
            "eligible beneficiaries may apply "
            "for approved affordable housing projects.\n\n"

            "Applicants may need Aadhaar, "
            "income proof and other required documents "
            "for verification."
        ),

    "apply_arh":
        (
            "To apply under ARH in PMAY-U 2.0, "
            "beneficiaries may register through "
            "approved rental housing providers "
            "or implementing agencies.\n\n"

            "Eligibility and document requirements "
            "may vary by city."
        ),

    "apply_iss":
        (
            "To apply under ISS in PMAY-U 2.0, "
            "eligible beneficiaries generally "
            "need an approved housing loan and "
            "required verification documents.\n\n"

            "Interest subsidy eligibility depends "
            "on income category and ownership conditions."
        ),


    # =====================================
    # NO DOCUMENTS
    # =====================================

    "missing_aadhaar":
        (
            "Aadhaar is generally important in "
            "PMAY-U 2.0 for beneficiary identity "
            "verification and application processing.\n\n"

            "If Aadhaar is unavailable or incorrect, "
            "applicants may need to update or obtain "
            "it before verification."
        ),

    "missing_income_proof":
        (
            "If income proof is unavailable, "
            "PMAY-U 2.0 may sometimes accept "
            "self-declaration or alternate "
            "verification depending on local rules.\n\n"

            "Acceptance varies by scheme type "
            "and authority."
        ),

    "missing_land_papers":
        (
            "Missing land papers may affect "
            "eligibility for schemes like BLC "
            "under PMAY-U 2.0 where land ownership "
            "verification is important.\n\n"

            "Applicants may check whether alternate "
            "ownership proof is accepted."
        ),

    "missing_address_proof":
        (
            "Address proof may be needed during "
            "PMAY-U 2.0 verification.\n\n"

            "Applicants may use accepted identity "
            "or residence-related documents depending "
            "on authority requirements."
        ),


    # =====================================
    # FAMILY HOUSE
    # =====================================

    "family_pucca_house":
        (
            "If any member of the beneficiary "
            "family already owns a pucca house "
            "anywhere in India, PMAY-U 2.0 "
            "eligibility may be affected.\n\n"

            "Family generally includes husband, "
            "wife and unmarried children."
        ),

    "parents_house":
        (
            "If the house is in parents' name, "
            "eligibility under PMAY-U 2.0 may "
            "depend on family definition, ownership "
            "status and dependency conditions.\n\n"

            "Authorities may review family and "
            "ownership details during verification."
        ),

    "joint_family_property":
        (
            "Joint family property may affect "
            "PMAY-U 2.0 eligibility depending on "
            "ownership share and family conditions.\n\n"

            "Authorities may verify ownership "
            "status before approval."
        ),

    "family_house_eligibility":
        (
            "PMAY-U 2.0 eligibility may be affected "
            "if the beneficiary family already "
            "owns a pucca house anywhere in India.\n\n"

            "Ownership verification is one of "
            "the important eligibility checks."
        ),

    # =====================================
    # CONFUSED
    # =====================================

    "confused_buy":
        (
            "If you want to buy a house, "
            "PMAY-U 2.0 may support eligible "
            "families through affordable housing "
            "schemes or home loan subsidy benefits.\n\n"

            "Eligibility generally depends on "
            "income category, house ownership "
            "condition and scheme type.\n\n"

            "If your family does not own a "
            "pucca house, you may have a better "
            "chance of eligibility."
        ),

    "confused_build":
        (
            "If you already own land and want "
            "to build or improve a house, "
            "BLC (Beneficiary Led Construction) "
            "under PMAY-U 2.0 may be relevant.\n\n"

            "Eligibility generally depends on "
            "land ownership, income category "
            "and house ownership condition."
        ),

    "confused_rent":
        (
            "If you are looking for affordable "
            "rental housing, ARH (Affordable "
            "Rental Housing) under PMAY-U 2.0 "
            "may be useful.\n\n"

            "This scheme mainly supports urban "
            "migrants, workers, students and "
            "economically weaker groups looking "
            "for affordable rented accommodation."
        ),

    "confused_eligibility":
        (
            "To check PMAY-U 2.0 eligibility, "
            "important factors generally include:\n\n"

            "• Family income\n"
            "• Pucca house ownership\n"
            "• Family situation\n"
            "• Urban area eligibility\n\n"

            "If you share these details, "
            "eligibility may become clearer."
        ),


    # =====================================
    # HESITANT TO APPLY
    # =====================================

    "hesitant_no_house":
        (
            "If your beneficiary family does "
            "not own a pucca house anywhere "
            "in India, you may potentially "
            "be eligible under PMAY-U 2.0.\n\n"

            "Final eligibility depends on "
            "income category, family condition "
            "and verification."
        ),

    "hesitant_income":
        (
            "Income category plays an important "
            "role in PMAY-U 2.0 eligibility.\n\n"

            "Families under EWS, LIG or MIG "
            "categories may become eligible "
            "depending on scheme type and "
            "other conditions.\n\n"

            "Even if income is low, you may "
            "still qualify for support."
        ),

    "hesitant_rent_slum":
        (
            "People living on rent, in slums "
            "or chawls may also become eligible "
            "under PMAY-U 2.0 depending on "
            "income category and house ownership condition.\n\n"

            "Living in rented or inadequate "
            "housing does not automatically "
            "make someone ineligible."
        ),

    "hesitant_unsure":
        (
            "That is completely understandable. "
            "Many people are unsure before applying "
            "for PMAY-U 2.0.\n\n"

            "Generally, if your family does not "
            "own a pucca house and falls within "
            "eligible income categories, it may "
            "still be worth checking eligibility."
        ),


    # =====================================
    # HOUSE PROBLEM
    # =====================================

    "house_problem_ownership":
        (
            "If your issue is related to house "
            "ownership, PMAY-U 2.0 eligibility "
            "may depend on whether the beneficiary "
            "family already owns a pucca house "
            "anywhere in India.\n\n"

            "Ownership details are verified "
            "during application review."
        ),

    "house_problem_damage":
        (
            "If your house is damaged or unsafe, "
            "eligibility under PMAY-U 2.0 may "
            "depend on housing condition, local "
            "verification and scheme applicability.\n\n"

            "Authorities may review whether "
            "housing improvement or support "
            "can be provided."
        ),

    "house_problem_rent":
        (
            "If your housing issue relates to "
            "rent or lack of affordable housing, "
            "ARH under PMAY-U 2.0 may help in "
            "certain situations.\n\n"

            "Eligibility depends on city-level "
            "implementation and beneficiary conditions."
        ),

    "house_problem_eligibility":
        (
            "Housing-related eligibility under "
            "PMAY-U 2.0 usually depends on income, "
            "house ownership condition, family "
            "status and scheme requirements.\n\n"

            "Different schemes may apply depending "
            "on your situation."
        ),


    # =====================================
    # COMPLICATED CASE
    # =====================================

    "complicated_family":
        (
            "If your case involves family-related "
            "complications, PMAY-U 2.0 eligibility "
            "may depend on family structure, "
            "marital status, ownership and dependency.\n\n"

            "Family generally includes husband, "
            "wife and unmarried children."
        ),

    "complicated_ownership":
        (
            "Ownership-related complications "
            "under PMAY-U 2.0 may involve joint "
            "property, inherited property, parents' "
            "house or partial ownership.\n\n"

            "Eligibility depends on verification "
            "and ownership rules."
        ),

    "complicated_documents":
        (
            "Document-related complications "
            "such as missing Aadhaar, income proof "
            "or ownership papers may sometimes "
            "be resolved through alternate documents "
            "or correction process.\n\n"

            "Acceptance depends on local authority rules."
        ),

    "complicated_income":
        (
            "Income-related complications may "
            "happen if applicants have irregular "
            "income, informal work or no formal proof.\n\n"

            "In some PMAY-U 2.0 cases, alternate "
            "verification or self-declaration "
            "may be considered."
        ),

    "complicated_rejection":
        (
            "If your case is complicated due "
            "to rejection, the reason may be "
            "related to eligibility, documents, "
            "ownership or verification issues.\n\n"

            "Understanding the rejection reason "
            "may help determine correction or "
            "reapplication options."
        ),

    # =====================================
    # FAMILY HOUSE CONFUSION
    # =====================================

    "ownership_my_name":
        (
            "If the house ownership is in your "
            "name, PMAY-U 2.0 eligibility may "
            "depend on whether it is considered "
            "a pucca house and your family status.\n\n"

            "Beneficiary families already owning "
            "a pucca house anywhere in India may "
            "not qualify under certain PMAY-U 2.0 schemes."
        ),

    "ownership_parents":
        (
            "If the house belongs to your parents, "
            "PMAY-U 2.0 eligibility may depend on "
            "whether you are considered part of "
            "the same beneficiary family.\n\n"

            "Family generally includes husband, "
            "wife and unmarried children.\n\n"

            "Ownership verification may be done "
            "during application review."
        ),

    "ownership_joint_family":
        (
            "Joint family property may affect "
            "PMAY-U 2.0 eligibility depending on "
            "ownership share and beneficiary status.\n\n"

            "Authorities may verify who legally "
            "owns the property before approval."
        ),

    "ownership_unsure":
        (
            "That is understandable. PMAY-U 2.0 "
            "eligibility may depend on whose name "
            "appears in ownership records and "
            "whether the house is considered "
            "part of your beneficiary family.\n\n"

            "Checking ownership documents may help."
        ),


    # =====================================
    # RENT + FAMILY HOUSE CONFUSION
    # =====================================

    "family_house_yes":
        (
            "If your beneficiary family already "
            "owns a pucca house anywhere in India, "
            "PMAY-U 2.0 eligibility may be affected.\n\n"

            "Family generally includes husband, "
            "wife and unmarried children."
        ),

    "family_house_no":
        (
            "If your beneficiary family does not "
            "own a pucca house anywhere in India, "
            "you may potentially qualify under "
            "PMAY-U 2.0 depending on income and "
            "other eligibility conditions."
        ),

    "family_house_unsure":
        (
            "That is okay. PMAY-U 2.0 eligibility "
            "often depends on whether the beneficiary "
            "family owns a pucca house anywhere in India.\n\n"

            "If possible, checking ownership details "
            "may help avoid eligibility confusion."
        ),

    "family_relative_house":
        (
            "If the house belongs to another "
            "relative, eligibility under PMAY-U 2.0 "
            "may depend on whether they are considered "
            "part of your beneficiary family.\n\n"

            "Family generally includes husband, "
            "wife and unmarried children."
        ),


    # =====================================
    # AADHAAR PROBLEM
    # =====================================

    "aadhaar_address_issue":
        (
            "Address mismatch in Aadhaar may "
            "sometimes delay PMAY-U 2.0 verification.\n\n"

            "Applicants may consider updating "
            "Aadhaar details if the mismatch "
            "causes verification issues."
        ),

    "aadhaar_missing":
        (
            "Aadhaar is generally important for "
            "PMAY-U 2.0 identity verification.\n\n"

            "If Aadhaar is unavailable, applicants "
            "may need to obtain or update it before "
            "application or verification."
        ),

    "aadhaar_wrong_details":
        (
            "Incorrect Aadhaar details such as "
            "name, address or date of birth may "
            "cause PMAY-U 2.0 verification delays.\n\n"

            "Correcting Aadhaar information may help."
        ),

    "aadhaar_verification_issue":
        (
            "If Aadhaar verification is failing "
            "under PMAY-U 2.0, the issue may be "
            "related to mismatch, missing details "
            "or technical verification problems.\n\n"

            "Checking Aadhaar information carefully "
            "may help resolve the issue."
        ),


    # =====================================
    # WIDOW + MONEY + DOC ISSUE
    # =====================================

    "widow_money_eligibility":
        (
            "Widows may receive priority consideration "
            "under PMAY-U 2.0 depending on eligibility.\n\n"

            "If your beneficiary family does not "
            "own a pucca house and falls under "
            "eligible income conditions, support "
            "may still be possible."
        ),

    "widow_document_issue":
        (
            "If documents are creating difficulty, "
            "some PMAY-U 2.0 cases may allow alternate "
            "verification or local authority review "
            "depending on the missing documents.\n\n"

            "Document requirements may vary by scheme."
        ),

    "widow_income_issue":
        (
            "If income or money is the main concern, "
            "PMAY-U 2.0 may still support eligible "
            "low-income families depending on "
            "income category and eligibility.\n\n"

            "Low income does not automatically "
            "mean ineligible."
        ),

    "widow_unsure":
        (
            "That is understandable. Since your "
            "situation involves widow status, "
            "documents and income concerns, PMAY-U 2.0 "
            "eligibility may depend on multiple factors.\n\n"

            "Clarifying your main concern may help "
            "identify the best option."
        ),


    # =====================================
    # LANDLORD ISSUE
    # =====================================

    "renting_eligibility":
        (
            "Living in a rented house does not "
            "automatically make someone ineligible "
            "for PMAY-U 2.0.\n\n"

            "Eligibility generally depends on "
            "income category, house ownership "
            "condition and beneficiary family status."
        ),

    "rent_document_issue":
        (
            "If you are worried about address or "
            "document issues while renting, PMAY-U 2.0 "
            "verification may depend on accepted "
            "identity and address documents.\n\n"

            "Requirements may vary by authority."
        ),

    "housing_safety":
        (
            "If housing safety or pressure from "
            "a landlord is a concern, local support "
            "or housing-related authorities may "
            "sometimes help depending on the situation.\n\n"

            "PMAY-U 2.0 eligibility itself usually "
            "depends on housing and income conditions."
        ),

    "rent_unsure":
        (
            "That sounds stressful. PMAY-U 2.0 "
            "eligibility while renting may still "
            "be possible depending on income, "
            "family ownership condition and documents.\n\n"

            "Understanding the main concern may help."
        ),

    # =====================================
    # MAYBE PMAY NOT FOR PEOPLE LIKE ME
    # =====================================

    "pmay_people_housing":
        (
            "If you are facing housing problems, "
            "PMAY-U 2.0 may still be worth checking.\n\n"

            "Eligibility often depends on housing "
            "condition, income category and whether "
            "your beneficiary family owns a pucca "
            "house anywhere in India.\n\n"

            "Many eligible people initially think "
            "they may not qualify, so checking "
            "eligibility can still be helpful."
        ),

    "pmay_people_income":
        (
            "Low income does not automatically "
            "mean you are ineligible for PMAY-U 2.0.\n\n"

            "PMAY-U 2.0 includes categories such "
            "as EWS and LIG to support eligible "
            "families needing housing assistance.\n\n"

            "Income category and verification "
            "play an important role."
        ),

    "pmay_people_no_house":
        (
            "If your beneficiary family does "
            "not own a pucca house anywhere in India, "
            "you may potentially qualify under "
            "PMAY-U 2.0 depending on income and "
            "other scheme conditions.\n\n"

            "No house ownership may improve "
            "eligibility chances."
        ),

    "pmay_people_unsure":
        (
            "That is completely understandable. "
            "Many people are unsure whether "
            "PMAY-U 2.0 applies to them.\n\n"

            "Eligibility usually depends on:\n\n"

            "• Family income\n"
            "• House ownership\n"
            "• Housing condition\n"
            "• Scheme eligibility\n\n"

            "It may still be worth checking."
        ),


    # =====================================
    # PAPERS WEIRD
    # =====================================

    "paper_name_mismatch":
        (
            "Name mismatch in documents may "
            "sometimes delay PMAY-U 2.0 verification.\n\n"

            "If names are different across Aadhaar, "
            "bank account or identity documents, "
            "authorities may ask for correction "
            "or clarification.\n\n"

            "Updating details may help avoid delays."
        ),

    "paper_address_mismatch":
        (
            "Address mismatch may sometimes "
            "affect PMAY-U 2.0 document verification.\n\n"

            "Applicants may need updated address "
            "proof or Aadhaar correction depending "
            "on authority requirements.\n\n"

            "Requirements may vary by location."
        ),

    "paper_missing_documents":
        (
            "Missing documents do not always "
            "mean PMAY-U 2.0 eligibility is impossible.\n\n"

            "In some cases, alternate proof, "
            "self-declaration or local authority "
            "verification may help depending "
            "on scheme and missing document type."
        ),

    "paper_ownership_issue":
        (
            "Ownership-related document issues "
            "may affect eligibility under "
            "PMAY-U 2.0, especially for schemes "
            "such as BLC.\n\n"

            "Authorities may verify land or "
            "property ownership during review."
        ),


    # =====================================
    # FAMILY SITUATION MESSY
    # =====================================

    "messy_family_ownership":
        (
            "Family ownership situations may "
            "affect PMAY-U 2.0 eligibility depending "
            "on whose name appears in ownership records.\n\n"

            "Beneficiary family generally includes "
            "husband, wife and unmarried children."
        ),

    "messy_family_separation":
        (
            "If there is separation or family "
            "conflict, PMAY-U 2.0 eligibility "
            "may depend on current family status, "
            "ownership condition and beneficiary details.\n\n"

            "Verification may be required."
        ),

    "messy_family_inheritance":
        (
            "Inheritance-related housing situations "
            "may affect PMAY-U 2.0 eligibility "
            "depending on legal ownership status.\n\n"

            "Authorities may review whose name "
            "appears in property records."
        ),

    "messy_family_documents":
        (
            "If family documents are confusing "
            "or incomplete, PMAY-U 2.0 verification "
            "may depend on alternate proof or "
            "local authority clarification.\n\n"

            "Supporting documents may help "
            "during review."
        ),


    # =====================================
    # TEMPORARY / NOT FULLY SLUM
    # =====================================

    "temporary_housing":
        (
            "If you live in temporary or unstable "
            "housing, PMAY-U 2.0 eligibility may "
            "still be worth checking.\n\n"

            "Housing condition, ownership status "
            "and local implementation may influence eligibility.\n\n"

            "Temporary housing does not automatically "
            "mean you are ineligible."
        ),

    "unsafe_housing":
        (
            "Unsafe, damaged or inadequate housing "
            "conditions may sometimes strengthen "
            "the need for housing support under "
            "PMAY-U 2.0.\n\n"

            "Authorities may verify housing condition "
            "during assessment."
        ),

    "informal_settlement":
        (
            "If you live in an informal settlement "
            "or semi-slum type condition, PMAY-U 2.0 "
            "eligibility may depend on local "
            "implementation and housing verification.\n\n"

            "Housing condition and ownership details "
            "may be reviewed."
        ),

    "temporary_unsure":
        (
            "That is understandable. Housing situations "
            "are sometimes difficult to classify.\n\n"

            "PMAY-U 2.0 eligibility may still depend "
            "on housing condition, income category "
            "and whether the beneficiary family "
            "owns a pucca house."
        ),

    # =====================================
    # SOMEONE USED MY DETAILS
    # =====================================

    "details_aadhaar_misuse":
        (
            "If you are worried someone may "
            "have misused your Aadhaar details, "
            "it may be important to check whether "
            "your information was used incorrectly "
            "during PMAY-U 2.0 application or verification.\n\n"

            "Avoid sharing Aadhaar, OTP or bank "
            "details with unknown persons.\n\n"

            "If something feels wrong, checking "
            "official records or contacting "
            "concerned authorities may help."
        ),

    "details_duplicate_issue":
        (
            "Duplicate beneficiary issues may "
            "sometimes happen if records show "
            "multiple applications or ownership-related confusion.\n\n"

            "PMAY-U 2.0 verification usually checks "
            "for duplicate claims before approval.\n\n"

            "Clarifying your application details "
            "with concerned authorities may help."
        ),

    "details_fake_application":
        (
            "If you suspect someone submitted "
            "a fake PMAY-U 2.0 application using "
            "your details, it may be important "
            "to verify your beneficiary status "
            "through official channels.\n\n"

            "Avoid sharing personal documents "
            "with unauthorized persons."
        ),

    "details_unsure":
        (
            "That concern is understandable. "
            "If you feel someone may have used "
            "your details, checking Aadhaar, "
            "beneficiary records or application "
            "status may help clarify the situation.\n\n"

            "Official verification may be useful."
        ),


    # =====================================
    # MARRIAGE SITUATION
    # =====================================

    "marriage_separation":
        (
            "If there is separation between spouses, "
            "PMAY-U 2.0 eligibility may depend on "
            "current family situation, ownership "
            "status and supporting records.\n\n"

            "Authorities may review beneficiary "
            "family details during verification."
        ),

    "marriage_spouse_house":
        (
            "If your spouse owns a pucca house, "
            "PMAY-U 2.0 eligibility may be affected "
            "because beneficiary family generally "
            "includes husband, wife and unmarried children.\n\n"

            "Ownership verification is important."
        ),

    "marriage_divorce":
        (
            "In divorce situations, PMAY-U 2.0 "
            "eligibility may depend on current "
            "ownership status, legal records and "
            "beneficiary family condition.\n\n"

            "Verification may be required to "
            "understand eligibility."
        ),

    "marriage_after":
        (
            "Eligibility after marriage under "
            "PMAY-U 2.0 may depend on spouse ownership, "
            "family condition and whether the "
            "beneficiary family already owns "
            "a pucca house anywhere in India."
        ),


    # =====================================
    # WHICH SCHEME
    # =====================================

    "scheme_buy":
        (
            "If you want to buy a house, "
            "PMAY-U 2.0 schemes such as AHP "
            "or ISS may be relevant depending "
            "on income and eligibility.\n\n"

            "ISS may help through housing loan "
            "subsidy, while AHP focuses on "
            "affordable housing projects."
        ),

    "scheme_build":
        (
            "If you want to build or improve "
            "a house on your own land, "
            "BLC (Beneficiary Led Construction) "
            "under PMAY-U 2.0 may be relevant.\n\n"

            "Land ownership and eligibility "
            "verification are important."
        ),

    "scheme_rent":
        (
            "If you are looking for affordable "
            "rental housing, ARH (Affordable "
            "Rental Housing) under PMAY-U 2.0 "
            "may be relevant.\n\n"

            "ARH mainly supports urban migrants, "
            "workers and economically weaker groups."
        ),

    "scheme_subsidy":
        (
            "If you mainly need loan or subsidy "
            "support, ISS (Interest Subsidy Scheme) "
            "under PMAY-U 2.0 may be relevant.\n\n"

            "Eligible beneficiaries may receive "
            "interest subsidy on housing loans."
        ),


    # =====================================
    # WRONG REJECTION
    # =====================================

    "wrong_rejection_ownership":
        (
            "If rejection happened due to ownership, "
            "PMAY-U 2.0 authorities may have found "
            "that the beneficiary family owns a "
            "pucca house anywhere in India.\n\n"

            "If you believe this is incorrect, "
            "ownership records may need clarification."
        ),

    "wrong_rejection_income":
        (
            "Income-related rejection may happen "
            "if income proof, category or verification "
            "details do not match eligibility rules.\n\n"

            "Checking income documents may help "
            "understand the rejection."
        ),

    "wrong_rejection_documents":
        (
            "Document-related rejection may happen "
            "due to missing proof, mismatch or "
            "verification issues.\n\n"

            "Correcting or resubmitting documents "
            "may sometimes help."
        ),

    "wrong_rejection_duplicate":
        (
            "Rejection may happen if authorities "
            "detect duplicate beneficiary records "
            "or application conflicts.\n\n"

            "Clarifying beneficiary details with "
            "concerned authorities may help."
        ),


    # =====================================
    # FAMILY SAYS DON'T APPLY
    # =====================================

    "family_doubt_no_house":
        (
            "If your beneficiary family does "
            "not own a pucca house anywhere in India, "
            "PMAY-U 2.0 may still be worth checking.\n\n"

            "Many eligible families assume they "
            "may not qualify, but eligibility depends "
            "on multiple conditions."
        ),

    "family_doubt_income":
        (
            "Low income does not automatically "
            "mean PMAY-U 2.0 is not for you.\n\n"

            "Schemes often support EWS and LIG "
            "families who need housing assistance."
        ),

    "family_doubt_housing":
        (
            "If housing condition is difficult, "
            "unsafe or temporary, PMAY-U 2.0 "
            "may still be relevant depending "
            "on eligibility and local implementation."
        ),

    "family_doubt_unsure":
        (
            "That is understandable. Many people "
            "feel unsure before applying for "
            "PMAY-U 2.0.\n\n"

            "Checking eligibility may still be "
            "worth considering before deciding."
        ),

    # =====================================
    # DON'T UNDERSTAND TERMS
    # =====================================

    "understand_eligibility":
        (
            "Eligibility in PMAY-U 2.0 means "
            "checking whether a person or family "
            "qualifies for housing support.\n\n"

            "It usually depends on:\n\n"

            "• Family income\n"
            "• Whether your family owns a pucca house\n"
            "• Family situation\n"
            "• Scheme conditions\n\n"

            "For many people, not owning a pucca "
            "house and falling under eligible "
            "income categories are important factors."
        ),

    "understand_documents":
        (
            "Documents in PMAY-U 2.0 are mainly "
            "used for identity, income and "
            "eligibility verification.\n\n"

            "Common documents may include:\n\n"

            "• Aadhaar Card\n"
            "• Income proof\n"
            "• Bank account details\n"
            "• Address proof\n"
            "• Land papers (for some schemes)\n\n"

            "Required documents may vary depending "
            "on the PMAY-U 2.0 scheme."
        ),

    "understand_subsidy":
        (
            "Subsidy in PMAY-U 2.0 generally means "
            "financial support to make housing "
            "more affordable.\n\n"

            "For example, under ISS (Interest "
            "Subsidy Scheme), eligible people "
            "may receive home loan interest support "
            "to reduce EMI burden.\n\n"

            "Eligibility depends on income and "
            "scheme conditions."
        ),

    "understand_schemes":
        (
            "PMAY-U 2.0 includes different schemes "
            "for different housing situations.\n\n"

            "• BLC → for building/improving house on own land\n"
            "• AHP → affordable housing projects\n"
            "• ARH → affordable rental housing\n"
            "• ISS → home loan subsidy support\n\n"

            "The right scheme depends on your "
            "housing need and eligibility."
        ),


    # =====================================
    # BANK + DOCUMENT + NO FIXED PLACE
    # =====================================

    "bank_document_dbt":
        (
            "Bank or DBT issues may sometimes "
            "affect PMAY-U 2.0 benefit transfer "
            "or verification.\n\n"

            "Applicants may need correct bank "
            "details linked properly for smooth "
            "verification and benefit processing.\n\n"

            "Mismatched details may sometimes "
            "cause delays."
        ),

    "bank_document_address":
        (
            "Address proof issues may happen if "
            "you move often, rent homes or do "
            "not have a fixed place.\n\n"

            "PMAY-U 2.0 authorities may sometimes "
            "accept alternate documents depending "
            "on local rules.\n\n"

            "Requirements can vary by city."
        ),

    "bank_document_rent_migration":
        (
            "Living on rent or moving frequently "
            "does not automatically make someone "
            "ineligible for PMAY-U 2.0.\n\n"

            "Eligibility generally depends on "
            "income category, ownership condition "
            "and local implementation.\n\n"

            "Many migrant or rented families "
            "may still qualify."
        ),

    "bank_document_unsure":
        (
            "That is understandable. When there "
            "are bank, document and housing issues "
            "together, things can feel confusing.\n\n"

            "Starting with the biggest issue first "
            "usually makes PMAY-U 2.0 eligibility "
            "easier to understand."
        ),


    # =====================================
    # WHAT COUNTS AS HOUSE
    # =====================================

    "house_temporary":
        (
            "Temporary structures may not always "
            "be treated the same as a permanent "
            "pucca house under PMAY-U 2.0.\n\n"

            "Housing condition, durability and "
            "ownership situation may matter "
            "during eligibility checking."
        ),

    "house_semi_pucca":
        (
            "Semi-pucca, damaged or weak houses "
            "may sometimes be treated differently "
            "from fully permanent pucca houses "
            "under PMAY-U 2.0.\n\n"

            "Authorities may review housing "
            "condition during verification."
        ),

    "house_family_owned":
        (
            "If the house belongs to family members, "
            "PMAY-U 2.0 eligibility may depend on "
            "whether it counts under your beneficiary "
            "family ownership.\n\n"

            "Family generally includes husband, "
            "wife and unmarried children."
        ),

    "house_unsure":
        (
            "That confusion is understandable. "
            "Many people are unsure what counts "
            "as a pucca house under PMAY-U 2.0.\n\n"

            "Housing type, ownership and condition "
            "usually matter during eligibility review."
        ),


    # =====================================
    # TOO MANY PROBLEMS
    # =====================================

    "many_problem_house":
        (
            "If housing is the biggest concern, "
            "PMAY-U 2.0 eligibility may depend "
            "on your current housing condition "
            "and whether your beneficiary family "
            "owns a pucca house anywhere in India."
        ),

    "many_problem_income":
        (
            "Income-related concerns are common "
            "in PMAY-U 2.0 applications.\n\n"

            "Even low-income or irregular income "
            "families may still qualify depending "
            "on category and verification."
        ),

    "many_problem_documents":
        (
            "Document issues such as missing "
            "Aadhaar, income proof or address "
            "documents may sometimes be resolved "
            "through updates or alternate proof "
            "depending on local rules."
        ),

    "many_problem_family":
        (
            "Family situations such as separation, "
            "joint ownership or dependency may "
            "affect PMAY-U 2.0 eligibility.\n\n"

            "Authorities may review beneficiary "
            "family details during verification."
        ),

    "many_problem_rejection":
        (
            "If rejection is one of the biggest "
            "problems, understanding the rejection "
            "reason may help identify whether "
            "correction or reapplication is possible."
        ),


    # =====================================
    # CHATBOT CANT UNDERSTAND
    # =====================================

    "chatbot_house":
        (
            "House ownership confusion is very "
            "common in PMAY-U 2.0.\n\n"

            "Eligibility often depends on whether "
            "you or your beneficiary family own "
            "a pucca house anywhere in India."
        ),

    "chatbot_income":
        (
            "Income situations can sometimes feel "
            "confusing, especially with informal "
            "jobs or irregular earnings.\n\n"

            "PMAY-U 2.0 eligibility usually depends "
            "on income category and verification."
        ),

    "chatbot_family":
        (
            "Family situations such as marriage, "
            "separation, parents' house or joint "
            "family ownership may affect eligibility.\n\n"

            "We can understand your case step by step."
        ),

    "chatbot_documents":
        (
            "Document problems are very common "
            "in PMAY-U 2.0 cases.\n\n"

            "Issues like Aadhaar mismatch, missing "
            "proof or ownership documents may "
            "sometimes be resolved depending on "
            "verification requirements."
        ),

    # =====================================
    # BANK ISSUE
    # =====================================

    "bank_dbt_delay":
        (
            "DBT (Direct Benefit Transfer) delay "
            "may sometimes happen due to bank "
            "verification, account mismatch or "
            "processing delays under PMAY-U 2.0.\n\n"

            "Checking whether your bank account "
            "is active and correctly linked may help.\n\n"

            "In some cases, local authority or "
            "bank verification may be required."
        ),

    "bank_inactive_account":
        (
            "If your bank account is inactive or "
            "not operational, PMAY-U 2.0 payment "
            "or subsidy processing may get delayed.\n\n"

            "Applicants may need to update or "
            "activate the account before benefit transfer."
        ),

    "bank_wrong_account":
        (
            "Wrong bank account details may affect "
            "PMAY-U 2.0 verification or benefit transfer.\n\n"

            "Even small mismatches in account number, "
            "IFSC code or beneficiary name may "
            "sometimes create delays.\n\n"

            "Checking bank details carefully may help."
        ),

    "bank_mismatch":
        (
            "Bank mismatch may happen if names, "
            "documents or account details do not "
            "match PMAY-U 2.0 records.\n\n"

            "Correcting mismatched details may "
            "sometimes help resolve delays or rejection."
        ),


    # =====================================
    # WHICH SCHEME BRO
    # =====================================

    "scheme_bro_build":
        (
            "If you want to build or improve a "
            "house on your own land, BLC "
            "(Beneficiary Led Construction) under "
            "PMAY-U 2.0 may be suitable.\n\n"

            "Land ownership and eligibility "
            "verification are usually important."
        ),

    "scheme_bro_buy":
        (
            "If you want to buy a house, AHP "
            "(Affordable Housing in Partnership) "
            "or ISS (Interest Subsidy Scheme) "
            "under PMAY-U 2.0 may be relevant.\n\n"

            "The right option depends on income, "
            "loan requirement and eligibility."
        ),

    "scheme_bro_rent":
        (
            "If affordable rental housing is "
            "your concern, ARH (Affordable Rental "
            "Housing) under PMAY-U 2.0 may be useful.\n\n"

            "It mainly supports urban workers, "
            "migrants and economically weaker groups."
        ),

    "scheme_bro_loan":
        (
            "If reducing home loan burden is "
            "the main concern, ISS under "
            "PMAY-U 2.0 may help through "
            "interest subsidy on housing loans.\n\n"

            "Eligibility depends on income "
            "category and loan approval."
        ),


    # =====================================
    # EMBARRASSED TO ASK
    # =====================================

    "embarrassed_house":
        (
            "No worries — housing-related concerns "
            "are very common in PMAY-U 2.0.\n\n"

            "Eligibility often depends on housing "
            "condition and whether your beneficiary "
            "family owns a pucca house anywhere in India."
        ),

    "embarrassed_income":
        (
            "Many people feel unsure about income "
            "eligibility, especially with irregular "
            "or low earnings.\n\n"

            "PMAY-U 2.0 includes support categories "
            "such as EWS and LIG, so low income "
            "does not automatically mean ineligible."
        ),

    "embarrassed_documents":
        (
            "Document confusion happens very often "
            "in PMAY-U 2.0 cases.\n\n"

            "Issues like Aadhaar mismatch, missing "
            "proof or ownership documents may "
            "sometimes be corrected or verified."
        ),

    "embarrassed_family":
        (
            "Family situations such as separation, "
            "joint property or parents' house can "
            "make PMAY-U 2.0 feel confusing.\n\n"

            "Eligibility usually depends on "
            "beneficiary family definition and ownership."
        ),

    "embarrassed_rejection":
        (
            "Getting rejected can feel discouraging, "
            "but rejection does not always mean "
            "permanent ineligibility.\n\n"

            "Sometimes rejection happens due to "
            "documents, mismatch or verification issues."
        ),


    # =====================================
    # TOO MANY ISSUES
    # =====================================

    "many_issue_ownership":
        (
            "Ownership concerns are one of the "
            "most important PMAY-U 2.0 eligibility factors.\n\n"

            "Eligibility may depend on whether "
            "your beneficiary family owns a "
            "pucca house anywhere in India."
        ),

    "many_issue_documents":
        (
            "Document issues such as Aadhaar, "
            "income proof or ownership papers "
            "may sometimes feel overwhelming.\n\n"

            "Many cases can still be clarified "
            "through correction or alternate proof."
        ),

    "many_issue_family":
        (
            "Family situations such as marriage, "
            "joint ownership or separation may "
            "sometimes affect PMAY-U 2.0 eligibility.\n\n"

            "Clarifying family status usually helps."
        ),

    "many_issue_income":
        (
            "Income confusion is common in PMAY-U 2.0.\n\n"

            "Even if income is irregular or low, "
            "eligibility may still be possible "
            "depending on category and verification."
        ),

    "many_issue_status":
        (
            "If application status is the biggest "
            "concern, delays may sometimes happen "
            "due to verification, documents or "
            "approval processing."
        ),


    # =====================================
    # NAME MISMATCH
    # =====================================

    "mismatch_aadhaar":
        (
            "Mismatch in Aadhaar details such as "
            "name, DOB or address may sometimes "
            "cause PMAY-U 2.0 verification delays.\n\n"

            "Correcting Aadhaar details may help."
        ),

    "mismatch_bank":
        (
            "Bank detail mismatch may happen if "
            "the beneficiary name or account details "
            "do not match PMAY-U 2.0 records.\n\n"

            "Even small spelling differences may matter."
        ),

    "mismatch_pan":
        (
            "PAN mismatch may sometimes create "
            "verification problems if details "
            "do not match other submitted records."
        ),

    "mismatch_application":
        (
            "Mismatch in application form details "
            "may sometimes lead to rejection or delay.\n\n"

            "Checking spelling, income and identity "
            "details carefully may help."
        ),

    "mismatch_property":
        (
            "Property or ownership document mismatch "
            "may affect PMAY-U 2.0 eligibility, "
            "especially in ownership-based schemes."
        ),


    # =====================================
    # REJECTED DUE TO MISMATCH
    # =====================================

    "reject_mismatch_aadhaar":
        (
            "Aadhaar mismatch may sometimes lead "
            "to rejection if identity details "
            "do not match submitted records.\n\n"

            "Correcting Aadhaar details may help "
            "before reapplying."
        ),

    "reject_mismatch_income":
        (
            "Income proof mismatch may happen if "
            "declared income and documents differ.\n\n"

            "Checking supporting documents may help "
            "understand rejection."
        ),

    "reject_mismatch_bank":
        (
            "Bank mismatch may sometimes affect "
            "verification or subsidy transfer "
            "under PMAY-U 2.0.\n\n"

            "Checking account details carefully may help."
        ),

    "reject_mismatch_address":
        (
            "Address mismatch may sometimes cause "
            "verification issues if documents "
            "show different locations."
        ),

    "reject_mismatch_ownership":
        (
            "Ownership mismatch may happen if "
            "land or house records do not match "
            "submitted beneficiary details.\n\n"

            "Clarifying ownership documents may help."
        ),

    # =====================================
    # WHICH SCHEME FOR ME
    # =====================================

    "scheme_for_me_build":
        (
            "If you want to build or improve "
            "a house on land you own, BLC "
            "(Beneficiary Led Construction) "
            "under PMAY-U 2.0 may be suitable.\n\n"

            "This scheme generally supports "
            "eligible families who already "
            "have land and want assistance "
            "for constructing or improving housing.\n\n"

            "Eligibility usually depends on "
            "income category, land ownership "
            "and house ownership condition."
        ),

    "scheme_for_me_buy":
        (
            "If you want to buy a house, "
            "AHP (Affordable Housing in Partnership) "
            "or ISS (Interest Subsidy Scheme) "
            "under PMAY-U 2.0 may be relevant.\n\n"

            "AHP focuses on affordable housing "
            "projects, while ISS may help reduce "
            "housing loan burden through interest subsidy.\n\n"

            "The right scheme depends on income "
            "and eligibility."
        ),

    "scheme_for_me_rent":
        (
            "If affordable rental housing is "
            "your concern, ARH (Affordable Rental "
            "Housing) under PMAY-U 2.0 may help.\n\n"

            "This scheme mainly supports urban "
            "workers, migrants, students and "
            "economically weaker groups looking "
            "for affordable rented accommodation."
        ),

    "scheme_for_me_subsidy":
        (
            "If your main concern is reducing "
            "housing loan burden, ISS under "
            "PMAY-U 2.0 may help through "
            "interest subsidy on eligible loans.\n\n"

            "This support may help reduce EMI "
            "burden and make home ownership "
            "more affordable depending on eligibility."
        ),


    # =====================================
    # ELIGIBILITY
    # =====================================

    "eligible_no_house":
        (
            "If your beneficiary family does "
            "not own a pucca house anywhere "
            "in India, PMAY-U 2.0 may still "
            "be worth checking.\n\n"

            "Not owning a permanent house is "
            "often an important eligibility factor, "
            "although income and family conditions "
            "also matter."
        ),

    "eligible_rent":
        (
            "Living on rent does not automatically "
            "make someone ineligible for PMAY-U 2.0.\n\n"

            "Many rented families may still qualify "
            "depending on income, ownership condition "
            "and scheme type.\n\n"

            "Rental housing support may also be "
            "available through ARH."
        ),

    "eligible_income":
        (
            "Income category is one of the important "
            "factors in PMAY-U 2.0 eligibility.\n\n"

            "Categories such as EWS and LIG are "
            "often eligible depending on scheme type, "
            "house ownership and verification."
        ),

    "eligible_unsure":
        (
            "That is completely understandable. "
            "Many people feel unsure about "
            "PMAY-U 2.0 eligibility.\n\n"

            "Eligibility usually depends on:\n\n"

            "• Family income\n"
            "• House ownership\n"
            "• Housing condition\n"
            "• Family situation\n\n"

            "Checking these details step by step "
            "can make things clearer."
        ),


    # =====================================
    # HOUSE NOT MINE BUT KINDA MINE
    # =====================================

    "house_kind_my_name":
        (
            "If the house is legally in your name, "
            "PMAY-U 2.0 eligibility may depend on "
            "whether it counts as a pucca house "
            "and your beneficiary family situation.\n\n"

            "House ownership is an important "
            "eligibility factor."
        ),

    "house_kind_family":
        (
            "If the house belongs to another "
            "family member, PMAY-U 2.0 eligibility "
            "may depend on whether they are part "
            "of your beneficiary family.\n\n"

            "Beneficiary family generally includes "
            "husband, wife and unmarried children."
        ),

    "house_kind_joint":
        (
            "Joint family property may sometimes "
            "make PMAY-U 2.0 eligibility confusing.\n\n"

            "Authorities may check legal ownership "
            "records and ownership share before approval."
        ),

    "house_kind_unsure":
        (
            "That confusion is understandable. "
            "PMAY-U 2.0 eligibility may depend "
            "on whose name appears in ownership "
            "documents and whether the house "
            "counts under your beneficiary family."
        ),


    # =====================================
    # STATUS
    # =====================================

    "status_pending":
        (
            "Pending status in PMAY-U 2.0 usually "
            "means the application is still under "
            "verification or approval process.\n\n"

            "Sometimes delays happen due to "
            "document checking, ownership review "
            "or verification workload."
        ),

    "status_rejected":
        (
            "Rejected status may happen due to "
            "eligibility, ownership, income or "
            "document mismatch issues.\n\n"

            "Understanding the rejection reason "
            "may help determine whether correction "
            "or reapplication is possible."
        ),

    "status_under_review":
        (
            "Under review usually means your "
            "PMAY-U 2.0 application is still "
            "being checked by authorities.\n\n"

            "Document verification and eligibility "
            "assessment may still be ongoing."
        ),

    "status_no_update":
        (
            "No update for a long time may feel "
            "frustrating, but PMAY-U 2.0 applications "
            "sometimes take time depending on "
            "verification and approval stages."
        ),


    # =====================================
    # RENT ROOM
    # =====================================

    "rent_room_rental":
        (
            "If you are mainly looking for "
            "affordable rental support, ARH "
            "under PMAY-U 2.0 may be relevant.\n\n"

            "It supports affordable rental "
            "housing for eligible urban workers "
            "and economically weaker groups."
        ),

    "rent_room_ownership":
        (
            "If your goal is eventually owning "
            "a permanent house, PMAY-U 2.0 may "
            "still be worth checking depending "
            "on income and ownership condition.\n\n"

            "Schemes such as AHP or ISS may "
            "sometimes help eligible families."
        ),

    "rent_room_eligibility":
        (
            "Even if you currently rent a room "
            "and do not own a house, PMAY-U 2.0 "
            "eligibility may still be possible.\n\n"

            "House ownership, income category "
            "and family condition are important factors."
        ),

    "rent_room_unsure":
        (
            "That is okay — many people are not "
            "sure where to begin.\n\n"

            "Understanding whether you want "
            "rental help, house ownership or "
            "eligibility checking may help identify "
            "the right PMAY-U 2.0 option."
        ),

    # =====================================
    # FAMILY COMPLICATED
    # =====================================

    "family_comp_ownership":
        (
            "Ownership-related family situations "
            "can sometimes affect PMAY-U 2.0 eligibility.\n\n"

            "Authorities may verify whose name "
            "appears in ownership records and whether "
            "the property belongs to the beneficiary family.\n\n"

            "Even when ownership is shared or unclear, "
            "it does not automatically mean someone "
            "is ineligible. Verification usually helps "
            "clarify the situation."
        ),

    "family_comp_separation":
        (
            "If separation between family members "
            "or spouses is involved, PMAY-U 2.0 "
            "eligibility may depend on current family "
            "status and ownership records.\n\n"

            "Beneficiary family details are generally "
            "reviewed during verification.\n\n"

            "The final outcome depends on the specific "
            "circumstances and supporting documents."
        ),

    "family_comp_inheritance":
        (
            "Inheritance situations can make "
            "PMAY-U 2.0 eligibility feel confusing.\n\n"

            "Authorities may check who legally owns "
            "the property and whether inheritance "
            "has been formally recorded.\n\n"

            "Inherited property does not always lead "
            "to the same eligibility outcome, so "
            "ownership verification is important."
        ),

    "family_comp_housing":
        (
            "Family housing situations such as "
            "living together, staying in a family-owned "
            "house or shared housing arrangements "
            "may affect PMAY-U 2.0 eligibility.\n\n"

            "The key factor is often whether the "
            "beneficiary family owns a pucca house "
            "and how ownership is recorded."
        ),

    # =====================================
    # SCARED TO APPLY
    # =====================================

    "scared_eligibility":
        (
            "Many people feel uncertain about "
            "eligibility before applying for "
            "PMAY-U 2.0.\n\n"

            "Not knowing whether you qualify is "
            "completely normal. Eligibility usually "
            "depends on income, house ownership, "
            "family condition and scheme requirements.\n\n"

            "Checking eligibility does not harm your "
            "application and may help you understand "
            "your options."
        ),

    "scared_rejection":
        (
            "Fear of rejection is very common.\n\n"

            "However, PMAY-U 2.0 applications may be "
            "rejected for specific reasons such as "
            "documents, ownership or eligibility issues.\n\n"

            "Understanding the reason is often the "
            "first step toward correcting the problem "
            "or determining whether reapplication is possible."
        ),

    "scared_documents":
        (
            "Document concerns are one of the most "
            "common reasons people hesitate to apply.\n\n"

            "Missing or incorrect documents do not "
            "always mean the application cannot proceed.\n\n"

            "In some situations, updates, corrections "
            "or alternate proof may help depending on "
            "local authority requirements."
        ),

    "scared_ownership":
        (
            "Ownership-related questions are very "
            "common under PMAY-U 2.0.\n\n"

            "Many applicants are unsure whether a "
            "family property, inherited property or "
            "shared ownership affects eligibility.\n\n"

            "Verification usually focuses on who legally "
            "owns the property and whether it counts "
            "under the beneficiary family."
        ),

    # =====================================
    # THEY SAY IM NOT ELIGIBLE
    # =====================================

    "not_eligible_ownership":
        (
            "If someone believes you are not eligible "
            "because of ownership, it may be related "
            "to whether the beneficiary family owns "
            "a pucca house anywhere in India.\n\n"

            "However, assumptions are not always correct. "
            "Actual eligibility depends on verified records."
        ),

    "not_eligible_income":
        (
            "Income-related assumptions are common.\n\n"

            "PMAY-U 2.0 supports different income "
            "categories, including EWS and LIG.\n\n"

            "The actual outcome depends on verified "
            "income details rather than guesses."
        ),

    "not_eligible_family_house":
        (
            "Many people assume that living in a "
            "family-owned house automatically makes "
            "someone ineligible.\n\n"

            "In reality, eligibility may depend on "
            "ownership records, beneficiary family "
            "definition and verification."
        ),

    "not_eligible_rejection":
        (
            "A previous rejection does not always "
            "mean permanent ineligibility.\n\n"

            "The reason for rejection is important. "
            "Some issues may be corrected while others "
            "may require clarification or updated documents."
        ),

    # =====================================
    # APP ISSUE
    # =====================================

    "app_issue_documents":
        (
            "If the issue is document-related, "
            "it may involve missing documents, "
            "mismatch issues or incomplete verification.\n\n"

            "Checking submitted records carefully "
            "may help identify the problem."
        ),

    "app_issue_verification":
        (
            "Verification delays can happen when "
            "authorities are reviewing eligibility, "
            "documents or ownership information.\n\n"

            "This does not automatically mean "
            "there is a problem with the application."
        ),

    "app_issue_rejection":
        (
            "If the application appears to have "
            "a rejection-related issue, understanding "
            "the exact reason is important.\n\n"

            "Rejections are often linked to documents, "
            "ownership, eligibility or mismatch concerns."
        ),

    "app_issue_pending":
        (
            "Pending status usually means the "
            "application is still being processed "
            "or verified.\n\n"

            "Some PMAY-U 2.0 applications may remain "
            "pending for a period depending on "
            "verification and approval workload."
        ),

    # =====================================
    # FEELS IMPOSSIBLE
    # =====================================

    "impossible_housing":
        (
            "Housing difficulties do not automatically "
            "disqualify someone from PMAY-U 2.0.\n\n"

            "In fact, housing need is often one of the "
            "reasons people explore PMAY-U 2.0 support.\n\n"

            "Eligibility depends on several factors, "
            "not just current housing challenges."
        ),

    "impossible_family":
        (
            "Family situations can feel complicated, "
            "but they do not automatically prevent "
            "someone from qualifying under PMAY-U 2.0.\n\n"

            "Eligibility is usually based on verified "
            "family and ownership information."
        ),

    "impossible_income":
        (
            "Income concerns are common, especially "
            "for families with low or irregular earnings.\n\n"

            "PMAY-U 2.0 includes support for eligible "
            "lower-income categories, so income alone "
            "does not determine the outcome."
        ),

    "impossible_unsure":
        (
            "When multiple issues exist at the same time, "
            "PMAY-U 2.0 can feel overwhelming.\n\n"

            "Breaking the situation into smaller parts "
            "such as housing, income, documents and family "
            "status often makes it easier to understand."
        ),

    # =====================================
    # FRAUD
    # =====================================

    "fraud_aadhaar":
        (
            "If you suspect Aadhaar misuse, it may be "
            "important to check whether your personal "
            "details were used incorrectly during any "
            "application or verification process.\n\n"

            "Avoid sharing Aadhaar, OTP or bank details "
            "with unknown persons."
        ),

    "fraud_fake_approval":
        (
            "If someone claims your application was "
            "approved but the information seems suspicious, "
            "it may be important to verify the status "
            "through official channels.\n\n"

            "Do not rely only on unofficial messages "
            "or calls."
        ),

    "fraud_duplicate":
        (
            "Duplicate beneficiary concerns may arise "
            "when records appear to show multiple "
            "applications or conflicting information.\n\n"

            "Authorities generally verify beneficiary "
            "details before approval."
        ),

    "fraud_calls":
        (
            "Be cautious of suspicious calls claiming "
            "to guarantee PMAY-U 2.0 approval or asking "
            "for money, OTPs or personal information.\n\n"

            "Official verification should always be "
            "done through trusted channels."
        ),

    # =====================================
    # FAMILY OWNS STUFF SOMEWHERE MAYBE
    # =====================================

    "family_stuff_family_house":
        (
            "If your beneficiary family owns a "
            "pucca house anywhere in India, it may "
            "affect eligibility under PMAY-U 2.0.\n\n"

            "Beneficiary family generally includes "
            "husband, wife and unmarried children.\n\n"

            "Authorities usually verify ownership "
            "records before approval. The exact "
            "impact depends on whose name appears "
            "in the ownership documents."
        ),

    "family_stuff_parents_house":
        (
            "If the house belongs to your parents, "
            "PMAY-U 2.0 eligibility may depend on "
            "whether that property is considered part "
            "of your beneficiary family situation.\n\n"

            "Many applicants are confused about this, "
            "so ownership records and family details "
            "are usually reviewed during verification."
        ),

    "family_stuff_relative_house":
        (
            "If the property belongs to another "
            "relative, eligibility under PMAY-U 2.0 "
            "may depend on whether that person is "
            "considered part of your beneficiary family.\n\n"

            "The key factor is usually legal ownership "
            "and family relationship."
        ),

    "family_stuff_unsure":
        (
            "That is a common situation. Many people "
            "are unsure about who legally owns a property "
            "or whether it affects PMAY-U 2.0 eligibility.\n\n"

            "Checking ownership records may help clarify "
            "whether the property is relevant to your application."
        ),

    # =====================================
    # BROKE AF NO HOUSE
    # =====================================

    "broke_rent":
        (
            "Living on rent does not automatically "
            "make someone ineligible for PMAY-U 2.0.\n\n"

            "In fact, many eligible beneficiaries "
            "currently live in rented accommodation.\n\n"

            "Eligibility generally depends on income, "
            "house ownership condition and scheme requirements."
        ),

    "broke_slum":
        (
            "Families living in slums may still be "
            "considered for PMAY-U 2.0 benefits depending "
            "on eligibility, housing condition and "
            "local implementation.\n\n"

            "Housing need is often an important factor "
            "during evaluation."
        ),

    "broke_chawl":
        (
            "People living in chawls may also be "
            "eligible under PMAY-U 2.0 depending on "
            "income category, ownership condition and "
            "housing circumstances.\n\n"

            "Verification may include review of "
            "current housing conditions."
        ),

    "broke_temporary":
        (
            "Temporary or unstable housing situations "
            "do not automatically disqualify someone "
            "from PMAY-U 2.0.\n\n"

            "Housing condition, ownership status and "
            "income eligibility are usually considered "
            "together during review."
        ),

    # =====================================
    # APPLIED LONG AGO
    # =====================================

    "old_application_pending":
        (
            "If your PMAY-U 2.0 application has been "
            "pending for a long time, it may still be "
            "under document verification, ownership "
            "checking or approval review.\n\n"

            "Long processing times can happen depending "
            "on workload and local verification stages."
        ),

    "old_application_review":
        (
            "Under Review usually means authorities "
            "are still checking eligibility, documents "
            "or beneficiary information.\n\n"

            "This status does not automatically indicate "
            "a problem with the application."
        ),

    "old_application_sanction":
        (
            "If the application is sanctioned, it "
            "generally means approval has been granted "
            "for the relevant stage under PMAY-U 2.0.\n\n"

            "Further processing or benefit release may "
            "still take time depending on the scheme."
        ),

    "old_application_verification":
        (
            "Verification stage means authorities are "
            "reviewing submitted documents, eligibility "
            "conditions and beneficiary details.\n\n"

            "Applications may remain in this stage until "
            "verification is completed."
        ),

    # =====================================
    # WEIRD MARRIAGE SITUATION
    # =====================================

    "marriage_weird_separation":
        (
            "If separation is involved, PMAY-U 2.0 "
            "eligibility may depend on current family "
            "status, ownership condition and supporting records.\n\n"

            "Authorities may review the actual beneficiary "
            "family situation during verification."
        ),

    "marriage_weird_spouse_house":
        (
            "If your spouse owns a pucca house, it may "
            "affect PMAY-U 2.0 eligibility because "
            "beneficiary family generally includes "
            "husband, wife and unmarried children.\n\n"

            "Ownership records are an important factor."
        ),

    "marriage_weird_divorce":
        (
            "Divorce-related situations may affect "
            "eligibility depending on ownership status, "
            "legal records and current family condition.\n\n"

            "Authorities may review documentation to "
            "understand the situation correctly."
        ),

    "marriage_weird_after":
        (
            "Eligibility after marriage may depend on "
            "house ownership, spouse details and family "
            "status under PMAY-U 2.0.\n\n"

            "The outcome often depends on verified records "
            "rather than marital status alone."
        ),

    # =====================================
    # BANK ISSUE
    # =====================================

    "bank_issue_dbt":
        (
            "DBT delays may happen because of account "
            "verification, beneficiary matching or "
            "processing delays under PMAY-U 2.0.\n\n"

            "Checking whether the account is active "
            "and correctly linked may help identify issues."
        ),

    "bank_issue_inactive":
        (
            "If the bank account is inactive, PMAY-U 2.0 "
            "payments or benefit transfers may be delayed.\n\n"

            "Updating or reactivating the account may "
            "be necessary before processing can continue."
        ),

    "bank_issue_wrong_account":
        (
            "Incorrect account details such as account "
            "number, IFSC code or beneficiary name may "
            "cause verification or payment problems.\n\n"

            "Reviewing bank information carefully may help."
        ),

    "bank_issue_mismatch":
        (
            "Bank mismatch issues may occur when account "
            "details do not match submitted PMAY-U 2.0 records.\n\n"

            "Even small differences in names or account "
            "information may sometimes delay verification "
            "or benefit transfer."
        ),

    # =====================================
    # IDK WHICH SCHEME BRO
    # =====================================

    "scheme_build":
        (
            "If you want to build or improve a house "
            "on land that you own, BLC (Beneficiary "
            "Led Construction) under PMAY-U 2.0 may "
            "be relevant.\n\n"

            "This component supports eligible families "
            "who need assistance for constructing a new "
            "house or enhancing an existing one on their "
            "own land."
        ),

    "scheme_buy":
        (
            "If your goal is to buy a house, AHP "
            "(Affordable Housing in Partnership) under "
            "PMAY-U 2.0 may be relevant.\n\n"

            "This component helps eligible beneficiaries "
            "access affordable housing projects developed "
            "under approved partnerships."
        ),

    "scheme_rent":
        (
            "If you are looking for affordable rental "
            "housing, ARH (Affordable Rental Housing) "
            "under PMAY-U 2.0 may be suitable.\n\n"

            "It is designed to support eligible urban "
            "residents who need affordable rental "
            "accommodation."
        ),

    "scheme_loan":
        (
            "If your main concern is reducing housing "
            "loan burden, ISS (Interest Subsidy Scheme) "
            "under PMAY-U 2.0 may help.\n\n"

            "Eligible beneficiaries may receive interest "
            "subsidy support, helping reduce the overall "
            "cost of home ownership."
        ),

    # =====================================
    # EMBARRASSED TO ASK
    # =====================================

    "embarrassed_house":
        (
            "Housing-related concerns are very common "
            "under PMAY-U 2.0.\n\n"

            "The key factors usually include current "
            "housing condition, house ownership status "
            "and whether the beneficiary family already "
            "owns a pucca house anywhere in India."
        ),

    "embarrassed_income":
        (
            "Many applicants are unsure about income "
            "eligibility.\n\n"

            "PMAY-U 2.0 includes support for categories "
            "such as EWS, LIG and other eligible groups. "
            "Income is important, but eligibility also "
            "depends on ownership and family conditions."
        ),

    "embarrassed_documents":
        (
            "Document-related concerns are one of the "
            "most common issues faced by applicants.\n\n"

            "Problems may involve Aadhaar, income proof, "
            "ownership records or address verification. "
            "Many issues can often be clarified or corrected."
        ),

    "embarrassed_family":
        (
            "Family situations such as marriage, "
            "separation, joint ownership or inherited "
            "property can sometimes make eligibility "
            "feel confusing.\n\n"

            "PMAY-U 2.0 eligibility is usually assessed "
            "based on the beneficiary family definition "
            "and ownership status."
        ),

    "embarrassed_rejection":
        (
            "Fear of rejection is understandable.\n\n"

            "However, rejection generally happens for "
            "specific reasons such as eligibility issues, "
            "document problems or ownership conditions. "
            "Understanding the reason is often the first "
            "step toward resolving it."
        ),

    # =====================================
    # TOO MANY ISSUES TOGETHER
    # =====================================

    "many_ownership":
        (
            "Ownership is one of the most important "
            "eligibility checks under PMAY-U 2.0.\n\n"

            "Authorities generally verify whether the "
            "beneficiary family owns a pucca house "
            "anywhere in India."
        ),

    "many_documents":
        (
            "Document issues may involve Aadhaar, "
            "income proof, ownership records, address "
            "proof or bank details.\n\n"

            "Identifying the exact document issue can "
            "help determine the next step."
        ),

    "many_family":
        (
            "Family-related concerns may involve marriage, "
            "joint families, separation, inheritance or "
            "ownership within the family.\n\n"

            "These situations are usually reviewed during "
            "eligibility verification."
        ),

    "many_income":
        (
            "Income plays an important role in determining "
            "eligibility under PMAY-U 2.0.\n\n"

            "Different scheme components may apply to "
            "different income categories such as EWS, "
            "LIG and MIG."
        ),

    "many_status":
        (
            "Application status concerns may include "
            "pending verification, approval delays, "
            "sanction stages or subsidy processing.\n\n"

            "Understanding the current stage can help "
            "identify what action may be needed."
        ),

    # =====================================
    # RULES FEEL CONFUSING
    # =====================================

    "rules_ownership":
        (
            "House ownership rules under PMAY-U 2.0 "
            "are important because eligibility often "
            "depends on whether the beneficiary family "
            "owns a pucca house anywhere in India.\n\n"

            "Ownership records are usually verified "
            "during the application process."
        ),

    "rules_income":
        (
            "Income rules help determine which PMAY-U 2.0 "
            "category may apply to a beneficiary.\n\n"

            "Income verification is generally used along "
            "with ownership and family details when "
            "assessing eligibility."
        ),

    "rules_family":
        (
            "Family rules usually relate to the definition "
            "of a beneficiary family.\n\n"

            "This commonly includes husband, wife and "
            "unmarried children, though verification "
            "depends on the specific situation."
        ),

    "rules_eligibility":
        (
            "PMAY-U 2.0 eligibility is typically assessed "
            "using a combination of income, ownership, "
            "family details and scheme-specific conditions.\n\n"

            "Meeting one condition alone does not always "
            "guarantee eligibility."
        ),

    # =====================================
    # WORKFLOW
    # =====================================

    "workflow_verification":
        (
            "Verification is the stage where documents, "
            "beneficiary details, ownership information "
            "and eligibility conditions are checked.\n\n"

            "Applications generally move forward after "
            "successful verification."
        ),

    "workflow_approval":
        (
            "Approval involves reviewing verified "
            "applications according to PMAY-U 2.0 "
            "guidelines and applicable scheme criteria.\n\n"

            "Approval timelines may vary depending on "
            "local processes and verification workload."
        ),

    "workflow_subsidy":
        (
            "The subsidy flow generally involves "
            "eligibility verification, approval and "
            "benefit processing under the applicable "
            "PMAY-U 2.0 component.\n\n"

            "The exact flow depends on the scheme."
        ),

    "workflow_implementation":
        (
            "Implementation refers to how PMAY-U 2.0 "
            "benefits are processed and delivered after "
            "eligibility and approval stages are completed.\n\n"

            "The process may include verification, "
            "sanction, monitoring and benefit release."
        ),
    
    # =====================================
    # PROCESS
    # =====================================

    "process_verification":
        (
            "Verification is one of the most important "
            "stages of PMAY-U 2.0. During this stage, "
            "authorities review beneficiary details, "
            "income information, ownership records and "
            "supporting documents.\n\n"

            "The purpose of verification is to confirm "
            "that the applicant satisfies the eligibility "
            "conditions of the applicable PMAY-U 2.0 component.\n\n"

            "Applications generally move to the next stage "
            "only after verification is completed."
        ),

    "process_subsidy":
        (
            "Subsidy release under PMAY-U 2.0 generally "
            "happens after eligibility verification and "
            "approval of the beneficiary.\n\n"

            "The exact process may vary depending on the "
            "scheme component and implementation stage.\n\n"

            "Delays can sometimes occur due to verification, "
            "bank account issues or administrative processing."
        ),

    "process_approval":
        (
            "Approval is the stage where verified "
            "applications are reviewed according to "
            "PMAY-U 2.0 guidelines and eligibility rules.\n\n"

            "Approval does not happen instantly and may "
            "require multiple levels of review depending "
            "on the scheme and local authority processes."
        ),

    "process_monitoring":
        (
            "Construction monitoring is generally used "
            "for housing components where physical "
            "construction or improvement work is involved.\n\n"

            "Authorities may monitor progress at different "
            "stages to ensure that assistance is being "
            "utilized according to approved guidelines."
        ),

    # =====================================
    # VILLAGE HOUSE
    # =====================================

    "village_my_house":
        (
            "If a pucca house in a village is legally "
            "owned by you, it may affect PMAY-U 2.0 "
            "eligibility.\n\n"

            "One of the key eligibility checks is whether "
            "the beneficiary family already owns a pucca "
            "house anywhere in India.\n\n"

            "Authorities generally verify ownership records "
            "before making a final determination."
        ),

    "village_family_house":
        (
            "If the village house belongs to another "
            "family member, eligibility may depend on "
            "whether that person is part of your "
            "beneficiary family.\n\n"

            "Ownership and family relationship are both "
            "important factors during PMAY-U 2.0 verification."
        ),

    "village_ancestral_house":
        (
            "Ancestral property situations can sometimes "
            "be complex under PMAY-U 2.0.\n\n"

            "Authorities may review legal ownership, "
            "inheritance records and beneficiary family "
            "details before determining eligibility.\n\n"

            "The outcome depends on the specific ownership status."
        ),

    "village_unsure":
        (
            "Many applicants are unsure whether a village "
            "house affects eligibility.\n\n"

            "The key consideration is usually who legally "
            "owns the house and whether it is considered "
            "part of the beneficiary family's housing assets."
        ),

    # =====================================
    # FAMILY HOUSE
    # =====================================

    "family_problem_parents":
        (
            "If the house belongs to your parents, PMAY-U 2.0 "
            "eligibility may depend on ownership records and "
            "beneficiary family definition.\n\n"

            "Simply living in a parent's house does not always "
            "lead to the same eligibility outcome, so verification "
            "of ownership is important."
        ),

    "family_problem_joint":
        (
            "Joint family ownership can sometimes make "
            "eligibility assessment more complicated.\n\n"

            "Authorities may review ownership shares, "
            "property records and family relationships "
            "during verification."
        ),

    "family_problem_inherited":
        (
            "Inherited property may affect PMAY-U 2.0 "
            "eligibility depending on the legal ownership "
            "position and supporting documentation.\n\n"

            "Verification generally focuses on whether "
            "the inherited property counts as a pucca house "
            "owned by the beneficiary family."
        ),

    "family_problem_unclear":
        (
            "If ownership is not clear, it may be helpful "
            "to first determine whose name appears in the "
            "property records.\n\n"

            "PMAY-U 2.0 eligibility decisions are generally "
            "based on verified ownership information."
        ),

    # =====================================
    # NO SALARY PROOF
    # =====================================

    "income_self_declaration":
        (
            "If you do not have formal salary proof, a "
            "self-declaration may sometimes be used as "
            "supporting information depending on local "
            "verification requirements.\n\n"

            "Authorities may still require additional "
            "evidence to assess income eligibility."
        ),

    "income_local_certificate":
        (
            "Certificates issued by competent local "
            "authorities may sometimes help support "
            "income verification where formal salary "
            "documents are unavailable.\n\n"

            "Acceptance depends on applicable PMAY-U 2.0 "
            "verification requirements."
        ),

    "income_informal":
        (
            "Many applicants earn income through informal "
            "or non-salaried work.\n\n"

            "In such cases, alternative supporting documents "
            "or declarations may be considered during "
            "verification, subject to local requirements."
        ),

    "income_no_proof":
        (
            "If no income proof is currently available, "
            "additional verification may be required before "
            "eligibility can be assessed.\n\n"

            "Applicants are generally advised to explore "
            "whether any alternate supporting documents or "
            "declarations can be provided."
        ),

    # =====================================
    # REJECTED
    # =====================================

    "reject_ownership":
        (
            "Ownership-related rejection may occur if "
            "records indicate that the beneficiary family "
            "owns a pucca house or if ownership information "
            "does not satisfy scheme conditions.\n\n"

            "Understanding the specific ownership issue is "
            "important before considering further action."
        ),

    "reject_income":
        (
            "Income-related rejection may occur if income "
            "criteria are not met or if submitted income "
            "information cannot be verified.\n\n"

            "The exact reason should ideally be confirmed "
            "through application records."
        ),

    "reject_documents":
        (
            "Document-related rejection may happen because "
            "of missing records, incomplete submissions or "
            "document mismatches.\n\n"

            "Reviewing the submitted documents may help "
            "identify the exact issue."
        ),

    "reject_verification":
        (
            "Verification mismatch generally means that "
            "submitted information did not match available "
            "records during the verification process.\n\n"

            "This may involve identity details, ownership, "
            "income information or other supporting records."
        ),

    # =====================================
    # PENDING TOO LONG
    # =====================================

    "pending_verification":
        (
            "If the application is still in verification, "
            "authorities may be reviewing eligibility, "
            "documents, ownership records or beneficiary details.\n\n"

            "Applications can sometimes remain at this stage "
            "until all checks are completed."
        ),

    "pending_ulb":
        (
            "ULB (Urban Local Body) review is an important "
            "stage under PMAY-U 2.0.\n\n"

            "Applications may remain pending while local "
            "authorities verify information and process approvals."
        ),

    "pending_approval":
        (
            "If the application is awaiting approval, "
            "it generally means verification has progressed "
            "and the application is under administrative review.\n\n"

            "Approval timelines may vary depending on workload "
            "and local processes."
        ),

    "pending_dbt":
        (
            "If the application is at the DBT stage, "
            "the process may involve bank verification, "
            "beneficiary confirmation and benefit transfer procedures.\n\n"

            "Delays can sometimes occur due to account "
            "mismatches or processing requirements."
        ),

    # =====================================
    # BANK ISSUE
    # =====================================

    "bank_dbt_delay":
        (
            "DBT (Direct Benefit Transfer) delays under "
            "PMAY-U 2.0 can sometimes occur due to "
            "verification checks, beneficiary validation "
            "or banking-related processing.\n\n"

            "Authorities may need to confirm account "
            "details before benefit transfer is completed. "
            "Checking the current application stage and "
            "bank account status may help identify the issue."
        ),

    "bank_inactive_account":
        (
            "If the bank account is inactive, closed or "
            "restricted, PMAY-U 2.0 benefit transfers "
            "may not be processed successfully.\n\n"

            "Applicants are generally advised to ensure "
            "that the bank account remains active and "
            "capable of receiving transfers."
        ),

    "bank_wrong_details":
        (
            "Incorrect bank account information such as "
            "account number, IFSC code or beneficiary name "
            "may create delays during PMAY-U 2.0 processing.\n\n"

            "Even small mistakes in account information "
            "can sometimes prevent successful benefit transfer."
        ),

    "bank_mismatch":
        (
            "Bank mismatch issues may occur when the "
            "beneficiary name or account details do not "
            "match PMAY-U 2.0 records.\n\n"

            "Such mismatches may delay verification, "
            "approval or DBT processing until corrected."
        ),

    # =====================================
    # AADHAAR ISSUE
    # =====================================

    "aadhaar_wrong_details":
        (
            "Incorrect Aadhaar details such as name, "
            "date of birth or other personal information "
            "may affect PMAY-U 2.0 verification.\n\n"

            "Consistency between Aadhaar and submitted "
            "application records is generally important."
        ),

    "aadhaar_address_mismatch":
        (
            "Address mismatches between Aadhaar and other "
            "submitted documents may sometimes lead to "
            "additional verification requirements.\n\n"

            "Authorities may review supporting records "
            "to confirm beneficiary details."
        ),

    "aadhaar_missing":
        (
            "If Aadhaar is unavailable or not submitted, "
            "additional verification requirements may apply "
            "depending on applicable PMAY-U 2.0 procedures.\n\n"

            "The exact requirement may vary according to "
            "local implementation guidelines."
        ),

    "aadhaar_verification":
        (
            "Aadhaar verification helps confirm the "
            "identity of the beneficiary during PMAY-U 2.0 "
            "processing.\n\n"

            "Verification issues may sometimes occur due "
            "to incorrect information, technical problems "
            "or document inconsistencies."
        ),

    # =====================================
    # RENT HOUSE
    # =====================================

    "rent_support":
        (
            "If you are looking for affordable rental "
            "housing support, ARH (Affordable Rental Housing) "
            "under PMAY-U 2.0 may be relevant.\n\n"

            "This component is intended to support eligible "
            "urban residents who need affordable rental accommodation."
        ),

    "rent_eligibility":
        (
            "Living in a rented house does not automatically "
            "make someone ineligible for PMAY-U 2.0.\n\n"

            "Eligibility is generally assessed using factors "
            "such as income, house ownership condition and "
            "beneficiary family status."
        ),

    # =====================================
    # NO LAND
    # =====================================

    "no_land_build":
        (
            "For BLC under PMAY-U 2.0, land ownership is "
            "generally an important requirement because the "
            "scheme supports construction on beneficiary-owned land.\n\n"

            "If land is not available, other PMAY-U 2.0 "
            "components may be more suitable."
        ),

    "no_land_buy":
        (
            "If you do not own land but want to purchase "
            "a house, components such as AHP under PMAY-U 2.0 "
            "may be relevant depending on eligibility.\n\n"

            "The focus in such cases is generally on housing "
            "access rather than land ownership."
        ),

    "no_land_rent":
        (
            "If land ownership is not available and your "
            "main concern is affordable accommodation, "
            "ARH under PMAY-U 2.0 may be worth exploring.\n\n"

            "This component focuses on rental housing support."
        ),

    "no_land_unsure":
        (
            "Not owning land does not automatically mean "
            "that PMAY-U 2.0 options are unavailable.\n\n"

            "The most suitable component depends on whether "
            "your goal is to buy, rent or otherwise improve "
            "your housing situation."
        ),

    # =====================================
    # DOCUMENTS
    # =====================================

    "docs_general":
        (
            "General PMAY-U 2.0 documentation commonly "
            "includes identity proof, Aadhaar, address proof, "
            "income-related documents, bank account details "
            "and other supporting records.\n\n"

            "Actual requirements may vary depending on the "
            "scheme component and verification stage."
        ),

    "docs_blc":
        (
            "BLC documentation generally includes identity "
            "proof, Aadhaar, income-related documents, bank "
            "details and land ownership records.\n\n"

            "Land ownership verification is particularly "
            "important under BLC."
        ),

    "docs_ahp":
        (
            "AHP documentation generally includes beneficiary "
            "identity records, income verification, Aadhaar, "
            "bank details and documents required by the "
            "housing project authority.\n\n"

            "Requirements may vary by project."
        ),

    "docs_arh":
        (
            "ARH requirements may include identity verification "
            "and other supporting documents required by the "
            "housing provider or implementing authority.\n\n"

            "The exact requirements depend on local implementation."
        ),

    "docs_iss":
        (
            "ISS documentation generally includes Aadhaar, "
            "income-related documents, housing loan records, "
            "bank details and other documents required for "
            "subsidy assessment.\n\n"

            "Verification requirements may vary according "
            "to the loan and scheme conditions."
        ),

    # =====================================
    # DAMAGED HOUSE
    # =====================================

    "damage_partial":
        (
            "A partially damaged house may be relevant "
            "when assessing housing condition under "
            "PMAY-U 2.0.\n\n"

            "The impact on eligibility depends on the "
            "extent of damage and applicable scheme criteria."
        ),

    "damage_severe":
        (
            "A severely damaged house may indicate a need "
            "for housing assistance, but eligibility under "
            "PMAY-U 2.0 still depends on ownership, income "
            "and other verification conditions.\n\n"

            "Housing condition may be reviewed during assessment."
        ),

    "damage_unsafe":
        (
            "If the house is unsafe to live in, housing "
            "condition may become an important consideration "
            "during PMAY-U 2.0 evaluation.\n\n"

            "Authorities may review supporting information "
            "and housing circumstances."
        ),

    "damage_improvement":
        (
            "If the primary concern is improving an existing "
            "house, certain PMAY-U 2.0 components may support "
            "housing enhancement subject to eligibility conditions.\n\n"

            "Ownership and beneficiary verification remain important."
        ),

    # =====================================
    # FAMILY ISSUE
    # =====================================

    "family_issue_ownership":
        (
            "Family ownership situations can sometimes "
            "affect PMAY-U 2.0 eligibility.\n\n"

            "Authorities generally verify whether the "
            "beneficiary family owns a pucca house anywhere "
            "in India and whose name appears in the ownership records.\n\n"

            "Ownership details are often one of the most "
            "important factors during eligibility assessment."
        ),

    "family_issue_separation":
        (
            "If separation between spouses or family members "
            "is involved, PMAY-U 2.0 eligibility may depend "
            "on the current beneficiary family situation and "
            "ownership records.\n\n"

            "Verification is usually based on documented "
            "family status rather than assumptions."
        ),

    "family_issue_inheritance":
        (
            "Inherited property can sometimes create confusion "
            "during PMAY-U 2.0 eligibility assessment.\n\n"

            "Authorities may review inheritance records, "
            "ownership status and whether the inherited "
            "property qualifies as a pucca house owned by "
            "the beneficiary family."
        ),

    "family_issue_eligibility":
        (
            "Family eligibility under PMAY-U 2.0 is generally "
            "based on the beneficiary family definition, "
            "income category and ownership condition.\n\n"

            "The assessment usually considers husband, wife "
            "and unmarried children along with housing status."
        ),

    # =====================================
    # TOO CONFUSING
    # =====================================

    "confusing_eligibility":
        (
            "Eligibility under PMAY-U 2.0 is usually determined "
            "using multiple factors including income category, "
            "house ownership condition, beneficiary family "
            "status and scheme-specific requirements.\n\n"

            "Understanding these factors one at a time often "
            "makes the process easier to follow."
        ),

    "confusing_documents":
        (
            "Document-related confusion is very common among "
            "PMAY-U 2.0 applicants.\n\n"

            "Typical requirements may include Aadhaar, "
            "identity proof, address proof, income-related "
            "documents, bank details and ownership records "
            "depending on the scheme component."
        ),

    "confusing_subsidy":
        (
            "PMAY-U 2.0 subsidy support depends on the "
            "applicable scheme component and beneficiary eligibility.\n\n"

            "The subsidy process generally involves "
            "verification, approval and benefit processing "
            "before assistance is released."
        ),

    "confusing_status":
        (
            "Application status can move through stages such as "
            "verification, review, approval, sanction and "
            "benefit processing.\n\n"

            "Knowing the current stage often helps determine "
            "what action, if any, may be required next."
        ),

    # =====================================
    # NO UPDATE
    # =====================================

    "update_pending":
        (
            "If the application is pending, authorities may "
            "still be reviewing eligibility, documents or "
            "ownership information under PMAY-U 2.0.\n\n"

            "Pending status does not automatically indicate "
            "a problem with the application."
        ),

    "update_review":
        (
            "Under Review generally means that the application "
            "is being examined by the concerned authority.\n\n"

            "This stage may involve validation of beneficiary "
            "details, eligibility checks and document review."
        ),

    "update_verification":
        (
            "Verification is the stage where documents, "
            "ownership information, income details and other "
            "eligibility conditions are checked.\n\n"

            "Applications may remain in this stage until all "
            "required verification activities are completed."
        ),

    "update_approval":
        (
            "If the application is at the approval stage, "
            "verification may already have been completed "
            "and the case is being reviewed for final approval.\n\n"

            "Approval timelines can vary depending on local "
            "processing and administrative workload."
        ),

    # =====================================
    # FRAUD FEAR
    # =====================================

    "fraud_otp":
        (
            "You should never share OTPs related to Aadhaar, "
            "bank accounts or PMAY-U 2.0 applications with "
            "unknown individuals.\n\n"

            "Fraudsters may attempt to obtain OTPs to gain "
            "unauthorized access to personal information or accounts."
        ),

    "fraud_fake_approval":
        (
            "Be cautious if someone claims your PMAY-U 2.0 "
            "application has been approved and asks for money, "
            "fees or personal information.\n\n"

            "Application status should always be verified "
            "through official channels."
        ),

    "fraud_identity":
        (
            "Identity misuse concerns may arise if you suspect "
            "someone has used your Aadhaar, personal details "
            "or documents without permission.\n\n"

            "Personal information should only be shared through "
            "trusted and authorized processes."
        ),

    "fraud_calls":
        (
            "Suspicious calls promising guaranteed PMAY-U 2.0 "
            "approval or requesting payments should be treated carefully.\n\n"

            "Applicants should avoid sharing sensitive information "
            "with unknown callers."
        ),

    # =====================================
    # SCARED TO APPLY
    # =====================================

    "scared_apply_eligibility":
        (
            "Many people are unsure whether they qualify for "
            "PMAY-U 2.0 before applying.\n\n"

            "Eligibility depends on factors such as income, "
            "house ownership, beneficiary family status and "
            "scheme-specific conditions.\n\n"

            "Checking eligibility does not automatically mean "
            "that the application will be rejected."
        ),

    "scared_apply_rejection":
        (
            "Fear of rejection is understandable, but rejection "
            "usually occurs for specific reasons such as ownership, "
            "eligibility, income or document-related issues.\n\n"

            "Understanding the actual requirements can often "
            "reduce uncertainty."
        ),

    "scared_apply_documents":
        (
            "Many applicants worry about documentation.\n\n"

            "PMAY-U 2.0 applications commonly require identity, "
            "address, income and bank-related records, though "
            "requirements vary by scheme component.\n\n"

            "Document issues can often be identified and addressed "
            "during the application process."
        ),

    "scared_apply_fraud":
        (
            "Concerns about fraud are understandable, especially "
            "when personal documents and financial information "
            "are involved.\n\n"

            "Applicants should only rely on official PMAY-U 2.0 "
            "processes and avoid sharing sensitive information "
            "with unverified individuals."
        ),

    # =====================================
    # IDK WHAT TO DO
    # =====================================

    "idk_house":
        (
            "If housing is the main concern, PMAY-U 2.0 "
            "eligibility often depends on current housing "
            "conditions and whether the beneficiary family "
            "owns a pucca house anywhere in India.\n\n"

            "Understanding your housing situation is usually "
            "the first step toward identifying the most relevant "
            "PMAY-U 2.0 support option."
        ),

    "idk_income":
        (
            "If income is the biggest concern, PMAY-U 2.0 "
            "uses income categories such as EWS, LIG and "
            "other eligible groups for different components.\n\n"

            "Income is important, but eligibility is usually "
            "assessed together with ownership and family conditions."
        ),

    "idk_documents":
        (
            "Document-related concerns are very common under "
            "PMAY-U 2.0.\n\n"

            "Issues may involve Aadhaar, income proof, address "
            "verification, ownership records or bank details.\n\n"

            "Identifying the specific document issue usually "
            "makes the next step much clearer."
        ),

    "idk_family":
        (
            "Family situations such as marriage, separation, "
            "joint ownership or inherited property can sometimes "
            "affect PMAY-U 2.0 eligibility.\n\n"

            "The beneficiary family definition and ownership "
            "status are often important during verification."
        ),

    "idk_rejection":
        (
            "If rejection is the main concern, it may be helpful "
            "to identify whether the issue involved eligibility, "
            "ownership, income or documentation.\n\n"

            "Understanding the reason for rejection is often the "
            "first step toward finding a solution."
        ),

    # =====================================
    # MIXED ISSUES
    # =====================================

    "mixed_rejection":
        (
            "If rejection seems to be the biggest issue, "
            "it may be useful to identify the specific reason "
            "provided during PMAY-U 2.0 processing.\n\n"

            "Many rejections are linked to eligibility, "
            "ownership, income or document verification concerns."
        ),

    "mixed_ownership":
        (
            "Ownership-related confusion is very common.\n\n"

            "PMAY-U 2.0 eligibility often depends on whether "
            "the beneficiary family owns a pucca house anywhere "
            "in India and whose name appears in ownership records.\n\n"

            "Ownership verification is usually an important part "
            "of the assessment process."
        ),

    "mixed_verification":
        (
            "Verification concerns may involve identity records, "
            "ownership documents, income information or beneficiary details.\n\n"

            "A verification issue does not automatically mean "
            "rejection, but it may require clarification before "
            "processing can continue."
        ),

    "mixed_fraud":
        (
            "If fraud is the main concern, it is important to "
            "determine whether the issue involves suspicious calls, "
            "identity misuse, fake approvals or unauthorized use "
            "of personal information.\n\n"

            "Sensitive information should only be shared through "
            "trusted PMAY-U 2.0 processes."
        ),

    # =====================================
    # ELIGIBLE + INELIGIBLE
    # =====================================

    "eligible_confused_ownership":
        (
            "Many applicants feel both eligible and ineligible "
            "because of ownership questions.\n\n"

            "PMAY-U 2.0 eligibility often depends on whether "
            "the beneficiary family owns a pucca house anywhere "
            "in India and how ownership is recorded."
        ),

    "eligible_confused_family":
        (
            "Family-related situations can make eligibility "
            "feel unclear.\n\n"

            "Marriage, separation, joint families and inherited "
            "property may all influence how eligibility is assessed "
            "under PMAY-U 2.0."
        ),

    "eligible_confused_income":
        (
            "Income confusion is very common because eligibility "
            "depends on income category as well as other conditions.\n\n"

            "Meeting or missing one income-related condition does "
            "not automatically determine the final outcome."
        ),

    "eligible_confused_rejection":
        (
            "Sometimes applicants worry that they are eligible "
            "but may still be rejected.\n\n"

            "Rejection is generally based on specific verification, "
            "ownership, income or document-related findings rather "
            "than assumptions."
        ),

    # =====================================
    # EVERYTHING SAYS POSSIBLY
    # =====================================

    "possibly_house":
        (
            "If housing is the biggest source of confusion, "
            "the key question is usually whether the beneficiary "
            "family owns a pucca house and what the current "
            "housing condition is.\n\n"

            "These factors play an important role in PMAY-U 2.0 eligibility."
        ),

    "possibly_family":
        (
            "Family-related eligibility can feel complicated "
            "because it depends on beneficiary family definition, "
            "ownership status and family circumstances.\n\n"

            "Clarifying the family situation often helps reduce uncertainty."
        ),

    "possibly_income":
        (
            "Income-related eligibility depends on the applicable "
            "PMAY-U 2.0 category and supporting verification.\n\n"

            "Income is important, but it is only one part of the "
            "overall eligibility assessment."
        ),

    "possibly_documents":
        (
            "When everything seems uncertain, document verification "
            "is often a good place to start.\n\n"

            "Aadhaar, ownership records, income proof and bank "
            "details are commonly reviewed during PMAY-U 2.0 processing.\n\n"

            "Ensuring these documents are accurate can help reduce confusion."
        ),

    "confused_ownership":
        (
            "Many PMAY-U 2.0 applicants feel both eligible "
            "and ineligible because of ownership-related questions.\n\n"

            "The most important check is usually whether "
            "the beneficiary family owns a pucca house "
            "anywhere in India and whose name appears in "
            "the ownership records.\n\n"

            "Clarifying ownership often resolves a large "
            "part of the eligibility confusion."
        ),

    "confused_family":
        (
            "Family situations such as marriage, separation, "
            "joint families, inheritance or living with relatives "
            "can make PMAY-U 2.0 eligibility difficult to understand.\n\n"

            "Eligibility is generally assessed using beneficiary "
            "family definitions and verified ownership details."
        ),

    "confused_income":
        (
            "Income-related confusion is very common because "
            "PMAY-U 2.0 eligibility is not based on income alone.\n\n"

            "Income category, ownership condition and family "
            "status are usually assessed together before a "
            "final eligibility determination is made."
        ),

    "confused_rejection":
        (
            "Many applicants worry about rejection even when "
            "they appear eligible.\n\n"

            "Rejection usually occurs because of specific "
            "ownership, document, income or verification "
            "issues rather than assumptions."
        ),

    "messy_ownership":
        (
            "Housing ownership situations are often more "
            "complicated than they appear.\n\n"

            "Joint ownership, inherited property, village "
            "houses and family-owned houses can all affect "
            "how PMAY-U 2.0 eligibility is assessed.\n\n"

            "The key factor is usually documented ownership."
        ),

    "messy_family":
        (
            "Many applicants have complex family situations "
            "involving marriage, separation, inheritance or "
            "joint households.\n\n"

            "PMAY-U 2.0 verification generally focuses on "
            "the beneficiary family definition and housing "
            "ownership rather than personal assumptions."
        ),

    "messy_documents":
        (
            "When a case feels complicated, documents are "
            "often the best place to start.\n\n"

            "Aadhaar, ownership records, income proof and "
            "bank details can usually help clarify eligibility "
            "and application requirements."
        ),

    "messy_rejection":
        (
            "Fear of rejection is understandable, especially "
            "when the situation feels complicated.\n\n"

            "However, PMAY-U 2.0 decisions are generally based "
            "on verified information rather than how unusual "
            "a situation sounds."
        ),

    "situation_eligibility":
        (
            "If eligibility is your main concern, the most "
            "important factors are usually house ownership, "
            "income category, beneficiary family status and "
            "scheme-specific conditions under PMAY-U 2.0.\n\n"

            "Looking at these factors individually often makes "
            "the situation easier to understand."
        ),

    "situation_family":
        (
            "Family ownership situations are one of the most "
            "common reasons applicants become uncertain about "
            "PMAY-U 2.0 eligibility.\n\n"

            "Understanding who legally owns the property is "
            "usually an important first step."
        ),

    "situation_documents":
        (
            "Document-related concerns can often be identified "
            "and resolved once the specific issue is known.\n\n"

            "Common concerns include Aadhaar, ownership proof, "
            "income records and bank account verification."
        ),

    "situation_housing":
        (
            "Your current housing condition plays an important "
            "role in determining which PMAY-U 2.0 component may "
            "be most relevant.\n\n"

            "Living on rent, in a slum, in a damaged house or "
            "without adequate housing may lead to different considerations."
        ),

    "dontknow_status":
        (
            "Application status confusion is very common.\n\n"

            "PMAY-U 2.0 applications may move through stages "
            "such as verification, review, approval, sanction "
            "and benefit processing.\n\n"

            "Knowing the current stage often helps identify "
            "the next step."
        ),

    "fake_ownership":
        (
            "Unusual ownership situations are more common than "
            "many people realize.\n\n"

            "Inherited property, shared ownership, family "
            "housing and unclear records can all affect "
            "PMAY-U 2.0 eligibility assessment."
        ),

    "fake_family":
        (
            "Complex family situations do not automatically "
            "disqualify someone from PMAY-U 2.0.\n\n"

            "Authorities generally review documented family "
            "and ownership information before making decisions."
        ),

    "fake_documents":
        (
            "If the situation seems difficult to explain, "
            "documents often provide the clearest picture.\n\n"

            "Identity records, ownership documents and income "
            "proof are commonly used during PMAY-U 2.0 verification."
        ),

    "fake_housing":
        (
            "Housing situations can sometimes sound unusual "
            "but still be valid for PMAY-U 2.0 assessment.\n\n"

            "The important factor is understanding the actual "
            "housing condition and ownership status rather than "
            "how complicated it appears."
        ),

    # =====================================
    # LIFE TOO COMPLICATED
    # =====================================

    "laugh_housing":
        (
            "Many PMAY-U 2.0 applicants have housing situations "
            "that feel complicated or difficult to explain.\n\n"

            "What usually matters most is the actual housing "
            "condition, ownership status and whether the "
            "beneficiary family already owns a pucca house "
            "anywhere in India.\n\n"

            "Complicated situations can still be assessed step by step."
        ),

    "laugh_family":
        (
            "Family conflicts, separation, joint families, "
            "inheritance issues and shared housing situations "
            "are more common than many people realize.\n\n"

            "PMAY-U 2.0 eligibility is generally based on "
            "verified family and ownership information rather "
            "than how unusual the situation sounds."
        ),

    "laugh_income":
        (
            "Income situations are not always straightforward.\n\n"

            "Many applicants have irregular, seasonal or "
            "informal sources of income.\n\n"

            "PMAY-U 2.0 verification focuses on determining "
            "eligibility based on available supporting information "
            "and applicable requirements."
        ),

    "laugh_documents":
        (
            "Document concerns are one of the most common "
            "issues faced by PMAY-U 2.0 applicants.\n\n"

            "Problems involving Aadhaar, ownership records, "
            "income proof or bank details can often be reviewed "
            "and addressed once the specific issue is identified."
        ),

    # =====================================
    # CONFLICTING ADVICE
    # =====================================

    "advice_eligibility":
        (
            "Different people often provide different opinions "
            "about PMAY-U 2.0 eligibility.\n\n"

            "Actual eligibility is generally determined through "
            "income category, ownership status, beneficiary family "
            "details and scheme-specific conditions rather than "
            "informal advice."
        ),

    "advice_ownership":
        (
            "Ownership is one of the most misunderstood parts "
            "of PMAY-U 2.0 eligibility.\n\n"

            "The important question is usually whether the "
            "beneficiary family owns a pucca house anywhere "
            "in India and how ownership is documented."
        ),

    "advice_subsidy":
        (
            "Subsidy-related information can vary because "
            "different PMAY-U 2.0 components operate differently.\n\n"

            "Understanding the applicable scheme component "
            "often helps clarify how subsidy support may work."
        ),

    "advice_process":
        (
            "Application processes may appear confusing because "
            "they involve multiple stages such as verification, "
            "review, approval and benefit processing.\n\n"

            "Understanding the current stage often makes the "
            "overall process easier to follow."
        ),

    # =====================================
    # EXHAUSTED
    # =====================================

    "exhausted_eligibility":
        (
            "If everything feels overwhelming, eligibility is "
            "often the best place to start.\n\n"

            "PMAY-U 2.0 eligibility generally depends on income, "
            "house ownership condition, beneficiary family status "
            "and applicable scheme requirements."
        ),

    "exhausted_documents":
        (
            "Starting with documents can sometimes simplify the process.\n\n"

            "Common PMAY-U 2.0 requirements may include Aadhaar, "
            "identity proof, income-related documents, ownership "
            "records and bank account details."
        ),

    "exhausted_subsidy":
        (
            "If subsidy is the main point of confusion, it may help "
            "to first identify the relevant PMAY-U 2.0 component.\n\n"

            "Eligibility and subsidy support usually depend on "
            "scheme-specific conditions."
        ),

    "exhausted_status":
        (
            "Application status can often explain where things stand.\n\n"

            "Knowing whether the application is under verification, "
            "review, approval or benefit processing can make the "
            "next steps much clearer."
        ),

    # =====================================
    # COMPLEX FAMILY
    # =====================================

    "family_complex_ownership":
        (
            "Complex ownership situations may involve family-owned "
            "property, shared ownership or unclear ownership records.\n\n"

            "PMAY-U 2.0 verification generally focuses on legal "
            "ownership and beneficiary family details."
        ),

    "family_complex_separation":
        (
            "Separation-related situations can sometimes affect "
            "eligibility assessment.\n\n"

            "Authorities generally review the current family and "
            "ownership status using supporting documentation."
        ),

    "family_complex_inheritance":
        (
            "Inherited property can create additional questions "
            "during PMAY-U 2.0 verification.\n\n"

            "The key consideration is often whether the inherited "
            "property qualifies as a pucca house owned by the "
            "beneficiary family."
        ),

    "family_complex_dependency":
        (
            "Dependency situations may involve parents, children "
            "or other family members who rely on the applicant.\n\n"

            "Such circumstances may be reviewed along with family "
            "structure and ownership information."
        ),

    # =====================================
    # HOUSE OR FAMILY FIRST
    # =====================================

    "house_or_family_house":
        (
            "If the housing situation feels most urgent, it may be "
            "helpful to first understand ownership status, current "
            "housing condition and whether the beneficiary family "
            "already owns a pucca house.\n\n"

            "These factors are often central to PMAY-U 2.0 eligibility."
        ),

    "house_or_family_family":
        (
            "If the family situation feels more urgent, it may be "
            "helpful to clarify family relationships, ownership "
            "connections and beneficiary family status first.\n\n"

            "This information is often important during PMAY-U 2.0 verification."
        ),
    # =====================================
    # PAPERWORK + FAMILY DRAMA
    # =====================================

    "drama_documents":
        (
            "When paperwork becomes the main issue, the best "
            "approach is usually to identify the exact document "
            "causing the problem.\n\n"

            "Under PMAY-U 2.0, common concerns involve Aadhaar, "
            "ownership records, income proof, address proof and "
            "bank account verification.\n\n"

            "Resolving one document issue at a time often makes "
            "the overall situation much easier to manage."
        ),

    "drama_ownership":
        (
            "Ownership-related concerns are one of the most "
            "common reasons people feel confused about PMAY-U 2.0.\n\n"

            "The key questions are usually who legally owns the "
            "property and whether the beneficiary family already "
            "owns a pucca house anywhere in India.\n\n"

            "Clarifying ownership records often helps resolve "
            "many eligibility concerns."
        ),

    "drama_family":
        (
            "Family conflicts involving property, inheritance, "
            "joint ownership, separation or dependency can make "
            "PMAY-U 2.0 eligibility feel complicated.\n\n"

            "However, eligibility is generally assessed using "
            "documented family and ownership information rather "
            "than personal opinions or family disagreements."
        ),

    # =====================================
    # HARD TO EXPLAIN
    # =====================================

    "explain_housing":
        (
            "If housing is the main concern, it may help to focus "
            "first on where you currently live, whether you own "
            "property and what kind of housing support you need.\n\n"

            "PMAY-U 2.0 housing assistance often depends on current "
            "housing condition and ownership status."
        ),

    "explain_documents":
        (
            "If your situation feels difficult to explain, documents "
            "can often provide the clearest picture.\n\n"

            "Identity records, ownership documents, income proof and "
            "bank details are commonly reviewed during PMAY-U 2.0 "
            "verification and may help clarify the situation."
        ),

    "explain_family":
        (
            "Family situations can be complicated, especially when "
            "property ownership, inheritance or living arrangements "
            "are involved.\n\n"

            "PMAY-U 2.0 verification generally focuses on documented "
            "family relationships and ownership status."
        ),

    "explain_status":
        (
            "If your concern relates to application status, it may "
            "help to first determine whether the application is under "
            "verification, review, approval or benefit processing.\n\n"

            "Knowing the stage often makes the situation easier to understand."
        ),

    # =====================================
    # RENT VS OWNERSHIP
    # =====================================

    "rent_stability":
        (
            "If your immediate priority is affordable and stable "
            "housing, rental-focused options may be more relevant "
            "than ownership-focused support.\n\n"

            "ARH (Affordable Rental Housing) under PMAY-U 2.0 is "
            "intended to support eligible beneficiaries who need "
            "affordable rental accommodation.\n\n"

            "This option may be useful when immediate housing needs "
            "are more important than long-term ownership goals."
        ),

    "future_ownership":
        (
            "If your long-term goal is to own a house, PMAY-U 2.0 "
            "components such as BLC, AHP or ISS may be more relevant "
            "depending on your circumstances.\n\n"

            "Ownership-focused support generally requires eligibility "
            "assessment based on income, ownership condition and "
            "beneficiary family status."
        ),

    # =====================================
    # ALL SCHEMES SOUND SAME
    # =====================================

    "allschemes_build":
        (
            "If your goal is to build or improve a house on land "
            "that you own, BLC (Beneficiary Led Construction) under "
            "PMAY-U 2.0 may be the most relevant component.\n\n"

            "BLC focuses on construction and enhancement of housing "
            "on beneficiary-owned land."
        ),

    "allschemes_buy":
        (
            "If you are looking to purchase a house, AHP "
            "(Affordable Housing in Partnership) under PMAY-U 2.0 "
            "may be worth exploring.\n\n"

            "This component focuses on helping eligible beneficiaries "
            "access affordable housing projects."
        ),

    "allschemes_rent":
        (
            "If your immediate need is affordable accommodation "
            "without purchasing property, ARH (Affordable Rental Housing) "
            "under PMAY-U 2.0 may be the most suitable option.\n\n"

            "This component focuses on affordable rental housing."
        ),

    "allschemes_loan":
        (
            "If housing loan burden is the main concern, ISS "
            "(Interest Subsidy Scheme) under PMAY-U 2.0 may help "
            "reduce financial pressure through eligible subsidy support.\n\n"

            "The exact benefit depends on scheme conditions and eligibility."
        ),

    # =====================================
    # ALL SCHEMES PARTIALLY FIT
    # =====================================

    "partial_blc":
        (
            "If land ownership and house construction are your "
            "highest priorities, BLC under PMAY-U 2.0 may be the "
            "closest match.\n\n"

            "This component is intended for beneficiaries who "
            "own land and require housing construction or enhancement support."
        ),

    "partial_ahp":
        (
            "If your goal is purchasing an affordable house rather "
            "than building one yourself, AHP may be more relevant.\n\n"

            "AHP focuses on access to affordable housing projects "
            "for eligible beneficiaries."
        ),

    "partial_arh":
        (
            "If rental stability is the most urgent need, ARH may "
            "be the most practical option.\n\n"

            "This component is designed to provide affordable rental "
            "housing support for eligible urban residents."
        ),

    "partial_iss":
        (
            "If the biggest concern is housing loan affordability, "
            "ISS may be the most relevant PMAY-U 2.0 component.\n\n"

            "This scheme focuses on reducing loan-related financial "
            "burden through eligible interest subsidy support."
        ),
    # =====================================
    # SHARED DOCUMENTS REGRET
    # =====================================

    "regret_identity":
        (
            "If you are worried that personal information may have "
            "been misused, it is important to understand exactly "
            "which documents were shared and with whom.\n\n"

            "Identity-related concerns may involve Aadhaar, bank "
            "details or other personal records used during PMAY-U 2.0 "
            "verification.\n\n"

            "Being cautious with sensitive information is always advisable."
        ),

    "regret_fake_application":
        (
            "If you suspect someone may have submitted or attempted "
            "to submit a PMAY-U 2.0 application using your information, "
            "the situation should be reviewed carefully.\n\n"

            "Application-related records and beneficiary information "
            "should always match the actual applicant."
        ),

    "regret_document_misuse":
        (
            "Document misuse concerns can arise when copies of Aadhaar, "
            "income records, ownership documents or bank details are "
            "shared without clear safeguards.\n\n"

            "Understanding exactly which documents were shared can help "
            "identify the level of risk."
        ),

    # =====================================
    # TRUST ISSUES
    # =====================================

    "trust_documents":
        (
            "Many PMAY-U 2.0 applicants become uncertain because "
            "different people provide different advice about documents.\n\n"

            "The most important step is identifying which specific "
            "document is causing confusion and whether it affects "
            "eligibility or verification."
        ),

    "trust_fraud":
        (
            "Fraud concerns are understandable when different people "
            "provide conflicting information.\n\n"

            "Applicants should be cautious about sharing personal "
            "information, OTPs, banking details or sensitive documents "
            "with unverified individuals."
        ),

    "trust_privacy":
        (
            "Privacy concerns usually relate to how personal information "
            "such as Aadhaar, bank records and ownership documents are used.\n\n"

            "PMAY-U 2.0 verification relies on personal information, "
            "which is why applicants often want clarity about data handling."
        ),

    "trust_approval":
        (
            "Approval-related confusion often happens because applications "
            "move through multiple stages including verification, review, "
            "approval and benefit processing.\n\n"

            "Understanding the current stage usually helps reduce uncertainty."
        ),

    # =====================================
    # WHO COUNTS AS FAMILY
    # =====================================

    "family_legal_marriage":
        (
            "Marriage-related questions are common under PMAY-U 2.0.\n\n"

            "Eligibility assessment may consider marital status, "
            "beneficiary family definition and ownership information "
            "depending on the situation."
        ),

    "family_legal_parents":
        (
            "Questions involving parents often arise when applicants "
            "live with family or when housing ownership is connected "
            "to parental property.\n\n"

            "Ownership records and beneficiary family definitions are "
            "usually important in such situations."
        ),

    "family_legal_ownership":
        (
            "Ownership and family definitions often overlap.\n\n"

            "PMAY-U 2.0 eligibility commonly considers whether the "
            "beneficiary family owns a pucca house anywhere in India "
            "and who legally owns that property."
        ),

    "family_legal_dependency":
        (
            "Dependency situations may involve children, parents or "
            "other family members who rely on the applicant.\n\n"

            "Such circumstances may be reviewed alongside family and "
            "ownership information during assessment."
        ),

    # =====================================
    # EXHAUSTION
    # =====================================

    "exhaustion_ownership":
        (
            "When everything feels overwhelming, ownership is often "
            "one of the most important issues to clarify first.\n\n"

            "Many PMAY-U 2.0 eligibility questions ultimately depend "
            "on housing ownership and beneficiary family ownership status."
        ),

    "exhaustion_verification":
        (
            "Verification concerns may involve documents, identity "
            "records, ownership information or income verification.\n\n"

            "Clarifying verification issues often resolves multiple "
            "other concerns at the same time."
        ),

    "exhaustion_rejection":
        (
            "Fear of rejection can sometimes make every part of the "
            "process feel uncertain.\n\n"

            "Understanding the actual reason for concern is often more "
            "useful than assuming rejection will occur."
        ),

    "exhaustion_housing":
        (
            "If housing stability is the biggest concern, it may help "
            "to focus first on current housing conditions and available "
            "PMAY-U 2.0 support options.\n\n"

            "Addressing the most urgent housing need can simplify the "
            "overall decision process."
        ),

    # =====================================
    # TRUST NOBODY
    # =====================================

    "trustnone_eligibility":
        (
            "Eligibility information often sounds inconsistent because "
            "different situations lead to different outcomes.\n\n"

            "PMAY-U 2.0 eligibility is generally based on verified "
            "ownership, income, family and scheme-specific conditions."
        ),

    "trustnone_privacy":
        (
            "Privacy concerns are understandable when personal records "
            "and financial information are involved.\n\n"

            "Applicants often seek clarity about how information is "
            "used during verification and benefit processing."
        ),

    "trustnone_ownership":
        (
            "Ownership questions are among the most common sources of "
            "conflicting advice in PMAY-U 2.0 discussions.\n\n"

            "The actual assessment is usually based on verified "
            "ownership records rather than assumptions."
        ),

    "trustnone_approval":
        (
            "Approval processes can appear inconsistent because "
            "applications move through multiple review stages.\n\n"

            "Understanding the current application stage often helps "
            "separate facts from assumptions."
        ),

    # =====================================
    # NEED HOUSING OR CLARITY
    # =====================================

    "clarity_housing":
        (
            "If housing stability is the most urgent need, it may be "
            "helpful to first identify your current housing situation "
            "and what type of support would be most useful.\n\n"

            "PMAY-U 2.0 includes different components for different "
            "housing needs."
        ),

    "clarity_eligibility":
        (
            "If eligibility is the biggest concern, it may help to "
            "focus first on ownership, income and beneficiary family "
            "conditions.\n\n"

            "These are usually the core factors considered during "
            "PMAY-U 2.0 assessment."
        ),

    "clarity_documents":
        (
            "Document-related clarity can often simplify the entire process.\n\n"

            "Reviewing Aadhaar, ownership records, income proof and "
            "bank information may help identify the actual issue."
        ),

    "clarity_application":
        (
            "Application confusion often comes from not knowing "
            "which stage the application is currently in.\n\n"

            "Verification, review, approval and benefit processing "
            "all involve different requirements and timelines."
        ),

    # =====================================
    # ELIGIBILITY
    # =====================================

    "eligible_own_house":
        (
            "If you already own a house, PMAY-U 2.0 eligibility "
            "may depend on the type of house, ownership details "
            "and whether the beneficiary family already owns a "
            "pucca house anywhere in India.\n\n"

            "Ownership is one of the most important eligibility "
            "checks under PMAY-U 2.0, so understanding the exact "
            "ownership situation is often the first step."
        ),

    "eligible_rent":
        (
            "Living on rent does not automatically make someone "
            "eligible or ineligible for PMAY-U 2.0.\n\n"

            "Eligibility is generally assessed using housing "
            "condition, income category, beneficiary family "
            "status and ownership information.\n\n"

            "Many eligible applicants currently live in rented accommodation."
        ),

    "eligible_unclear":
        (
            "Many people are unsure whether they qualify for "
            "PMAY-U 2.0 because their housing situation is "
            "not straightforward.\n\n"

            "Understanding where you live, whether you own "
            "property and what type of housing support you need "
            "can help identify the most relevant scheme component."
        ),

    # =====================================
    # ARH VS OWNERSHIP
    # =====================================

    "arh_better":
        (
            "ARH (Affordable Rental Housing) under PMAY-U 2.0 "
            "is generally intended for people who need affordable "
            "and stable housing without purchasing a property.\n\n"

            "It may be more suitable when immediate housing needs "
            "are the priority and long-term ownership is not the "
            "current goal."
        ),

    "ownership_better":
        (
            "Ownership-focused PMAY-U 2.0 components such as "
            "BLC, AHP or ISS are generally intended for people "
            "whose long-term goal is owning a house.\n\n"

            "The most suitable option depends on whether you "
            "want to build, buy or finance a house."
        ),

    # =====================================
    # DIFFERENCE BETWEEN SCHEMES
    # =====================================

    "difference_blc":
        (
            "BLC (Beneficiary Led Construction) under PMAY-U 2.0 "
            "is generally meant for eligible beneficiaries who "
            "own land and want to construct or improve a house.\n\n"

            "If land ownership and construction are your priorities, "
            "BLC may be the most relevant component."
        ),

    "difference_ahp":
        (
            "AHP (Affordable Housing in Partnership) focuses on "
            "providing access to affordable housing projects for "
            "eligible beneficiaries.\n\n"

            "This component is generally relevant when your goal "
            "is purchasing a house rather than constructing one."
        ),

    "difference_arh":
        (
            "ARH (Affordable Rental Housing) focuses on affordable "
            "rental accommodation rather than ownership.\n\n"

            "It is generally intended for people who need stable "
            "housing but are not currently seeking to buy a house."
        ),

    "difference_iss":
        (
            "ISS (Interest Subsidy Scheme) focuses on reducing "
            "housing loan burden through eligible subsidy support.\n\n"

            "This component is most relevant when housing finance "
            "and loan affordability are the primary concerns."
        ),

    # =====================================
    # NONE FIT ME
    # =====================================

    "fit_blc":
        (
            "If land ownership or construction is the most urgent "
            "issue, BLC may still be worth exploring even if your "
            "situation does not fit perfectly into a single category.\n\n"

            "Many applicants have circumstances that overlap "
            "multiple PMAY-U 2.0 components."
        ),

    "fit_arh":
        (
            "If rental stability is the biggest concern, ARH may "
            "be the closest match because it focuses on affordable "
            "rental housing rather than ownership.\n\n"

            "This can be useful when immediate housing stability "
            "matters more than long-term ownership."
        ),

    "fit_ahp":
        (
            "If your goal is eventually owning a house, AHP may "
            "be more relevant than rental-focused support.\n\n"

            "It focuses on helping eligible beneficiaries access "
            "affordable housing projects."
        ),

    "fit_iss":
        (
            "If loan affordability is the main challenge, ISS may "
            "be the most relevant PMAY-U 2.0 component.\n\n"

            "Its purpose is to reduce housing loan burden through "
            "eligible interest subsidy support."
        ),

    # =====================================
    # RIGHT SCHEME
    # =====================================

    "rightscheme_blc":
        (
            "If you plan to build or improve a house on land you "
            "own, BLC is often the first PMAY-U 2.0 component to review.\n\n"

            "Land ownership is generally an important requirement "
            "for this component."
        ),

    "rightscheme_ahp":
        (
            "If your objective is purchasing a house through an "
            "affordable housing project, AHP may be the most "
            "appropriate PMAY-U 2.0 option.\n\n"

            "This component focuses on housing purchase rather "
            "than construction or rental support."
        ),

    "rightscheme_arh":
        (
            "If you need affordable housing immediately but are "
            "not currently planning to purchase a property, ARH "
            "may be the most suitable PMAY-U 2.0 component.\n\n"

            "Its primary focus is rental housing support."
        ),

    "rightscheme_iss":
        (
            "If housing loan burden is your main concern, ISS may "
            "be the most relevant component because it focuses on "
            "eligible interest subsidy support.\n\n"

            "This can help reduce the cost of housing finance."
        ),

    # =====================================
    # STRESS
    # =====================================

    "stress_delay":
        (
            "Approval delays can happen for various reasons, "
            "including verification workload, document review "
            "or administrative processing.\n\n"

            "A delay does not automatically indicate rejection "
            "or a problem with the application."
        ),

    "stress_rejection":
        (
            "Rejection concerns are common, especially when there "
            "has been little communication about the application.\n\n"

            "Actual decisions are generally based on verified "
            "eligibility, ownership, income and document information."
        ),

    "stress_updates":
        (
            "Lack of updates can make the process feel uncertain.\n\n"

            "Applications often move through verification, review, "
            "approval and benefit-processing stages before a final "
            "outcome is visible."
        ),

    # =====================================
    # WHERE TO START
    # =====================================

    "start_house":
        (
            "Housing is often the best place to start because "
            "PMAY-U 2.0 eligibility is closely connected to "
            "current housing condition and ownership status.\n\n"

            "Understanding your housing situation can help narrow "
            "down the most relevant scheme component."
        ),

    "start_documents":
        (
            "Documents are often the foundation of the PMAY-U 2.0 "
            "process.\n\n"

            "Reviewing Aadhaar, ownership records, income proof "
            "and bank details can help identify potential issues early."
        ),

    "start_money":
        (
            "Financial concerns may involve income eligibility, "
            "housing affordability or loan-related stress.\n\n"

            "Understanding the financial challenge often helps "
            "identify the most suitable PMAY-U 2.0 option."
        ),

    "start_family":
        (
            "Family situations can influence eligibility when "
            "ownership, inheritance, dependency or marital status "
            "are involved.\n\n"

            "Clarifying family-related details is often an important step."
        ),

    "start_status":
        (
            "If you already have an application, understanding "
            "its current stage can be a good starting point.\n\n"

            "Verification, review, approval and benefit processing "
            "each involve different checks and timelines."
        ),
    # =====================================
    # MESSED UP APPLICATION
    # =====================================

    "messed_documents":
        (
            "Document-related mistakes are among the most common "
            "issues faced by PMAY-U 2.0 applicants.\n\n"

            "Problems may involve Aadhaar details, ownership "
            "documents, income proof, address records or missing files.\n\n"

            "In many cases, identifying the exact document issue "
            "is the first step toward resolving the concern."
        ),

    "messed_details":
        (
            "Application detail errors can include incorrect names, "
            "addresses, family information, income details or other entries.\n\n"

            "Small mistakes do not automatically mean rejection, "
            "but they may affect verification and processing.\n\n"

            "Reviewing the submitted information carefully can help "
            "identify the actual issue."
        ),

    "messed_bank":
        (
            "Bank-related concerns may involve account details, "
            "DBT information, inactive accounts or verification mismatches.\n\n"

            "Since PMAY-U 2.0 benefits often rely on verified bank "
            "information, accuracy is important during processing."
        ),

    "messed_scheme":
        (
            "Many applicants worry that they selected the wrong "
            "PMAY-U 2.0 component.\n\n"

            "The most suitable scheme generally depends on whether "
            "you want to build, buy, rent or reduce housing loan burden.\n\n"

            "Understanding your actual housing need can help determine "
            "whether the selected scheme is appropriate."
        ),

    # =====================================
    # SHOULD I APPLY
    # =====================================

    "hesitate_eligibility":
        (
            "Many people hesitate because they are unsure about eligibility.\n\n"

            "PMAY-U 2.0 eligibility is generally assessed using "
            "income category, housing ownership condition, "
            "beneficiary family status and applicable scheme rules.\n\n"

            "Being uncertain does not automatically mean you are ineligible."
        ),

    "hesitate_rejection":
        (
            "Fear of rejection is very common among applicants.\n\n"

            "However, PMAY-U 2.0 decisions are generally based on "
            "verified information such as ownership, income and "
            "document records rather than assumptions.\n\n"

            "Understanding the requirements often reduces this concern."
        ),

    "hesitate_documents":
        (
            "Document concerns are one of the biggest reasons people "
            "delay applying under PMAY-U 2.0.\n\n"

            "Most issues become easier to manage once the specific "
            "missing, incorrect or unclear document is identified."
        ),

    "hesitate_housing":
        (
            "Many applicants are unsure whether their housing situation "
            "qualifies under PMAY-U 2.0.\n\n"

            "Current housing condition, ownership status and beneficiary "
            "family circumstances are usually important factors during assessment."
        ),

    # =====================================
    # PEOPLE GET CONFUSED
    # =====================================

    "confuse_house":
        (
            "Housing situations can be more complicated than they seem.\n\n"

            "Village houses, inherited property, shared ownership, "
            "rental accommodation and damaged houses can all create "
            "eligibility questions under PMAY-U 2.0.\n\n"

            "The important part is understanding the actual housing condition."
        ),

    "confuse_family":
        (
            "Family situations involving marriage, separation, "
            "inheritance or joint households often create confusion.\n\n"

            "PMAY-U 2.0 assessment generally focuses on beneficiary "
            "family definitions and verified ownership information."
        ),

    "confuse_documents":
        (
            "If people become confused when you explain your case, "
            "documents often provide the clearest picture.\n\n"

            "Identity records, ownership proof, income documents "
            "and bank information usually help clarify the situation."
        ),

    "confuse_income":
        (
            "Income-related situations can be difficult to explain, "
            "especially when earnings are irregular, seasonal or informal.\n\n"

            "PMAY-U 2.0 assessment generally considers income alongside "
            "other eligibility factors rather than in isolation."
        ),

    # =====================================
    # EVERY ANSWER CREATES NEW CONFUSION
    # =====================================

    "newconfusion_eligibility":
        (
            "Eligibility questions often lead to additional confusion "
            "because multiple conditions may apply at the same time.\n\n"

            "Income, ownership, beneficiary family status and scheme "
            "requirements are usually assessed together under PMAY-U 2.0."
        ),

    "newconfusion_subsidy":
        (
            "Subsidy-related confusion is common because different "
            "PMAY-U 2.0 components provide different types of support.\n\n"

            "Understanding the applicable scheme is often the first "
            "step toward understanding subsidy eligibility."
        ),

    "newconfusion_documents":
        (
            "Documents can affect many parts of the application process.\n\n"

            "Verification, approval and benefit processing often depend "
            "on accurate and complete records."
        ),

    "newconfusion_status":
        (
            "Application status can feel confusing because cases move "
            "through several stages such as verification, review, "
            "approval and benefit processing.\n\n"

            "Knowing the current stage often helps reduce uncertainty."
        ),

    # =====================================
    # SOUNDS FAKE
    # =====================================

    "fakecase_ownership":
        (
            "Ownership situations are frequently more complicated "
            "than people expect.\n\n"

            "Family-owned property, inherited houses and shared "
            "ownership arrangements can all affect PMAY-U 2.0 assessment.\n\n"

            "Unusual ownership situations are not uncommon."
        ),

    "fakecase_family":
        (
            "Complex family situations occur much more often than "
            "many applicants realize.\n\n"

            "PMAY-U 2.0 verification generally focuses on documented "
            "family relationships and ownership records rather than "
            "how unusual the situation sounds."
        ),

    "fakecase_housing":
        (
            "Housing situations do not need to fit a simple pattern "
            "to be assessed under PMAY-U 2.0.\n\n"

            "The important factor is understanding the actual housing "
            "condition and support requirement."
        ),

    # =====================================
    # NO HOUSE BUT FEEL INELIGIBLE
    # =====================================

    "nohouse_land":
        (
            "Even if you do not own a house, land ownership can still "
            "be an important factor when evaluating PMAY-U 2.0 options.\n\n"

            "Certain components may be more relevant for beneficiaries "
            "who own land but do not have adequate housing."
        ),

    "nohouse_family_property":
        (
            "Many applicants become uncertain because property is owned "
            "by parents, relatives or other family members.\n\n"

            "PMAY-U 2.0 eligibility often depends on beneficiary family "
            "ownership conditions and documented property records."
        ),

    "nohouse_unsure":
        (
            "It is common to feel uncertain about eligibility even "
            "when you do not personally own a house.\n\n"

            "Questions about family property, land ownership, housing "
            "conditions and beneficiary family status often create confusion.\n\n"

            "Clarifying these factors usually helps determine which "
            "PMAY-U 2.0 component may be relevant."
        ),
    # =====================================
    # FAMILY TOO MESSY
    # =====================================

    "messyfamily_marriage":
        (
            "Marriage-related situations can sometimes affect "
            "PMAY-U 2.0 eligibility assessment.\n\n"

            "Questions often arise about beneficiary family "
            "definition, ownership status and household details.\n\n"

            "Clarifying current family circumstances is usually "
            "an important first step."
        ),

    "messyfamily_separation":
        (
            "Separation-related situations can create confusion "
            "about family status and housing eligibility.\n\n"

            "PMAY-U 2.0 assessment generally relies on current "
            "family and ownership information supported by records."
        ),

    "messyfamily_inheritance":
        (
            "Inherited property can sometimes affect PMAY-U 2.0 "
            "eligibility depending on ownership status and the "
            "type of property involved.\n\n"

            "Understanding who legally owns the property is often important."
        ),

    "messyfamily_dependency":
        (
            "Dependency situations involving parents, children "
            "or other family members can influence how a household "
            "is assessed under PMAY-U 2.0.\n\n"

            "Family structure and ownership information are often reviewed together."
        ),

    # =====================================
    # EMBARRASSED ASKING QUESTIONS
    # =====================================

    "embarrassed_eligibility":
        (
            "Many applicants are unsure about eligibility and "
            "ask similar questions.\n\n"

            "PMAY-U 2.0 eligibility usually depends on housing "
            "ownership, beneficiary family status, income category "
            "and scheme-specific conditions.\n\n"

            "Basic questions are often the best place to start."
        ),

    "embarrassed_subsidy":
        (
            "Subsidy-related questions are among the most common "
            "PMAY-U 2.0 concerns.\n\n"

            "Different scheme components provide different forms "
            "of support, which is why subsidy information can seem confusing."
        ),

    "embarrassed_status":
        (
            "Application status questions are extremely common.\n\n"

            "PMAY-U 2.0 applications may move through verification, "
            "review, approval and benefit-processing stages.\n\n"

            "Understanding the current stage often answers many questions."
        ),

    "embarrassed_documents":
        (
            "Document-related doubts are normal.\n\n"

            "Applicants often seek clarification regarding Aadhaar, "
            "ownership proof, income documents, address proof and "
            "bank account information."
        ),

    # =====================================
    # EVERYONE UNDERSTANDS EXCEPT ME
    # =====================================

    "everyone_eligibility":
        (
            "Many people feel confused about PMAY-U 2.0 eligibility "
            "because multiple conditions are considered together.\n\n"

            "Income, ownership, beneficiary family details and "
            "scheme-specific requirements all play a role."
        ),

    "everyone_documents":
        (
            "Documents can feel overwhelming at first.\n\n"

            "Breaking them into categories such as identity proof, "
            "ownership proof, income verification and bank details "
            "usually makes the process easier to understand."
        ),

    "everyone_subsidy":
        (
            "Subsidy information often sounds complicated because "
            "different PMAY-U 2.0 components offer different benefits.\n\n"

            "Understanding the relevant scheme is usually the first step."
        ),

    "everyone_scheme":
        (
            "Choosing the right PMAY-U 2.0 component is one of the "
            "most common areas of confusion.\n\n"

            "The correct option generally depends on whether you "
            "want to build, buy, rent or reduce housing loan burden."
        ),

    # =====================================
    # QUALIFY OR DESPERATE
    # =====================================

    "desperate_house":
        (
            "Owning a house does not automatically determine PMAY-U 2.0 eligibility.\n\n"

            "Eligibility may depend on the type of house, ownership "
            "records and whether the beneficiary family owns a "
            "pucca house anywhere in India."
        ),

    "desperate_rent":
        (
            "Many eligible PMAY-U 2.0 applicants currently live "
            "in rented accommodation.\n\n"

            "Living on rent is often considered together with "
            "income, ownership and housing conditions."
        ),

    "desperate_instability":
        (
            "Housing instability is a genuine concern and may be "
            "relevant when evaluating PMAY-U 2.0 support options.\n\n"

            "Current housing conditions are often an important part "
            "of the assessment process."
        ),

    # =====================================
    # OVERTHINKING
    # =====================================

    "overthink_eligibility":
        (
            "Many applicants spend a lot of time worrying about "
            "eligibility before understanding the actual requirements.\n\n"

            "PMAY-U 2.0 eligibility is usually based on objective "
            "conditions such as ownership, income and beneficiary family status."
        ),

    "overthink_money":
        (
            "Financial concerns are one of the most common reasons "
            "people feel uncertain about applying.\n\n"

            "Income category, affordability concerns and loan-related "
            "questions are often reviewed separately."
        ),

    "overthink_documents":
        (
            "Document concerns can feel overwhelming until the exact "
            "issue is identified.\n\n"

            "Most PMAY-U 2.0 document questions involve identity, "
            "ownership, income or banking information."
        ),

    "overthink_delays":
        (
            "Application delays often create unnecessary stress.\n\n"

            "Delays can occur for many administrative reasons and do "
            "not automatically indicate rejection or ineligibility."
        ),

    # =====================================
    # STABLE PLACE TO LIVE
    # =====================================

    "stable_rental":
        (
            "If your main goal is affordable and stable housing, "
            "rental-focused support may be the most relevant option.\n\n"

            "ARH (Affordable Rental Housing) under PMAY-U 2.0 focuses "
            "on providing affordable rental accommodation for eligible beneficiaries."
        ),

    "stable_ownership":
        (
            "If your long-term goal is owning a house, PMAY-U 2.0 "
            "components such as BLC, AHP or ISS may be more relevant.\n\n"

            "The appropriate option depends on whether you plan to "
            "build, buy or finance a house."
        ),

    "stable_construction":
        (
            "If you already have access to land and want to build "
            "or improve a house, construction-related support may "
            "be worth exploring.\n\n"

            "BLC (Beneficiary Led Construction) under PMAY-U 2.0 "
            "focuses on housing construction and enhancement."
        ),
    # =====================================
    # BEFORE I GIVE UP
    # =====================================

    "giveup_house":
        (
            "Before giving up on PMAY-U 2.0, it may help to first "
            "understand how your housing ownership situation affects eligibility.\n\n"

            "Ownership of a pucca house by the beneficiary family "
            "is one of the most important factors considered during assessment.\n\n"

            "Clarifying ownership details often answers many eligibility questions."
        ),

    "giveup_rent":
        (
            "Many PMAY-U 2.0 applicants currently live in rented accommodation.\n\n"

            "Living on rent does not automatically make someone "
            "eligible or ineligible. Housing condition, ownership "
            "status and income category are usually considered together.\n\n"

            "Understanding these factors may help determine whether "
            "PMAY-U 2.0 is worth exploring further."
        ),

    "giveup_instability":
        (
            "If housing instability is a major concern, PMAY-U 2.0 "
            "may still be worth reviewing before making a decision.\n\n"

            "The scheme is intended to support eligible beneficiaries "
            "facing housing-related challenges through different components.\n\n"

            "Understanding your housing condition is often the first step."
        ),

    # =====================================
    # SHOULD I EVEN TRY
    # =====================================

    "shouldtry_eligibility":
        (
            "Many people hesitate because they are unsure whether "
            "they qualify under PMAY-U 2.0.\n\n"

            "Eligibility generally depends on factors such as "
            "housing ownership, beneficiary family status, income "
            "category and scheme-specific conditions.\n\n"

            "Being uncertain does not necessarily mean you are ineligible."
        ),

    "shouldtry_documents":
        (
            "Document concerns are one of the most common reasons "
            "people delay or avoid applying.\n\n"

            "In many situations, identifying the exact missing or "
            "unclear document makes the process much easier to understand.\n\n"

            "Document issues are often more manageable than they first appear."
        ),

    "shouldtry_rejection":
        (
            "Fear of rejection is very common among applicants.\n\n"

            "However, PMAY-U 2.0 decisions are generally based on "
            "verified eligibility information rather than assumptions.\n\n"

            "Understanding the actual requirements often helps reduce this worry."
        ),

    "shouldtry_housing":
        (
            "If housing needs are genuine, it may be worthwhile to "
            "understand available PMAY-U 2.0 options before deciding not to apply.\n\n"

            "Different scheme components address different housing situations."
        ),

    # =====================================
    # OVERWHELMED
    # =====================================

    "overwhelmed_house":
        (
            "When everything feels overwhelming, housing is often "
            "a good place to start.\n\n"

            "Current housing condition, ownership status and living "
            "arrangements play an important role in PMAY-U 2.0 assessment.\n\n"

            "Clarifying housing details can simplify many other questions."
        ),

    "overwhelmed_family":
        (
            "Family situations involving marriage, separation, "
            "inheritance or shared housing can create uncertainty.\n\n"

            "PMAY-U 2.0 generally evaluates documented family and "
            "ownership information rather than personal circumstances alone."
        ),

    "overwhelmed_money":
        (
            "Financial concerns are among the most common challenges "
            "faced by applicants.\n\n"

            "Income category, affordability concerns and housing "
            "loan burden may all affect which PMAY-U 2.0 component "
            "is most relevant."
        ),

    "overwhelmed_documents":
        (
            "Document concerns can feel overwhelming when combined "
            "with other issues.\n\n"

            "Breaking the problem into identity, ownership, income "
            "and banking documents often makes the process easier to manage."
        ),

    # =====================================
    # DON'T UNDERSTAND PMAY
    # =====================================

    "understand_eligibility":
        (
            "Eligibility is often the best place to begin learning "
            "about PMAY-U 2.0.\n\n"

            "Eligibility generally depends on ownership condition, "
            "beneficiary family status, income category and applicable scheme rules."
        ),

    "understand_documents":
        (
            "Documents are an important part of PMAY-U 2.0 verification.\n\n"

            "Applicants commonly need identity, ownership, income "
            "and banking-related records depending on the situation."
        ),

    "understand_subsidy":
        (
            "Subsidy-related questions are very common because "
            "different PMAY-U 2.0 components offer different benefits.\n\n"

            "Understanding the relevant scheme component often makes subsidy rules clearer."
        ),

    "understand_scheme":
        (
            "PMAY-U 2.0 includes different components because "
            "housing needs are not the same for everyone.\n\n"

            "Some people need rental support, some need ownership "
            "support, while others need assistance with construction "
            "or housing finance."
        ),

    # =====================================
    # DON'T KNOW CATEGORY
    # =====================================

    "category_build":
        (
            "If your goal is to build or improve a house on land "
            "you own, construction-focused support may be most relevant.\n\n"

            "BLC under PMAY-U 2.0 is generally intended for eligible "
            "beneficiaries requiring housing construction or enhancement."
        ),

    "category_buy":
        (
            "If your goal is purchasing a house, ownership-focused "
            "housing support may be more relevant than rental assistance.\n\n"

            "Affordable housing project options may be worth exploring."
        ),

    "category_rent":
        (
            "If your immediate priority is affordable accommodation, "
            "rental-focused housing support may be more relevant.\n\n"

            "ARH under PMAY-U 2.0 focuses on affordable rental housing."
        ),

    "category_loan":
        (
            "If loan affordability is the biggest concern, housing "
            "finance support may be more relevant than construction "
            "or rental assistance.\n\n"

            "ISS under PMAY-U 2.0 focuses on eligible interest subsidy support."
        ),

    # =====================================
    # PMAY WORTH TRYING
    # =====================================

    "worth_house":
        (
            "Whether PMAY-U 2.0 is worth pursuing often depends on "
            "how housing ownership affects your situation.\n\n"

            "Understanding ownership details is usually one of the "
            "first steps when evaluating eligibility."
        ),

    "worth_nohouse":
        (
            "If you do not own a house, PMAY-U 2.0 may still be "
            "worth understanding before making a decision.\n\n"

            "Eligibility depends on several factors, but lack of "
            "adequate housing is often an important consideration."
        ),

    "worth_difficulties":
        (
            "If you are experiencing housing difficulties, PMAY-U 2.0 "
            "may provide relevant support depending on your circumstances.\n\n"

            "The most suitable option depends on the nature of the housing challenge."
        ),

    # =====================================
    # CONFUSING FOR NORMAL PEOPLE
    # =====================================

    "normal_eligibility":
        (
            "Many applicants initially find eligibility rules confusing.\n\n"

            "PMAY-U 2.0 eligibility usually depends on a combination "
            "of ownership, income, family and housing-related factors."
        ),

    "normal_documents":
        (
            "Document requirements can seem complicated until they "
            "are grouped into simple categories.\n\n"

            "Identity proof, ownership records, income documents "
            "and banking information are common examples."
        ),

    "normal_subsidy":
        (
            "Subsidy rules can appear confusing because different "
            "PMAY-U 2.0 components provide different forms of assistance.\n\n"

            "Understanding the scheme component usually helps clarify the benefit."
        ),

    "normal_status":
        (
            "Application status can be difficult to understand because "
            "cases move through multiple processing stages.\n\n"

            "Verification, review, approval and benefit processing "
            "each serve different purposes within PMAY-U 2.0."
        ),
    # =====================================
    # WORTH CHECKING
    # =====================================

    "worthcheck_house":
        (
            "Whether PMAY-U 2.0 is worth exploring often depends "
            "on your housing ownership situation.\n\n"

            "Eligibility commonly considers whether the beneficiary "
            "family owns a pucca house anywhere in India and the "
            "current housing condition.\n\n"

            "Understanding ownership details can help determine "
            "whether PMAY-U 2.0 may be relevant to your case."
        ),

    "worthcheck_rent":
        (
            "Many PMAY-U 2.0 beneficiaries currently live in "
            "rented accommodation before applying.\n\n"

            "Living on rent does not automatically determine "
            "eligibility, but it may be an important factor when "
            "evaluating housing needs and scheme suitability.\n\n"

            "Understanding your overall housing situation is usually "
            "a good first step."
        ),

    "worthcheck_difficulty":
        (
            "If you are facing housing-related difficulties, "
            "PMAY-U 2.0 may be worth reviewing before deciding "
            "whether to apply.\n\n"

            "Different PMAY-U 2.0 components address different "
            "housing needs such as ownership, construction, rental "
            "housing or housing finance support."
        ),

    # =====================================
    # CONFLICTING RULES
    # =====================================

    "conflict_ownership":
        (
            "Ownership-related situations are one of the most "
            "common reasons applicants feel that PMAY-U 2.0 rules "
            "conflict with each other.\n\n"

            "Family-owned property, inherited houses, shared "
            "ownership and village property can all create "
            "eligibility questions.\n\n"

            "Clarifying ownership status often resolves much of the confusion."
        ),

    "conflict_income":
        (
            "Income-related confusion can occur when applicants "
            "are unsure which income category applies to them.\n\n"

            "PMAY-U 2.0 eligibility generally considers income "
            "alongside ownership and family conditions rather "
            "than using income alone."
        ),

    "conflict_family":
        (
            "Family situations involving marriage, separation, "
            "joint households or dependency can sometimes make "
            "PMAY-U 2.0 eligibility difficult to interpret.\n\n"

            "Beneficiary family definitions and ownership records "
            "are often reviewed together."
        ),

    "conflict_housing":
        (
            "Housing-related questions can arise when the current "
            "living situation does not fit a simple category.\n\n"

            "PMAY-U 2.0 assessment often considers the actual "
            "housing condition along with ownership and family information."
        ),

    # =====================================
    # QUALIFY + DISQUALIFY
    # =====================================

    "qualify_ownership":
        (
            "Many applicants feel both eligible and ineligible "
            "because of ownership-related concerns.\n\n"

            "The key question is often whether the beneficiary "
            "family owns a pucca house anywhere in India and how "
            "ownership is documented.\n\n"

            "Ownership details frequently determine which PMAY-U 2.0 "
            "conditions apply."
        ),

    "qualify_family":
        (
            "Family circumstances can sometimes create mixed signals "
            "about eligibility.\n\n"

            "Marriage, separation, inheritance and household "
            "structure may all affect how PMAY-U 2.0 conditions "
            "are interpreted."
        ),

    "qualify_income":
        (
            "Income-related uncertainty is very common.\n\n"

            "PMAY-U 2.0 eligibility generally depends on income "
            "category together with ownership, family status and "
            "scheme-specific requirements.\n\n"

            "Meeting one condition does not automatically determine "
            "the final outcome."
        ),

    # =====================================
    # PORTAL FEAR
    # =====================================

    "portal_login":
        (
            "Login problems can make the PMAY-U 2.0 process feel "
            "more difficult than the eligibility rules themselves.\n\n"

            "Many login issues are related to credentials, "
            "verification requirements or account access problems "
            "rather than eligibility concerns."
        ),

    "portal_tracking":
        (
            "Application tracking can be confusing, especially when "
            "status updates are delayed or difficult to interpret.\n\n"

            "Understanding the current processing stage often helps "
            "clarify what is happening."
        ),

    "portal_status":
        (
            "Status information can sometimes create anxiety when "
            "the meaning of a stage is unclear.\n\n"

            "PMAY-U 2.0 applications may pass through verification, "
            "review, approval and benefit-processing stages."
        ),

    "portal_error":
        (
            "Technical errors do not automatically indicate a problem "
            "with eligibility or application quality.\n\n"

            "Portal-related issues can occur for a variety of "
            "technical reasons and are often separate from the "
            "actual PMAY-U 2.0 assessment process."
        ),

    # =====================================
    # PORTAL OR MY MISTAKE
    # =====================================

    "mistake_login":
        (
            "If login is the main issue, the problem may be related "
            "to account access, credentials or verification rather "
            "than the application itself.\n\n"

            "Identifying the exact login difficulty is usually the "
            "first step toward resolving it."
        ),

    "mistake_tracking":
        (
            "Tracking concerns often arise when applicants are unsure "
            "whether the application is progressing normally.\n\n"

            "Knowing the current PMAY-U 2.0 stage can help determine "
            "whether there is an actual issue."
        ),

    "mistake_upload":
        (
            "Document upload problems are among the most common "
            "portal-related concerns.\n\n"

            "Issues may involve file format, document quality, "
            "upload completion or verification requirements."
        ),

    "mistake_status":
        (
            "Status visibility concerns do not always indicate an error.\n\n"

            "Applications may take time to move between verification, "
            "review and approval stages, which can sometimes make "
            "the process appear inactive."
        ),
    # =====================================
    # TECHNOLOGY FEAR
    # =====================================

    "tech_login":
        (
            "Login issues are one of the most common frustrations "
            "for PMAY-U 2.0 applicants.\n\n"

            "Problems may involve account access, verification "
            "requirements or credential-related difficulties.\n\n"

            "In many cases, login issues are technical and separate "
            "from eligibility or application approval."
        ),

    "tech_tracking":
        (
            "Application tracking can feel confusing when there are "
            "few updates or unfamiliar status messages.\n\n"

            "PMAY-U 2.0 applications typically move through stages "
            "such as verification, review, approval and benefit processing.\n\n"

            "Understanding the stage often makes tracking easier."
        ),

    "tech_updates":
        (
            "Delayed or unclear updates can make applicants feel "
            "that nothing is happening.\n\n"

            "However, applications may continue moving through "
            "internal processing stages even when visible updates "
            "are limited."
        ),

    "tech_upload":
        (
            "Document upload issues are among the most common "
            "technical concerns.\n\n"

            "File quality, format, size or verification requirements "
            "can sometimes affect successful submission under PMAY-U 2.0."
        ),

    # =====================================
    # PAPERWORK HARDER THAN ELIGIBILITY
    # =====================================

    "paper_identity":
        (
            "Identity-related paperwork issues often involve name "
            "differences, missing details or inconsistencies between records.\n\n"

            "Accurate identity information is important because it "
            "is commonly used during PMAY-U 2.0 verification."
        ),

    "paper_ownership":
        (
            "Ownership proof can sometimes be more confusing than "
            "eligibility rules themselves.\n\n"

            "Property records, inheritance documents and ownership "
            "evidence may all play a role depending on the situation.\n\n"

            "Clear ownership information is often important for assessment."
        ),

    "paper_address":
        (
            "Address-related confusion may occur when different "
            "documents show different addresses or outdated information.\n\n"

            "Address verification can be an important part of "
            "PMAY-U 2.0 processing."
        ),

    # =====================================
    # DOCUMENTS TELL DIFFERENT STORIES
    # =====================================

    "docs_name":
        (
            "Name mismatches across documents are a common source "
            "of verification concerns.\n\n"

            "Differences in spelling, initials or record updates "
            "can sometimes create confusion during processing."
        ),

    "docs_address":
        (
            "Address mismatches often occur when records have not "
            "been updated consistently across documents.\n\n"

            "Verification may become easier once address information "
            "is aligned where necessary."
        ),

    "docs_ownership":
        (
            "Ownership-related document differences can create "
            "uncertainty about eligibility.\n\n"

            "The most important factor is usually understanding "
            "which records accurately reflect the property's ownership status."
        ),

    "docs_family":
        (
            "Family-related document differences may involve "
            "household composition, dependency information or "
            "beneficiary family records.\n\n"

            "Clarifying family information often helps resolve confusion."
        ),

    # =====================================
    # DBT CONFUSION
    # =====================================

    "dbt_bank":
        (
            "DBT (Direct Benefit Transfer) generally relies on "
            "verified banking information.\n\n"

            "Many applicants are mainly concerned about whether "
            "their bank account information is correctly linked "
            "for benefit processing under PMAY-U 2.0."
        ),

    "dbt_timing":
        (
            "Questions about subsidy timing are very common.\n\n"

            "Applicants often want to understand when benefits "
            "may be processed and how DBT-related payments are handled.\n\n"

            "Processing timelines can vary depending on verification and approvals."
        ),

    "dbt_tracking":
        (
            "Payment tracking concerns usually involve understanding "
            "whether a benefit has been processed, transferred or is "
            "still under review.\n\n"

            "Knowing the current application stage often helps explain the status."
        ),

    # =====================================
    # NOBODY EXPLAINED DBT
    # =====================================

    "dbt_money":
        (
            "Many applicants simply want to understand where "
            "PMAY-U 2.0 benefits are directed.\n\n"

            "DBT generally refers to benefits being processed "
            "through verified banking channels rather than through intermediaries."
        ),

    "dbt_payment":
        (
            "Payment timing is one of the most common DBT-related questions.\n\n"

            "Benefit processing typically depends on successful "
            "verification, approvals and completion of required stages."
        ),

    "dbt_linking":
        (
            "Bank linking concerns usually involve ensuring that "
            "the correct account information is available for benefit processing.\n\n"

            "Accurate banking details can be important for smooth DBT transactions."
        ),

    # =====================================
    # HOUSING LOAN STRESS
    # =====================================

    "loan_emi":
        (
            "EMI burden is often the biggest concern for applicants "
            "considering housing finance support.\n\n"

            "ISS (Interest Subsidy Scheme) under PMAY-U 2.0 focuses "
            "on helping eligible beneficiaries reduce loan-related pressure."
        ),

    "loan_subsidy":
        (
            "Subsidy timing can create uncertainty, especially for "
            "people already managing housing loan commitments.\n\n"

            "Many applicants want clarity on how subsidy processing "
            "fits into the overall PMAY-U 2.0 process."
        ),

    "loan_approval":
        (
            "Approval uncertainty can make housing finance feel even "
            "more stressful.\n\n"

            "Verification, review and approval stages all influence "
            "when final decisions become available under PMAY-U 2.0."
        ),
    # =====================================
    # FINANCE LANGUAGE
    # =====================================

    "finance_loan":
        (
            "Housing loan terms can seem complicated when first "
            "encountering PMAY-U 2.0 information.\n\n"

            "A housing loan is generally the amount borrowed for "
            "purchasing, constructing or improving a house, which "
            "is then repaid through regular installments.\n\n"

            "Understanding loan basics often makes other PMAY-U 2.0 "
            "financial concepts easier to understand."
        ),

    "finance_subsidy":
        (
            "A subsidy is generally a financial benefit intended to "
            "reduce the overall housing-related burden for eligible beneficiaries.\n\n"

            "Under PMAY-U 2.0, subsidy-related support depends on "
            "scheme conditions and eligibility requirements.\n\n"

            "Understanding subsidy concepts often helps applicants "
            "make better housing decisions."
        ),

    "finance_dbt":
        (
            "DBT stands for Direct Benefit Transfer.\n\n"

            "In simple terms, it refers to eligible benefits being "
            "processed through verified banking channels rather than "
            "through intermediaries.\n\n"

            "Understanding DBT basics often helps reduce confusion "
            "about payments and benefit processing."
        ),

    # =====================================
    # ALL SCHEMES SOUND USEFUL
    # =====================================

    "alluseful_blc":
        (
            "If your goal is to construct or improve a house on "
            "land you own, BLC (Beneficiary Led Construction) under "
            "PMAY-U 2.0 may be the most relevant component.\n\n"

            "BLC focuses specifically on construction-related housing support."
        ),

    "alluseful_ahp":
        (
            "If your goal is purchasing a house through an affordable "
            "housing project, AHP (Affordable Housing in Partnership) "
            "may be more relevant.\n\n"

            "This component focuses on access to affordable housing units."
        ),

    "alluseful_arh":
        (
            "If affordable accommodation is the immediate priority, "
            "ARH (Affordable Rental Housing) may be the most suitable option.\n\n"

            "This component focuses on rental housing rather than ownership."
        ),

    "alluseful_iss":
        (
            "If housing loan burden is your primary concern, "
            "ISS (Interest Subsidy Scheme) may be the most relevant "
            "PMAY-U 2.0 component.\n\n"

            "It focuses on eligible support related to housing finance."
        ),

    # =====================================
    # WHICH SCHEME MATCHES LIFE
    # =====================================

    "life_arh":
        (
            "If affordable rental accommodation is your biggest need, "
            "ARH may be the closest match.\n\n"

            "It is intended for beneficiaries who need housing stability "
            "without necessarily pursuing ownership immediately."
        ),

    "life_ahp":
        (
            "If your long-term goal is owning a house, AHP may be "
            "worth exploring.\n\n"

            "This component focuses on helping eligible beneficiaries "
            "access affordable housing projects."
        ),

    "life_blc":
        (
            "If you already have land and want to build or improve "
            "a house, BLC may be the most relevant PMAY-U 2.0 option.\n\n"

            "Land ownership is generally an important factor for this component."
        ),

    "life_iss":
        (
            "If the biggest challenge is managing housing loan costs, "
            "ISS may be the most suitable option.\n\n"

            "This component focuses on reducing eligible housing "
            "finance burden through subsidy support."
        ),

    # =====================================
    # HALF FITS EVERY SCHEME
    # =====================================

    "halffit_house":
        (
            "If obtaining a permanent house is the highest priority, "
            "ownership-focused PMAY-U 2.0 components may be more relevant.\n\n"

            "Understanding whether you plan to buy, build or finance "
            "a house can help identify the best path."
        ),

    "halffit_rent":
        (
            "If immediate housing stability is more important than "
            "ownership, rental-focused support may be worth considering.\n\n"

            "ARH is specifically designed around affordable rental housing."
        ),

    "halffit_land":
        (
            "Owning land often changes which PMAY-U 2.0 component "
            "may be most relevant.\n\n"

            "Construction-focused support such as BLC may become "
            "more applicable in such situations."
        ),

    "halffit_loan":
        (
            "If housing loan pressure is the main concern, "
            "finance-related support may be more relevant than "
            "construction or rental assistance.\n\n"

            "ISS focuses on eligible housing loan support."
        ),

    # =====================================
    # RIGHT PATH
    # =====================================

    "rightpath_blc":
        (
            "If your objective is constructing or improving a house "
            "on land you own, BLC is often the first PMAY-U 2.0 "
            "component worth exploring.\n\n"

            "It focuses specifically on beneficiary-led construction support."
        ),

    "rightpath_ahp":
        (
            "If purchasing an affordable house is the goal, "
            "AHP may provide the clearest path.\n\n"

            "This component is designed around affordable housing projects."
        ),

    "rightpath_arh":
        (
            "If your immediate concern is affordable accommodation, "
            "ARH may be the most practical option.\n\n"

            "It focuses on affordable rental housing support."
        ),

    "rightpath_iss":
        (
            "If housing loan affordability is the biggest concern, "
            "ISS may be the most relevant PMAY-U 2.0 component.\n\n"

            "It focuses on eligible interest subsidy support."
        ),

    # =====================================
    # WAIT OR COMPLAIN
    # =====================================

    "wait_delay":
        (
            "Approval delays can happen for several reasons, including "
            "verification workload, document review or administrative processing.\n\n"

            "A delay does not automatically mean rejection, but "
            "understanding the current stage can help determine the next step."
        ),

    "wait_update":
        (
            "Missing updates are one of the most common concerns "
            "raised by PMAY-U 2.0 applicants.\n\n"

            "Applications may continue moving through internal "
            "processing stages even when visible updates are limited."
        ),

    "wait_issue":
        (
            "If there is a specific unresolved issue, identifying "
            "whether it involves documents, verification, ownership "
            "or application status is often the best starting point.\n\n"

            "Understanding the root issue usually helps determine "
            "whether follow-up action is necessary."
        ),
    # =====================================
    # WHO TO TRUST
    # =====================================

    "trust_privacy":
        (
            "Privacy concerns are understandable when sharing personal "
            "information for PMAY-U 2.0 applications.\n\n"

            "Applicants commonly provide identity, address, banking "
            "and housing-related information during verification.\n\n"

            "It is generally important to share sensitive information "
            "only through official processes and verified channels."
        ),

    "trust_agents":
        (
            "Concerns about fake agents are common among applicants.\n\n"

            "Some people worry about unofficial promises, misleading "
            "guidance or requests for unnecessary payments.\n\n"

            "Understanding official PMAY-U 2.0 procedures can help "
            "reduce confusion and improve confidence."
        ),

    "trust_documents":
        (
            "Document-related trust concerns often involve who can "
            "access, verify or handle personal records.\n\n"

            "Identity proof, ownership documents and banking details "
            "are particularly sensitive and should be handled carefully."
        ),

    "trust_approval":
        (
            "Approval-related pressure can make applicants feel "
            "uncertain about whom to trust.\n\n"

            "PMAY-U 2.0 approvals are generally based on eligibility "
            "and verification processes rather than personal influence or promises."
        ),

    # =====================================
    # FRAUD FEAR
    # =====================================

    "fraud_otp":
        (
            "OTP-related scams are a common concern whenever financial "
            "or personal information is involved.\n\n"

            "Many applicants worry about unauthorized access to accounts "
            "or misuse of verification credentials.\n\n"

            "Protecting OTP information is generally an important safety practice."
        ),

    "fraud_fakeapproval":
        (
            "Fake approval claims can create confusion and anxiety.\n\n"

            "Applicants sometimes receive misleading information about "
            "approval status, subsidy release or application progress.\n\n"

            "Official status verification is usually the most reliable approach."
        ),

    "fraud_identity":
        (
            "Identity misuse concerns are understandable when personal "
            "documents are submitted during the PMAY-U 2.0 process.\n\n"

            "Applicants often worry about unauthorized use of Aadhaar, "
            "banking information or beneficiary records."
        ),

    # =====================================
    # EVERYTHING STUCK
    # =====================================

    "stuck_status":
        (
            "Application status can sometimes appear unchanged for a period of time.\n\n"

            "PMAY-U 2.0 applications may move through verification, "
            "review, approval and processing stages before visible updates appear."
        ),

    "stuck_approval":
        (
            "Approval-related delays can feel frustrating, especially "
            "when applicants are waiting for a decision.\n\n"

            "Delays do not automatically indicate rejection and may "
            "sometimes relate to ongoing verification activities."
        ),

    "stuck_documents":
        (
            "Document issues are one of the most common reasons "
            "applications appear delayed or inactive.\n\n"

            "Verification may take longer if documents require review, "
            "clarification or confirmation."
        ),

    "stuck_money":
        (
            "Money-related delays often involve subsidy processing, "
            "DBT stages or approval dependencies.\n\n"

            "Understanding the current stage of the application can "
            "help identify whether payment-related processing is pending."
        ),

    # =====================================
    # WHAT PROBLEM FIRST
    # =====================================

    "problem_house":
        (
            "Housing concerns are often the foundation of PMAY-U 2.0 eligibility questions.\n\n"

            "Ownership, rental situation, housing condition and "
            "availability of land may all influence which scheme component is relevant."
        ),

    "problem_money":
        (
            "Financial concerns commonly involve income category, "
            "housing affordability, loan burden or subsidy-related questions.\n\n"

            "Understanding the financial aspect often helps narrow down the issue."
        ),

    "problem_documents":
        (
            "Documents are frequently the first area worth reviewing "
            "because they affect verification, approval and eligibility assessment.\n\n"

            "Identity, ownership, income and banking records are common examples."
        ),

    "problem_family":
        (
            "Family-related concerns may involve marriage, separation, "
            "inheritance, dependency or beneficiary family definitions.\n\n"

            "These situations can sometimes affect PMAY-U 2.0 eligibility assessment."
        ),

    "problem_status":
        (
            "Application status concerns often arise when applicants "
            "are unsure what stage the application has reached.\n\n"

            "Understanding whether the case is under verification, "
            "review or approval can help identify the next step."
        ),

    # =====================================
    # APPLIED WRONG
    # =====================================

    "wrong_scheme":
        (
            "Many applicants worry they selected the wrong PMAY-U 2.0 component.\n\n"

            "The most suitable scheme usually depends on whether the "
            "goal is to build, buy, rent or reduce housing loan burden.\n\n"

            "Understanding the intended housing outcome often clarifies the choice."
        ),

    "wrong_details":
        (
            "Application detail concerns may involve names, addresses, "
            "income information, family details or other records.\n\n"

            "Small mistakes do not automatically determine the final outcome, "
            "but identifying them early can be helpful."
        ),

    "wrong_documents":
        (
            "Document concerns are among the most common worries after applying.\n\n"

            "Applicants often wonder whether the correct ownership, "
            "identity or income-related documents were submitted."
        ),

    # =====================================
    # NOTHING MAKING SENSE
    # =====================================

    "sense_eligibility":
        (
            "Eligibility can seem confusing because multiple PMAY-U 2.0 "
            "conditions are often considered together.\n\n"

            "Income, ownership, family status and housing conditions "
            "may all influence eligibility assessment."
        ),

    "sense_status":
        (
            "Application status is one of the most common sources of confusion.\n\n"

            "Different processing stages serve different purposes, "
            "which can make updates difficult to interpret."
        ),

    "sense_subsidy":
        (
            "Subsidy-related questions can be difficult because "
            "different PMAY-U 2.0 components provide different benefits.\n\n"

            "Understanding the relevant scheme component usually helps clarify the process."
        ),

    "sense_paperwork":
        (
            "Paperwork often feels overwhelming because several types "
            "of documents may be reviewed during verification.\n\n"

            "Breaking documents into identity, ownership, income and "
            "banking categories usually makes the process easier to understand."
        ),
    # =====================================
    # SOMETHING MESSED UP
    # =====================================

    "messedup_documents":
        (
            "When something feels wrong but is difficult to explain, "
            "documents are often a good place to start.\n\n"

            "PMAY-U 2.0 applications commonly rely on identity, "
            "ownership, income and banking records during verification.\n\n"

            "Reviewing document-related concerns can often help identify "
            "the actual issue more clearly."
        ),

    "messedup_money":
        (
            "Money-related concerns may involve income category, "
            "bank details, subsidy expectations or housing loan pressure.\n\n"

            "Many applicants feel uncertain about finances during the "
            "PMAY-U 2.0 process, especially when multiple factors are involved.\n\n"

            "Understanding the financial concern often helps narrow down the problem."
        ),

    "messedup_approval":
        (
            "Approval concerns can be difficult to identify because "
            "applications pass through multiple stages.\n\n"

            "Verification, review and approval activities may happen "
            "before a visible outcome appears.\n\n"

            "Knowing the current stage often helps explain what is happening."
        ),

    "messedup_family":
        (
            "Family situations can sometimes create eligibility and "
            "documentation questions under PMAY-U 2.0.\n\n"

            "Marriage, separation, inheritance and dependency-related "
            "issues are common examples.\n\n"

            "Clarifying the family situation is often an important first step."
        ),

    # =====================================
    # WAITING ANGER
    # =====================================

    "waiting_approval":
        (
            "Approval delays can be frustrating, especially after "
            "waiting for a long time.\n\n"

            "PMAY-U 2.0 approvals may depend on verification, "
            "document review and administrative processing.\n\n"

            "A delay does not automatically indicate rejection."
        ),

    "waiting_status":
        (
            "Status-related uncertainty is one of the most common "
            "sources of frustration for applicants.\n\n"

            "Applications may remain at a particular stage while "
            "verification or review activities are still ongoing."
        ),

    "waiting_updates":
        (
            "Missing updates can make it seem like nothing is happening.\n\n"

            "However, PMAY-U 2.0 applications may continue moving "
            "through internal processes even when visible updates are limited.\n\n"

            "Understanding the current stage often helps reduce uncertainty."
        ),

    # =====================================
    # EVERYTHING PROBLEM
    # =====================================

    "everything_housing":
        (
            "Housing concerns often affect many other PMAY-U 2.0 questions.\n\n"

            "Ownership status, rental conditions, housing quality and "
            "availability of land can all influence eligibility and scheme selection.\n\n"

            "Starting with housing details can simplify the discussion."
        ),

    "everything_finance":
        (
            "Financial pressure can make every part of the process "
            "feel more difficult.\n\n"

            "Income category, affordability concerns, subsidy questions "
            "and housing loan burden are common financial topics under PMAY-U 2.0."
        ),

    "everything_application":
        (
            "Application-related concerns may involve verification, "
            "status tracking, approval delays or document review.\n\n"

            "Identifying the exact stage often makes the situation easier to understand."
        ),

    # =====================================
    # PORTAL FEAR
    # =====================================

    "portalfear_status":
        (
            "Many applicants worry about seeing an unexpected status change.\n\n"

            "However, status updates are generally part of the normal "
            "PMAY-U 2.0 processing workflow and do not automatically indicate a problem."
        ),

    "portalfear_rejection":
        (
            "Fear of rejection is common, especially when applicants "
            "are unsure about their eligibility or documentation.\n\n"

            "PMAY-U 2.0 decisions are generally based on verified "
            "information rather than assumptions."
        ),

    "portalfear_technical":
        (
            "Technical concerns are understandable, particularly when "
            "using online systems.\n\n"

            "Portal-related issues may involve login problems, "
            "document uploads or temporary system errors and are "
            "often separate from eligibility assessment."
        ),

    # =====================================
    # DOCUMENT FATIGUE
    # =====================================

    "tireddocs_missing":
        (
            "Missing document requests can feel exhausting when they "
            "occur repeatedly.\n\n"

            "Applicants are commonly asked for identity, ownership, "
            "income or banking-related documents depending on the case.\n\n"

            "Identifying the specific missing document usually helps."
        ),

    "tireddocs_mismatch":
        (
            "Document mismatches are one of the most common reasons "
            "additional clarification may be required.\n\n"

            "Differences in names, addresses or ownership information "
            "can sometimes affect verification."
        ),

    "tireddocs_repeat":
        (
            "Repeated document requests can be frustrating and may "
            "make the process feel never-ending.\n\n"

            "In some cases, additional verification or clarification "
            "may be required before processing can continue."
        ),

    # =====================================
    # WEIRD FAMILY SITUATION
    # =====================================

    "weirdfamily_marriage":
        (
            "Marriage-related situations can sometimes affect how "
            "beneficiary family information is assessed under PMAY-U 2.0.\n\n"

            "Current household structure and ownership details are "
            "often important factors during evaluation."
        ),

    "weirdfamily_separation":
        (
            "Separation-related cases are more common than many people realize.\n\n"

            "PMAY-U 2.0 assessment generally focuses on documented "
            "family and ownership information relevant to the application."
        ),

    "weirdfamily_inheritance":
        (
            "Inherited property can create questions about ownership "
            "status and eligibility.\n\n"

            "Understanding who legally owns the property is often "
            "important when evaluating housing-related conditions."
        ),

    "weirdfamily_dependency":
        (
            "Dependency-related situations involving parents, children "
            "or other family members can sometimes affect household assessment.\n\n"

            "Family composition and housing ownership details are "
            "often reviewed together under PMAY-U 2.0."
        ),
    # =====================================
    # STOP TRYING
    # =====================================

    "stoptrying_rejection":
        (
            "Many applicants consider giving up because they fear rejection.\n\n"

            "However, PMAY-U 2.0 eligibility is generally determined "
            "through verification of ownership, income, beneficiary "
            "family details and other scheme requirements.\n\n"

            "Concern about rejection does not automatically mean the "
            "application lacks merit."
        ),

    "stoptrying_delay":
        (
            "Long waiting periods can make the process feel discouraging.\n\n"

            "PMAY-U 2.0 applications may pass through verification, "
            "review and approval stages before a final outcome is available.\n\n"

            "Delays alone do not necessarily indicate a negative result."
        ),

    "stoptrying_money":
        (
            "Financial pressure can make housing-related decisions "
            "feel much harder.\n\n"

            "Many applicants explore PMAY-U 2.0 because of affordability, "
            "housing costs or loan-related concerns.\n\n"

            "Understanding the exact financial challenge often helps identify suitable options."
        ),

    "stoptrying_housing":
        (
            "Housing instability is a genuine concern and often the "
            "reason people begin exploring PMAY-U 2.0 in the first place.\n\n"

            "Different PMAY-U 2.0 components are designed to address "
            "different housing needs and situations."
        ),

    # =====================================
    # FEEL LOST
    # =====================================

    "lost_eligibility":
        (
            "Eligibility confusion is one of the most common reasons "
            "people feel lost during the PMAY-U 2.0 process.\n\n"

            "Eligibility often depends on multiple factors including "
            "housing ownership, income category, beneficiary family "
            "status and scheme-specific conditions."
        ),

    "lost_documents":
        (
            "Document requirements can feel overwhelming because "
            "several types of records may be involved.\n\n"

            "Identity proof, ownership records, income documents "
            "and banking details are commonly reviewed during verification."
        ),

    "lost_money":
        (
            "Financial terms, subsidy information and housing costs "
            "can sometimes make the PMAY-U 2.0 process difficult to follow.\n\n"

            "Breaking the issue into income, subsidy or loan-related "
            "questions often helps simplify the situation."
        ),

    "lost_approval":
        (
            "Approval stages can feel confusing when applicants are "
            "unsure what each status actually means.\n\n"

            "Verification, review and approval are separate parts of "
            "the PMAY-U 2.0 workflow and may take different amounts of time."
        ),

    # =====================================
    # SCARED OR CONFUSED
    # =====================================

    "scared_fraud":
        (
            "Fraud concerns are understandable when personal and "
            "housing-related information is involved.\n\n"

            "Applicants commonly worry about fake agents, identity misuse "
            "or misleading approval claims during the PMAY-U 2.0 process."
        ),

    "scared_rejection":
        (
            "Fear of rejection can sometimes feel stronger than the "
            "actual eligibility uncertainty.\n\n"

            "PMAY-U 2.0 decisions are generally based on documented "
            "eligibility factors rather than assumptions."
        ),

    "scared_money":
        (
            "Financial uncertainty often creates both stress and confusion.\n\n"

            "Income category, affordability concerns and housing loan "
            "burden are common areas that applicants worry about."
        ),

    "scared_eligibility":
        (
            "Eligibility rules may appear complicated because several "
            "conditions are often assessed together.\n\n"

            "Ownership, income, family status and housing condition "
            "can all influence PMAY-U 2.0 eligibility assessment."
        ),

    # =====================================
    # STABLE PLACE
    # =====================================

    "stability_rental":
        (
            "If immediate housing stability is the priority, "
            "rental-focused support may be the most relevant area to explore.\n\n"

            "ARH (Affordable Rental Housing) under PMAY-U 2.0 focuses "
            "on providing affordable rental accommodation for eligible beneficiaries."
        ),

    "stability_ownership":
        (
            "If your goal is long-term housing security through ownership, "
            "ownership-focused PMAY-U 2.0 components may be more relevant.\n\n"

            "The most suitable option depends on whether you plan to buy or build."
        ),

    "stability_construction":
        (
            "If you already have access to land and want to improve "
            "housing conditions, construction-focused support may be worth exploring.\n\n"

            "BLC under PMAY-U 2.0 focuses on eligible construction and enhancement support."
        ),

    # =====================================
    # APPLICATION OR LIFE
    # =====================================

    "lifemess_application":
        (
            "Many applicants worry they made a mistake somewhere in "
            "the application process.\n\n"

            "Concerns often involve documents, details, scheme selection "
            "or status updates.\n\n"

            "Identifying the exact application concern is usually the best starting point."
        ),

    "lifemess_housing":
        (
            "Sometimes the real challenge is not the application but "
            "the housing situation itself.\n\n"

            "Ownership questions, unstable accommodation, family housing "
            "issues or affordability concerns can all contribute to uncertainty."
        ),

    # =====================================
    # EXHAUSTED REPEATING
    # =====================================

    "repeat_approval":
        (
            "Repeatedly explaining the same situation while waiting "
            "for approval can feel exhausting.\n\n"

            "Approval-related concerns often involve delays, status "
            "uncertainty or pending verification activities."
        ),

    "repeat_eligibility":
        (
            "Eligibility questions can become frustrating when the "
            "same concerns keep resurfacing.\n\n"

            "Clarifying ownership, income and beneficiary family "
            "conditions often helps narrow down the actual issue."
        ),

    "repeat_paperwork":
        (
            "Paperwork fatigue is a common experience among applicants.\n\n"

            "Repeated requests, verification questions or document "
            "mismatches can make the process feel never-ending.\n\n"

            "Identifying the specific paperwork concern often helps "
            "make the situation more manageable."
        ),
    # =====================================
    # PORTAL + OFFICE CONFUSION
    # =====================================

    "confusing_portal":
        (
            "Portal-related confusion is very common among PMAY-U 2.0 applicants.\n\n"

            "Status messages, delayed updates and technical issues can "
            "sometimes make the process seem more complicated than it actually is.\n\n"

            "Understanding the current application stage often helps reduce uncertainty."
        ),

    "confusing_approval":
        (
            "Approval stages can be difficult to understand because "
            "applications usually pass through verification, review "
            "and approval before a final outcome is available.\n\n"

            "A delay at one stage does not automatically indicate a problem."
        ),

    "confusing_advice":
        (
            "Conflicting advice from different people can make PMAY-U 2.0 "
            "feel much more confusing than necessary.\n\n"

            "Applicants often receive different interpretations about "
            "eligibility, documents or approval timelines.\n\n"

            "Focusing on the specific issue usually helps separate facts from assumptions."
        ),

    # =====================================
    # OVERCOMPLICATING
    # =====================================

    "overcomplicate_housing":
        (
            "Housing concerns often sit at the center of PMAY-U 2.0 questions.\n\n"

            "Ownership, rental accommodation, housing condition and "
            "availability of land can all influence which scheme component is relevant.\n\n"

            "Starting with housing details often simplifies the discussion."
        ),

    "overcomplicate_documents":
        (
            "Document concerns can sometimes make a situation appear "
            "more complicated than it actually is.\n\n"

            "Identity proof, ownership records, income documents and "
            "bank details are the most common areas reviewed during verification."
        ),

    "overcomplicate_money":
        (
            "Financial concerns may involve income category, subsidy "
            "questions, affordability issues or housing loan burden.\n\n"

            "Breaking the financial issue into smaller parts often makes it easier to understand."
        ),

    "overcomplicate_approval":
        (
            "Approval concerns are common because applicants may not "
            "know what happens behind the scenes during processing.\n\n"

            "Verification and review activities can continue even when visible updates are limited."
        ),

    # =====================================
    # NOBODY UNDERSTANDS
    # =====================================

    "understood_family":
        (
            "Family situations are often more complex than they appear.\n\n"

            "Marriage, separation, dependency, inheritance and shared "
            "households can all create PMAY-U 2.0 eligibility questions.\n\n"

            "These situations are more common than many applicants realize."
        ),

    "understood_ownership":
        (
            "Ownership-related concerns frequently cause confusion.\n\n"

            "Family-owned property, inherited houses, shared ownership "
            "or unclear records can all affect how housing conditions are assessed."
        ),

    "understood_housing":
        (
            "Housing situations do not always fit into simple categories.\n\n"

            "Rental accommodation, temporary housing, inherited homes "
            "and damaged houses can all create different PMAY-U 2.0 questions."
        ),

    "understood_finances":
        (
            "Financial concerns can feel difficult to explain because "
            "income, affordability, loan burden and subsidy expectations "
            "often overlap.\n\n"

            "Clarifying the main financial concern usually helps identify the next step."
        ),

    # =====================================
    # SCARED TO HOPE
    # =====================================

    "hope_approval":
        (
            "Waiting for approval can create uncertainty and make it "
            "difficult to stay optimistic.\n\n"

            "PMAY-U 2.0 applications generally move through multiple "
            "verification and review stages before final decisions are reached."
        ),

    "hope_eligibility":
        (
            "Many applicants worry about eligibility even when they "
            "appear to meet some requirements.\n\n"

            "Eligibility is usually determined by a combination of "
            "ownership, income, beneficiary family status and scheme conditions."
        ),

    "hope_financial":
        (
            "Financial support is often one of the main reasons people "
            "explore PMAY-U 2.0.\n\n"

            "Understanding which component may apply to your housing "
            "situation can help clarify what support might be relevant."
        ),

    # =====================================
    # EVERYTHING MESSY
    # =====================================

    "messy_house":
        (
            "Housing-related concerns are often the best place to start "
            "when everything feels complicated.\n\n"

            "Ownership, rental conditions and housing quality can influence "
            "many other PMAY-U 2.0 questions."
        ),

    "messy_money":
        (
            "Financial pressure can affect how applicants view the entire process.\n\n"

            "Income concerns, affordability, subsidy questions and "
            "housing loan burden are common examples."
        ),

    "messy_documents":
        (
            "Document concerns are frequently the source of uncertainty "
            "during verification and approval.\n\n"

            "Identity, ownership, income and banking records are often reviewed together."
        ),

    "messy_family":
        (
            "Family situations involving marriage, separation, dependency "
            "or inheritance can create multiple PMAY-U 2.0 questions at once.\n\n"

            "Clarifying the family situation is often the first step."
        ),

    # =====================================
    # WHO COUNTS AS FAMILY
    # =====================================

    "familylegal_parents":
        (
            "Questions involving parents are common when assessing "
            "beneficiary family conditions under PMAY-U 2.0.\n\n"

            "Housing ownership and household relationships may both "
            "be relevant depending on the situation."
        ),

    "familylegal_marriage":
        (
            "Marriage can affect how beneficiary family information "
            "is interpreted during PMAY-U 2.0 assessment.\n\n"

            "Household structure and ownership details are often reviewed together."
        ),

    "familylegal_separation":
        (
            "Separation-related situations can create uncertainty "
            "about family definitions and housing eligibility.\n\n"

            "Current family circumstances and supporting records are often important."
        ),

    "familylegal_dependency":
        (
            "Dependency questions involving children, parents or other "
            "family members can sometimes affect household assessment.\n\n"

            "Understanding who forms part of the beneficiary family is often important."
        ),

    # =====================================
    # FAMILY + PROPERTY ISSUES
    # =====================================

    "property_inheritance":
        (
            "Inherited property can create complex questions about "
            "ownership status and PMAY-U 2.0 eligibility.\n\n"

            "Understanding who legally owns the property is often a key factor."
        ),

    "property_separation":
        (
            "Property concerns combined with separation-related issues "
            "can sometimes make ownership situations difficult to interpret.\n\n"

            "Clarifying both the family and ownership aspects is usually important."
        ),

    "property_ownership":
        (
            "Ownership conflicts are one of the most common reasons "
            "family and property issues become difficult to resolve.\n\n"

            "Clear ownership records often help explain how housing-related "
            "conditions should be assessed under PMAY-U 2.0."
        ),
    
    # =====================================
    # PENDING + LANDLORD + FAMILY
    # =====================================

    "pendinglandlord_approval":
        (
            "Waiting for approval while facing pressure from other directions "
            "can make the PMAY-U 2.0 process feel much more difficult.\n\n"

            "Applications may spend time in verification, review and "
            "approval stages before a final outcome is available.\n\n"

            "An approval delay does not automatically mean rejection."
        ),

    "pendinglandlord_housing":
        (
            "Housing pressure is often one of the main reasons people "
            "apply under PMAY-U 2.0.\n\n"

            "Rental uncertainty, landlord pressure and housing instability "
            "can make waiting for updates particularly stressful.\n\n"

            "Understanding the current application stage may help clarify expectations."
        ),

    "pendinglandlord_family":
        (
            "Family pressure can make an already difficult housing situation "
            "feel even more overwhelming.\n\n"

            "Many applicants face questions from relatives while still "
            "waiting for PMAY-U 2.0 decisions and updates."
        ),

    # =====================================
    # ELIGIBILITY + FAMILY + TECHNICAL
    # =====================================

    "threethings_eligibility":
        (
            "Eligibility concerns often create uncertainty because "
            "PMAY-U 2.0 evaluates multiple conditions together.\n\n"

            "Housing ownership, income category, beneficiary family "
            "status and scheme requirements may all play a role."
        ),

    "threethings_family":
        (
            "Family-related concerns can sometimes be more complicated "
            "than the PMAY-U 2.0 rules themselves.\n\n"

            "Marriage, separation, inheritance and shared housing "
            "situations frequently create additional questions."
        ),

    "threethings_portal":
        (
            "Portal issues can make applicants feel that something is wrong "
            "even when the application is progressing normally.\n\n"

            "Login difficulties, missing updates and technical problems "
            "are common concerns during the PMAY-U 2.0 process."
        ),

    # =====================================
    # SUBSIDY + LOAN + FAMILY ARGUMENTS
    # =====================================

    "subsidyloan_timing":
        (
            "Subsidy timing is one of the most common concerns for "
            "PMAY-U 2.0 applicants managing financial commitments.\n\n"

            "Delays in processing can sometimes create uncertainty "
            "about housing-related planning and expenses."
        ),

    "subsidyloan_emi":
        (
            "EMI pressure can make any delay feel much more serious.\n\n"

            "Many applicants explore PMAY-U 2.0 support because "
            "housing finance obligations place strain on household budgets.\n\n"

            "Understanding the loan-related concern is often the first step."
        ),

    "subsidyloan_approval":
        (
            "Subsidy processing is often connected to verification "
            "and approval-related stages.\n\n"

            "Understanding whether the application is pending review, "
            "approval or another stage can help explain the delay."
        ),

    # =====================================
    # RULES + LIFE COLLISION
    # =====================================

    "collision_ownership":
        (
            "Ownership concerns are one of the most common reasons "
            "PMAY-U 2.0 cases feel complicated.\n\n"

            "Family-owned property, inherited houses and shared "
            "ownership arrangements can create multiple questions at once."
        ),

    "collision_housing":
        (
            "Housing situations do not always fit into simple categories.\n\n"

            "Rental accommodation, damaged houses, inherited homes "
            "or unstable living arrangements can all affect how a "
            "case is understood."
        ),

    "collision_family":
        (
            "Family situations can overlap with ownership and housing concerns.\n\n"

            "Marriage, separation, dependency and inheritance issues "
            "often create multiple PMAY-U 2.0 questions simultaneously."
        ),

    "collision_finances":
        (
            "Financial concerns frequently overlap with eligibility, "
            "housing and application-related questions.\n\n"

            "Income, affordability, subsidy expectations and loan burden "
            "can all contribute to uncertainty."
        ),

    # =====================================
    # SYSTEM SLOW OR CASE DIFFICULT
    # =====================================

    "systemslow_delay":
        (
            "It can be difficult to tell whether a delay is caused by "
            "normal processing time or a specific issue.\n\n"

            "PMAY-U 2.0 applications may remain under verification "
            "or review for some time before visible progress appears."
        ),

    "systemslow_eligibility":
        (
            "Sometimes applicants worry that a complex eligibility "
            "situation is causing delays.\n\n"

            "Ownership, income, family status and housing conditions "
            "may require additional review depending on the case."
        ),

    "systemslow_updates":
        (
            "Missing updates are a common source of uncertainty.\n\n"

            "Applications may continue progressing internally even "
            "when new status information is not immediately visible."
        ),

    # =====================================
    # FAMILY + RENT + PMAY CONFUSION
    # =====================================

    "pressure_housing":
        (
            "Housing pressure is often the most urgent concern for "
            "people exploring PMAY-U 2.0.\n\n"

            "Rental costs, unstable accommodation and long-term "
            "housing security can all influence decision-making."
        ),

    "pressure_family":
        (
            "Family pressure can make PMAY-U 2.0 decisions feel more stressful.\n\n"

            "Different opinions about housing, finances or eligibility "
            "may create additional uncertainty."
        ),

    "pressure_application":
        (
            "Application-related stress often comes from uncertainty "
            "about status, approval timelines or eligibility.\n\n"

            "Breaking the issue into smaller parts usually makes it "
            "easier to understand and address."
        ),
    # =====================================
    # CANNOT EXPLAIN CASE
    # =====================================

    "cant_explain_house":
        (
            "Many PMAY-U 2.0 applicants struggle to explain their "
            "housing situation clearly, especially when ownership, "
            "renting and family arrangements overlap.\n\n"

            "Starting with where you currently live and whether you "
            "or your beneficiary family own a pucca house often helps "
            "simplify the discussion."
        ),

    "cant_explain_money":
        (
            "Financial concerns can involve income category, housing "
            "expenses, loan burden or subsidy expectations.\n\n"

            "Breaking the issue into smaller parts usually makes it "
            "easier to understand which PMAY-U 2.0 component may be relevant."
        ),

    "cant_explain_family":
        (
            "Family situations are often more complicated than they seem.\n\n"

            "Marriage, separation, inheritance, dependency and shared "
            "housing arrangements can all affect PMAY-U 2.0 discussions.\n\n"

            "Clarifying the family situation is often the best starting point."
        ),

    "cant_explain_documents":
        (
            "Many applicants feel overwhelmed by document requirements.\n\n"

            "Identity proof, ownership records, income documents and "
            "bank details are commonly reviewed during PMAY-U 2.0 verification.\n\n"

            "Identifying which document is causing concern can help narrow the issue."
        ),

    # =====================================
    # PMAY STRESS
    # =====================================

    "sleep_approval":
        (
            "Long approval timelines can create significant stress, "
            "especially when housing needs are urgent.\n\n"

            "PMAY-U 2.0 applications may move through verification, "
            "review and approval stages before a final decision is reached.\n\n"

            "A delay alone does not automatically indicate rejection."
        ),

    "sleep_money":
        (
            "Financial pressure is one of the most common reasons "
            "applicants feel anxious during the PMAY-U 2.0 process.\n\n"

            "Housing costs, loan obligations and uncertainty about "
            "future support can all contribute to stress."
        ),

    "sleep_eligibility":
        (
            "Eligibility uncertainty can make applicants feel stuck "
            "between hope and concern.\n\n"

            "PMAY-U 2.0 eligibility generally depends on factors such as "
            "income, ownership status, beneficiary family conditions "
            "and scheme-specific requirements."
        ),

    # =====================================
    # BLC CONFUSION
    # =====================================

    "blc_land":
        (
            "BLC (Beneficiary Led Construction) under PMAY-U 2.0 is "
            "primarily intended for eligible beneficiaries who want to "
            "construct or improve a house on land available to them.\n\n"

            "Land-related questions are among the most common sources "
            "of confusion when evaluating BLC eligibility."
        ),

    "blc_eligibility":
        (
            "BLC eligibility depends on multiple conditions including "
            "housing ownership, beneficiary family status and other "
            "PMAY-U 2.0 requirements.\n\n"

            "Many applicants find it helpful to review these conditions "
            "step by step rather than all at once."
        ),

    "blc_verification":
        (
            "BLC applications generally require verification of "
            "beneficiary and property-related information.\n\n"

            "Document review and local verification processes may be "
            "part of the overall assessment."
        ),

    # =====================================
    # AHP FITS ME?
    # =====================================

    "ahp_buy":
        (
            "AHP (Affordable Housing in Partnership) under PMAY-U 2.0 "
            "is generally relevant for eligible beneficiaries looking "
            "to purchase an affordable housing unit.\n\n"

            "If your goal is home ownership through an approved housing "
            "project, AHP may be worth exploring further."
        ),

    "ahp_unsure":
        (
            "If you are unsure whether AHP fits your situation, it may "
            "help to first identify whether your goal is buying a house, "
            "building a house, renting accommodation or reducing loan burden.\n\n"

            "Different PMAY-U 2.0 components serve different housing needs."
        ),

    # =====================================
    # AHP RULES
    # =====================================

    "ahp_eligibility":
        (
            "AHP eligibility depends on PMAY-U 2.0 requirements such as "
            "income category, housing ownership conditions and beneficiary eligibility.\n\n"

            "Understanding these requirements is often the first step "
            "toward determining whether AHP is suitable."
        ),

    "ahp_purchase":
        (
            "AHP focuses on affordable housing units developed through "
            "approved housing projects.\n\n"

            "Applicants who are looking to purchase a home rather than "
            "construct one often explore AHP."
        ),

    "ahp_verification":
        (
            "Verification for AHP may involve beneficiary information, "
            "eligibility review and supporting documents.\n\n"

            "The exact process can vary depending on the housing project "
            "and local implementation."
        ),

    # =====================================
    # IS AHP WORTH CHECKING?
    # =====================================

    "ahp_flat":
        (
            "If you are looking for an affordable flat through a housing "
            "project, AHP under PMAY-U 2.0 may be worth reviewing.\n\n"

            "This component focuses on providing access to affordable "
            "housing units for eligible beneficiaries."
        ),

    "ahp_support":
        (
            "If your goal is purchasing a home through an affordable "
            "housing project, AHP may provide relevant support pathways.\n\n"

            "Understanding your housing objective is usually the best "
            "way to determine whether AHP is worth exploring further."
        ),
    # =====================================
    # ARH FITS ME
    # =====================================

    "arh_rental":
        (
            "ARH (Affordable Rental Housing) under PMAY-U 2.0 is "
            "primarily intended for people who need affordable rental accommodation.\n\n"

            "It may be relevant for beneficiaries who are not currently "
            "looking to purchase a house but need stable and affordable housing.\n\n"

            "Understanding your current housing situation can help determine "
            "whether ARH is worth exploring further."
        ),

    "arh_unsure":
        (
            "If you are unsure whether ARH fits your situation, it may help "
            "to first identify whether your goal is renting, buying, building "
            "or reducing housing loan burden.\n\n"

            "Different PMAY-U 2.0 components are designed for different housing needs."
        ),

    # =====================================
    # ARH RULES
    # =====================================

    "arh_housing":
        (
            "ARH focuses on affordable rental housing rather than home ownership.\n\n"

            "Many applicants become confused because PMAY-U 2.0 includes both "
            "ownership-based and rental-based housing solutions.\n\n"

            "Understanding your housing objective usually helps clarify whether ARH is relevant."
        ),

    "arh_eligibility":
        (
            "ARH eligibility depends on applicable PMAY-U 2.0 conditions "
            "and local implementation requirements.\n\n"

            "Housing situation, beneficiary status and rental housing needs "
            "may all be considered during assessment."
        ),

    "arh_verification":
        (
            "ARH applications may involve verification of beneficiary "
            "information and supporting documents.\n\n"

            "The exact verification process can vary depending on the "
            "housing project and implementation authority."
        ),

    # =====================================
    # ISS FITS ME
    # =====================================

    "iss_loan":
        (
            "ISS (Interest Subsidy Scheme) under PMAY-U 2.0 is generally "
            "relevant for eligible beneficiaries who have a housing loan "
            "or are planning to obtain one.\n\n"

            "The scheme focuses on reducing housing loan burden through "
            "interest subsidy support for eligible applicants."
        ),

    "iss_unsure":
        (
            "If you are unsure whether ISS fits your situation, it may help "
            "to first identify whether you have a housing loan, plan to take one, "
            "or are looking for another type of housing assistance.\n\n"

            "Different PMAY-U 2.0 components address different housing needs."
        ),

    # =====================================
    # ISS RULES
    # =====================================

    "iss_loan_confusion":
        (
            "Many applicants are unsure how loan-related benefits work "
            "under PMAY-U 2.0 ISS.\n\n"

            "ISS focuses on eligible housing loans and interest subsidy support, "
            "which may help reduce overall loan burden."
        ),

    "iss_eligibility":
        (
            "ISS eligibility generally depends on factors such as income category, "
            "housing ownership conditions and other PMAY-U 2.0 requirements.\n\n"

            "Reviewing eligibility conditions step by step often makes them easier to understand."
        ),

    "iss_verification":
        (
            "ISS applications may require verification of loan details, "
            "beneficiary information and supporting documents.\n\n"

            "Verification is an important part of the PMAY-U 2.0 assessment process."
        ),

    # =====================================
    # ISS WORTH CHECKING
    # =====================================

    "iss_have_loan":
        (
            "If you already have a housing loan, ISS under PMAY-U 2.0 may be worth reviewing.\n\n"

            "Eligible beneficiaries may receive interest subsidy support, "
            "which can help reduce housing loan burden over time."
        ),

    "iss_need_support":
        (
            "If your primary concern is housing loan affordability, "
            "ISS may be a relevant PMAY-U 2.0 component to explore.\n\n"

            "The scheme is designed to support eligible beneficiaries "
            "through interest subsidy on qualifying housing loans."
        ),

    # =====================================
    # INCOME FITS AHP
    # =====================================

    "incomefit_category":
        (
            "Income category is one of the most common concerns when evaluating "
            "PMAY-U 2.0 eligibility.\n\n"

            "Applicants are generally assessed under categories such as "
            "EWS, LIG or MIG based on applicable income criteria.\n\n"

            "Understanding your income category is often the first step."
        ),

    "incomefit_eligibility":
        (
            "Income is only one part of PMAY-U 2.0 eligibility assessment.\n\n"

            "Housing ownership, beneficiary family conditions and scheme-specific "
            "requirements may also be considered when determining eligibility."
        ),

    "incomefit_scheme":
        (
            "Sometimes the real question is not income alone, but whether "
            "AHP is the most suitable PMAY-U 2.0 component for your situation.\n\n"

            "Your housing goal, ownership status and eligibility conditions "
            "can help determine which scheme may be most relevant."
        ),

    # =====================================
    # AHP INCOME
    # =====================================

    "ahp_income_eligibility":
        (
            "Income eligibility is one of the most common concerns before "
            "applying under AHP in PMAY-U 2.0.\n\n"

            "Applicants are generally assessed under applicable income "
            "categories such as EWS, LIG or MIG, along with other "
            "eligibility conditions.\n\n"

            "Income alone does not determine eligibility; housing ownership "
            "and beneficiary conditions may also be considered."
        ),

    "ahp_income_verification":
        (
            "Income verification may require supporting documents or "
            "other acceptable proof during the PMAY-U 2.0 process.\n\n"

            "Verification helps confirm eligibility and ensure that "
            "applications are assessed under the correct category."
        ),

    # =====================================
    # ARH INCOME
    # =====================================

    "arh_income_eligibility":
        (
            "Income-related questions are common for applicants considering "
            "ARH under PMAY-U 2.0.\n\n"

            "Income may be one factor considered along with housing need "
            "and beneficiary eligibility conditions."
        ),

    "arh_rental_eligibility":
        (
            "ARH is intended for beneficiaries seeking affordable rental housing.\n\n"

            "Understanding your current rental situation and housing need "
            "is often just as important as understanding income requirements."
        ),

    "arh_income_verification":
        (
            "Verification may involve reviewing beneficiary details and "
            "supporting records relevant to the PMAY-U 2.0 process.\n\n"

            "The exact requirements can vary depending on implementation."
        ),

    "arh_before_income":
        (
            "Before applying for ARH under PMAY-U 2.0, many applicants "
            "want to understand whether their income category may fit "
            "the applicable eligibility conditions.\n\n"

            "Income is typically considered together with housing need "
            "and other beneficiary requirements."
        ),

    "arh_before_rental":
        (
            "ARH focuses on affordable rental accommodation rather than ownership.\n\n"

            "If your primary need is stable rental housing, ARH may be "
            "worth exploring further under PMAY-U 2.0."
        ),

    "arh_before_verification":
        (
            "Many applicants prefer understanding verification requirements "
            "before applying.\n\n"

            "Identity, beneficiary and supporting information may be reviewed "
            "during the assessment process."
        ),

    # =====================================
    # ISS INCOME
    # =====================================

    "iss_income_eligibility":
        (
            "Income eligibility is a common concern for applicants exploring "
            "ISS under PMAY-U 2.0.\n\n"

            "Income category may influence eligibility, but housing ownership "
            "conditions and other scheme requirements are also important."
        ),

    "iss_loan_eligibility":
        (
            "ISS is primarily designed for eligible beneficiaries with "
            "housing loan-related needs.\n\n"

            "Understanding whether a housing loan is involved is often "
            "an important step when evaluating ISS suitability."
        ),

    "iss_income_verification":
        (
            "Income verification is generally part of determining eligibility "
            "under PMAY-U 2.0 ISS.\n\n"

            "Supporting records may be reviewed to confirm eligibility conditions."
        ),

    "iss_before_income":
        (
            "Before applying for ISS, many applicants first want clarity "
            "on whether their income category may qualify.\n\n"

            "Income is usually evaluated together with housing loan and "
            "other PMAY-U 2.0 eligibility requirements."
        ),

    "iss_before_loan":
        (
            "ISS is most relevant when housing loan-related support is needed.\n\n"

            "If reducing housing loan burden is your goal, ISS may be a "
            "PMAY-U 2.0 component worth reviewing."
        ),

    "iss_before_verification":
        (
            "Verification requirements often create uncertainty before applying.\n\n"

            "Loan information, beneficiary details and supporting records "
            "may be reviewed during assessment."
        ),

    # =====================================
    # PORTAL FEELS BROKEN
    # =====================================

    "portal_tracking":
        (
            "Application tracking issues are among the most common portal-related concerns.\n\n"

            "Applicants sometimes experience difficulty locating updates "
            "or understanding the current PMAY-U 2.0 application stage.\n\n"

            "This does not automatically indicate a problem with eligibility."
        ),

    "portal_missing":
        (
            "A missing application can feel alarming, especially after "
            "submitting information and documents.\n\n"

            "In some situations, the issue may relate to tracking, search "
            "criteria or application visibility rather than the application itself."
        ),

    "portal_mismatch":
        (
            "Status mismatches can occur when information appears different "
            "from what an applicant expects.\n\n"

            "Verification, review and approval stages may sometimes create "
            "confusion about current application progress under PMAY-U 2.0."
        ),

    # =====================================
    # STATUS DIFFERENT EVERYWHERE
    # =====================================

    "status_portal":
        (
            "Portal updates are often the primary source of application information "
            "under PMAY-U 2.0.\n\n"

            "However, status updates may not always appear immediately after "
            "internal processing activities occur.\n\n"

            "Differences between portal information and other sources can sometimes "
            "be due to update timing rather than an actual issue."
        ),

    "status_sms":
        (
            "SMS notifications are intended to provide important updates, "
            "but they may not always contain the same level of detail as the portal.\n\n"

            "Timing differences between SMS alerts and portal updates can "
            "sometimes create confusion."
        ),

    "status_office":
        (
            "Information received from an office or local authority may sometimes "
            "appear different from online updates.\n\n"

            "This can happen when application processing is ongoing and "
            "different systems are updated at different times."
        ),

    # =====================================
    # PORTAL ISSUE OR MY MISTAKE
    # =====================================

    "portalmistake_tracking":
        (
            "Application tracking issues are among the most common PMAY-U 2.0 concerns.\n\n"

            "Applicants may have difficulty locating updates, understanding "
            "current status or identifying the stage of processing.\n\n"

            "A tracking issue does not automatically mean there is a problem "
            "with the application itself."
        ),

    "portalmistake_visibility":
        (
            "Status visibility concerns can occur when applicants expect "
            "to see updates that have not yet appeared.\n\n"

            "Verification and review activities may continue even when "
            "visible changes are limited."
        ),

    "portalmistake_login":
        (
            "Login-related issues can make it difficult to access "
            "application information.\n\n"

            "These technical concerns are often separate from eligibility "
            "or approval assessment under PMAY-U 2.0."
        ),

    # =====================================
    # VERIFICATION STAGE
    # =====================================

    "verification_purpose":
        (
            "Verification is an important part of the PMAY-U 2.0 process.\n\n"

            "It generally helps confirm beneficiary information, "
            "documents, housing details and other eligibility-related records.\n\n"

            "Being under verification does not automatically indicate a problem."
        ),

    "verification_status":
        (
            "Many applicants are unsure what a verification status actually means.\n\n"

            "In most cases, it indicates that information is being reviewed "
            "before the application can move to later stages."
        ),

    "verification_nextstep":
        (
            "After verification, an application may move to review, "
            "approval or other processing stages depending on the case.\n\n"

            "The exact path can vary based on PMAY-U 2.0 implementation procedures."
        ),

    # =====================================
    # GEO TAGGING
    # =====================================

    "geotag_status":
        (
            "Geo-tagging can sometimes appear as part of application progress "
            "or verification activities.\n\n"

            "Applicants are often unsure how it relates to the current status "
            "of their PMAY-U 2.0 application."
        ),

    "geotag_verification":
        (
            "Geo-tagging is commonly associated with location-related verification.\n\n"

            "Its purpose is generally to help validate housing or project-related "
            "information during processing."
        ),

    "geotag_nextstep":
        (
            "Many applicants want to know what happens after geo-tagging.\n\n"

            "The next stage may depend on verification results and other "
            "PMAY-U 2.0 processing requirements."
        ),

    # =====================================
    # STATUS LYING
    # =====================================

    "lyingstatus_portal":
        (
            "When portal information appears inconsistent, it can feel frustrating.\n\n"

            "In many cases, the issue is related to update timing rather than "
            "incorrect information.\n\n"

            "Processing activities may continue even when visible updates are delayed."
        ),

    "lyingstatus_sms":
        (
            "SMS updates can sometimes appear different from portal information.\n\n"

            "Differences may occur because notifications and status systems "
            "are updated at different times."
        ),

    "lyingstatus_office":
        (
            "Office-provided updates may occasionally seem different from "
            "online records.\n\n"

            "This can happen when information is received from different "
            "stages of the PMAY-U 2.0 process."
        ),

    # =====================================
    # WAIT / COMPLAIN / GIVE UP
    # =====================================

    "wait_delay":
        (
            "Long delays can understandably make applicants wonder what to do next.\n\n"

            "PMAY-U 2.0 applications may sometimes remain in verification "
            "or review stages longer than expected.\n\n"

            "A delay alone does not necessarily indicate rejection."
        ),

    "wait_status":
        (
            "Contradictory status information can create significant uncertainty.\n\n"

            "Understanding which source is providing the information is often "
            "the first step toward clarifying the situation."
        ),

    "wait_updates":
        (
            "Missing updates are one of the most common reasons applicants "
            "feel stuck or discouraged.\n\n"

            "Applications may continue progressing internally even when "
            "new status information is not immediately visible.\n\n"

            "Lack of updates does not automatically mean that processing has stopped."
        ),

    # =====================================
    # STATUS STRESS
    # =====================================

    "stressstatus_delay":
        (
            "Long approval timelines can create significant stress, "
            "especially when housing needs are urgent.\n\n"

            "PMAY-U 2.0 applications may move through verification, "
            "review and approval stages before a final decision is reached.\n\n"

            "A delay alone does not automatically mean rejection or ineligibility."
        ),

    "stressstatus_verification":
        (
            "Verification can sometimes feel never-ending because applicants "
            "may not know what is being reviewed.\n\n"

            "The verification stage generally helps confirm beneficiary, "
            "housing and document-related information before further processing."
        ),

    "stressstatus_updates":
        (
            "Unclear or infrequent updates are one of the most common "
            "sources of frustration during the PMAY-U 2.0 process.\n\n"

            "Applications may continue moving through internal stages "
            "even when visible updates are limited."
        ),

    # =====================================
    # FAMILY SAYS ELIGIBLE
    # =====================================

    "familyeligible_house":
        (
            "Housing conditions often play a major role in PMAY-U 2.0 eligibility.\n\n"

            "Applicants commonly become uncertain when their actual living "
            "situation differs from what family members believe.\n\n"

            "Housing ownership and current living conditions are often important factors."
        ),

    "familyeligible_income":
        (
            "Income category is one of the most common areas of confusion.\n\n"

            "Family members may assume eligibility based on income alone, "
            "while PMAY-U 2.0 generally considers additional conditions as well."
        ),

    "familyeligible_ownership":
        (
            "Ownership-related questions frequently create conflicting opinions.\n\n"

            "Whether you or your beneficiary family own a pucca house "
            "can be an important consideration under PMAY-U 2.0."
        ),

    # =====================================
    # FEEL ELIGIBLE BUT NOT LEGALLY
    # =====================================

    "emotioneligible_ownership":
        (
            "Many applicants feel they deserve support but remain uncertain "
            "about ownership-related conditions.\n\n"

            "Ownership status is often reviewed together with other "
            "PMAY-U 2.0 eligibility requirements."
        ),

    "emotioneligible_family":
        (
            "Family-related situations such as marriage, separation, "
            "dependency or inheritance can sometimes create uncertainty.\n\n"

            "These situations may influence how eligibility is assessed."
        ),

    "emotioneligible_documents":
        (
            "Documentation concerns are common even among applicants "
            "who believe they may otherwise qualify.\n\n"

            "Identity, ownership, income and address records are often "
            "important parts of the verification process."
        ),

    # =====================================
    # ENDLESS REQUIREMENTS
    # =====================================

    "requirements_documents":
        (
            "Document requirements can feel overwhelming because several "
            "different records may be reviewed during PMAY-U 2.0 processing.\n\n"

            "Identity proof, ownership records, income documents and "
            "bank details are common examples."
        ),

    "requirements_eligibility":
        (
            "Eligibility may seem complicated because multiple conditions "
            "are often considered together.\n\n"

            "Income, ownership, beneficiary family status and scheme-specific "
            "requirements can all influence assessment."
        ),

    "requirements_verification":
        (
            "Verification is intended to confirm the information provided "
            "during the PMAY-U 2.0 application process.\n\n"

            "Although it may feel repetitive, verification is generally "
            "an important step before approval decisions are made."
        ),

    # =====================================
    # DOCUMENTS ENOUGH?
    # =====================================

    "docenough_identity":
        (
            "Identity proof is one of the most important document categories "
            "used during PMAY-U 2.0 verification.\n\n"

            "Applicants commonly worry whether their identity records "
            "meet the required standards."
        ),

    "docenough_address":
        (
            "Address-related documents are frequently reviewed as part "
            "of beneficiary verification.\n\n"

            "Address mismatches or incomplete records are common concerns."
        ),

    "docenough_ownership":
        (
            "Ownership documents often create uncertainty, especially in cases "
            "involving inherited, shared or family-owned property.\n\n"

            "Clear ownership information is usually important for assessment."
        ),

    "docenough_income":
        (
            "Income proof is a common concern because applicants are often "
            "unsure what documentation may be accepted.\n\n"

            "Income verification can play an important role in determining "
            "the appropriate PMAY-U 2.0 category."
        ),

    # =====================================
    # WHAT CATEGORY AM I?
    # =====================================

    "category_income":
        (
            "Income category is often the starting point for understanding "
            "PMAY-U 2.0 eligibility.\n\n"

            "Applicants are generally assessed under categories such as "
            "EWS, LIG or MIG based on applicable income criteria."
        ),

    "category_eligibility":
        (
            "Category and eligibility are closely related but not identical.\n\n"

            "Even after identifying an income category, other PMAY-U 2.0 "
            "requirements may still need to be considered."
        ),

    "category_scheme":
        (
            "Sometimes the real challenge is choosing the most suitable "
            "PMAY-U 2.0 component rather than identifying an income category.\n\n"

            "Your housing goal, ownership situation and eligibility conditions "
            "can all help determine the most relevant scheme."
        ),

    # =====================================
    # FAMILY INCOME CONFUSION
    # =====================================

    "familyincome_spouse":
        (
            "Spouse income is one of the most common sources of confusion "
            "when understanding PMAY-U 2.0 eligibility.\n\n"

            "Applicants often wonder whether income should be considered "
            "individually or together with their spouse's income.\n\n"

            "Beneficiary family and income-related conditions are generally "
            "reviewed together during eligibility assessment."
        ),

    "familyincome_parents":
        (
            "Questions about parents' income are common, especially when "
            "multiple generations live in the same household.\n\n"

            "Applicants are often unsure whether parental income affects "
            "their PMAY-U 2.0 eligibility or category assessment."
        ),

    "familyincome_joint":
        (
            "Joint family income situations can feel complicated because "
            "several family members may contribute financially.\n\n"

            "Understanding how the beneficiary family is defined is often "
            "an important step when evaluating income-related questions."
        ),

    # =====================================
    # INCOME RULES
    # =====================================

    "incomerules_category":
        (
            "Income categories such as EWS, LIG and MIG are frequently "
            "used within PMAY-U 2.0 eligibility discussions.\n\n"

            "Many applicants are unsure which category may apply to them "
            "and how category selection affects eligibility."
        ),

    "incomerules_proof":
        (
            "Income proof requirements are a common concern, especially "
            "for applicants with informal or variable sources of income.\n\n"

            "Verification generally relies on supporting records or other "
            "acceptable documentation where applicable."
        ),

    "incomerules_family":
        (
            "Family income questions often arise when applicants are unsure "
            "whose income should be considered during assessment.\n\n"

            "Understanding beneficiary family definitions is usually helpful "
            "when addressing this concern."
        ),

    # =====================================
    # RULES FEEL HIDDEN
    # =====================================

    "hiddenrules_family":
        (
            "Family-related rules can sometimes appear complicated because "
            "household situations vary significantly between applicants.\n\n"

            "Marriage, dependency, separation and beneficiary family definitions "
            "are common areas of confusion."
        ),

    "hiddenrules_ownership":
        (
            "Ownership rules are among the most misunderstood aspects of PMAY-U 2.0.\n\n"

            "Applicants often have questions about family property, inherited "
            "houses, shared ownership and pucca house conditions."
        ),

    "hiddenrules_housing":
        (
            "Housing-related rules may feel unclear because different "
            "PMAY-U 2.0 components serve different housing needs.\n\n"

            "Buying, building, renting and housing loan support may each "
            "involve different eligibility considerations."
        ),

    # =====================================
    # OWNERSHIP RULES
    # =====================================

    "ownership_land":
        (
            "Land ownership questions are especially common among applicants "
            "considering construction-related support under PMAY-U 2.0.\n\n"

            "Applicants often want to understand how land availability "
            "affects eligibility and scheme suitability."
        ),

    "ownership_house":
        (
            "House ownership is one of the most important eligibility-related "
            "considerations under PMAY-U 2.0.\n\n"

            "Many applicants are unsure whether existing housing arrangements "
            "affect their eligibility."
        ),

    "ownership_spouse":
        (
            "Spouse ownership situations can create uncertainty, particularly "
            "when property is held in one person's name.\n\n"

            "Applicants frequently ask how spouse-owned property may affect "
            "PMAY-U 2.0 eligibility assessment."
        ),

    "ownership_inheritance":
        (
            "Inherited property often creates questions about legal ownership "
            "and housing eligibility.\n\n"

            "Understanding who officially owns the property is usually an "
            "important part of evaluating ownership-related concerns."
        ),

    # =====================================
    # BENEFICIARY VALIDATION
    # =====================================

    "beneficiary_status":
        (
            "Beneficiary validation status can be confusing because many "
            "applicants are unsure what it means in practice.\n\n"

            "It generally indicates that beneficiary-related information "
            "is being reviewed or confirmed as part of the PMAY-U 2.0 process."
        ),

    "beneficiary_meaning":
        (
            "Beneficiary validation is typically intended to confirm that "
            "application information matches relevant eligibility records.\n\n"

            "Many applicants see the term without understanding its role "
            "within the overall application workflow."
        ),

    "beneficiary_nextstep":
        (
            "After beneficiary validation, applications may move to "
            "additional review, verification or approval-related stages.\n\n"

            "The exact next step depends on the current PMAY-U 2.0 processing stage."
        ),

    # =====================================
    # GEO TAGGING SCARY
    # =====================================

    "geoscary_location":
        (
            "Geo-tagging is commonly associated with location-related "
            "verification activities under PMAY-U 2.0.\n\n"

            "Many applicants worry when they first hear the term, even "
            "though it is generally used for validation purposes."
        ),

    "geoscary_status":
        (
            "Applicants sometimes worry that geo-tagging may negatively "
            "affect their application status.\n\n"

            "Geo-tagging is generally part of verification-related processes "
            "rather than an automatic approval or rejection decision."
        ),

    # =====================================
    # APPROVED OR VERIFYING
    # =====================================

    "approved_statusword":
        (
            "Many PMAY-U 2.0 applicants become confused by status wording "
            "because different stages can sound similar.\n\n"

            "Terms related to verification, review and approval may appear "
            "close in meaning even though they represent different workflow stages.\n\n"

            "Understanding the exact wording is often the first step toward clarity."
        ),

    "approved_verification":
        (
            "Verification generally indicates that beneficiary, document "
            "or housing-related information is still being reviewed.\n\n"

            "An application under verification has not necessarily reached "
            "the final approval stage yet."
        ),

    "approved_approval":
        (
            "Approval stages usually occur after required verification "
            "and review activities are completed.\n\n"

            "Many applicants are unsure whether their case is still under "
            "review or has already moved into approval processing."
        ),

    # =====================================
    # WHO IS APPROVING
    # =====================================

    "approving_ulb":
        (
            "ULB (Urban Local Body) plays an important role in many "
            "PMAY-U 2.0 implementation and verification processes.\n\n"

            "Applicants often see references to ULB activities without "
            "fully understanding how they fit into the overall workflow."
        ),

    "approving_verification":
        (
            "Verification is one of the key stages before final decisions "
            "can be made under PMAY-U 2.0.\n\n"

            "It helps confirm beneficiary information, documents and "
            "other relevant eligibility-related details."
        ),

    "approving_approval":
        (
            "Approval stages can seem confusing because multiple reviews "
            "may occur before a final outcome is recorded.\n\n"

            "Applicants often want to understand who reviews the application "
            "and when approval decisions are made."
        ),

    # =====================================
    # DELAYED VERIFICATION STILL CHANCE?
    # =====================================

    "chance_verification":
        (
            "Delayed verification does not automatically mean rejection "
            "under PMAY-U 2.0.\n\n"

            "Applications may remain under verification for various reasons, "
            "including document review, beneficiary checks or workflow processing.\n\n"

            "Verification delay alone is not usually enough to determine the final outcome."
        ),

    "chance_updates":
        (
            "Missing updates can make applicants feel that nothing is happening.\n\n"

            "However, PMAY-U 2.0 applications may continue progressing through "
            "internal stages even when visible updates are limited."
        ),

    "chance_approval":
        (
            "Approval uncertainty is common when verification takes longer "
            "than expected.\n\n"

            "A delayed timeline does not necessarily indicate that the "
            "application has been rejected or closed."
        ),

    # =====================================
    # PORTAL EXHAUSTION
    # =====================================

    "portalstress_delay":
        (
            "Repeatedly checking for updates during a long delay can feel exhausting.\n\n"

            "Many PMAY-U 2.0 applicants experience frustration when expected "
            "progress is not immediately visible."
        ),

    "portalstress_wording":
        (
            "Status descriptions can sometimes feel unclear or difficult to interpret.\n\n"

            "Applicants often see technical terms without understanding "
            "how they relate to the overall PMAY-U 2.0 process."
        ),

    "portalstress_updates":
        (
            "Missing or infrequent updates are one of the most common "
            "sources of portal-related stress.\n\n"

            "Applications may continue moving through internal stages "
            "even when updates are not immediately reflected."
        ),

    # =====================================
    # TRUST PORTAL OR OFFICE
    # =====================================

    "trustsource_portal":
        (
            "When portal information appears inconsistent, applicants "
            "often become uncertain about their actual status.\n\n"

            "Differences may sometimes occur because updates are reflected "
            "at different times across systems."
        ),

    "trustsource_office":
        (
            "Office-provided information may occasionally seem different "
            "from online records.\n\n"

            "This can happen when information comes from different stages "
            "of PMAY-U 2.0 processing."
        ),

    "trustsource_both":
        (
            "Conflicting information from multiple sources can understandably "
            "create frustration and uncertainty.\n\n"

            "Differences do not always indicate a problem and may sometimes "
            "result from timing or workflow-related updates."
        ),

    # =====================================
    # INCOME / DOCUMENTS / STATUS
    # =====================================

    "mixedproblem_income":
        (
            "Income-related concerns often involve category eligibility, "
            "income proof or family income assessment.\n\n"

            "Understanding the income-related issue is often the first step "
            "toward clarifying PMAY-U 2.0 eligibility questions."
        ),

    "mixedproblem_documents":
        (
            "Document concerns commonly involve identity proof, address proof, "
            "ownership records or income-related documents.\n\n"

            "Document verification plays an important role in PMAY-U 2.0 processing."
        ),

    "mixedproblem_status":
        (
            "Status-related concerns often involve tracking, verification, "
            "approval stages or missing updates.\n\n"

            "Understanding the current application stage can help identify "
            "what may be causing uncertainty."
        ),

    # =====================================
    # OFFICER SAYS POSITIVE / PORTAL NEGATIVE
    # =====================================

    "trust_status_mismatch":
        (
            "Conflicting information from different sources can be frustrating.\n\n"

            "Sometimes office feedback and portal updates may not appear "
            "identical because they are updated at different stages of the "
            "PMAY-U 2.0 process.\n\n"

            "A mismatch does not automatically indicate approval or rejection."
        ),

    "trust_verification_delay":
        (
            "Verification delays can create uncertainty, especially when "
            "other updates appear positive.\n\n"

            "PMAY-U 2.0 applications may remain under review while "
            "beneficiary or document checks are being completed."
        ),

    # =====================================
    # STATUS CONFUSING + MENTAL EXHAUSTION
    # =====================================

    "mental_delay":
        (
            "Long delays can make applicants feel exhausted and uncertain.\n\n"

            "PMAY-U 2.0 applications may spend time in verification, review "
            "and approval stages before a final outcome is visible.\n\n"

            "A delay alone does not automatically mean rejection."
        ),

    "mental_rejection":
        (
            "Many applicants worry that a slow process means rejection.\n\n"

            "However, PMAY-U 2.0 applications may remain active even when "
            "updates are delayed or progress appears slow."
        ),

    "mental_wording":
        (
            "Status wording can sometimes feel difficult to understand.\n\n"

            "Terms such as verification, beneficiary validation, review "
            "or approval may sound similar even though they represent "
            "different stages of processing."
        ),

    # =====================================
    # APPLICATION STRESS > HOUSING STRESS
    # =====================================

    "applicationstress_status":
        (
            "Status uncertainty is one of the most common sources of stress "
            "during the PMAY-U 2.0 process.\n\n"

            "Applicants often spend significant time trying to understand "
            "what their current application stage actually means."
        ),

    "applicationstress_eligibility":
        (
            "Eligibility concerns can create ongoing uncertainty, especially "
            "when ownership, income or family situations feel complicated.\n\n"

            "Many PMAY-U 2.0 applicants experience similar confusion."
        ),

    "applicationstress_verification":
        (
            "Verification stages can feel stressful when applicants are "
            "unsure what information is being reviewed.\n\n"

            "Verification is generally intended to confirm beneficiary and "
            "application details before further processing."
        ),

    # =====================================
    # I DON'T UNDERSTAND PMAY
    # =====================================

    "basic_house":
        (
            "Many people first explore PMAY-U 2.0 because they need better "
            "housing, rental support or home ownership assistance.\n\n"

            "Understanding your housing situation is often the best place to start."
        ),

    "basic_eligibility":
        (
            "PMAY-U 2.0 eligibility generally depends on factors such as "
            "income category, housing ownership and beneficiary family conditions.\n\n"

            "Learning eligibility basics is often the first step."
        ),

    "basic_process":
        (
            "The PMAY-U 2.0 process typically involves application, "
            "verification, review and approval-related stages.\n\n"

            "Many applicants initially find the workflow confusing."
        ),

    # =====================================
    # PMAY WORTH TRYING?
    # =====================================

    "worth_house":
        (
            "Whether PMAY-U 2.0 is worth exploring often depends on your "
            "current housing situation and needs.\n\n"

            "Housing ownership, rental situation and housing difficulty "
            "are common starting points."
        ),

    "worth_income":
        (
            "Income category may influence which PMAY-U 2.0 options are "
            "most relevant to your situation.\n\n"

            "Many applicants begin by understanding their income category."
        ),

    "worth_eligibility":
        (
            "Eligibility concerns are common before applying.\n\n"

            "Understanding ownership, income and beneficiary-family conditions "
            "can help determine whether PMAY-U 2.0 is worth exploring further."
        ),

    # =====================================
    # DON'T UNDERSTAND RULES
    # =====================================

    "rule_house":
        (
            "Housing and ownership rules are among the most commonly "
            "misunderstood parts of PMAY-U 2.0.\n\n"

            "Applicants often have questions about pucca houses, family property "
            "and ownership conditions."
        ),

    "rule_income":
        (
            "Income-related rules may seem confusing because categories such as "
            "EWS, LIG and MIG have different criteria.\n\n"

            "Income is usually assessed together with other eligibility conditions."
        ),

    "rule_family":
        (
            "Family eligibility questions often involve spouse, children, "
            "parents or beneficiary-family definitions.\n\n"

            "These rules can affect how PMAY-U 2.0 eligibility is assessed."
        ),

    # =====================================
    # MANY RULES SCARY
    # =====================================

    "scary_eligibility":
        (
            "Eligibility rules can seem overwhelming when multiple conditions "
            "must be understood together.\n\n"

            "Income, ownership and beneficiary-family requirements are "
            "common areas of confusion."
        ),

    "scary_documents":
        (
            "Document requirements can feel intimidating at first.\n\n"

            "Identity, address, income and ownership-related records are "
            "among the most commonly discussed PMAY-U 2.0 documents."
        ),

    "scary_status":
        (
            "Application status stages often appear complicated because "
            "different processing terms are used throughout PMAY-U 2.0.\n\n"

            "Understanding the meaning of each stage usually makes the "
            "process easier to follow."
        ),

    # =====================================
    # PMAY WORTH TRYING MAYBE
    # =====================================

    "worthmaybe_house":
        (
            "Whether PMAY-U 2.0 is worth exploring often depends on your "
            "current housing situation.\n\n"

            "Applicants commonly evaluate factors such as renting, housing "
            "instability, existing housing conditions and long-term housing needs.\n\n"

            "Understanding your housing situation is usually the first step."
        ),

    "worthmaybe_income":
        (
            "Income-related concerns are common before exploring PMAY-U 2.0.\n\n"

            "Income category may affect which scheme components and eligibility "
            "conditions are most relevant to your situation.\n\n"

            "Income is generally considered together with other eligibility factors."
        ),

    "worthmaybe_eligibility":
        (
            "Many people are unsure whether they should even start the PMAY-U 2.0 process.\n\n"

            "Eligibility is usually assessed using factors such as housing ownership, "
            "income category and beneficiary-family conditions.\n\n"

            "Understanding these basics can help determine whether it is worth exploring further."
        ),

    # =====================================
    # FAMILY SAYS ELIGIBLE
    # =====================================

    "familysays_house":
        (
            "Family members may sometimes judge eligibility based only on "
            "current living conditions.\n\n"

            "However, PMAY-U 2.0 assessment may also consider ownership-related "
            "and beneficiary-family conditions in addition to housing needs."
        ),

    "familysays_ownership":
        (
            "Ownership-related concerns often create different opinions within families.\n\n"

            "Questions about family property, inherited houses and shared ownership "
            "are among the most common PMAY-U 2.0 eligibility concerns."
        ),

    "familysays_income":
        (
            "Family members may focus on income while eligibility can involve "
            "additional factors beyond income alone.\n\n"

            "Income category is important, but ownership and beneficiary-family "
            "conditions may also be reviewed."
        ),

    # =====================================
    # HIDDEN RULE FEAR
    # =====================================

    "hiddenfear_house":
        (
            "Many applicants worry there may be housing-related rules they have missed.\n\n"

            "Questions about current housing condition, pucca house ownership "
            "and housing eligibility are common under PMAY-U 2.0."
        ),

    "hiddenfear_family":
        (
            "Family-related rules can sometimes seem confusing because every "
            "household situation is different.\n\n"

            "Marriage, dependency, separation and beneficiary-family definitions "
            "are common areas of uncertainty."
        ),

    "hiddenfear_ownership":
        (
            "Ownership rules are among the most frequently misunderstood parts "
            "of PMAY-U 2.0.\n\n"

            "Applicants often worry about family property, inherited property "
            "or ownership records affecting eligibility."
        ),

    # =====================================
    # FEEL ELIGIBLE BUT HIDDEN PROBLEM
    # =====================================

    "hiddenproblem_house":
        (
            "Many applicants feel their housing need clearly qualifies them, "
            "but still worry that something has been overlooked.\n\n"

            "Housing-related eligibility questions are very common during "
            "the PMAY-U 2.0 process."
        ),

    "hiddenproblem_income":
        (
            "Income uncertainty can create concerns even when applicants "
            "otherwise feel eligible.\n\n"

            "Income category assessment is often reviewed together with "
            "other PMAY-U 2.0 eligibility conditions."
        ),

    "hiddenproblem_ownership":
        (
            "Ownership concerns are one of the most common reasons people "
            "feel uncertain about eligibility.\n\n"

            "Family-owned, inherited or shared property situations often "
            "raise additional questions."
        ),

    # =====================================
    # BENEFICIARY FAMILY
    # =====================================

    "beneficiary_parents":
        (
            "Many applicants are unsure whether parents are considered part "
            "of the beneficiary family under PMAY-U 2.0.\n\n"

            "Questions about household structure and family relationships "
            "are common when assessing eligibility."
        ),

    "beneficiary_spouse":
        (
            "Spouse-related questions are among the most common beneficiary-family concerns.\n\n"

            "Applicants often want to understand how spouse information, "
            "income and ownership situations affect assessment."
        ),

    "beneficiary_separate":
        (
            "Living separately can create confusion about how beneficiary-family "
            "conditions are interpreted.\n\n"

            "Many applicants seek clarification when household arrangements "
            "do not fit a simple category."
        ),

    # =====================================
    # RULES TOO CONFUSING
    # =====================================

    "toomanyrules_house":
        (
            "Housing rules can seem overwhelming at first because different "
            "PMAY-U 2.0 components support different housing needs.\n\n"

            "Buying, building and rental-related situations may involve "
            "different requirements."
        ),

    "toomanyrules_family":
        (
            "Family-related rules are often challenging because household "
            "situations vary significantly from one applicant to another.\n\n"

            "Beneficiary-family definitions are a common source of confusion."
        ),

    "toomanyrules_ownership":
        (
            "Ownership-related rules frequently cause uncertainty among applicants.\n\n"

            "Family property, inherited houses and shared ownership arrangements "
            "are some of the most common PMAY-U 2.0 concerns."
        ),

    # =====================================
    # FAMILY SAYS ELIGIBLE
    # =====================================

    "familyyes_house":
        (
            "Many applicants receive different opinions from family members "
            "about PMAY-U 2.0 eligibility.\n\n"

            "Housing condition and current living situation are important "
            "factors, but they are usually reviewed together with other "
            "eligibility requirements."
        ),

    "familyyes_income":
        (
            "Family members may focus mainly on income while PMAY-U 2.0 "
            "eligibility can involve additional conditions.\n\n"

            "Income category is important, but ownership and beneficiary-family "
            "conditions may also be considered."
        ),

    "familyyes_ownership":
        (
            "Ownership-related concerns often create uncertainty even when "
            "others believe you may be eligible.\n\n"

            "Family property, inherited property and pucca house ownership "
            "questions are common under PMAY-U 2.0."
        ),

    # =====================================
    # FULL FORM CONFUSION
    # =====================================

    "fullform_blc":
        (
            "BLC stands for Beneficiary Led Construction under PMAY-U 2.0.\n\n"

            "It is generally associated with eligible beneficiaries who want "
            "to construct or improve a house using available land."
        ),

    "fullform_ahp":
        (
            "AHP stands for Affordable Housing in Partnership.\n\n"

            "This PMAY-U 2.0 component is generally related to affordable "
            "housing units developed through approved housing projects."
        ),

    "fullform_arh":
        (
            "ARH stands for Affordable Rental Housing.\n\n"

            "It focuses on rental housing support rather than home ownership."
        ),

    "fullform_iss":
        (
            "ISS stands for Interest Subsidy Scheme under PMAY-U 2.0.\n\n"

            "It is generally associated with eligible housing loan-related support."
        ),

    # =====================================
    # MANY SCHEMES CONFUSING
    # =====================================

    "scheme_build":
        (
            "If your primary goal is constructing or improving a house, "
            "construction-related PMAY-U 2.0 options may be more relevant.\n\n"

            "Understanding land and housing availability is often the first step."
        ),

    "scheme_rent":
        (
            "If your immediate need is affordable rental accommodation, "
            "rental-focused PMAY-U 2.0 options may be worth understanding first.\n\n"

            "Rental needs are different from ownership needs."
        ),

    "scheme_buy":
        (
            "If your goal is purchasing a house or affordable housing unit, "
            "ownership-oriented PMAY-U 2.0 components may be more relevant.\n\n"

            "Many applicants start by identifying whether they want to buy rather than build."
        ),

    "scheme_loan":
        (
            "If reducing housing loan burden is your main concern, "
            "loan-support-related PMAY-U 2.0 components may be worth exploring.\n\n"

            "Housing loan requirements often differ from ownership or rental needs."
        ),

    # =====================================
    # WIFE SAYS AHP, I THINK BLC
    # =====================================

    "wife_blc":
        (
            "BLC and AHP serve different housing needs under PMAY-U 2.0.\n\n"

            "BLC is generally associated with construction or improvement "
            "of a house, making land-related questions important."
        ),

    "wife_ahp":
        (
            "AHP is generally associated with obtaining a housing unit "
            "through an approved affordable housing project.\n\n"

            "Applicants often compare AHP and BLC when deciding between "
            "building and obtaining ready housing."
        ),

    # =====================================
    # PMAY SCHEME NO UNDERSTAND
    # =====================================

    "understand_build":
        (
            "Building-related housing needs usually involve questions "
            "about land, construction and housing improvement.\n\n"

            "Understanding your housing goal often helps identify the most relevant PMAY-U 2.0 component."
        ),

    "understand_rent":
        (
            "Rental housing needs are different from ownership-related needs.\n\n"

            "Applicants seeking affordable accommodation often start by understanding rental-focused options."
        ),

    "understand_buy":
        (
            "Buying a house generally involves different PMAY-U 2.0 pathways "
            "than renting or constructing one.\n\n"

            "Identifying your housing objective is usually the best starting point."
        ),

    "understand_loan":
        (
            "Loan-related support is intended for applicants concerned about "
            "housing finance and affordability.\n\n"

            "Understanding whether a housing loan is involved helps narrow the options."
        ),

    # =====================================
    # ALL SCHEMES HEADACHE
    # =====================================

    "headpain_blc":
        (
            "BLC questions usually involve land, construction and eligibility-related concerns.\n\n"

            "Many applicants find BLC confusing because ownership and land availability may be important."
        ),

    "headpain_ahp":
        (
            "AHP questions often involve affordable housing projects, "
            "housing purchase and eligibility requirements.\n\n"

            "Understanding the housing objective usually helps simplify AHP decisions."
        ),

    "headpain_arh":
        (
            "ARH can feel confusing because it focuses on rental housing "
            "rather than ownership support.\n\n"

            "Applicants often compare ARH with ownership-oriented PMAY-U 2.0 options."
        ),

    "headpain_iss":
        (
            "ISS questions commonly involve housing loans, subsidy support "
            "and eligibility requirements.\n\n"

            "Loan-related terminology often creates confusion for applicants."
        ),

    # =====================================
    # WHICH VERTICAL
    # =====================================

    "vertical_build":
        (
            "If your goal is to build or improve a house, construction-related "
            "PMAY-U 2.0 support may be most relevant.\n\n"

            "Housing objective is usually the first factor used to identify the correct vertical."
        ),

    "vertical_rent":
        (
            "If your primary need is affordable rental accommodation, "
            "rental-focused PMAY-U 2.0 support may be worth exploring.\n\n"

            "Rental and ownership needs are assessed differently."
        ),

    "vertical_buy":
        (
            "Applicants looking to purchase a house often explore "
            "ownership-oriented PMAY-U 2.0 components.\n\n"

            "The housing objective usually helps determine the most relevant option."
        ),

    "vertical_loan":
        (
            "If housing loan affordability is the main concern, "
            "loan-related PMAY-U 2.0 support may be more relevant.\n\n"

            "Loan-support needs are different from construction or rental needs."
        ),

    # =====================================
    # BLC ELIGIBLE OR NOT
    # =====================================

    "blceligible_land":
        (
            "Land-related questions are among the most common concerns "
            "when evaluating BLC under PMAY-U 2.0.\n\n"

            "Applicants often want to understand how available land affects suitability."
        ),

    "blceligible_house":
        (
            "Housing ownership and current housing conditions are commonly "
            "reviewed when discussing BLC-related eligibility.\n\n"

            "Many applicants are unsure how existing housing situations are evaluated."
        ),

    "blceligible_family":
        (
            "Beneficiary-family conditions can sometimes create uncertainty "
            "when assessing BLC eligibility.\n\n"

            "Family ownership, household structure and related factors may raise questions."
        ),

    # =====================================
    # BLC PAPER CONFUSION
    # =====================================

    "blcpaper_land":
        (
            "Land-related documents are among the most common concerns "
            "for applicants exploring BLC under PMAY-U 2.0.\n\n"

            "Applicants often want clarity about land ownership records, "
            "supporting property documents and related verification requirements.\n\n"

            "Land documentation is frequently reviewed as part of the process."
        ),

    "blcpaper_aadhaar":
        (
            "Aadhaar-related concerns can create confusion when applicants "
            "are unsure whether their details match other records.\n\n"

            "Identity verification is an important part of PMAY-U 2.0 processing "
            "and applicants often seek clarification on Aadhaar-related requirements."
        ),

    "blcpaper_income":
        (
            "Income proof requirements can feel confusing, especially when "
            "income sources are informal or difficult to document.\n\n"

            "Income-related verification may be reviewed alongside other "
            "BLC eligibility and beneficiary requirements."
        ),

    # =====================================
    # BLC RULES HEADACHE
    # =====================================

    "blcrules_land":
        (
            "Land-related rules are among the most frequently discussed "
            "topics under BLC in PMAY-U 2.0.\n\n"

            "Applicants often have questions about land availability, "
            "ownership records and suitability for construction-related support."
        ),

    "blcrules_family":
        (
            "Family-related situations can affect how applicants understand "
            "BLC requirements.\n\n"

            "Beneficiary-family conditions, shared property situations and "
            "household arrangements are common sources of confusion."
        ),

    "blcrules_ownership":
        (
            "Ownership-related rules are one of the biggest reasons applicants "
            "find BLC difficult to understand.\n\n"

            "Questions involving inherited, shared or family-owned property "
            "are especially common."
        ),

    # =====================================
    # BLC PROCESS TIRED
    # =====================================

    "blcprocess_status":
        (
            "Many PMAY-U 2.0 applicants become tired trying to understand "
            "different application status stages.\n\n"

            "Status descriptions can sometimes feel technical and difficult to interpret."
        ),

    "blcprocess_delay":
        (
            "Long processing timelines can make the BLC process feel exhausting.\n\n"

            "Applications may spend time in verification, review and approval-related stages "
            "before final outcomes become visible."
        ),

    "blcprocess_verification":
        (
            "Verification stages can sometimes feel repetitive because applicants "
            "may not know exactly what is being reviewed.\n\n"

            "Verification generally helps confirm beneficiary and housing-related information."
        ),

    # =====================================
    # BLC STATUS MEANING
    # =====================================

    "blcstatus_meaning":
        (
            "Many applicants see a status but are unsure what it actually means.\n\n"

            "PMAY-U 2.0 status terms often refer to different processing, "
            "verification or approval-related activities."
        ),

    "blcstatus_stage":
        (
            "Understanding the current stage is often more important than "
            "focusing only on the status name.\n\n"

            "Different stages may indicate verification, review, approval "
            "or other workflow activities."
        ),

    "blcstatus_next":
        (
            "Applicants commonly want to know what happens after the current stage.\n\n"

            "The next step generally depends on the application's progress "
            "within the PMAY-U 2.0 workflow."
        ),

    # =====================================
    # AHP ELIGIBILITY
    # =====================================

    "ahpeligible_house":
        (
            "Housing-related eligibility questions are common when exploring "
            "AHP under PMAY-U 2.0.\n\n"

            "Applicants often want to understand how their current housing "
            "situation affects eligibility considerations."
        ),

    "ahpeligible_family":
        (
            "Family-related eligibility concerns can arise when household "
            "situations are complex.\n\n"

            "Beneficiary-family definitions and household circumstances "
            "are common areas of confusion."
        ),

    "ahpeligible_ownership":
        (
            "Ownership-related concerns are among the most common reasons "
            "people feel uncertain about AHP eligibility.\n\n"

            "Questions about family property, inherited property and housing "
            "ownership frequently arise."
        ),

    # =====================================
    # FEEL ELIGIBLE BUT HIDDEN PROBLEM
    # =====================================

    "hiddenahp_house":
        (
            "Many applicants feel their housing situation should qualify them "
            "but still worry they may have overlooked something important.\n\n"

            "Housing-related eligibility questions are very common under PMAY-U 2.0."
        ),

    "hiddenahp_family":
        (
            "Family situations sometimes create uncertainty even when applicants "
            "otherwise feel confident about eligibility.\n\n"

            "Household structure and beneficiary-family considerations may raise questions."
        ),

    "hiddenahp_ownership":
        (
            "Ownership concerns are one of the most common reasons applicants "
            "feel uncertain despite believing they may qualify.\n\n"

            "Family-owned, inherited and shared property situations often create doubt."
        ),

    # =====================================
    # AHP ELIGIBILITY HEADACHE
    # =====================================

    "ahppain_house":
        (
            "Housing-related eligibility requirements can seem complicated "
            "when applicants are unsure how their current living situation is assessed.\n\n"

            "Many AHP questions begin with understanding the housing need itself."
        ),

    "ahppain_ownership":
        (
            "Ownership-related eligibility questions are among the most common "
            "sources of confusion in AHP discussions.\n\n"

            "Property ownership situations often require careful understanding."
        ),

    "ahppain_family":
        (
            "Family eligibility concerns can feel difficult when household "
            "situations do not fit a simple category.\n\n"

            "Beneficiary-family conditions are frequently discussed by AHP applicants."
        ),

    # =====================================
    # AHP PAPER CONFUSION
    # =====================================

    "ahppaper_aadhaar":
        (
            "Aadhaar-related concerns are common when applying under "
            "AHP in PMAY-U 2.0.\n\n"

            "Applicants often worry about incorrect details, mismatches "
            "with other records, or whether Aadhaar information is properly updated.\n\n"

            "Identity verification is an important part of the application process."
        ),

    "ahppaper_income":
        (
            "Income proof requirements can feel confusing, especially when "
            "income sources are informal, seasonal or difficult to document.\n\n"

            "Income-related verification may be reviewed together with other "
            "PMAY-U 2.0 eligibility requirements."
        ),

    "ahppaper_address":
        (
            "Address-related documents are frequently reviewed during "
            "PMAY-U 2.0 verification.\n\n"

            "Applicants commonly worry about address mismatches, incomplete "
            "records or differences between documents."
        ),

    # =====================================
    # AHP VERIFICATION FEAR
    # =====================================

    "ahpverify_documents":
        (
            "Document verification can feel stressful when applicants are "
            "unsure whether they have provided everything correctly.\n\n"

            "Identity, income, address and other supporting documents may "
            "be reviewed as part of the PMAY-U 2.0 process."
        ),

    "ahpverify_officer":
        (
            "Many applicants become nervous when they hear about verification "
            "or officer-related checks.\n\n"

            "These checks are generally intended to validate beneficiary "
            "and application information before further processing."
        ),

    "ahpverify_delay":
        (
            "Verification delays can understandably create anxiety.\n\n"

            "However, a delay in verification does not automatically mean "
            "rejection under PMAY-U 2.0.\n\n"

            "Applications may continue progressing through different stages."
        ),

    # =====================================
    # BENEFICIARY FAMILY
    # =====================================

    "ahpfamily_parents":
        (
            "Questions about parents are common when understanding "
            "beneficiary-family conditions under PMAY-U 2.0.\n\n"

            "Applicants often want to know how household structure may "
            "affect eligibility assessment."
        ),

    "ahpfamily_spouse":
        (
            "Spouse-related questions are among the most common "
            "beneficiary-family concerns.\n\n"

            "Applicants frequently seek clarification about ownership, "
            "income and family-related eligibility conditions."
        ),

    "ahpfamily_separate":
        (
            "Separate living arrangements can sometimes create confusion "
            "about beneficiary-family interpretation.\n\n"

            "Many applicants have housing situations that do not fit a "
            "simple category and need additional clarification."
        ),

    # =====================================
    # AHP RULES
    # =====================================

    "ahprules_family":
        (
            "Family-related rules can feel complicated because household "
            "situations vary significantly from one applicant to another.\n\n"

            "Marriage, dependency and beneficiary-family definitions are "
            "common areas of confusion under PMAY-U 2.0."
        ),

    "ahprules_ownership":
        (
            "Ownership-related rules are among the most frequently misunderstood "
            "parts of PMAY-U 2.0 eligibility.\n\n"

            "Family property, inherited property and shared ownership situations "
            "often create uncertainty."
        ),

    "ahprules_housing":
        (
            "Housing-related rules can feel difficult to interpret when "
            "applicants are unsure how their current housing situation is evaluated.\n\n"

            "Housing need and ownership-related conditions are common concerns."
        ),

    # =====================================
    # AHP PROCESS
    # =====================================

    "ahpprocess_status":
        (
            "Application status is one of the most common sources of confusion "
            "for AHP applicants under PMAY-U 2.0.\n\n"

            "Different status labels may represent different stages of processing, "
            "review or approval."
        ),

    "ahpprocess_delay":
        (
            "Long processing timelines can make the application process feel exhausting.\n\n"

            "Applications may spend time in verification, review and approval "
            "stages before final outcomes become visible."
        ),

    "ahpprocess_verification":
        (
            "Verification stages can sometimes feel repetitive because applicants "
            "may not know what information is currently being reviewed.\n\n"

            "Verification generally helps confirm beneficiary and application details."
        ),

    # =====================================
    # AHP STATUS
    # =====================================

    "ahpstatus_meaning":
        (
            "Many applicants see a status message but are unsure what it actually means.\n\n"

            "PMAY-U 2.0 status terms often refer to different workflow, "
            "verification or approval-related activities."
        ),

    "ahpstatus_stage":
        (
            "Understanding the current stage is often more helpful than "
            "focusing only on the status name.\n\n"

            "Different stages may indicate verification, review, approval "
            "or other processing activities."
        ),

    "ahpstatus_next":
        (
            "Applicants frequently want to know what happens after the current stage.\n\n"

            "The next step generally depends on the application's progress "
            "within the PMAY-U 2.0 workflow and verification process."
        ),

    # =====================================
    # WIFE WANTS AHP
    # =====================================

    "wifeahp_eligibility":
        (
            "Different family members may have different opinions about "
            "whether AHP under PMAY-U 2.0 is suitable.\n\n"

            "Eligibility usually depends on housing, ownership and beneficiary-related "
            "conditions rather than personal opinions alone.\n\n"

            "Understanding the eligibility concern is often the best starting point."
        ),

    "wifeahp_house":
        (
            "Housing needs are often the reason applicants explore AHP "
            "under PMAY-U 2.0.\n\n"

            "Many people compare their current housing situation with "
            "available affordable housing options before deciding."
        ),

    "wifeahp_ownership":
        (
            "Ownership-related concerns frequently influence whether "
            "applicants believe AHP may be suitable.\n\n"

            "Family property, inherited property and housing ownership "
            "questions are common discussion points."
        ),

    # =====================================
    # AHP STRESS
    # =====================================

    "ahpstress_delay":
        (
            "Long waiting periods can make the PMAY-U 2.0 process feel stressful.\n\n"

            "Applications may spend time in verification, review and approval "
            "stages before visible progress appears."
        ),

    "ahpstress_eligibility":
        (
            "Eligibility uncertainty is one of the most common reasons "
            "applicants feel overwhelmed.\n\n"

            "Housing ownership, income and beneficiary-family conditions "
            "may all contribute to uncertainty."
        ),

    "ahpstress_family":
        (
            "Family opinions can sometimes increase confusion during "
            "the PMAY-U 2.0 process.\n\n"

            "Different interpretations of eligibility often create doubt "
            "even when applicants have reviewed the rules themselves."
        ),

    # =====================================
    # FAMILY SAYS YES, MIND SAYS NO
    # =====================================

    "mindno_house":
        (
            "Many applicants worry their housing situation may not match "
            "PMAY-U 2.0 eligibility expectations.\n\n"

            "Housing-related concerns are among the most common reasons "
            "people feel uncertain despite encouragement from family."
        ),

    "mindno_income":
        (
            "Income-related uncertainty can create doubt even when others "
            "believe you may qualify.\n\n"

            "Income category is important, but it is usually considered "
            "alongside other eligibility factors."
        ),

    "mindno_ownership":
        (
            "Ownership concerns are one of the biggest reasons applicants "
            "question their eligibility.\n\n"

            "Family property, inherited housing and shared ownership "
            "situations often create uncertainty."
        ),

    # =====================================
    # AHP FOR ME?
    # =====================================

    "ahpforme_house":
        (
            "AHP under PMAY-U 2.0 is generally associated with affordable "
            "housing units through approved housing projects.\n\n"

            "Applicants often begin by assessing whether their housing need "
            "aligns with this objective."
        ),

    "ahpforme_income":
        (
            "Income category is commonly reviewed when applicants try to "
            "understand whether AHP may be relevant.\n\n"

            "Income is generally evaluated together with other PMAY-U 2.0 conditions."
        ),

    "ahpforme_ownership":
        (
            "Ownership-related questions are among the most common concerns "
            "for people considering AHP.\n\n"

            "Current housing ownership and family property situations "
            "often influence suitability discussions."
        ),

    # =====================================
    # ARH ELIGIBILITY
    # =====================================

    "arheligible_rent":
        (
            "ARH (Affordable Rental Housing) under PMAY-U 2.0 focuses on "
            "affordable rental accommodation.\n\n"

            "Applicants often want to understand whether their current "
            "rental housing need aligns with the scheme objective."
        ),

    "arheligible_worker":
        (
            "Many ARH discussions involve workers, migrants and people "
            "seeking affordable rental housing options.\n\n"

            "Applicants often have questions about how their situation "
            "relates to the intended purpose of ARH."
        ),

    "arheligible_family":
        (
            "Family housing situations can sometimes create uncertainty "
            "when evaluating ARH suitability.\n\n"

            "Current housing arrangements and rental needs are common concerns."
        ),

    # =====================================
    # ARH RULES
    # =====================================

    "arhrules_rent":
        (
            "Rental housing rules are often the first area of confusion "
            "for applicants exploring ARH under PMAY-U 2.0.\n\n"

            "Many people compare rental-focused support with ownership-focused schemes."
        ),

    "arhrules_worker":
        (
            "Worker-related eligibility discussions can sometimes feel complex.\n\n"

            "Applicants often seek clarification on how their employment "
            "or living situation relates to ARH."
        ),

    "arhrules_eligibility":
        (
            "Eligibility-related questions are common because ARH differs "
            "from ownership-oriented PMAY-U 2.0 components.\n\n"

            "Understanding the rental housing objective often helps reduce confusion."
        ),

    # =====================================
    # ARH PAPERS
    # =====================================

    "arhpaper_aadhaar":
        (
            "Aadhaar-related concerns are common during PMAY-U 2.0 verification.\n\n"

            "Applicants often worry about incorrect details, mismatches "
            "or document consistency."
        ),

    "arhpaper_rentproof":
        (
            "Rental proof is often a source of uncertainty for applicants "
            "trying to understand documentation requirements.\n\n"

            "Many users are unsure what records may help demonstrate "
            "their rental housing situation."
        ),

    "arhpaper_address":
        (
            "Address-related documents frequently create confusion when "
            "different records contain different information.\n\n"

            "Address verification is a common topic during PMAY-U 2.0 discussions."
        ),
    
    # =====================================
    # ARH INCOME CONFUSION
    # =====================================

    "arhincome_eligibility":
        (
            "Income eligibility can feel confusing when applicants are unsure "
            "which income category or assessment method applies.\n\n"

            "Under PMAY-U 2.0, income is often reviewed together with housing "
            "and beneficiary-family conditions.\n\n"

            "Many ARH applicants start by understanding how their income fits into the process."
        ),

    "arhincome_proof":
        (
            "Income proof can be challenging when income is informal, "
            "seasonal or varies from month to month.\n\n"

            "Applicants often worry about whether their available records "
            "adequately support their application."
        ),

    "arhincome_rent":
        (
            "Rental situation and income concerns often overlap for ARH applicants.\n\n"

            "Many people want to understand how their current housing and "
            "financial situation may relate to ARH under PMAY-U 2.0."
        ),

    # =====================================
    # FAMILY INCOME
    # =====================================

    "arhfamilyincome_spouse":
        (
            "Spouse income is one of the most common family-income questions "
            "raised by PMAY-U 2.0 applicants.\n\n"

            "Many applicants are unsure how spouse-related financial information "
            "fits into the overall assessment."
        ),

    "arhfamilyincome_parents":
        (
            "Questions involving parents and household income can sometimes "
            "create confusion.\n\n"

            "Applicants often want clarity on how family relationships may affect evaluation."
        ),

    "arhfamilyincome_joint":
        (
            "Joint household income situations can feel difficult to understand.\n\n"

            "Many applicants seek clarification when multiple earning members "
            "are part of the same household."
        ),

    # =====================================
    # UNSTABLE SALARY
    # =====================================

    "arhsalary_unstable":
        (
            "Irregular or fluctuating income can create uncertainty when "
            "exploring PMAY-U 2.0 options.\n\n"

            "Many applicants have non-fixed income patterns and want to understand "
            "how those situations are evaluated."
        ),

    "arhsalary_rentproof":
        (
            "Rental proof and income concerns often appear together for ARH applicants.\n\n"

            "Applicants may be unsure which records best reflect their "
            "current rental housing situation."
        ),

    "arhsalary_eligibility":
        (
            "Eligibility questions are common when income is not consistent.\n\n"

            "Applicants often want to understand whether fluctuating income "
            "affects their ability to explore PMAY-U 2.0 support."
        ),

    # =====================================
    # BENEFICIARY FAMILY
    # =====================================

    "arhfamily_parents":
        (
            "Parents are a common source of beneficiary-family confusion.\n\n"

            "Applicants often seek clarification on how household structure "
            "and family relationships are interpreted."
        ),

    "arhfamily_spouse":
        (
            "Spouse-related beneficiary-family questions are among the most "
            "frequently discussed PMAY-U 2.0 topics.\n\n"

            "Housing, ownership and family arrangements often create uncertainty."
        ),

    "arhfamily_separate":
        (
            "Separate living arrangements can sometimes make beneficiary-family "
            "definitions feel unclear.\n\n"

            "Many applicants have living situations that require additional clarification."
        ),

    # =====================================
    # ARH RULES
    # =====================================

    "arhheadpain_rent":
        (
            "Rental housing rules are often the first area of confusion "
            "for people exploring ARH.\n\n"

            "Applicants commonly compare rental support with ownership-oriented housing options."
        ),

    "arhheadpain_family":
        (
            "Family-related situations can make ARH rules feel more complicated.\n\n"

            "Household structure and housing arrangements are common discussion points."
        ),

    "arhheadpain_ownership":
        (
            "Ownership-related concerns sometimes create confusion even when "
            "the primary focus is rental housing.\n\n"

            "Applicants often wonder how existing family housing situations "
            "may affect understanding of ARH."
        ),

    # =====================================
    # ARH PROCESS
    # =====================================

    "arhprocess_delay":
        (
            "Long processing timelines can feel exhausting for applicants.\n\n"

            "PMAY-U 2.0 applications may move through verification, review "
            "and approval-related stages before final outcomes become visible."
        ),

    "arhprocess_tracking":
        (
            "Tracking an application can feel frustrating when updates are "
            "unclear or infrequent.\n\n"

            "Many applicants spend significant time trying to understand their current stage."
        ),

    "arhprocess_approval":
        (
            "Approval-related uncertainty is a common source of stress.\n\n"

            "Applicants often want to know whether their application is progressing normally."
        ),

    # =====================================
    # ARH STATUS
    # =====================================

    "arhstatus_meaning":
        (
            "Many applicants see status messages without fully understanding "
            "what they represent.\n\n"

            "Status terms may refer to verification, review, approval or "
            "other PMAY-U 2.0 workflow activities."
        ),

    "arhstatus_stage":
        (
            "Understanding the current stage is often more useful than "
            "focusing only on the status label.\n\n"

            "Different stages may indicate different processing activities."
        ),

    "arhstatus_next":
        (
            "Applicants frequently want to know what happens after the current stage.\n\n"

            "The next step generally depends on the application's progress "
            "within the PMAY-U 2.0 workflow."
        ),

    # =====================================
    # ARH FOR ME?
    # =====================================

    "arhforme_rent":
        (
            "ARH under PMAY-U 2.0 is primarily focused on affordable rental housing.\n\n"

            "Applicants often start by understanding whether their current "
            "rental situation matches the purpose of the scheme.\n\n"

            "Rental housing needs are usually the first factor explored."
        ),

    "arhforme_worker":
        (
            "Many ARH applicants are unsure whether their work or living "
            "situation aligns with the scheme's intended purpose.\n\n"

            "Understanding your current living and employment circumstances "
            "can help reduce confusion."
        ),

    "arhforme_family":
        (
            "Family housing arrangements can sometimes make it difficult "
            "to understand whether ARH is suitable.\n\n"

            "Applicants often compare their housing situation with other PMAY-U 2.0 options."
        ),

    # =====================================
    # ARH STRESS
    # =====================================

    "arhstress_rent":
        (
            "Rental housing concerns can become stressful when housing "
            "stability feels uncertain.\n\n"

            "Many applicants explore ARH because they are looking for "
            "more affordable or stable rental arrangements."
        ),

    "arhstress_delay":
        (
            "Delays and uncertainty can make the PMAY-U 2.0 process feel exhausting.\n\n"

            "Applications may remain under review or verification before "
            "further progress becomes visible."
        ),

    "arhstress_eligibility":
        (
            "Eligibility confusion is one of the most common reasons "
            "applicants feel overwhelmed.\n\n"

            "Many users worry they may have misunderstood important requirements."
        ),

    # =====================================
    # FAMILY SAYS YES
    # =====================================

    "arhmindno_rent":
        (
            "Many applicants question whether their rental situation truly "
            "fits the purpose of ARH.\n\n"

            "Rental housing needs are often the starting point for understanding suitability."
        ),

    "arhmindno_family":
        (
            "Family opinions can sometimes create additional uncertainty.\n\n"

            "Housing arrangements and family circumstances may lead to different interpretations."
        ),

    "arhmindno_ownership":
        (
            "Ownership-related concerns frequently create doubt even when "
            "others believe ARH may be suitable.\n\n"

            "Applicants often want clarification about how housing ownership "
            "interacts with rental-focused schemes."
        ),

    # =====================================
    # IS ARH RIGHT?
    # =====================================

    "arhright_rent":
        (
            "Rental housing needs are usually the most important factor "
            "when exploring ARH under PMAY-U 2.0.\n\n"

            "Understanding your current rental situation often helps identify the next step."
        ),

    "arhright_worker":
        (
            "Work and living conditions are common topics when applicants "
            "try to understand whether ARH fits their circumstances.\n\n"

            "Many people start by evaluating their current housing reality."
        ),

    "arhright_housing":
        (
            "Housing need is often the key factor when comparing ARH "
            "with other PMAY-U 2.0 components.\n\n"

            "Clarifying the type of housing support needed can simplify the decision."
        ),

    # =====================================
    # ISS ELIGIBILITY
    # =====================================

    "isseligible_loan":
        (
            "ISS under PMAY-U 2.0 is generally associated with housing loan-related support.\n\n"

            "Applicants often begin by understanding how their housing loan situation "
            "fits within the scheme framework."
        ),

    "isseligible_house":
        (
            "House ownership questions are among the most common concerns "
            "for people exploring ISS.\n\n"

            "Applicants often want to understand how ownership conditions "
            "relate to loan-related support."
        ),

    "isseligible_family":
        (
            "Family-owned or inherited property situations may create uncertainty "
            "when evaluating ISS suitability.\n\n"

            "Many applicants seek clarification on property-related conditions."
        ),

    # =====================================
    # ISS CONFUSION
    # =====================================

    "issconfused_loan":
        (
            "Loan-related terminology can feel overwhelming when exploring ISS.\n\n"

            "Many applicants want to understand how housing loans, repayment "
            "and subsidy-related concepts connect together."
        ),

    "issconfused_ownership":
        (
            "Ownership-related questions frequently create confusion when "
            "people are evaluating ISS under PMAY-U 2.0.\n\n"

            "Property ownership is a common topic during eligibility discussions."
        ),

    "issconfused_eligibility":
        (
            "Eligibility concerns are common because ISS involves both "
            "housing and loan-related considerations.\n\n"

            "Applicants often seek clarity before deciding whether to proceed."
        ),

    # =====================================
    # ISS DOCUMENTS
    # =====================================

    "isspaper_loan":
        (
            "Loan-related documents are among the most common concerns "
            "for applicants exploring ISS.\n\n"

            "Applicants often want clarity about housing loan records, "
            "loan verification and supporting documentation."
        ),

    "isspaper_aadhaar":
        (
            "Aadhaar-related concerns can arise when applicants are unsure "
            "whether all records contain matching information.\n\n"

            "Identity verification remains an important part of the PMAY-U 2.0 process."
        ),

    "isspaper_bank":
        (
            "Bank-related documents often become important when discussing "
            "loan and subsidy-related processes.\n\n"

            "Applicants commonly seek clarification about account details, "
            "verification and related records."
        ),

    # =====================================
    # BANK PROCESS FEAR
    # =====================================

    "issbank_verify":
        (
            "Loan verification can feel intimidating, especially when applicants "
            "are unsure what information is being reviewed.\n\n"

            "Under PMAY-U 2.0 ISS, verification may involve checking loan-related, "
            "identity and eligibility information before further processing.\n\n"

            "Many applicants experience similar concerns during this stage."
        ),

    "issbank_subsidy":
        (
            "Subsidy timing is one of the most common concerns among ISS applicants.\n\n"

            "Applicants often worry when subsidy-related updates are delayed "
            "or difficult to understand.\n\n"

            "Delay alone does not necessarily indicate a problem."
        ),

    "issbank_documents":
        (
            "Document-related concerns are common during loan and subsidy processes.\n\n"

            "Applicants often worry about missing documents, mismatches "
            "or whether additional verification may be required."
        ),

    # =====================================
    # FAMILY INCOME
    # =====================================

    "issincome_spouse":
        (
            "Spouse income is one of the most frequently discussed topics "
            "when applicants try to understand ISS eligibility.\n\n"

            "Many people are unsure how spouse-related financial information "
            "fits into the overall assessment process."
        ),

    "issincome_parents":
        (
            "Questions involving parents and family income can sometimes "
            "create confusion.\n\n"

            "Applicants often seek clarity about how household relationships "
            "may affect understanding of eligibility."
        ),

    "issincome_joint":
        (
            "Joint household income situations can feel difficult to interpret.\n\n"

            "Many applicants want to understand how multiple earning members "
            "fit into the overall assessment."
        ),

    # =====================================
    # BENEFICIARY FAMILY
    # =====================================

    "issfamily_parents":
        (
            "Parents are a common source of beneficiary-family confusion "
            "under PMAY-U 2.0.\n\n"

            "Applicants frequently seek clarification about family structure "
            "and related eligibility concepts."
        ),

    "issfamily_spouse":
        (
            "Spouse-related questions are among the most common family concerns "
            "raised by ISS applicants.\n\n"

            "Housing ownership, income and family arrangements often create uncertainty."
        ),

    "issfamily_separate":
        (
            "Separate living arrangements can sometimes make beneficiary-family "
            "definitions feel unclear.\n\n"

            "Many applicants have situations that require additional clarification."
        ),

    # =====================================
    # ISS RULES
    # =====================================

    "issrules_loan":
        (
            "Loan-related rules can feel complicated when applicants are "
            "trying to understand how housing finance and subsidy support connect.\n\n"

            "Many users begin by understanding the basic loan-related requirements."
        ),

    "issrules_ownership":
        (
            "Ownership-related concerns are among the most common sources "
            "of confusion for ISS applicants.\n\n"

            "Questions about existing property, family ownership and housing "
            "situations frequently arise."
        ),

    "issrules_family":
        (
            "Family-related situations can make eligibility discussions feel more complex.\n\n"

            "Beneficiary-family conditions are a common area of uncertainty."
        ),

    # =====================================
    # ISS PROCESS
    # =====================================

    "issprocess_subsidy":
        (
            "Subsidy-related stages often create confusion because applicants "
            "may not know when or how updates will appear.\n\n"

            "Understanding subsidy-related workflow is a common concern."
        ),

    "issprocess_bank":
        (
            "Bank-related procedures can feel overwhelming, especially when "
            "multiple verification or loan-related steps are involved.\n\n"

            "Many applicants seek clarification on how the process works."
        ),

    "issprocess_status":
        (
            "Status confusion is one of the most common frustrations "
            "during PMAY-U 2.0 processing.\n\n"

            "Applicants often want to understand whether their application "
            "is progressing normally."
        ),

    # =====================================
    # WIFE SAYS APPLY
    # =====================================

    "isswife_loan":
        (
            "Different family members may have different opinions about "
            "whether ISS is suitable.\n\n"

            "Loan-related housing needs are often the starting point when "
            "exploring ISS under PMAY-U 2.0."
        ),

    "isswife_ownership":
        (
            "Ownership-related concerns frequently influence whether applicants "
            "believe ISS may fit their situation.\n\n"

            "Property-related questions are very common during eligibility discussions."
        ),

    "isswife_subsidy":
        (
            "Many applicants focus on subsidy support but remain unsure "
            "whether they fit the intended purpose of ISS.\n\n"

            "Understanding the housing and loan situation is often the first step."
        ),

    # =====================================
    # ISS STRESS
    # =====================================

    "issstress_loan":
        (
            "Housing loan concerns can become stressful when applicants are "
            "trying to understand multiple rules and requirements.\n\n"

            "Many ISS applicants experience similar uncertainty."
        ),

    "issstress_subsidy":
        (
            "Subsidy-related uncertainty is one of the most common reasons "
            "people feel overwhelmed during the PMAY-U 2.0 process.\n\n"

            "Applicants often worry about timing, eligibility and progress."
        ),

    "issstress_rejection":
        (
            "Rejection-related fear is understandable when requirements "
            "seem difficult to interpret.\n\n"

            "Many applicants worry they may have misunderstood an important rule "
            "even when their application is still progressing."
        ),

    # =====================================
    # ISS FOR ME
    # =====================================

    "issforme_loan":
        (
            "ISS under PMAY-U 2.0 is generally associated with housing "
            "loan-related support.\n\n"

            "Applicants often begin by understanding whether they already "
            "have a housing loan or plan to obtain one.\n\n"

            "Loan-related housing needs are usually the first factor considered."
        ),

    "issforme_income":
        (
            "Income-related concerns are common when evaluating ISS.\n\n"

            "Income category may influence which PMAY-U 2.0 support options "
            "are most relevant to an applicant's situation."
        ),

    "issforme_ownership":
        (
            "House ownership questions are among the most common concerns "
            "for applicants considering ISS.\n\n"

            "Many users want to understand how existing property situations "
            "relate to loan-related housing support."
        ),

    # =====================================
    # EVERYTHING CONFUSING IN ISS
    # =====================================

    "isseverything_loan":
        (
            "Loan-related terminology can feel overwhelming when exploring ISS.\n\n"

            "Many applicants first focus on understanding the housing loan "
            "portion before looking at subsidy-related details."
        ),

    "isseverything_subsidy":
        (
            "Subsidy-related information can feel confusing because applicants "
            "often want to know when, how and under what conditions support is processed.\n\n"

            "This is one of the most common ISS questions."
        ),

    "isseverything_bank":
        (
            "Bank-related procedures can appear complicated due to multiple "
            "verification and documentation stages.\n\n"

            "Many applicants seek clarification about how the process works."
        ),

    "isseverything_eligibility":
        (
            "Eligibility concerns are common because ISS combines housing, "
            "income and loan-related considerations.\n\n"

            "Applicants often want clarity before deciding whether to proceed."
        ),

    # =====================================
    # UNIVERSAL PMAY INCOME
    # =====================================

    "pmayincome_category":
        (
            "Income categories under PMAY-U 2.0 can feel confusing when applicants "
            "are unsure where they fit.\n\n"

            "Understanding the correct income category is often the first step "
            "before exploring scheme eligibility."
        ),

    "pmayincome_proof":
        (
            "Income proof questions are common, especially when income sources "
            "are informal, seasonal or not supported by standard salary documents.\n\n"

            "Many applicants seek clarification about acceptable income records."
        ),

    "pmayincome_family":
        (
            "Family income calculations can create confusion when multiple "
            "earning members live in the same household.\n\n"

            "Applicants often want to understand how household income is viewed."
        ),

    # =====================================
    # BLC INCOME
    # =====================================

    "blcincome_category":
        (
            "Income category confusion is common among BLC applicants.\n\n"

            "Many people are unsure how income categories relate to construction-related support."
        ),

    "blcincome_proof":
        (
            "Income proof requirements can feel difficult when applicants "
            "do not have traditional salary documentation.\n\n"

            "Many BLC applicants have similar concerns."
        ),

    "blcincome_self":
        (
            "Self-employed and irregular-income situations frequently create confusion.\n\n"

            "Applicants often want to understand how non-salaried income may be evaluated."
        ),

    # =====================================
    # AHP INCOME
    # =====================================

    "ahpincome_category":
        (
            "Income category questions are common when exploring AHP under PMAY-U 2.0.\n\n"

            "Applicants often want to understand where they fit before considering housing options."
        ),

    "ahpincome_proof":
        (
            "Income proof concerns are common among AHP applicants.\n\n"

            "Many users are unsure what documentation best reflects their situation."
        ),

    "ahpincome_family":
        (
            "Family income calculations can feel complicated when multiple "
            "household members contribute financially.\n\n"

            "This is a frequent source of confusion."
        ),

    # =====================================
    # ARH INCOME
    # =====================================

    "arhincome_category":
        (
            "Income category questions are common among ARH applicants.\n\n"

            "Many people want to understand how income relates to rental housing support."
        ),

    "arhincome_rentalsituation":
        (
            "Rental housing and income concerns often overlap.\n\n"

            "Applicants commonly try to understand how both factors fit together."
        ),

    "arhincome_family":
        (
            "Family income situations can sometimes make rental housing decisions "
            "feel more complicated.\n\n"

            "Applicants often seek clarity about household income considerations."
        ),

    # =====================================
    # ISS INCOME
    # =====================================

    "issincome_category":
        (
            "Income category confusion is common among ISS applicants.\n\n"

            "Many people want to understand where they fit before evaluating loan-related support."
        ),

    "issincome_loan":
        (
            "Loan-related eligibility and income questions often appear together.\n\n"

            "Applicants commonly want to understand how income and housing loans interact."
        ),

    "issincome_family":
        (
            "Family income calculations can create uncertainty when multiple "
            "earning members are involved.\n\n"

            "This is one of the most common ISS-related questions."
        ),

    # =====================================
    # WOMAN ELIGIBILITY
    # =====================================

    "woman_income":
        (
            "Many women exploring PMAY-U 2.0 are unsure whether their income "
            "situation affects eligibility.\n\n"

            "Income is generally considered together with housing ownership "
            "and beneficiary-family conditions.\n\n"

            "Understanding the income-related concern is often a good starting point."
        ),

    "woman_ownership":
        (
            "Ownership-related questions are among the most common concerns "
            "for women applicants under PMAY-U 2.0.\n\n"

            "Family property, inherited property and housing ownership situations "
            "often create uncertainty."
        ),

    "woman_family":
        (
            "Family-related eligibility questions are common because household "
            "situations can vary significantly.\n\n"

            "Applicants often seek clarity about family structure and beneficiary-family conditions."
        ),

    # =====================================
    # WOMAN DOCUMENTS
    # =====================================

    "womanpaper_identity":
        (
            "Identity-related documents are a common source of confusion "
            "during PMAY-U 2.0 applications.\n\n"

            "Applicants often worry about mismatches, missing records "
            "or document consistency."
        ),

    "womanpaper_family":
        (
            "Family-related documents can sometimes feel difficult to understand.\n\n"

            "Applicants often seek clarity regarding household and family-linked records."
        ),

    "womanpaper_income":
        (
            "Income-related proof can be confusing, especially when income "
            "sources are informal or difficult to document.\n\n"

            "Many PMAY-U 2.0 applicants have similar concerns."
        ),

    # =====================================
    # VERIFICATION FEAR
    # =====================================

    "womanverify_documents":
        (
            "Document verification can feel stressful when applicants are unsure "
            "whether everything has been submitted correctly.\n\n"

            "Identity, income and supporting records may be reviewed during processing."
        ),

    "womanverify_officer":
        (
            "Many applicants become nervous when they hear about verification checks.\n\n"

            "These checks are generally intended to confirm beneficiary and application details."
        ),

    "womanverify_delay":
        (
            "Verification delays can understandably create anxiety.\n\n"

            "However, delays alone do not automatically indicate rejection "
            "under PMAY-U 2.0."
        ),

    # =====================================
    # WOMAN INCOME
    # =====================================

    "womanincome_category":
        (
            "Income category confusion is common among PMAY-U 2.0 applicants.\n\n"

            "Many people are unsure where they fit and how income categories "
            "relate to housing support."
        ),

    "womanincome_proof":
        (
            "Income proof concerns are common, especially when applicants "
            "do not have traditional salary documentation.\n\n"

            "Many users seek clarification on acceptable supporting records."
        ),

    "womanincome_family":
        (
            "Family income calculations can feel complicated when multiple "
            "household members contribute financially.\n\n"

            "This is one of the most common income-related questions."
        ),

    # =====================================
    # WIDOW RULES
    # =====================================

    "widowrules_ownership":
        (
            "Ownership-related concerns are common among widow applicants "
            "exploring PMAY-U 2.0.\n\n"

            "Questions involving inherited property, family ownership and "
            "housing rights often arise."
        ),

    "widowrules_family":
        (
            "Family-related rules can sometimes feel difficult to interpret.\n\n"

            "Dependency, household structure and beneficiary-family situations "
            "are common areas of confusion."
        ),

    "widowrules_category":
        (
            "Many applicants want to understand how special or vulnerable-category "
            "considerations may apply under PMAY-U 2.0.\n\n"

            "This is a common area where applicants seek additional clarification."
        ),

    # =====================================
    # WIDOW PROCESS
    # =====================================

    "widowprocess_delay":
        (
            "Long processing timelines can feel exhausting and uncertain.\n\n"

            "Applications may spend time in verification and review stages "
            "before visible progress appears."
        ),

    "widowprocess_verification":
        (
            "Verification stages can sometimes feel confusing because applicants "
            "may not know exactly what information is being reviewed.\n\n"

            "Verification generally helps confirm application details."
        ),

    "widowprocess_approval":
        (
            "Approval-related uncertainty is a common source of stress.\n\n"

            "Applicants often want to know whether their application is progressing normally."
        ),

    # =====================================
    # SENIOR CITIZEN STATUS
    # =====================================

    "seniorstatus_meaning":
        (
            "Many senior citizens see a status update but are unsure "
            "what the wording actually means.\n\n"

            "Status terms often refer to verification, review or approval-related stages."
        ),

    "seniorstatus_stage":
        (
            "Understanding the current stage is often more useful than "
            "focusing only on the status name.\n\n"

            "Different stages may indicate different processing activities."
        ),

    "seniorstatus_next":
        (
            "Applicants frequently want to know what happens after the current stage.\n\n"

            "The next step generally depends on the application's progress "
            "within the PMAY-U 2.0 workflow."
        ),

    # =====================================
    # OFFICER CHECK FEAR
    # =====================================

    "officercheck_documents":
        (
            "Many PMAY-U 2.0 applicants become anxious about whether their "
            "documents are complete, correct and consistent.\n\n"

            "Document review is a normal part of verification and does not "
            "automatically indicate a problem with the application."
        ),

    "officercheck_verification":
        (
            "Verification checks can feel intimidating when applicants are "
            "unsure what information is being reviewed.\n\n"

            "In most cases, verification is intended to confirm identity, "
            "housing and application-related details."
        ),

    "officercheck_approval":
        (
            "Many applicants worry that officer review may delay approval.\n\n"

            "However, review and approval are separate parts of the PMAY-U 2.0 process, "
            "and additional verification does not automatically mean rejection."
        ),

    # =====================================
    # LIFE CONFUSION
    # =====================================

    "lifedifficult_income":
        (
            "Financial pressure can make PMAY-U 2.0 eligibility feel difficult to understand.\n\n"

            "Many applicants start by identifying whether income-related concerns "
            "are creating the biggest obstacle."
        ),

    "lifedifficult_housing":
        (
            "Housing instability can make it difficult to determine which PMAY-U 2.0 "
            "component may be most relevant.\n\n"

            "Understanding the housing situation is often the first step."
        ),

    "lifedifficult_family":
        (
            "Family-related housing and ownership situations can sometimes make "
            "eligibility feel more complicated than expected.\n\n"

            "Many applicants experience similar confusion."
        ),

    # =====================================
    # MENTAL STRESS
    # =====================================

    "mentalstress_documents":
        (
            "Document requirements can feel overwhelming when multiple records, "
            "proofs and verification stages are involved.\n\n"

            "Many PMAY-U 2.0 applicants identify paperwork as their biggest challenge."
        ),

    "mentalstress_income":
        (
            "Income-related uncertainty is one of the most common reasons "
            "applicants feel stressed during the PMAY-U 2.0 process.\n\n"

            "Questions about category, proof and family income are very common."
        ),

    "mentalstress_approval":
        (
            "Approval-related uncertainty can create significant stress, "
            "especially when updates are delayed or difficult to interpret.\n\n"

            "Many applicants experience similar concerns while waiting for progress."
        ),

    # =====================================
    # LOGIN STRESS
    # =====================================

    "loginstress_otp":
        (
            "OTP-related problems are among the most common portal issues.\n\n"

            "Applicants often report delayed OTP delivery, repeated OTP requests "
            "or verification difficulties during login."
        ),

    "loginstress_password":
        (
            "Password-related issues can become frustrating when access to the "
            "PMAY-U 2.0 portal is interrupted.\n\n"

            "Many applicants experience password recovery or login difficulties."
        ),

    "loginstress_account":
        (
            "Account-access issues can occur for several reasons, including "
            "verification mismatches or login-related problems.\n\n"

            "Understanding the exact access issue is often the best starting point."
        ),

    # =====================================
    # PORTAL NOT WORKING
    # =====================================

    "portalnotwork_login":
        (
            "Login failures can occur due to account verification issues, "
            "temporary portal problems or credential-related errors.\n\n"

            "Many applicants experience similar technical difficulties."
        ),

    "portalnotwork_otp":
        (
            "OTP-related issues are a frequent cause of login frustration.\n\n"

            "Applicants often report delays, invalid OTP messages or repeated requests."
        ),

    "portalnotwork_password":
        (
            "Password-related errors can prevent access even when application "
            "information is otherwise correct.\n\n"

            "Recovery and reset issues are common concerns."
        ),

    # =====================================
    # WEBSITE STRESS
    # =====================================

    "website_upload":
        (
            "Document upload issues are among the most common PMAY-U 2.0 portal complaints.\n\n"

            "Applicants may encounter file-size limits, unsupported formats "
            "or upload failures."
        ),

    "website_captcha":
        (
            "Captcha-related problems can be frustrating, especially when "
            "verification repeatedly fails.\n\n"

            "Many users experience similar issues while accessing portal services."
        ),

    "website_error":
        (
            "Website errors may occur because of technical issues, maintenance "
            "activities or temporary service disruptions.\n\n"

            "Portal errors do not necessarily affect application eligibility."
        ),

    # =====================================
    # PORTAL PROBLEM
    # =====================================

    "portalproblem_opening":
        (
            "Website access issues can occur due to browser problems, "
            "network conditions or temporary portal outages.\n\n"

            "Many users report occasional difficulties opening portal pages."
        ),

    "portalproblem_upload":
        (
            "Upload-related issues are among the most frequently reported "
            "technical concerns during PMAY-U 2.0 applications.\n\n"

            "Understanding the exact upload error often helps identify the cause."
        ),

    "portalproblem_captcha":
        (
            "Captcha failures can prevent applicants from progressing through "
            "portal steps even when other information is correct.\n\n"

            "This is a common technical issue reported by users."
        ),

    # =====================================
    # PORTAL CONFUSION
    # =====================================

    "portalconfusing_tracking":
        (
            "Tracking-related confusion is one of the most common PMAY-U 2.0 concerns.\n\n"

            "Applicants often see limited updates and become unsure whether "
            "their application is progressing normally.\n\n"

            "Understanding the current tracking stage is usually the first step."
        ),

    "portalconfusing_details":
        (
            "Incorrect or inconsistent details shown on the portal can feel worrying.\n\n"

            "Applicants often become concerned when personal information, "
            "documents or application records appear different than expected."
        ),

    "portalconfusing_missing":
        (
            "Missing application information can create significant uncertainty.\n\n"

            "Many applicants worry that their application was not submitted "
            "properly or is not being reflected correctly on the portal."
        ),

    # =====================================
    # PORTAL HEADACHE
    # =====================================

    "portalheadache_login":
        (
            "Login-related issues are among the most common reasons applicants "
            "struggle with the PMAY-U 2.0 portal.\n\n"

            "OTP, password and account-access difficulties can make tracking difficult."
        ),

    "portalheadache_status":
        (
            "Status-related confusion often causes applicants to repeatedly "
            "check the portal without understanding what changed.\n\n"

            "Many users experience similar frustration."
        ),

    "portalheadache_technical":
        (
            "Technical portal issues can make the application process feel much harder.\n\n"

            "Website errors, loading failures and system issues are common concerns."
        ),

    # =====================================
    # PORTAL STRESS
    # =====================================

    "portalstress_login":
        (
            "Repeated login difficulties can become mentally exhausting.\n\n"

            "Many applicants report frustration when access problems prevent them "
            "from checking updates."
        ),

    "portalstress_tracking":
        (
            "Tracking uncertainty is a common source of stress.\n\n"

            "Applicants often feel stuck when the portal does not clearly explain progress."
        ),

    "portalstress_technical":
        (
            "Technical failures can create the impression that something is wrong "
            "with the application even when the issue is portal-related.\n\n"

            "Many users experience similar concerns."
        ),

    # =====================================
    # STATUS CONFUSION
    # =====================================

    "statusconfusion_meaning":
        (
            "Many applicants see a status but are unsure what the wording actually means.\n\n"

            "Status labels often correspond to verification, review, approval "
            "or workflow-related stages under PMAY-U 2.0."
        ),

    "statusconfusion_stage":
        (
            "Understanding the current stage is often more useful than focusing "
            "only on the status text.\n\n"

            "Different stages may indicate different processing activities."
        ),

    "statusconfusion_next":
        (
            "Applicants frequently want to know what happens after the current stage.\n\n"

            "The next step generally depends on the application's progress "
            "within the PMAY-U 2.0 workflow."
        ),

    # =====================================
    # BRAIN TIRED CHECKING
    # =====================================

    "checkingtired_delay":
        (
            "Long waiting periods can make applicants feel stuck and exhausted.\n\n"

            "Delays do not automatically indicate rejection and may simply reflect "
            "ongoing review or verification."
        ),

    "checkingtired_wording":
        (
            "Status wording can sometimes feel unclear or overly technical.\n\n"

            "Many applicants struggle to understand what a particular portal message means."
        ),

    "checkingtired_tracking":
        (
            "Repeatedly checking application progress without clear updates "
            "can become frustrating.\n\n"

            "Tracking confusion is one of the most common PMAY-U 2.0 concerns."
        ),

    # =====================================
    # TRACKING STRESS
    # =====================================

    "trackingstress_missing":
        (
            "Missing status updates can create uncertainty about whether "
            "the application is progressing normally.\n\n"

            "Many applicants experience concern when updates appear incomplete."
        ),

    "trackingstress_issue":
        (
            "Tracking-related issues can make it difficult to understand "
            "the actual progress of an application.\n\n"

            "Clarifying the exact issue is often the best starting point."
        ),

    "trackingstress_delay":
        (
            "Waiting for updates can feel stressful when timelines are unclear.\n\n"

            "Many PMAY-U 2.0 applicants experience similar concerns while "
            "monitoring application progress."
        ),

    # =====================================
    # STATUS UNDERSTANDING
    # =====================================

    "statusunderstand_meaning":
        (
            "Many PMAY-U 2.0 applicants see a status update but are unsure "
            "what the wording actually means.\n\n"

            "Status labels often correspond to verification, review, approval "
            "or other workflow-related stages within the application process.\n\n"

            "Understanding the meaning of the status is often the first step before deciding what to do next."
        ),

    "statusunderstand_stage":
        (
            "Applicants are often more concerned about where their application "
            "currently stands than the exact wording shown on the portal.\n\n"

            "Different stages may indicate verification, review, approval "
            "or other processing activities."
        ),

    "statusunderstand_next":
        (
            "Many users want to know what happens after the current stage.\n\n"

            "The next step usually depends on the application's progress "
            "within the PMAY-U 2.0 workflow and any pending reviews."
        ),

    # =====================================
    # BRAIN TIRED
    # =====================================

    "braintired_delay":
        (
            "Long waiting periods can become mentally exhausting.\n\n"

            "Many PMAY-U 2.0 applicants feel frustrated when updates are delayed "
            "and progress is difficult to track."
        ),

    "braintired_rejection":
        (
            "Rejection-related worry is common when applications remain unchanged "
            "for a long time.\n\n"

            "Many applicants fear the worst even when no rejection decision has been communicated."
        ),

    "braintired_status":
        (
            "Repeatedly checking unclear status updates can become frustrating.\n\n"

            "Status confusion is one of the most common concerns among applicants."
        ),

    # =====================================
    # NO UPDATE
    # =====================================

    "noupdate_delay":
        (
            "Delays are one of the most common reasons applicants feel stuck.\n\n"

            "Long processing timelines do not automatically indicate a problem "
            "with the application."
        ),

    "noupdate_response":
        (
            "Many applicants become frustrated when they feel there has been "
            "little or no response regarding their application.\n\n"

            "Lack of visible communication can create uncertainty about progress."
        ),

    "noupdate_status":
        (
            "Sometimes the biggest challenge is not the delay itself "
            "but understanding what the current status actually means.\n\n"

            "Many applicants experience similar confusion."
        ),

    # =====================================
    # COMPLAINT PROCESS
    # =====================================

    "complaint_delay":
        (
            "Applicants often consider complaint-related options after "
            "experiencing long delays.\n\n"

            "Understanding the cause of the delay is usually the first step."
        ),

    "complaint_officer":
        (
            "Some applicants become concerned about interactions with "
            "officials or verification-related processes.\n\n"

            "Clarifying the specific concern often helps determine the next action."
        ),

    "complaint_noupdate":
        (
            "No-update situations are a common reason applicants seek help.\n\n"

            "Many users want to understand whether the lack of updates is normal or requires follow-up."
        ),

    # =====================================
    # ANGRY ABOUT DELAY
    # =====================================

    "angrydelay_status":
        (
            "Long delays combined with unclear status updates can feel extremely frustrating.\n\n"

            "Many PMAY-U 2.0 applicants struggle when progress is difficult to understand."
        ),

    "angrydelay_officer":
        (
            "Applicants sometimes associate delays with verification or officer-related processes.\n\n"

            "Understanding where the application currently stands is often important."
        ),

    "angrydelay_updates":
        (
            "Lack of updates over a long period can create significant frustration.\n\n"

            "Many applicants simply want clarity about whether progress is still occurring."
        ),

    # =====================================
    # ANGRY OFFICER
    # =====================================

    "angryofficer_delay":
        (
            "Delays combined with communication difficulties can make the process feel overwhelming.\n\n"

            "Many applicants experience similar frustration when progress appears slow."
        ),

    "angryofficer_rejection":
        (
            "Applicants sometimes worry that repeated issues may eventually lead to rejection.\n\n"

            "This concern is common when communication and updates are unclear."
        ),

    "angryofficer_communication":
        (
            "Communication-related concerns are one of the most common sources "
            "of frustration during PMAY-U 2.0 processing.\n\n"

            "Many applicants simply want clearer information about their application's progress."
        ),

    # =====================================
    # OFFICE FATIGUE
    # =====================================

    "officefatigue_delay":
        (
            "Repeated office visits without clear progress can feel exhausting.\n\n"
            "Many PMAY-U 2.0 applicants experience frustration when applications "
            "remain in processing stages for longer than expected.\n\n"
            "Long delays alone do not automatically indicate rejection."
        ),

    "officefatigue_approval":
        (
            "Approval-related uncertainty is one of the most common reasons "
            "applicants repeatedly visit offices seeking clarification.\n\n"
            "Many users simply want confirmation that their application is progressing."
        ),

    "officefatigue_noupdate":
        (
            "Lack of updates can be more frustrating than the waiting itself.\n\n"
            "Many PMAY-U 2.0 applicants feel uncertain when no visible progress appears."
        ),

    # =====================================
    # NO SUBSIDY
    # =====================================

    "nosubsidy_delay":
        (
            "Subsidy-related delays are among the most common concerns raised by applicants.\n\n"
            "Processing, verification and workflow stages may sometimes take time "
            "before financial updates become visible."
        ),

    "nosubsidy_approval":
        (
            "Many applicants wonder whether subsidy release depends on approval-related stages.\n\n"
            "Understanding the application's current progress often helps reduce confusion."
        ),

    "nosubsidy_issue":
        (
            "When subsidy updates are unclear, applicants often worry that something went wrong.\n\n"
            "Many users seek clarification regarding subsidy-related workflow and status."
        ),

    # =====================================
    # HELPLESS
    # =====================================

    "helpless_status":
        (
            "Feeling stuck because of unclear status updates is very common.\n\n"
            "Many applicants simply want to understand where their application currently stands."
        ),

    "helpless_complaint":
        (
            "Applicants sometimes consider complaint-related options when progress feels unclear.\n\n"
            "Understanding the exact issue is usually the first step before escalation."
        ),

    "helpless_approval":
        (
            "Approval uncertainty can leave applicants feeling powerless and confused.\n\n"
            "Many PMAY-U 2.0 users experience similar concerns while waiting."
        ),

    # =====================================
    # CRYING DELAY
    # =====================================

    "crying_delay":
        (
            "Extended delays can create significant emotional stress.\n\n"
            "Many applicants become discouraged when expected progress does not appear."
        ),

    "crying_complaint":
        (
            "When delays continue for a long period, applicants often start exploring complaint options.\n\n"
            "Understanding the underlying issue is usually important before proceeding."
        ),

    "crying_noupdate":
        (
            "A complete lack of updates can feel overwhelming.\n\n"
            "Many PMAY-U 2.0 applicants experience uncertainty when no visible changes appear."
        ),

    # =====================================
    # SUBSIDY CONFUSION
    # =====================================

    "subsidyconfused_amount":
        (
            "Many applicants are unsure how subsidy-related amounts are determined.\n\n"
            "Questions about financial support calculations are very common."
        ),

    "subsidyconfused_delay":
        (
            "Subsidy delays are one of the most frequently reported concerns.\n\n"
            "Applicants often want to understand why financial updates take time."
        ),

    "subsidyconfused_nomoney":
        (
            "Some applicants see progress in their application but remain concerned "
            "because no financial benefit appears to have been received.\n\n"
            "This is a common source of confusion."
        ),

    # =====================================
    # SUBSIDY STATUS
    # =====================================

    "subsidystatus_meaning":
        (
            "Subsidy-related status messages can sometimes feel unclear or technical.\n\n"
            "Applicants often seek clarification regarding the meaning of specific status updates."
        ),

    "subsidystatus_stage":
        (
            "Understanding the current subsidy stage is often more useful than focusing "
            "only on the status wording.\n\n"
            "Different stages may indicate different processing activities."
        ),

    "subsidystatus_next":
        (
            "Many applicants want to know what happens after the current subsidy stage.\n\n"
            "The next step generally depends on the application's progress and review status."
        ),

    # =====================================
    # ANGRY SUBSIDY DELAY
    # =====================================

    "angrysubsidy_amount":
        (
            "Financial expectations and subsidy-related amounts can sometimes create frustration.\n\n"
            "Many applicants seek clarity about how support is processed."
        ),

    "angrysubsidy_delay":
        (
            "Long subsidy delays are one of the most emotionally frustrating PMAY-U 2.0 concerns.\n\n"
            "Many applicants worry when financial progress appears slow."
        ),

    "angrysubsidy_nomoney":
        (
            "Applicants often become concerned when they expect financial support "
            "but do not see any related update.\n\n"
            "This is a common subsidy-related concern."
        ),

    # =====================================
    # MONEY STRESS
    # =====================================

    "moneystress_loan":
        (
            "Housing loan obligations can create significant financial pressure.\n\n"

            "Many PMAY-U 2.0 applicants worry about repayment responsibilities, "
            "loan approval progress or overall housing affordability.\n\n"

            "Loan-related concerns are among the most common financial questions."
        ),

    "moneystress_emi":
        (
            "EMI-related pressure can feel overwhelming when housing costs "
            "are already affecting daily finances.\n\n"

            "Many applicants seek clarity about how housing support may relate "
            "to ongoing loan obligations."
        ),

    "moneystress_bank":
        (
            "Bank-related issues can create uncertainty when applicants are "
            "expecting financial updates or payment-related progress.\n\n"

            "Many PMAY-U 2.0 users experience similar concerns."
        ),

    # =====================================
    # DBT STATUS
    # =====================================

    "dbtstatus_meaning":
        (
            "DBT status messages can sometimes appear technical or unclear.\n\n"

            "Applicants often want to understand what a particular DBT-related "
            "status actually means within the PMAY-U 2.0 workflow."
        ),

    "dbtstatus_credit":
        (
            "Many applicants are mainly concerned about whether financial "
            "benefits have moved to the money-credit stage.\n\n"

            "Understanding the current stage often helps reduce confusion."
        ),

    "dbtstatus_next":
        (
            "Applicants frequently want to know what happens after the current DBT stage.\n\n"

            "The next step generally depends on verification, approval "
            "and payment-related workflow progress."
        ),

    # =====================================
    # DBT CONFUSION
    # =====================================

    "dbtconfused_credit":
        (
            "Many applicants are unsure whether money has been processed, "
            "approved or credited.\n\n"

            "This is one of the most common DBT-related concerns."
        ),

    "dbtconfused_aadhaar":
        (
            "Aadhaar-linking questions frequently arise when applicants are "
            "trying to understand DBT-related processes.\n\n"

            "Identity and account linkage concerns are very common."
        ),

    "dbtconfused_bank":
        (
            "Bank-related issues can affect how applicants interpret "
            "DBT-related updates and payment information.\n\n"

            "Many users seek clarification regarding account-related concerns."
        ),

    # =====================================
    # MONEY FATIGUE
    # =====================================

    "moneytired_subsidy":
        (
            "Subsidy-related uncertainty is one of the most common reasons "
            "applicants feel financially exhausted.\n\n"

            "Questions about timing, processing and financial updates are common."
        ),

    "moneytired_emi":
        (
            "EMI obligations can create ongoing stress while applicants wait "
            "for housing-related progress.\n\n"

            "Many users experience similar financial concerns."
        ),

    "moneytired_bank":
        (
            "Bank-related uncertainty can feel exhausting when financial updates "
            "are already difficult to understand.\n\n"

            "Many PMAY-U 2.0 applicants report similar frustration."
        ),

    # =====================================
    # MONEY CRYING
    # =====================================

    "moneycry_loan":
        (
            "Housing loan pressure can affect both financial planning "
            "and emotional well-being.\n\n"

            "Many applicants feel overwhelmed when housing costs and uncertainty combine."
        ),

    "moneycry_subsidy":
        (
            "Subsidy-related uncertainty is a common source of financial stress.\n\n"

            "Applicants often worry when expected financial support is delayed or unclear."
        ),

    "moneycry_bank":
        (
            "Bank-related concerns can become emotionally draining when "
            "financial progress is difficult to track.\n\n"

            "Many users experience similar worries."
        ),

    # =====================================
    # AADHAAR SAFETY
    # =====================================

    "aadhaarsafety_aadhaar":
        (
            "Concern about sharing Aadhaar information is understandable.\n\n"

            "Applicants should always be cautious when sharing identity-related information "
            "and ensure they are using trusted and official PMAY-U 2.0 channels."
        ),

    "aadhaarsafety_otp":
        (
            "OTP information should be handled carefully.\n\n"

            "Applicants should avoid sharing OTPs with unknown individuals "
            "or unverified sources."
        ),

    "aadhaarsafety_bank":
        (
            "Bank-related information is sensitive and should be protected carefully.\n\n"

            "Applicants should verify requests before sharing financial details."
        ),

    # =====================================
    # PERSONAL INFO PRIVACY
    # =====================================

    "privacy_aadhaar":
        (
            "Many applicants are concerned about how Aadhaar-related information is used.\n\n"

            "Identity-related privacy questions are common during housing applications."
        ),

    "privacy_mobile":
        (
            "Mobile-number privacy concerns can arise when applicants receive "
            "calls, messages or verification requests.\n\n"

            "Many users seek reassurance regarding information security."
        ),

    "privacy_bank":
        (
            "Banking information is sensitive and applicants often want to know "
            "how it is used during PMAY-U 2.0 processing.\n\n"

            "Bank-related privacy concerns are common and understandable."
        ),

    # =====================================
    # SCARED SCAM
    # =====================================

    "scam_call":
        (
            "Unexpected calls claiming PMAY-U 2.0 approval, subsidy release "
            "or urgent verification can make applicants uneasy.\n\n"

            "Many users become concerned when callers ask for personal, banking "
            "or identity-related information."
        ),

    "scam_money":
        (
            "Requests involving money, processing fees or guaranteed approval "
            "can raise understandable concerns.\n\n"

            "Applicants often want to confirm whether financial requests are legitimate."
        ),

    "scam_otp":
        (
            "OTP-related concerns should always be taken seriously.\n\n"

            "Many applicants worry when someone requests OTP information "
            "during PMAY-U 2.0 related communication."
        ),

    # =====================================
    # FEAR CHEATED
    # =====================================

    "cheated_money":
        (
            "Financial fraud concerns can create significant stress.\n\n"

            "Applicants often become worried after sharing information or "
            "receiving unexpected payment-related requests."
        ),

    "cheated_call":
        (
            "Unexpected calls claiming to represent housing-related authorities "
            "can feel suspicious.\n\n"

            "Many applicants seek clarification when communication appears unusual."
        ),

    "cheated_details":
        (
            "Concern about personal information is understandable.\n\n"

            "Applicants often worry whether identity-related details have been "
            "shared too broadly or with the wrong person."
        ),

    # =====================================
    # REAL OR FAKE
    # =====================================

    "realfake_call":
        (
            "It can be difficult to determine whether a phone call is genuine "
            "or misleading.\n\n"

            "Many applicants become cautious when callers discuss approvals, "
            "verification or financial matters."
        ),

    "realfake_message":
        (
            "Messages related to PMAY-U 2.0 can sometimes create uncertainty.\n\n"

            "Applicants often want to know whether a message is legitimate or misleading."
        ),

    "realfake_money":
        (
            "Money-related communication can feel suspicious when it is unexpected.\n\n"

            "Applicants often seek reassurance before taking any action."
        ),

    # =====================================
    # HACKED FEAR
    # =====================================

    "hacked_login":
        (
            "Login-related concerns are common when applicants believe "
            "someone may have accessed their account.\n\n"

            "Unexpected access issues can understandably create anxiety."
        ),

    "hacked_otp":
        (
            "OTP-related security concerns are among the most common fears "
            "reported by applicants.\n\n"

            "Many users become worried after receiving unusual verification requests."
        ),

    "hacked_account":
        (
            "Unexpected account changes can create significant concern.\n\n"

            "Applicants often want to understand whether information has been modified."
        ),

    # =====================================
    # ACCOUNT PANIC
    # =====================================

    "panicaccount_login":
        (
            "Login difficulties can feel alarming, especially when applicants "
            "fear something has changed unexpectedly.\n\n"

            "Many users experience similar concerns."
        ),

    "panicaccount_otp":
        (
            "Unexpected OTP activity can create understandable concern.\n\n"

            "Applicants often become worried when verification messages appear unexpectedly."
        ),

    "panicaccount_details":
        (
            "Changed account information can feel serious and confusing.\n\n"

            "Many applicants seek clarification when personal details appear different."
        ),

    # =====================================
    # MONEY PANIC
    # =====================================

    "panicmoney_money":
        (
            "Financial uncertainty can create significant emotional stress.\n\n"

            "Applicants often become concerned when expected financial outcomes "
            "do not match what they anticipated."
        ),

    "panicmoney_bank":
        (
            "Bank-related concerns are common when applicants are waiting "
            "for financial updates or payment-related activity.\n\n"

            "Many users experience similar worries."
        ),

    "panicmoney_subsidy":
        (
            "Subsidy-related uncertainty is one of the most common financial concerns "
            "raised by PMAY-U 2.0 applicants.\n\n"

            "Applicants often seek clarity about progress and financial status."
        ),

    # =====================================
    # MONEY FEAR
    # =====================================

    "moneyfear_money":
        (
            "Financial uncertainty can feel overwhelming, especially when you "
            "are unsure about payments, subsidy-related progress, or expected benefits.\n\n"

            "Many PMAY-U 2.0 applicants experience similar concerns while waiting "
            "for updates regarding financial matters."
        ),

    "moneyfear_bank":
        (
            "Bank-related concerns are common when applicants are expecting "
            "financial updates, DBT-related activity, or account-linked communication.\n\n"

            "Many users want reassurance that their banking information and "
            "application records are aligned correctly."
        ),

    "moneyfear_suspicious":
        (
            "Unexpected calls, messages, account activity or requests for "
            "personal information can understandably create concern.\n\n"

            "Many applicants become cautious when something appears unusual "
            "during the PMAY-U 2.0 process."
        ),

    # =====================================
    # HOUSE OWNERSHIP CONFUSION
    # =====================================

    "houseowner_family":
        (
            "Family ownership situations are one of the most common sources "
            "of PMAY-U 2.0 confusion.\n\n"

            "Applicants are often unsure how property owned by parents, spouse "
            "or other family members may relate to their housing situation."
        ),

    "houseowner_inheritance":
        (
            "Inherited property situations can feel difficult to interpret.\n\n"

            "Many applicants are uncertain about how inherited housing or property-related "
            "rights fit into their overall PMAY-U 2.0 circumstances."
        ),

    "houseowner_separation":
        (
            "Separation-related housing situations can create additional uncertainty "
            "regarding ownership and family arrangements.\n\n"

            "Many applicants seek clarification when housing and family circumstances overlap."
        ),

    # =====================================
    # FAMILY HOUSE STRESS
    # =====================================

    "familyhouse_father":
        (
            "Property associated with a father or parent is one of the most common "
            "ownership-related concerns raised by PMAY-U 2.0 applicants.\n\n"

            "Applicants often want to understand how family housing arrangements "
            "may affect their situation."
        ),

    "familyhouse_sibling":
        (
            "Property owned by a brother, sister or other sibling can sometimes "
            "create confusion about housing-related eligibility discussions.\n\n"

            "Many applicants seek clarity when family members own housing separately."
        ),

    "familyhouse_inheritance":
        (
            "Inherited property can create uncertainty when applicants are trying "
            "to understand their housing position under PMAY-U 2.0.\n\n"

            "Questions involving inheritance are among the most common family-property concerns."
        ),

    # =====================================
    # BANK
    # =====================================

    "bank_requirement":
        (
            "Bank account details are important for various PMAY-U 2.0 processes.\n\n"

            "Applicants are often unsure whether a bank account is mandatory, "
            "whose account should be used, or whether account details must match "
            "other application records."
        ),

    "bank_subsidy":
        (
            "Many applicants have questions about how subsidy-related payments "
            "or financial benefits are transferred.\n\n"

            "Bank account linkage and payment processing are common areas of confusion."
        ),

    "bank_mismatch":
        (
            "Bank account mismatches can occur when details differ across "
            "application records, identity documents or financial information.\n\n"

            "Many applicants seek clarification when account-related information "
            "does not appear consistent."
        ),

    "bank_inactive":
        (
            "Inactive or unused bank accounts can sometimes create uncertainty "
            "for applicants expecting financial updates.\n\n"

            "Many users want to understand whether account status may affect "
            "PMAY-U 2.0 related processes."
        ),

    # =====================================
    # FAMILY
    # =====================================

    "family_eligibility":
        (
            "Family eligibility is one of the most important parts of PMAY-U 2.0.\n\n"

            "Applicants often have questions about who is considered part of the "
            "beneficiary family and how family circumstances may affect eligibility."
        ),

    "family_separate":
        (
            "Separate family situations can sometimes be difficult to interpret.\n\n"

            "Applicants frequently ask about living separately, independent households "
            "or family arrangements under PMAY-U 2.0."
        ),

    "family_spouse":
        (
            "Spouse-related ownership and housing situations are among the most "
            "common family-related concerns.\n\n"

            "Applicants often want to understand how a spouse's housing or property "
            "status may relate to their situation."
        ),

    "family_inherited":
        (
            "Inherited property can create confusion regarding family housing "
            "and ownership discussions.\n\n"

            "Many applicants seek clarification when inheritance and housing "
            "circumstances overlap."
        ),

    # =====================================
    # INCOME
    # =====================================

    "income_eligibility":
        (
            "Income is an important factor in PMAY-U 2.0 eligibility assessment.\n\n"

            "Many applicants want to understand whether their household income "
            "falls within the applicable category or eligibility criteria."
        ),

    "income_proof":
        (
            "Income proof requirements can sometimes feel confusing.\n\n"

            "Applicants often have questions about salary documents, declarations "
            "or other income-related records."
        ),

    "income_category":
        (
            "Income categories can be difficult to understand when applicants "
            "are unsure where they fit.\n\n"

            "Category-related questions are among the most common PMAY-U 2.0 concerns."
        ),

    "income_change":
        (
            "Changes in employment, salary or household income can create uncertainty.\n\n"

            "Many applicants want to know how changing income situations may affect "
            "their PMAY-U 2.0 application."
        ),

    # =====================================
    # SUBSIDY / LOAN
    # =====================================

    "loan_iss":
        (
            "Many applicants are specifically interested in loan-related housing "
            "support under the Interest Subsidy Scheme (ISS).\n\n"

            "Questions about housing loans, subsidy benefits and financial assistance "
            "are very common."
        ),

    "loan_financial":
        (
            "General PMAY-U 2.0 financial assistance can sometimes be confused "
            "with loan-related subsidy programs.\n\n"

            "Applicants often seek clarity regarding the type of housing support "
            "that may be relevant to their situation."
        )

}
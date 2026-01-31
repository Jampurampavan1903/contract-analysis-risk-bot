def explain_clause(clause, risks):
    explanations = []

    if "Termination Risk" in risks:
        explanations.append(
            "This clause allows one or both parties to end the contract. You should check notice periods and whether termination is one-sided."
        )

    if "Penalty Risk" in risks:
        explanations.append(
            "This clause may require you to pay a penalty or damages if certain conditions are not met. This can increase financial risk."
        )

    if "Indemnity Risk" in risks:
        explanations.append(
            "This clause may require you to cover losses or legal costs for the other party. Indemnity clauses can create significant liability."
        )

    if "Confidentiality Risk" in risks:
        explanations.append(
            "This clause requires you to protect sensitive information. Breaching it may lead to legal or financial consequences."
        )

    if "Non-Compete Risk" in risks:
        explanations.append(
            "This clause may restrict your ability to work with competitors or start similar businesses after the contract ends."
        )

    if not explanations:
        explanations.append(
            "This clause appears to be low risk and does not impose major legal or financial obligations."
        )

    return explanations

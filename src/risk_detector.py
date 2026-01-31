def detect_risks(clauses):
    risk_results = []
    total_score = 0

    for clause in clauses:
        clause_lower = clause.lower()
        risks = []
        score = 0

        if "terminate" in clause_lower or "termination" in clause_lower:
            risks.append("Termination Risk")
            score += 3

        if "penalty" in clause_lower or "liquidated damages" in clause_lower:
            risks.append("Penalty Risk")
            score += 3

        if "indemnify" in clause_lower or "indemnity" in clause_lower:
            risks.append("Indemnity Risk")
            score += 4

        if "confidential" in clause_lower:
            risks.append("Confidentiality Risk")
            score += 2

        if "non-compete" in clause_lower or "non compete" in clause_lower:
            risks.append("Non-Compete Risk")
            score += 4

        if score == 0:
            risk_level = "Low"
        elif score <= 3:
            risk_level = "Medium"
        else:
            risk_level = "High"

        total_score += score

        risk_results.append({
            "clause": clause,
            "risks": risks if risks else ["Low Risk"],
            "risk_level": risk_level,
            "score": score
        })

    return risk_results, total_score

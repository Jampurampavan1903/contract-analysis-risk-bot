import re

def split_into_clauses(text):
    # Split on numbered clauses and headings
    raw_clauses = re.split(r'\n\s*\d+[\.\)]\s+|\n[A-Z][A-Z\s]{3,}\n', text)

    clauses = []
    for clause in raw_clauses:
        cleaned = clause.strip()
        if len(cleaned) > 50:
            clauses.append(cleaned)

    return clauses

import streamlit as st
from src.parser import extract_text
from src.clause_splitter import split_into_clauses
from src.risk_detector import detect_risks
from src.explainer import explain_clause

st.set_page_config(page_title="Contract Analysis & Risk Assessment Bot")

st.title("Contract Analysis & Risk Assessment Bot")
st.write("Upload a contract document (PDF, DOCX, or TXT)")

uploaded_file = st.file_uploader(
    "Choose a contract file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:
    text = extract_text(uploaded_file)

    if text.strip() == "":
        st.error("No text could be extracted from this file.")
    else:
        st.success("Text extracted successfully.")

        clauses = split_into_clauses(text)
        risk_analysis, total_score = detect_risks(clauses)

        st.subheader("Contract Risk Summary")
        st.metric("Overall Contract Risk Score", total_score)

        st.subheader("Clause-wise Risk Assessment & Explanation")

        for i, item in enumerate(risk_analysis, start=1):
            st.markdown(f"### Clause {i} — Risk Level: {item['risk_level']}")
            st.write(item["clause"])

            st.markdown("**Detected Risks:** " + ", ".join(item["risks"]))
            st.markdown(f"**Risk Score:** {item['score']}")

            explanations = explain_clause(item["clause"], item["risks"])

            st.markdown("**Plain-Language Explanation:**")
            for exp in explanations:
                st.write("- " + exp)

            st.markdown("---")

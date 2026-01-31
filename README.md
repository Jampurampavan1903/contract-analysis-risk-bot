# Contract Analysis & Risk Assessment Bot

A GenAI-powered legal assistant built as part of a **Data Science Hackathon** to help Small and Medium Enterprises (SMEs) understand contracts, identify legal risks, and receive actionable insights in plain language.

---

## 📌 Problem Statement

Small and medium business owners often struggle to interpret complex legal contracts, which can lead to hidden risks, unfavorable clauses, and compliance issues.  
This project addresses that challenge by building an AI-powered system that analyzes contracts and highlights risks clearly and transparently.

---

## 🚀 Solution Overview

The **Contract Analysis & Risk Assessment Bot** allows users to upload a contract document and automatically:

- Extract contract text
- Break the contract into clauses
- Assess risk at clause level
- Provide a contract-level risk score
- Highlight unfavorable clauses
- Explain risks in simple business-friendly language

The application is designed to be **privacy-preserving**, **easy to use**, and **deployable as a web application**.

---

## 🧠 Key Features

- 📄 Upload contracts in **PDF, DOCX, or TXT**
- 🔍 Clause & sub-clause extraction
- ⚠️ Clause-wise risk scoring (Low / Medium / High)
- 📊 Overall contract risk assessment
- 📝 Plain-language explanations
- 🧾 Highlighting of unfavorable terms
- 🌐 Web-based UI using Streamlit

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **UI Framework:** Streamlit
- **NLP Processing:** spaCy, NLTK
- **Document Parsing:** pdfplumber, python-docx
- **Deployment:** Render (public URL)
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
contract_analysis_bot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files & folders
├── src/
│   ├── parser.py          # Text extraction logic
│   ├── clause_splitter.py # Clause extraction
│   └── risk_engine.py     # Risk scoring logic
└── sample_contract.txt    # Sample input file


# Contract Analysis & Risk Assessment Bot

**Author: Saipavankalyan Jampuram**  
Graduate Student | Data Science & AI  
GitHub: https://github.com/Jampurampavan1903

---

A **GenAI-powered legal contract analysis system** built as part of a **Data Science Hackathon**.  
This application helps Small and Medium Enterprises (SMEs) understand complex contracts, identify legal risks, and make informed decisions using clear, plain-language explanations.

---

## 🧩 Problem Statement

Legal contracts are often lengthy, complex, and difficult to interpret for non-legal professionals.  
SMEs frequently face hidden risks such as unfavorable clauses, unilateral termination terms, penalties, or compliance issues, which can lead to financial and legal consequences.

The challenge is to build a system that can:
- Analyze contracts automatically  
- Detect risks and unfavorable clauses  
- Explain legal implications in simple, non-technical language  

---

## 💡 Solution Overview

The **Contract Analysis & Risk Assessment Bot** is a web-based application that allows users to upload a contract document and receive:

- Clause-by-clause analysis  
- Risk scoring at both clause and contract levels  
- Plain-language explanations of risks  
- Highlighting of unfavorable or sensitive clauses  

The system is designed to be **privacy-focused**, **easy to use**, and **deployable as a public web application**.

---

## 🚀 Key Features

- 📄 Upload contracts in **PDF, DOCX, or TXT**
- 🔍 Automatic text extraction
- 🧠 Clause & sub-clause identification
- ⚠️ Clause-wise risk classification (**Low / Medium / High**)
- 📊 Overall contract risk score
- 📝 Simplified explanations for business users
- 🧾 Highlighting of potentially unfavorable clauses
- 🌐 Interactive web interface using Streamlit

---

## 🛠️ Technology Stack

- **Programming Language:** Python 3  
- **Web Framework:** Streamlit  
- **NLP Libraries:** spaCy, NLTK  
- **Document Parsing:** pdfplumber, python-docx  
- **Version Control:** Git & GitHub  
- **Deployment Platform:** Render (Public URL)  

---

## 📂 Project Structure

```text
contract_analysis_bot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── parser.py
│   ├── clause_splitter.py
│   └── risk_engine.py

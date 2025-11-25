#  TestCase Studio

> **AI-powered tool that converts requirement documents into clean, structured software test cases.**  
> Built with **Streamlit** + **Groq LLM** for fast, consistent test-case generation.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/omkar1872/TestCase-Studio/main/test_image_1.png" alt="TestCase Studio Screenshot" width="95%">
</p>

---

## 🔎 Project Overview

**TestCase Studio** automates the creation of software test cases from written requirements. It reduces manual effort for QA engineers and developers by using a Large Language Model (Groq LLM) to interpret requirement text (from TXT, PDF, DOCX or pasted text) and produce well-structured test cases consisting of:

- **ID** (unique identifier)  
- **Title** (short descriptive name)  
- **Preconditions** (setup prior to execution)  
- **Steps** (clear, reproducible steps)  
- **Expected Result** (the outcome to validate)

**Why this matters:** Writing test cases manually is repetitive, time-consuming and inconsistent across teams. This tool standardizes and accelerates test-case generation saving time and improving coverage.

---

## ⚙️ Key Features

- Upload requirement files (TXT, PDF, DOCX) or paste requirement text.
- Generate multiple test cases in one click.
- Clean, copy-ready output with separators and clear fields.
- Download results as a `.txt` file for documentation or importing into test management tools.
- Lightweight Streamlit UI, easily deployable to Hugging Face Spaces or any cloud host.

---

## 🧰 Tools & Libraries — Detailed Explanation

### **Python**
The core language used for logic, file handling, and integration with external APIs.

### **Streamlit**
- Purpose: Rapidly build interactive web apps with Python.
- Why used: Minimal boilerplate, instant UI updates, great for demos and internal tools.
- Key parts used: `st.file_uploader`, `st.text_area`, `st.download_button`, `st.markdown`, `st.code`.

### **Groq (LLM)**
- Purpose: Generate natural-language test cases from requirements.
- Why used: LLMs can understand intent and reformat requirements into structured test cases quickly.
- Integration: The app sends a prompt + requirements to Groq and parses the text response for display/download.

### **PyPDF2**
- Purpose: Extract plain text from PDF files.
- Why used: Many requirements are archived as PDFs; PyPDF2 allows reading and extracting text on the server.

### **docx2txt**
- Purpose: Extract plain text from Microsoft Word `.docx`.
- Why used: Many stakeholders provide requirements in Word docs. `docx2txt` reads these reliably.

### **python-dotenv (optional)**
- Purpose: Load environment variables from `.env` during local development.
- Security note: Do not commit `.env` to GitHub. Use GitHub Secrets / Hugging Face Secrets for deployments.

### **GitHub & Git**
- Purpose: Version control and remote repository hosting.
- Why used: Share code with recruiters and collaborators; show professional workflow.

### **Hugging Face Spaces (optional platform)**
- Purpose: Deploy Streamlit apps as public web demos.
- Why used: Simple, fast deployment for Streamlit; supports secrets for API keys (recommended).

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/omkar1872/TestCase-Studio.git
cd TestCase-Studio
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Groq API key:

- Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

---

## Usage

1. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

2. Open the app in your browser.
3. Choose **Upload File** or **Paste Text** as the input method.
4. Set the approximate number of test cases to generate.
5. Click **Generate Test Cases**.
6. View results in the app and optionally download as a TXT file.

---

## File Structure

```
TestCase-Studio/
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

---

## Output Images
<p align="center">
  <img src="https://raw.githubusercontent.com/omkar1872/TestCase-Studio/main/test_image_2.png" alt="TestCase Studio Screenshot" width="95%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/omkar1872/TestCase-Studio/main/test_image_3.png" alt="TestCase Studio Screenshot" width="95%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/omkar1872/TestCase-Studio/main/test_image_4.png" alt="TestCase Studio Screenshot" width="95%">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/omkar1872/TestCase-Studio/main/test_image_5.png" alt="TestCase Studio Screenshot" width="95%">
</p>
## License

This project is licensed under the **MIT License**.





# 🧪 TestCase Studio

Streamlit app to generate clean software test cases from requirements using Groq LLM.

---

## Project Overview

**TestCase Studio** helps QA engineers and developers generate detailed and clean test cases from requirement documents. Users can either **upload a TXT, PDF, or DOCX file** or **paste requirement text** directly into the app. The app leverages Groq LLM to generate structured test cases with a clean, readable format.

---

## Features

- Upload requirement file (TXT, PDF, DOCX) or paste text directly.
- Generate detailed test cases with:
  - ID
  - Title
  - Preconditions
  - Steps
  - Expected Results
- Clean output format with separators for each test case.
- Download generated test cases as TXT.
- Modern Streamlit UI with a clean theme.

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

## Screenshots

![App Screenshot](screenshot.png) *(Add screenshot if desired)*

---

## License

This project is licensed under the **MIT License**.

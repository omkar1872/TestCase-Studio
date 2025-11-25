# 🧪 TestCase Studio

A Streamlit-based AI tool that automatically generates clean, structured software test cases from requirement documents using **Groq LLM**.

---
<p align="center"> <img src="https://raw.githubusercontent.com/omkar1872/TestCase-Studio/main/test_image_1.png" alt="TestCase Studio Screenshot" width="95%"> </p>

## 📌 Project Overview

**TestCase Studio** helps QA engineers, developers, and product teams quickly convert software requirements into **well-formatted test cases**.  

Manually writing test cases takes time. This tool automates most of that effort using an LLM — helping teams improve productivity and standardize testing documentation.

You can upload a requirement document (TXT, PDF, DOCX) or paste text, select how many test cases you want, and instantly get **professionally structured test cases**.

---

## 🚀 Features

- 📄 **Supports multiple inputs**  
  - Upload TXT, PDF, or DOCX files  
  - Paste text manually  

- 🧠 **AI-generated clean test cases** including:  
  - Test Case ID  
  - Title  
  - Preconditions  
  - Steps  
  - Expected Results  

- 🎨 **Modern UI** using Streamlit with custom theme  
- 📥 **Download results as TXT**  
- 🔍 Expandable viewer for generated test cases  
- 🖥️ Works on both local machine & Hugging Face Spaces  

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Core logic |
| **Streamlit** | Frontend & UI |
| **Groq LLM** | Test case generation |
| **docx2txt** | Read DOCX files |
| **PyPDF2** | Read PDF files |
| **dotenv / os** | Environment variable management |

---

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



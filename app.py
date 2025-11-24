import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import docx2txt
import PyPDF2

# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ------------------------------
# Streamlit page config and theme
# ------------------------------
st.set_page_config(page_title="🧪 TestCase Studio", layout="wide")
st.title("TestCase Studio")

# Custom CSS for clean theme
st.markdown(
    """
    <style>
    body {background-color: #f0f4f8; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
    .stButton>button {background-color: #00796b; color: white; font-size:16px; border-radius:8px; height: 40px; width: 100%;}
    .stTextArea>div>div>textarea {font-size: 14px;}
    .stFileUploader>div>div>label {font-weight: bold;}
    .stExpanderHeader {font-weight: bold; font-size: 16px; color: #00796b;}
    </style>
    """,
    unsafe_allow_html=True
)

st.write("Choose one input method to provide requirements:")

# ------------------------------
# Input method selection
# ------------------------------
input_method = st.radio("Select Input Type:", ("Upload File", "Paste Text"))

uploaded_file = None
manual_text = None

if input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload requirement file (TXT / PDF / DOCX)", type=["txt", "pdf", "docx"])
else:
    manual_text = st.text_area("Paste requirement text here", height=200)

num_testcases = st.number_input("Approximate number of test cases to generate", min_value=1, max_value=50, value=10)

generate_btn = st.button("Generate Test Cases")

# ------------------------------
# Helper function to read file
# ------------------------------
def read_file(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return None

# ------------------------------
# Call Groq API to generate test cases
# ------------------------------
def call_groq_generate_testcases(text, num_testcases=10):
    prompt = f"""
You are a QA expert. For the following requirement, generate approximately {num_testcases} detailed test cases in the following clean format:

====================================================
ID: TC_001
Title: <Test Case Title>
Preconditions: <Preconditions>
Steps:
1. <Step 1>
2. <Step 2>
...
Expected Result: <Expected Result>
====================================================

ONLY return the test cases in this clean format with lines separating each test case. Do not include anything else.
Requirement:
\"\"\"{text}\"\"\"
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user", "content": prompt}],
        max_tokens=1500
    )
    return response.choices[0].message.content

# ------------------------------
# Generate test cases
# ------------------------------
if generate_btn:
    if input_method == "Upload File":
        if uploaded_file is not None:
            try:
                requirement_text = read_file(uploaded_file)
            except Exception:
                st.error("Could not read uploaded file. Make sure it is a TXT, PDF, or DOCX.")
                st.stop()
        else:
            st.error("Please upload a file to continue.")
            st.stop()
    else:  # Paste Text
        if manual_text and manual_text.strip() != "":
            requirement_text = manual_text.strip()
        else:
            st.error("Please paste requirement text to continue.")
            st.stop()

    st.info("Generating Test Cases — please wait ...")
    try:
        testcases_output = call_groq_generate_testcases(requirement_text, num_testcases)
    except Exception as e:
        st.error(f"Error generating test cases: {e}")
        st.stop()

    st.subheader("🔸 Generated Test Cases")
    with st.expander("View Test Cases", expanded=True):
        st.text(testcases_output)

    st.download_button(
        "Download Test Cases as TXT",
        testcases_output,
        file_name="Generated_Test_Cases.txt",
        mime="text/plain"
    )

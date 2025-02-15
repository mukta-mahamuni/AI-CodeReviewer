import streamlit as st
from code_review import review_code_googleai

st.markdown(
    """
    <style>
    body {
        font-family: 'Poppins', sans-serif;
    }
    .title {
        color: #4A90E2;
        font-size: 36px;
        text-align: center;
        font-weight: bold;
    }
    .stTextArea>textarea { 
        font-size: 18px;
        font-family: 'Courier New', monospace;
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 10px;
    }

    .stButton>button {
        background-color: #ff5733;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px 20px;
    }

    .review-header {
        font-size: 24px;
        color: green;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Gen-AI Powered Code Reviewer🔎")
st.write("Submit your Python🐍 Code for AI-Powered review using💡Google Gemini!")

code = st.text_area("📝Enter your Python Code here:", height=200, help="Paste your Python Code here.")

if st.button("🔍Review Code"):
    if code.strip():
        with st.spinner("⏳Analyzing Code..."):
            response = review_code_googleai(code)
        st.markdown("🛠️AI Code Review:")
        st.success(response)
    else:
        st.warning("⚠️Please enter some Python code before submitting.")

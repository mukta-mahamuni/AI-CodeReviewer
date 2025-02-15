import google.generativeai as genai
from config import GOOGLEAI_API_KEY

genai.configure(api_key=GOOGLEAI_API_KEY)

def review_code_googleai(code):
    """Review Python code using Google Gemini API."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Analyze this Python Code, detect bugs, and suggest fixes:\n\n{code}")

    return response.text
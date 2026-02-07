from google import genai

# Gemini client (uses your API key)
client = genai.Client(api_key="AIzaSyB1K_tXt20iFKhPKXOO5INDTcJDaAHVZxI")

def analyze_resume(resume_text, jd_text):
    prompt = f"""
You are an expert ATS and resume optimization assistant.

Analyze the resume against the job description and:
1. Identify missing skills and keywords
2. Suggest ATS-friendly improvements
3. Recommend stronger resume bullet points

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text
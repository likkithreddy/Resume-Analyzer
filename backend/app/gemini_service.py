# app/gemini_service.py

import google.generativeai as genai
import json
import re
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_learning_plan_batch(skills):

    skill_list = "\n".join([f"- {skill}" for skill in skills])

    prompt = f"""
    Generate structured learning plans for the following skills:

    {skill_list}

    Return strictly valid JSON as an array like:

    [
      {{
        "skill": "Skill Name",
        "recommendation": "Short 2 sentence career advice",
        "roadmap_steps": ["Step1", "Step2", "Step3", "Step4"],
        "estimated_time": "Realistic time estimate",
        "career_impact": "High/Medium/Low"
      }}
    ]

    Do not add explanations.
    Only return JSON.
    """

    response = model.generate_content(prompt)

    text = response.text
    text = re.sub(r"```json|```", "", text).strip()

    try:
        return json.loads(text)
    except:
        return []

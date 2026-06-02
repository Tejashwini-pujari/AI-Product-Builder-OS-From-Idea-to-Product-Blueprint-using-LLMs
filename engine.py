# import os
# import json
# import google.generativeai as genai
# from dotenv import load_dotenv
# from prompts import *

# # Load .env
# load_dotenv()

# # Read Gemini key
# api_key = os.getenv("GEMINI_API_KEY")

# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found in .env file")

# # Configure Gemini
# genai.configure(api_key=api_key)

# # Model
# model = genai.GenerativeModel("gemini-2.0-flash")


# def call_llm(prompt, user_input):
#     full_prompt = f"""
# {prompt}

# USER INPUT:
# {user_input}

# Return ONLY valid JSON.
# """

#     response = model.generate_content(full_prompt)

#     content = response.text.strip()

#     # Remove markdown code fences if present
#     content = content.replace("```json", "")
#     content = content.replace("```", "")
#     content = content.strip()

#     try:
#         return json.loads(content)
#     except Exception:
#         return {
#             "raw_output": content
#         }


# def run_full_pipeline(user_input):

#     prd = call_llm(PRD_PROMPT, user_input)

#     system_design = call_llm(
#         SYSTEM_DESIGN_PROMPT,
#         json.dumps(prd)
#     )

#     execution = call_llm(
#         EXECUTION_PROMPT,
#         json.dumps(system_design)
#     )

#     risks = call_llm(
#         RISK_PROMPT,
#         json.dumps(execution)
#     )

#     evaluation = call_llm(
#         EVALUATION_PROMPT,
#         json.dumps({
#             "prd": prd,
#             "system_design": system_design,
#             "execution": execution,
#             "risks": risks
#         })
#     )

#     return {
#         "PRD": prd,
#         "SYSTEM_DESIGN": system_design,
#         "EXECUTION": execution,
#         "RISKS": risks,
#         "EVALUATION": evaluation
#     }


import json
from prompts import *


def call_llm(prompt, user_input):
    return {
        "product_name": "AI Startup OS",
        "target_users": [
            "Startups",
            "Founders",
            "Product Managers"
        ],
        "features": [
            "Meeting Analysis",
            "Roadmap Generation",
            "Task Creation",
            "Risk Detection",
            "Executive Summary Generation"
        ],
        "status": "Demo Mode"
    }


def run_full_pipeline(user_input):

    prd = call_llm(PRD_PROMPT, user_input)

    system_design = {
        "frontend": "React",
        "backend": "FastAPI",
        "database": "PostgreSQL",
        "ai_layer": "LLM Service",
        "status": "Generated"
    }

    execution = {
        "phase_1": "Requirement Gathering",
        "phase_2": "Architecture Design",
        "phase_3": "Development",
        "phase_4": "Testing",
        "phase_5": "Deployment"
    }

    risks = {
        "risk_1": "Data Privacy",
        "risk_2": "Scalability",
        "risk_3": "Model Hallucination"
    }

    evaluation = {
        "market_potential": "High",
        "technical_feasibility": "High",
        "business_value": "High"
    }

    return {
        "PRD": prd,
        "SYSTEM_DESIGN": system_design,
        "EXECUTION": execution,
        "RISKS": risks,
        "EVALUATION": evaluation
    }

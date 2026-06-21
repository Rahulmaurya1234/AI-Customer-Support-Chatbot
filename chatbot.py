import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

chat = model.start_chat(history=[])

FAQ = """
Password Reset:
Go to Settings > Security > Reset Password.

Refund Policy:
Refund available within 7 days.

Contact Support:
support@company.com

Account Verification:
Upload valid government ID proof.

Working Hours:
Monday to Saturday, 9 AM to 6 PM.
"""


def get_response(message: str):

    prompt = f"""
You are an AI Customer Support Assistant.

Company FAQ:
{FAQ}

Rules:
- Prefer FAQ information when relevant.
- If FAQ doesn't contain the answer, use your own knowledge.
- Never say "I don't know" unless necessary.
- Give helpful and professional responses.

Question:
{message}
"""
    response = chat.send_message(prompt)

    return response.text
from google import genai

from config import settings


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def ask_gemini(prompt: str):

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text
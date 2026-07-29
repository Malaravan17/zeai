from sqlalchemy.orm import Session

from ai_services.capability_service import detect_capabilities
from ai_services.prompt_builder import build_prompt
from ai_services.gemini_service import ask_gemini

from services.weather_service import get_current_weather
from services.market_service import get_market_prices


def process_question(
        db: Session,
        farm_id: int,
        question: str
):

    capabilities = detect_capabilities(question)

    context = {}

    if "weather" in capabilities:

        context["weather"] = get_current_weather(
            db,
            farm_id
        )

    if "market" in capabilities:

        context["market"] = get_market_prices(
            db,
            farm_id
        )

    prompt = build_prompt(
        question,
        context
    )

    response = ask_gemini(
        prompt
    )

    return response


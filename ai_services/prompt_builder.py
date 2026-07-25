def build_prompt(
        question: str,
        context: dict
):

    prompt = ""

    # System Role
    prompt += (
        "You are an AI Farmer Advisory Assistant.\n"
        "Provide accurate, practical and farmer-friendly advice.\n\n"
    )

    # Farmer Question
    prompt += "Farmer Question:\n"
    prompt += f"{question}\n\n"

    # Weather Information
    if "weather" in context:

        weather = context["weather"]

        prompt += "Weather Information:\n"

        prompt += (
            f"Farm Name: {weather['farm_name']}\n"
        )

        prompt += (
            f"District: {weather['district']}\n"
        )

        prompt += (
            f"State: {weather['state']}\n"
        )

        prompt += (
            f"Temperature: {weather['temperature']}°C\n"
        )

        prompt += (
            f"Humidity: {weather['humidity']}%\n"
        )

        prompt += (
            f"Wind Speed: {weather['wind_speed']} km/h\n"
        )

        prompt += (
            f"Condition: {weather['condition']}\n\n"
        )

        prompt += "Weather Advice:\n"

        for advice in weather["advice"]:

            prompt += f"- {advice}\n"

        prompt += "\n"

    # Market Information
    if "market" in context:

        market = context["market"]

        prompt += "Market Information:\n"

        prompt += f"{market}\n\n"

    return prompt

from agents import Agent, ModelSettings, function_tool

import os 
from dotenv import load_dotenv

@function_tool
def get_weather(city: str) -> str:
    """returns weather info for the specified city."""
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    model="gpt-5-nano",
    tools=[get_weather],
)

agent = Agent(
    name="Agent Portfolio",
    model="gpt-4.1-nano",
    instructions="Tu es mon agent personnel en charge de répondre à des questions sur moi. " \
    "Tu as accès à une base de données contenant des informations sur mon parcours académique, " \
    "mes projets, mes compétences et mes expériences professionnelles. Utilise ces informations " \
    "pour répondre de manière précise et pertinente aux questions qui te sont posées. " \
    "Si tu ne trouves pas la réponse dans la base de données, indique que tu n'as " \
    "pas cette information au lieu d'inventer une réponse.",
    tools=[get_upstash_data],
)
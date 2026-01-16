from agents import Agent, ModelSettings, function_tool

import os 
from dotenv import load_dotenv
from upstash import Index

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Créer une fonction que l'agent peut utiliser pour interroger la base de données Upstash
@function_tool
def get_upstash_data(query: str) -> str:

    url_upstash = os.getenv("UPSTASH_VECTOR_REST_URL")
    token_upstash = os.getenv("UPSTASH_VECTOR_REST_TOKEN")

    index = Index(url=url_upstash, token=token_upstash)

    results = index.query(
        query,
        top_k=5,
    )

    if not results['results']:
        return "Désolé, je n'ai pas trouvé d'informations pertinentes dans la base de données."

    response = "Voici les informations que j'ai trouvées:\n"
    for i, item in enumerate(results['results']):
        response += f"{i+1}. {item['metadata']['source']}: {item['text']}\n"

    return response

# Configurer l'agent avec des instructions spécifiques
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
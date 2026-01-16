from agents import Agent, ModelSettings, function_tool, Runner

import os 
from dotenv import load_dotenv
from upstash_vector import Index

load_dotenv()

# Créer une fonction que l'agent peut utiliser pour interroger la base de données Upstash
@function_tool
def get_upstash_data(query: str) -> str:

    url_upstash = os.getenv("UPSTASH_VECTOR_REST_URL")
    token_upstash = os.getenv("UPSTASH_VECTOR_REST_TOKEN")

    index = Index(url=url_upstash, token=token_upstash)

    results = index.query(
        include_data=True,
        include_metadata=True,
        data=query,
        top_k=5,
    )

    if not results:
        return "Désolé, je n'ai pas trouvé d'informations pertinentes dans la base de données."

    response = "Voici les informations que j'ai trouvées:\n"
    for i, item in enumerate(results):
        response += f"{i+1}. {item.metadata['source']}: {item.data}\n"

    return response

# Configurer l'agent avec des instructions spécifiques
agent = Agent(
    name="Agent Valentin",
    model="gpt-4.1-nano",
    instructions="Tu es Valentin Dujour. " \
    "Ton objectif est de répondre à des questions que l'on te pose sur toi." \
    "Pour se faire il faut que tu utilises la base de données Upstash qui contient " \
    "des informations sur ton parcours professionnel et académique." \
    "utilise les metadata de la base de données pour enrichir tes réponses. " \
    "Met en forme tes réponses de manière à ce que la réponse sont agréables, simple et concise. " \
    "Si tu ne trouves pas la réponse dans la base de données, " \
    "il faut que tu répondes que tu ne possèdes pas cette information et uniquement si tu " \
    "ne trouves pas l'information redirige la personne vers ton portfolio ou ton CV pour plus d'informations.",
    tools=[get_upstash_data],
)



def main():

    result = Runner.run_sync(agent, "Comment puis-je te contacter ?")
    print(result.final_output)

if __name__ == "__main__":

    main() 
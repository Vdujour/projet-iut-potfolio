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
    instructions= open("src/instructions.txt", "r", encoding="utf-8").read(),
    tools=[get_upstash_data],
    model_settings=ModelSettings(
        tool_choice="required",  # Force l'utilisation des outils
        max_tokens=2000,  # Assure des réponses complètes
    ),
)


def main():

    result = Runner.run_sync(agent, "Comment puis-je te contacter ?")
    print(result.final_output)

if __name__ == "__main__":

    main() 
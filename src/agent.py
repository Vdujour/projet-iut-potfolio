from agents import Agent, ModelSettings, OpenAIChatCompletionsModel, function_tool, Runner
from openai import AsyncOpenAI

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
    instructions= open("src/instructions.txt", "r", encoding="utf-8").read(),
    tools=[get_upstash_data],
    model = OpenAIChatCompletionsModel(
        model="openai/gpt-oss-120b",
        openai_client=AsyncOpenAI(
            base_url = "https://api.groq.com/openai/v1",
            api_key = os.getenv("GROQ_API_KEY")
        )
    ) 
)


def main():

    result = Runner.run_sync(agent, "Comment puis-je te contacter ?")
    print(result.final_output)

if __name__ == "__main__":

    main() 
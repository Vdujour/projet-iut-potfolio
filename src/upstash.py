from upstash_vector import Index
import os 
from dotenv import load_dotenv

from load import open_data
from split import split_text

load_dotenv()
url_upstash = os.getenv("UPSTASH_VECTOR_REST_URL")
token_upstash = os.getenv("UPSTASH_VECTOR_REST_TOKEN")

index = Index(url=url_upstash, token=token_upstash)

def push_data():
    """
    Push le fichier markdown découpé en chunks dans Upstash Vector avec des métadonnées.

    Args:
        None
    
    Returns:
        None
    """

    for file_name in os.listdir("data"):
            
        # Ouvrir les fichiers  
        file_content = open_data(file_name)
        
        # Splitter les fichiers par '##'
        file_chunks = split_text(file_content)


        # Pousser les chunks dans Upstash avec métadonnées
        for i, text in enumerate(file_chunks):
            index.upsert(vectors=[
                {
                    "id": f"{file_name}-chunk-{i}",
                    "data": text,
                    "metadata": {
                        "source": file_name,
                        "text": text
                    }
                }
            ])

        print(f"✅ Fichier '{file_name}' poussé avec {len(file_chunks)} chunks.")
    return
    
# Si l'index upstash est vide, alors on pousse sinon on ne fait rien
existing_vectors = index.info().vector_count
if existing_vectors == 0:
    push_data()
    print("✅ Tous les fichiers ont été poussés dans Upstash Vector.")
else:
    print(f"⚠️ L'index Upstash Vector contient déjà {existing_vectors} vecteurs. Aucune donnée n'a été poussée.")
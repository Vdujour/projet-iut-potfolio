from upstash_vector import Index
import os 
import random
from dotenv import load_dotenv

load_dotenv()
url_upstash = os.getenv("UPSTASH_VECTOR_REST_URL")
token_upstash = os.getenv("UPSTASH_VECTOR_REST_TOKEN")

index = Index(url=url_upstash, token=token_upstash)


# Fonction pour ouvrir le fichier markdown et lire son contenu
def open_data(file_name):

    # ouvrir le fichier et lire le contenu
    with open(os.path.join("data", file_name), 'r', encoding='utf-8') as file:
        text = file.read()
        return text
    

# Fonction pour découper le texte par '##' en chunks de taille définie avec un overlap
def split_text(text, chunk_size=500, overlap=50):

    # Split the text by '##'
    sections = text.split('##')
    chunks = []
    
    for section in sections:
        start = 0
        while start < len(section):
            end = start + chunk_size
            chunk = section[start:end]
            chunks.append(chunk)
            start += chunk_size - overlap  # Mettre la fin du dernier chunk au début du suivant
            
    return chunks


# Fonction pour splitter tous les fichiers markdown en chunks
def split_markdown():
    all_chunks = []
    
    # Parcourir tous les fichiers markdown dans le dossier 'data'
    for file_name in os.listdir("data"):
        if not file_name.endswith(".md"):
            continue
            
        file_content = open_data(file_name)
        
        # Utiliser différentes tailles selon le fichier
        if file_name in ["03-projet.md", "02-alternance.md"]:
            file_chunks = split_text(file_content, chunk_size=1200, overlap=200)
        else:
            file_chunks = split_text(file_content)
        
        # Ajouter les métadonnées avec le nom du fichier
        for chunk in file_chunks:
            all_chunks.append({
                "chunk": chunk,
                "source": file_name
            })
    
    print(f"Nombre total de chunks créés : {len(all_chunks)}")
    return all_chunks


# Fonction pour pousser les chunks dans Upstash Vector
def push_to_upstash(all_chunks):
    for i, item in enumerate(all_chunks):
        index.upsert(vectors=[
            {
                "id": f"{item['source']}-chunk-{i}",
                "data": item["chunk"],
                "metadata": {
                    "source": item["source"],
                    "text": item["chunk"],
                    "chunk_index": i
                }
            }
        ])
    
    print(f"✅ Total: {len(all_chunks)} chunks poussés dans Upstash")


if __name__ == "__main__":
    chunks = split_markdown()
    push_to_upstash(chunks)

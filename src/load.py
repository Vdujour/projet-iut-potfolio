import os 

# Fonction pour ouvrir le fichier markdown et lire son contenu
def open_data(file_name: str) -> str:
    """
    Ouvre un fichier markdown dans le dossier 'data' et retourne son contenu sous forme de chaîne de caractères.
    
    Args:
        file_name (str): Le nom du fichier markdown à ouvrir.
    
    Returns:
        str: Le contenu du fichier markdown.
    """

    # ouvrir le fichier et lire le contenu
    with open(os.path.join("data", file_name), 'r', encoding='utf-8') as file:
        text = file.read()
        return text
    
# print(open_data("01-presentation.md"))
from load import open_data

def split_text(text: str) -> list[str]:
    """
    Split the text by '##' and return non-empty chunks.
    
    Args:
        text (str): The input text to be split.
        
    Returns:
        list[str]: A list of non-empty text chunks.
    """

    chunks = text.split('##')
    chunks = [chunk for chunk in chunks if chunk != '']

    return chunks

# text_test = open_data("01-presentation.md")
# print(split_text(text_test))
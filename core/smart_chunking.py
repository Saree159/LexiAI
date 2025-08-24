from nltk.tokenize import sent_tokenize
from langdetect import detect
import nltk

def chunk_text_smart(text, max_tokens=300, overlap=50):
    try:
        language = detect(text)
    except:
        language = 'english'

    try:
        nltk.download('punkt', quiet=True)
        sentences = sent_tokenize(text, language=language)
    except:
        sentences = sent_tokenize(text)  # fallback

    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        token_count = len(sentence.split())

        if current_length + token_count > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap:]
            current_length = sum(len(s.split()) for s in current_chunk)

        current_chunk.append(sentence)
        current_length += token_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

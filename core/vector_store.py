from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from nltk.tokenize import sent_tokenize
from core.smart_chunking import chunk_text_smart  # Make sure this exists

class VectorSearch:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.text_chunks = []
        self.embeddings = []
        self.index = None

    def add_documents(self, text, chunk_size=300, overlap=50):
        self.text_chunks = chunk_text_smart(text, max_tokens=chunk_size, overlap=overlap)
        self.embeddings = self.model.encode(self.text_chunks, convert_to_tensor=False)
        self.index = faiss.IndexFlatL2(len(self.embeddings[0]))
        self.index.add(np.array(self.embeddings))

    def query(self, user_question, top_k=5):  # ⬅️ from 3 to 5
        question_embedding = self.model.encode([user_question])[0]
        D, I = self.index.search(np.array([question_embedding]), top_k)
        return [self.text_chunks[i] for i in I[0]]
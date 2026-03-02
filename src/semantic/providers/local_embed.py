from sentence_transformers import SentenceTransformer
from semantic.api.base import EmbeddingAPI


class LocalEmbedding(EmbeddingAPI):
    def __init__(self, model="BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model)

    def encode(self, text: str):
        vec = self.model.encode(text, normalize_embeddings=True)
        return vec.tolist()
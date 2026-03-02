from semantic.providers.local_embed import LocalEmbedding
from semantic.providers.gemma import GemmaProvider

# 🔁 CHANGE HERE ONLY
EMBEDDING_BACKEND = "local"
LLM_BACKEND = "gemma"


def load_embedding():
    if EMBEDDING_BACKEND == "local":
        return LocalEmbedding()
    raise ValueError("Unknown embedding backend")


def load_llm():
    if LLM_BACKEND == "gemma":
        return GemmaProvider()
    raise ValueError("Unknown LLM backend")
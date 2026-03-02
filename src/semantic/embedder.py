from semantic.api.config import load_embedding
from semantic.text_utils import chunk_text
"""
"""
_encoder = load_embedding()


def embed(text: str):
    return [_encoder.encode(c) for c in chunk_text(text)]
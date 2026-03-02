# src/semantic/text_utils.py

import re


def chunk_text(
    text: str,
    max_words: int = 200,
    overlap: int = 30
):
    """
    Split text into overlapping chunks for semantic embedding.

    Args:
        text: input text
        max_words: max words per chunk
        overlap: overlapping words between chunks

    Returns:
        List[str]
    """

    # Clean text
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split(" ")
    chunks = []

    start = 0
    while start < len(words):
        end = start + max_words
        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        start = end - overlap
        if start < 0:
            start = 0

    return chunks
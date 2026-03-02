import re
from html import escape
from bs4 import BeautifulSoup

ALLOWED_TAGS = {"b", "strong", "i", "em", "u", "s", "strike", "a", "code", "pre"}

def sanitize_for_telegram(text: str) -> str:
    if not text:
        return ""

    # 1. Remove all HTML using BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text(separator=" ")

    # 2. Escape everything (safety)
    text = escape(text)

    # 3. Cleanup whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()
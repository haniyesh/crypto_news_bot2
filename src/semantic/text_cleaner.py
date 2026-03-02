# src/semantic/text_cleaner.py

from bs4 import BeautifulSoup
import re


def clean_html(raw_html: str) -> str:
    """
    Remove HTML, scripts, styles, and normalize whitespace.
    """

    if not raw_html:
        return ""

    soup = BeautifulSoup(raw_html, "html.parser")

    # remove scripts and styles
    for tag in soup(["script", "style", "img", "figure"]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    # normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text
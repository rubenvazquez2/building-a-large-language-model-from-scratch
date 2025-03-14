"""
tokenizing_text.py
Description: Module with logic from section 2.2 of Building a Large Language Model from scratch
"""

from urllib import request
import logging
import re

from ballmfs.classes import SimpleTokenizerV1

logger = logging.getLogger("tokenizing_text")
logger.setLevel(logging.DEBUG)
s_handler = logging.StreamHandler()
s_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger.addHandler(s_handler)
s_handler.setFormatter(s_formatter)

if __name__ == "__main__":
    """
    self-test
    """
    # Get text for "The Verdict"
    URL = (
        "https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt"
    )
    FILE_PATH = "the-verdict.txt"
    request.urlretrieve(URL, FILE_PATH)

    with open("the-verdict.txt", "rt", encoding="utf-8") as fp:
        raw_text = fp.read()
    logger.info("Total number of characters: %d", len(raw_text))
    logger.info("%s", raw_text[:99])

    # Map each unique token to an integer
    preprocessed = re.split(r"([,.:;?_!\"()']|--|\s)", raw_text)
    preprocessed = [item for item in preprocessed if item.split()]
    all_words = sorted(set(preprocessed))
    vocab_size = len(all_words)
    logger.info(vocab_size)

    vocab = {token: integer for integer, token in enumerate(all_words)}
    for i, item in enumerate(vocab.items()):
        logger.info(item)
        if i >= 50:
            break

    tokenizer = SimpleTokenizerV1(vocab)
    text = """"It's the last he painted, you know,"
        Mrs. Gisburn said with pardonable pride."""
    ids = tokenizer.encode(text)
    logger.info(ids)
    logger.info(tokenizer.decode(ids))

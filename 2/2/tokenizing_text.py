"""
tokenizing_text.py
Description: Module with logic from section 2.2 of Building a Large Language Model from scratch
"""

from urllib import request
import logging, re

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

    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item for item in preprocessed if item.split()]
    logger.info(len(preprocessed))

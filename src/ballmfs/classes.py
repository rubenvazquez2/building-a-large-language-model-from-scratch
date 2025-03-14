"""
classes.py
Description: Classes available for ballmfs module
"""

import re
from typing import Dict, List


class SimpleTokenizerV1:
    """
    SimpleTokenizerV1
    Description: A class that handles encoding and decoding of tokens and token ids
    """

    def __init__(self, vocab: Dict[str, int]) -> None:
        self.str_to_int: Dict[str, int] = vocab
        self.int_to_str: Dict[int, str] = {i: s for s, i in vocab.items()}

    def encode(self, text: str) -> List[int]:
        """
        encode
        Description: Convert text into a list of token ids
        """
        # Split text up into tokens
        preprocessed = re.split(r"([,.:;?_!\"()']|--|\s)", text)
        preprocessed = [item.strip() for item in preprocessed if item.split()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids: List[int]) -> str:
        """
        decode
        Description: Convert list of token ids into text
        """
        text = " ".join([self.int_to_str[i] for i in ids])

        # Remove spaces before specified punctuations
        text = re.sub(r"\s+([,.?!\"()'])", r"\1", text)
        return text

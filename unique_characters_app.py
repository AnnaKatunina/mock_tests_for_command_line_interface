from collections import Counter
from functools import lru_cache


@lru_cache()
def get_unique_characters(text):
    if type(text) == str:
        numbers_unique_characters = sum(num for num in Counter(text).values() if num == 1)
        return numbers_unique_characters
    else:
        raise TypeError("Text must be string")

import re

def remove_numbers(text: str) -> str:
    return re.sub(r'\d', '', text)
import re

def count_letters_and_digits(s):
    return len(re.findall(r'[A-Za-z0-9]', s))

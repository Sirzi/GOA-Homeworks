def longest(s1, s2):
    unique_letters = set(s1) | set(s2)
    return ''.join(sorted(unique_letters))

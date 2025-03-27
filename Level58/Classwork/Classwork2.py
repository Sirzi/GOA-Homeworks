def longest_word(s):
    words = s.split()
    return max(words, key=len)

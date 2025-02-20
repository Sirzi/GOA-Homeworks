def find_short(s):
    words = s.split()
    return min(len(word) for word in words)
print(find_short("The quick brown fox"))


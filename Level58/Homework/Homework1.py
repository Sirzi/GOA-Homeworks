def vowelOne(s):
    vowels = "aeiouAEIOU"
    return ''.join(['1' if char in vowels else '0' for char in s])


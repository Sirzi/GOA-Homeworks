def disemvowel(s):
    return ''.join(char for char in s if char.lower() not in 'aeiou')
print(disemvowel("This website is for losers LOL!"))  
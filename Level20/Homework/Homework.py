letters = ["გიორგი", "ელენე", "მარიამი", "დათო", "სოფო"]
vowels = "აეიოუ"
def count_vowels(word):
    return sum(1 for letter in word if letter in vowels)
vowel_counts = {word: count_vowels(word) for word in letters}
print(vowel_counts)

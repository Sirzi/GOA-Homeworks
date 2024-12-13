num_words = int(input("Enter the number of words you want to input: "))
words = []

for _ in range(num_words):
    word = input("Enter a word: ")
    words.append(word)

result = " ".join(words)
print(result)

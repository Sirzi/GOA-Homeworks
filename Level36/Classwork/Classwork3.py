def get_count(sentence):
    return sum(1 for char in sentence if char in "aeiou")


print(get_count("hello world"))
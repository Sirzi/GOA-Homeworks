def is_isogram(string):
    string = string.lower()
    unique_characters = [char for char in string]
    return len(unique_characters) == len(set(unique_characters))


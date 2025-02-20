def XO(string):
    string = string.lower()
    count_x = string.count('x')
    count_o = string.count('o')
    return count_x == count_o


print(XO("ooxx"))
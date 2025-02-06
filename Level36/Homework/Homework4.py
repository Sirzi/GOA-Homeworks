def find_short(s):

    return min(len(word) for word in s.split())


print(find_short("hjello there friend")) 


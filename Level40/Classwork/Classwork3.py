def friend(names):
    return [name for name in names if len(name) == 4]

print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
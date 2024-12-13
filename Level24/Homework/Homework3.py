def custom_replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += string[i]
            i += 1
    return result


text = "Hello world, world!"
result = custom_replace(text, "world", "Python")
print(result)

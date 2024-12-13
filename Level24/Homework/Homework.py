def custom_split(string, delimiter=" "):
    result = []
    word = ""
    
    for char in string:
        if char == delimiter:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    
    if word:
        result.append(word)
    
    return result


input_string = "გიორგი და დავით"
split_result = custom_split(input_string)
print(split_result)

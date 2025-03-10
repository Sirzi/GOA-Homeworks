def remove_consecutive_duplicates(s):
    words = s.split()
    result = [words[0]] if words else []
    
    for i in range(1, len(words)):
        if words[i] != words[i - 1]:
            result.append(words[i])
    
    return " ".join(result)
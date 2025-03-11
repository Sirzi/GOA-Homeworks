def remove_consecutive_duplicates(s):
    splied_words = s.split(" ")
    result_arr = []
    for i in range(len(splied_words)):
        if (splied_words[i] != splied_words[i-1]) or (i == 0):
            result_arr.append(splied_words[i])
    return " ".join(result_arr)
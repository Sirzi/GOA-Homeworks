def lottery_filter(s):
    unique_digits = []
    for char in s:
        if char.isdigit() and char not in unique_digits:
            unique_digits.append(char)
    
    return ''.join(unique_digits) if unique_digits else "One more run!"

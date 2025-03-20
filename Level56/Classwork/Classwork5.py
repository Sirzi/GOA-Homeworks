def solve(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    if lower_count >= upper_count:
        return s.lower()
    else:
        return s.upper()
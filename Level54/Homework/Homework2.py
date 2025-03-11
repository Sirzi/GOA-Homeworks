def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    
    return sum(range(begin, end + 1, step))

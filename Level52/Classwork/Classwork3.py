def series_sum(n):
    if n == 0:
        return "0.00"
    
    total = sum(1 / (1 + (i - 1) * 3) for i in range(1, n + 1))
    
    return f"{total:.2f}"

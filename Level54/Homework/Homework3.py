def series_sum(n):
    if n == 0:
        return "0.00"
    
    total = sum(1 / (3 * i + 1) for i in range(n))
    return f"{total:.2f}"

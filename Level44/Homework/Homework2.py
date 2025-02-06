def sum_of_nth_row(n):

    start = n * (n - 1) + 1

    return sum(start + 2 * i for i in range(n))

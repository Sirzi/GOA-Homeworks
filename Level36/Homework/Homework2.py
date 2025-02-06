def square_digits(n):
    return int("".join(str(int(digit) ** 2) for digit in str(n)))


print(square_digits(9149)) 


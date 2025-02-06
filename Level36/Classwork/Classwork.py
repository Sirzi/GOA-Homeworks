def digitize(n):
    return [int(digit) for digit in str(n)][::-1]


print(digitize(12345))  
print(digitize(0))      
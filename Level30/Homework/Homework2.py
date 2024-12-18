def square(numbers):
    return sum(x ** 2 for x in numbers)
numbers = [3, 2, 7, 4]
result = square(numbers)
print(result)
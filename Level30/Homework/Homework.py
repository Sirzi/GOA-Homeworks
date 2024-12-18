def sum(arr):
    return sum(x for x in arr if x > 0)
numbers = [1, -4, 7, 12, -3]
result = sum(numbers)
print(result)  

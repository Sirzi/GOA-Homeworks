start = 1
end = 100
multiples = [num for num in range(start, end + 1) if num % 5 == 0 and num % 3 == 0]
print("Multiples of 5 and 3:", multiples)

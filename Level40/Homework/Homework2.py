def stray(numbers):

    return min(set(numbers), key=numbers.count)


print(stray([1, 1, 2])) 
print(stray([17, 17, 3, 17, 17, 17, 17]))  

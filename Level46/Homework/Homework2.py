def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"
print(high_and_low("1 2 3 4 5")) 


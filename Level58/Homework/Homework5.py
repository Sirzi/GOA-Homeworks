def find_twins(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num 
        seen.add(num)
    return None  


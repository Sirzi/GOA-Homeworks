def big_small(numbers: str) -> str:
    num_list = list(map(int, numbers.split()))
    
   
    highest = max(num_list)
    lowest = min(num_list)
    
    
    return str(highest) + " " + str(lowest)


print(big_small("1 2 3 4 5"))      
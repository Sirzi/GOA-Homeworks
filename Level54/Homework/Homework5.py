def two_oldest_ages(ages):
    sorted_ages = sorted(set(ages))
    return sorted_ages[-2:] 


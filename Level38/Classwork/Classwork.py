def manual_difference(first, second):

    difference = set()
    for item in first:
        if item not in second:
            difference.add(item)
    return difference


first = {2, 3, 4, 5}
second = {4, 5, 6, 7}
result = manual_difference(first, second)
print(result)  

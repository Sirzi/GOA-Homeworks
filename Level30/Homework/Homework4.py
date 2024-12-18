list = [1, 5, 9, 3]
def average(list):
    return sum(list) / len(list) if list else 0
average = average(list)
print(average)

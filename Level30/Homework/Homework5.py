arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def array(arr): 
    for x in arr:
        pos = sum(1 for x in arr if x > 0)
        neg = sum(x for x in arr if x < 0)
        return[pos, neg]
result = array(arr)
print(result)
        
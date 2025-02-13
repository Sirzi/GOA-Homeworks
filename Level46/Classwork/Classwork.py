def filter_list(lst):
    return [item for item in lst if isinstance(item, int)]

print(filter_list([1, 2, 'a', 'b'])) 


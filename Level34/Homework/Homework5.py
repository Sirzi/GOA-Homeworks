my_list = [1, 2, 3, 4]
print("Original list:", my_list)
my_list[0] = 10
print("Modified list:", my_list)
my_list.append(5)
print("List after appending 5:", my_list)
my_tuple = (1, 2, 3, 4)
print("\nOriginal tuple:", my_tuple)
try:
    my_tuple[0] = 10  
except TypeError as e:
    print("Error:", e)
try:
    my_tuple.append(5) 
except AttributeError as e:
    print("Error:", e)
new_tuple = my_tuple + (5,)
print("New tuple after concatenation:", new_tuple)

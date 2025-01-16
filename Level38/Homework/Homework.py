
my_set = {1, 2, 3, 4, 5}
print("შექმნილი set:", my_set)


my_set.add(6)
print("დამატებული ელემენტი 6:", my_set)

my_set.remove(4)
print("წაშლილი ელემენტი 4:", my_set)

my_set.discard(10)
print("წაშლილი (თუ არსებობს) ელემენტი 10:", my_set)


popped_element = my_set.pop()
print(f"შემთხვევით წაშლილი ელემენტი: {popped_element}, განახლებული set:", my_set)

my_set.clear()
print("ცარიელი set .clear()-ის შემდეგ:", my_set)


my_set = {1, 2, 3, 4, 5}
another_set = {4, 5, 6, 7, 8}


union_set = my_set.union(another_set)
print("გაერთიანება:", union_set)


intersection_set = my_set.intersection(another_set)
print("გადაკვეთა:", intersection_set)


difference_set = my_set.difference(another_set)
print("სხვაობა:", difference_set)


symmetric_difference_set = my_set.symmetric_difference(another_set)
print("სიმეტრიული სხვაობა:", symmetric_difference_set)


my_set.update({6, 7})
print("განახლებული set .update()-ის შემდეგ:", my_set)


my_set.intersection_update(another_set)
print("განახლებული set .intersection_update()-ის შემდეგ:", my_set)


my_set.difference_update({7, 8})
print("განახლებული set .difference_update()-ის შემდეგ:", my_set)


my_set.symmetric_difference_update({5, 6})
print("განახლებული set .symmetric_difference_update()-ის შემდეგ:", my_set)


is_subset = {4, 5}.issubset(another_set)
print("{4, 5} არის subset?:", is_subset)

is_superset = another_set.issuperset({6, 7})
print("{6, 7} არის superset?:", is_superset)


is_disjoint = my_set.isdisjoint({1, 2})
print("არ აქვთ საერთო ელემენტები?:", is_disjoint)

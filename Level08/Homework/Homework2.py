grade = input("What did you get on the test: ")
is_A = int(grade) >= 9
is_B = int(grade) >= 8 and int(grade) < 9
is_C = int(grade) >= 7 and int(grade) < 8
is_D = int(grade) >= 6 and int(grade) < 7
is_E = int(grade) < 6
print(is_A)
print(is_B)
print(is_C)
print(is_D)
print(is_E)
num_1 = input("What is your first number: ")
num_2 = input("What is your second number: ")
p = int(num_1) > int(num_2) 
q = num_1 < num_2
P_and_not_Q = p or q
print(P_and_not_Q)
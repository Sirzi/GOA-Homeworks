num_1 = input("What is your first number: ")
num_2 = input("What is your second number: ")
p = int(num_1) > int(num_2) 
q = int(num_1) < int(num_2)
P_and_not_Q = p or q
not_P_and_Q = q or p
P_xor_Q = p and q
a = int(input("What should a be: "))
b = int(input("What should b be: "))
c = int(input("What should c be: "))
is_a_greatest = a > b and a > c
b_is_middle = b < a and b > c
c_is_least = c < b and c < a
print("a is the greatest number: ", is_a_greatest)
print("b is in the middle of these numbers: ", b_is_middle)
print("c is the lowest of these numbers: ", c_is_least)
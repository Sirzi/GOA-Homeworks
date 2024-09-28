number = int(input("Enter a two-digit number: "))
tens_digit = number // 10
ones_digit = number % 10
sum_of_digits = tens_digit + ones_digit
print("The sum of the digits is:", sum_of_digits)
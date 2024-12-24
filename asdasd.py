amount = int(input("How much money would you like to convert: "))
from_currency = "gel"
convert = input("Enter the currency to convert to (usd, eur, rub): ")
rates = {
    ("gel", "usd"): 0.3,
    ("usd", "gel"): 3.3,
    ("gel", "eur"): 0.27,
    ("eur", "gel"): 3.7,
    ("gel", "rub"): 2.5,
    ("rub", "gel"): 0.4,
    ("usd", "eur"): 0.9,
    ("eur", "usd"): 1.1,
    ("usd", "rub"): 70,
    ("rub", "usd"): 0.014,
    ("eur", "rub"): 80,
    ("rub", "eur"): 0.0125
}
if (from_currency, convert) in rates:
    converted_amount = amount * rates[(from_currency, convert)]
    print(str(amount) + " " + from_currency + " is " + str(converted_amount) + " " + convert + ".")
else:
    print("Conversion not in database")
    
    
    
    
x = 1000
y = 500


deposit_amount = int(input("How much do you wanna give: "))
x += deposit_amount
print("Alice deposited", deposit_amount, "New balance:", x)


withdraw_amount = int(input("How much: "))
if withdraw_amount <= x:
    x -= withdraw_amount
    print("Alice withdrew", withdraw_amount, "New balance:", x)
else:
    print("Insufficient funds for withdrawal.")


transfer_amount = int(input("Idk"))
if transfer_amount <= x:
    x -= transfer_amount
    y += transfer_amount
    print("Alice have", transfer_amount, "to Bob.")
    print("Alices new balance:", x)
    print("Bobs new balance:", y)
else:
    print("Insufficient funds for transfer.")


print("Final balance of Alice:", x)
print("Final balance of Bob:", y)

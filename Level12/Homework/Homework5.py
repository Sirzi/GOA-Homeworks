print("მოგესალმებით! გთხოვთ, გაიარეთ რეგისტრაცია ჩვენს სოციალურ ქსელში.")


while True:
    name = input("შეიყვანეთ თქვენი სახელი: ")
    if name != "":  
        break
    else:
        print("სახელი ცარიელი არ უნდა იყოს!")


while True:
    password = input("შეიყვანეთ თქვენი პაროლი (უნდა შეიცავდეს მინიმუმ 5 სიმბოლოს): ")
    if password != "" and password.count(' ') == 0:  
        symbol_count = 0
        for char in password:
            symbol_count += 1
        if symbol_count >= 5:
            break
        else:
            print("პაროლი ძალიან მოკლეა! მინიმუმ 5 სიმბოლო შეიყვანეთ.")
    else:
        print("არასწორი პაროლი!")

# ასაკის შეყვანა
while True:
    age = input("შეიყვანეთ თქვენი ასაკი: ")
    if age.isdigit():  
        age = int(age)
        if age >= 13:  
            break
        else:
            print("ჩვენი სერვისის გამოყენება 13 წლიდან არის ნებადართული.")
    else:
        print("გთხოვთ, შეიყვანოთ რიცხვი.")

print("რეგისტრაცია წარმატებით დასრულდა!")

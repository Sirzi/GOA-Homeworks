def captainjack():
    gold_coin = int(input("შეიყვანეთ ოქროს მონეტების რაოდენობა: "))
    ships = {
        "150 მონეტიანი გემი": 150,
        "200 მონეტიანი გემი": 200,
        "250 მონეტიანი გემი": 250,
        "300 მონეტიანი გემი": 300,
        "350 მონეტიანი გემი": 350
    }

    if gold_coin == 0:
        return "ეკიპაჟი აჯანყდა!"

    print("აირჩიეთ გემი:")
    for ship in ships:
        print(f"- {ship}")

    chosen_ship = input("შეიყვანეთ გემის სახელი ზუსტად: ")

    if chosen_ship in ships:
        if gold_coin >= ships[chosen_ship]:
            return f"გილოცავ! თქვენ იყიდეთ {chosen_ship}."
        else:
            return "ეკიპაჟი აჯანყდა!"
    else:
        return "ასეთი გემი არ არსებობს."

student1 = {
    "სახელი": "გიორგი",
    "გვარი": "მანგოშვილი",
    "ასაკი": 15,
    "საშუალო ქულა": 8.7
}

student2 = {
    "სახელი": "ანა",
    "გვარი": "მელიქიძე",
    "ასაკი": 16,
    "საშუალო ქულა": 9.3
}


print("მოსწავლე 1-ის ინფორმაცია:")
for key, value in student1.items():
    print(key + ": " + str(value))

print("\nმოსწავლე 2-ის ინფორმაცია:")
for key, value in student2.items():
    print(key + ": " + str(value))

start = int(input("შეიყვანეთ დიაპაზონის დასაწყისი: "))
end = int(input("შეიყვანეთ დიაპაზონის ბოლო: "))


for number in range(start, end + 1):
   
    if number % 2 == 0 and number % 3 == 0:
        print("ეს ციფრები არის 3-ისა და 2-ის ჯერადები:", number)
    else:
        print("Uh oh")
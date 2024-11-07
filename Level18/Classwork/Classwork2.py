# წარმატებები
#      0 1  2   3  4  5 6  7
#                         -1      
arr = [9,5,94,711,52,96,71,8]

# Index-ებით მუშაობს
# start / end / step
print(arr[0:5:2])  # იღებს ელემენტებს ინდექსებიდან 0-დან 5-მდე (არა ჩათვლით), თითოეული მეორე ელემენტის მიხედვით
# შედეგი: [9, 94, 52]

print(arr[4:])     # იღებს ელემენტებს ინდექსიდან 4 ბოლომდე
# შედეგი: [52, 96, 71, 8]

print(arr[::1])    # იღებს მთელ სიას, ერთი ნაბიჯით თითოეული ელემენტის მიხედვით
# შედეგი: [9, 5, 94, 711, 52, 96, 71, 8]

print(arr[::-1])   # იღებს მთელ სიას უკუღმა
# შედეგი: [8, 71, 96, 52, 711, 94, 5, 9]

# სიტყვა "name"-ის უკუღმა შემოტრიალება
name = "name"
reversed_name = name[::-1]  # იყენებს სტრიქონის შებრუნებას
print(reversed_name)
# შედეგი: "eman"

# დამატებითი მაგალითი სახელზე "davit grdz"
name2 = "davit grdz"
reversed_name2 = name2[::-1]
print(reversed_name2)
# შედეგი: "zdrg tivad"

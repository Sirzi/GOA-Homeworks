
result = 0
count = 0 


while True:
    number = float(input("შეიყვანეთ დადებითი ციფრი (უარყოფითი ციფრის შეყვანით შეწყვეტთ): "))
    
    
    if number < 0:
        print("მომხმარებლის მიერ შეყვანილი ციფრი უარყოფითია. პროგრამა დასრულდა.")
        break
    
   
    result += number
    count += 1  


if count > 0:
    average = result / count
    print("შედეგი:", result)
    print("საშუალო არითმეტიკული:", average)
else:
    print("არ შეგიყვენიათ დადებითი ციფრები.")
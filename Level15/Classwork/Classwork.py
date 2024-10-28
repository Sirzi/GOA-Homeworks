giorgi_list = ["vaja", "daviti", "daviti2", True, 12 ]
res = ""

for element in giorgi_list:
    res += str(element)  
    if element != giorgi_list[-1]:
        res += " " 

print(res)  

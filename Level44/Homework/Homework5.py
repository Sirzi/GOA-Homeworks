def divisors(n):
    
    divs = []
      
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i: 
                divs.append(n // i)
    

    divs.sort()


    if divs:
        return divs
    else:
        return f"{n} is prime"
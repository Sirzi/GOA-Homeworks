rows = 4
for i in range(rows):
    
    print(' ' * i + '*' * (rows - i))


for i in range(1, rows):
    print(' ' * (rows - i - 1) + '*' * i)

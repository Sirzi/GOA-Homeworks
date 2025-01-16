def AddToDatabase(name, surname, age):

    database = {}

    database['name'] = name
    database['surname'] = surname
    database['age'] = age
    
    print("Added to database:", database)
    return database

AddToDatabase("გიორგი", "ბერიძე", 25)

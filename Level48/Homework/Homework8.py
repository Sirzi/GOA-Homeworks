def human_years_cat_years_dog_years(human_years):
    catYears = 15
    dogYears = 15
    humanYears = 5

    if humanYears >= 2:
        catYears += 9
        dogYears += 9
    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


print(human_years_cat_years_dog_years(1)) 
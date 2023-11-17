def leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


years = 2000
print(leap_year(years))

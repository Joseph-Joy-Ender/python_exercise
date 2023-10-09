miles = float(input("Enter miles driven or (-1) to end: "))
gallons = float(input("Enter gallons for each tankful or (-1) to end: "))

total_miles_per_gallon = 0

miles_per_gallon = miles / gallons
print(f'{miles_per_gallon:.5f}')
total_miles_per_gallon += miles_per_gallon

while miles != -1:
    miles = float(input("Enter miles driven or (-1) to end: "))
    gallons = float(input("Enter gallons for each tankful or (-1) to end: "))

    miles_per_gallon = miles / gallons
    print(f'{miles_per_gallon:.5f}')

    total_miles_per_gallon += miles_per_gallon

print(f"Total miles per gallon is {total_miles_per_gallon:.5f}")




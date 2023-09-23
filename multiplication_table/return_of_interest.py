principal = float(input("Enter an amount to invest: "))
interest_rate = 0.1
for year in range(1, 31):
    roi = interest_rate * principal
    investment = principal * (1 + interest_rate)
    principal = investment

    print(f'your roi is ${roi:.2f} your investment is now ${investment:.2f} in year {year}')


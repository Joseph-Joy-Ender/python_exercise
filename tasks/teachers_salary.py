def calculate_salary():
    current_monthly_rate = 20
    monthly_salary = 0
    teachers_name = input("Enter teachers name: ")
    number_of_period = int(input("Enter the number of periods: "))
    if number_of_period > 100:
        result = number_of_period - 100
        print(result)
        overtime = result * 25
        monthly_salary = number_of_period * current_monthly_rate + overtime
    else:
        monthly_salary = number_of_period * current_monthly_rate
    return monthly_salary


print(calculate_salary())

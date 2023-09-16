employee_name = input("Enter employee's name: ")
hours = float(input("Number of hours worked in a week: "))
hourly_pay = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withHolding rate: "))
state_tax = float(input("Enter state tax withHolding rate: "))
gross_pay = hours * hourly_pay
net_pay = gross_pay - federal_tax - state_tax

print("Enter employee's name is: ", employee_name)
print("Number of hours worked in a week is: ", hours)
print("Enter hourly pay rate: ", hourly_pay)
print("Enter federal tax withHolding rate is: ", federal_tax)
print("Enter state tax withHolding rate is: ", state_tax)
print("Gross pay is: ", gross_pay)
print("Net pay is: ", net_pay)



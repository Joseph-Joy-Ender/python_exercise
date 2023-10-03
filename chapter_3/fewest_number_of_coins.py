purchasePrice = int(input("Enter purchase price: "))
amountTendered = int(input("Enter amount tendered: "))

cents = amountTendered - purchasePrice

pCounter, qCounter, dCounter = 0, 0, 0
quarters = 25
pennies = 1
dime = 10

while cents > 0:
    if cents > (quarters + pennies + dime):
        cents = cents - (quarters + pennies + dime)
        pCounter += 1
        qCounter += 1
        dCounter += 1
    elif cents > (pennies + dime):
        cents = cents - (pennies + dime)
        pCounter += 1
        dCounter += 1
    elif cents >= pennies:
        cents = cents - pennies
        pCounter += 1
    else:
        break

print(f"Your change is: \n {qCounter} quarters \n {pCounter} pennies \n {dCounter} dime")


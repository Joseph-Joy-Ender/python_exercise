

def fahrenheit():
    print("Fahrenheit     celsius")
    result = ""
    for i in range(0, 101):
        formula = (9 / 5) * i + 32
        print(f"{i:>4}  {formula:>15.1f}")


fahrenheit()

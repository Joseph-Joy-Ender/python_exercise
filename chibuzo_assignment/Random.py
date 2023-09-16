import random

_precious = random.randint(1, 21)
print(_precious)

name = input("Enter your name: ")
if name:
    print(f' your name is {name}')
else:
    print("no name entered")

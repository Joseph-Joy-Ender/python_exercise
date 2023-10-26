def student_age():
    student_ages = {"dike": 33,
                    "ope": 25,
                    "melody": 20,
                    "precious": 27}
    name = input("Enter your name: ").lower()
    for k, v in student_ages.items():
        if name in k:
            return f'Hi, {name}, you are {v} years old'
        if name not in k:
            print("Your name is not in the dictionary: ")
            age = int(input("Enter your age: "))
            student_ages.update({name: age})
        return student_ages


print(student_age())

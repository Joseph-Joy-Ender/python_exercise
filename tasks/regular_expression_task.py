import re
print("True" if re.fullmatch(r'\d+[A-Z][a-z]*[A-Z][a-z]*', 'Nope,Hey') else "False")

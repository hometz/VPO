import re

def is_valid_name(name):
    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+$'
    return re.match(pattern, name)

names = []
while True:
    name = input("Enter name: ")
    if name == "":
        break
    while not is_valid_name(name):
        print("Invalid format. Please enter in the format: Name Surname Fathername")
        name = input("Enter name (Name Surname Fathername): ")
    names.append(name)

for name in names:
    print(name)
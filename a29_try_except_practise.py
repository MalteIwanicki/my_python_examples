while True:
    print("How old are you?")
    try:
        age = int(input())
    except ValueError:
        print("Error: you did not enter a number.")
    else:
        break

if 22 < age < 50:
    print("I'm not surprised.")
else:
    print("I'm surprised.")




""" Clean Code """

def get_number():
    try:
        return int(input())
    except ValueError:
        print("Error: you did not enter a number.")


while True:
    print("How old are you?")
    age = get_number()
    if age:
        break

if 22 < age < 50:
    print("I'm not surprised.")
else:
    print("I'm surprised.")

""" Cleaner Code """


def get_number():
    try:
        return int(input())
    except ValueError:
        print("Error: you did not enter a number.")


def get_age():
    while True:
        print("How old are you?")
        age = get_number()
        if age:
            return age


if 22 < get_age() < 50:
    print("I'm not surprised.")
else:
    print("I'm surprised.")

# example nested if statement
print("Say a number between 1 and 9")
number = int(input())

if number < 5:
    if number < 3:
        if number == 2:
            print("it's 2")
        else:
            print("it's 1")
    elif number == 3:
        print("it's 3")
    else:
        print("it's 4")
elif number == 5 or number == 6 or number == 7:
    if number == 5:
        print("it's 5")
    elif number == 6:
        print("it's 6")
    else:
        print("it's 7")
elif number == 8:
    print("it's 8")
else:
    print("it's 9")

print("done")
# This is a guess the number game.
import random

def ask_for_name():
    while True:
        print("What is your name?",end=" ")
        name = input()
        if name and len(name) > 1:
            return name
        else:
            print("That is not a name.")


def get_number():
    try:
        return int(input())
    except ValueError:
        print("That is not a number. Try again")


def guess():
    while True:
        print("Take a guess:",end=" ")
        number = get_number()
        if number and MIN <= number <= MAX:
            return number
        print("Number not in range, try again")


if __name__ == "__main__":
    MIN = 1
    MAX = 20
    attempts = 6
    secret_number = random.randint(MIN, MAX)
    name = ask_for_name()

    print("Let us play a game " + name + ". Guess a number between "
          + str(MIN) + " and " + str(MAX) + ".")
    print("You may guess " + str(attempts) + " times.")

    for a in range(attempts + 1):
        number = guess()
        if number == secret_number:
            print("Well done " + name + ", "
                  + str(secret_number) + " was indeed my secret number.")
            break
        elif number < secret_number:
            print("No, my number is higher.")
        else:
            print("No, my number is lower.")
    else:
        print("Sorry " + name + ", my secret number was " + str(secret_number) + ".")

# Guess the number game
import random

print("What is your name?", end=" ")
name = input()
print("Let us play a game " + name + ". Guess a number between 1 and 20.")
print("You may guess 6 times.")
secret_number = random.randint(1, 20)
for guesses_taken in range(1, 7):
    print("Take a guess:", end=" ")
    guess = int(input())
    if guess == secret_number:
        print("Well done " + name + ", "
              + str(secret_number) + " was indeed my secret number. "
              + "You took " + str(guesses_taken) + " guesses.")
        break
    elif guess < secret_number:
        print("No, my number is higher.")
    else:
        print("No, my number is lower.")
else:
    print("Sorry " + name + ", my secret number was " + str(secret_number) + ".")

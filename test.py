import math
import random
numbers_to_guess_1 = []
while len(numbers_to_guess_1) != 10:
    numbers_to_guess_1.append(random.randint(1, 99))
for i in range(10):
    guess = int(input("Enter an integer from 1 to 99: "))
    while numbers_to_guess_1[i] != guess:
        checking_guess(guess)
    else:
        break
        print("you guessed it!")

def checking_guess(guess):
        if guess < numbers_to_guess_1[i]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > numbers_to_guess_1[i]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 99: "))
    



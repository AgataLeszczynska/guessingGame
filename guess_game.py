import math
import random
to_guess_list_1 = []
while len(to_guess_list_1) != 10:
    to_guess_list_1.append(random.randint(1, 99))
for i in range(10):
    guess = int(input("Enter an integer from 1 to 99: "))
    while to_guess_list_1[i] != guess:
        if guess < to_guess_list_1[i]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > to_guess_list_1[i]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")


to_guess_list_2 = []
while len(to_guess_list_2) != 10:
    to_guess_list_2.append(random.randint(1, 49))
for i in range(10):
    guess = int(input("Enter an integer from 1 to 49: "))
    while to_guess_list_2[i] != guess:
        if guess < to_guess_list_2[i]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 49: "))
        elif guess > to_guess_list_2[i]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
import math # importing module with mathematical functions
import random # importing module implementing random numbers 
a = [] # initialization of an empty list
a.append(random.randint(1, 99)) # returns random integer between 1 -99 and adding it to thelist a
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
for i in range(10):# looping through a list in range 0-9
    g = int(input("Enter an integer from 1 to 99: "))# asking for input; change input into integer
    while a[i] != g:# looping/comparison of the value of the ith elemnt of the list with value of the g
        if g < a[i]:# check if if the value of g is less than i elemnt of the list a
            print("guess is low") # printing information about the result 
            g = int(input("Enter an integer from 1 to 99: ")) #assign integer input to the g  
        elif g > a[i]: #checking if g is greater than ith element of the list
            print("guess is high") # printing information about the result 
            g = int(input("Enter an integer from 1 to 99: ")) #assign integer input to the g 
        else:
            break #breaking the while loop
    print("you guessed it!")
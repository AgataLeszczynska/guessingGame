import math # importing module with mathematical functions
import random # importing module implementing random numbers 
a = []# initialization of an empty list a
a.append(random.randint(1, 99))#returns first random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns second random integer between 1 -99 and adding it to the list a 
a.append(random.randint(1, 99))#returns third random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns fourth random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns fifth random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns sixth random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns seventh random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns eight random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns ninth random integer between 1 -99 and adding it to the list a
a.append(random.randint(1, 99))#returns tenth random integer between 1 -99 and adding it to the list a
for i in range(10):#looping through a list in range 0-9
    g = int(input("Enter an integer from 1 to 99: "))#asking for input; assigning input to g variable;change input into integer
    while a[i] != g:#looping by comparing of the value of the ith elemnt of the list with value of the g
        if g < a[i]:#check if if the value of g is less than i element of the list a
            print("guess is low")#printing information about result of a guess
            g = int(input("Enter an integer from 1 to 99: "))#asking for input; assigning input to g variable;change input into integer  
        elif g > a[i]:#checking if g is greater than ith element of the list a
            print("guess is high")#printing information about result of a guess
            g = int(input("Enter an integer from 1 to 99: "))#asking for input; assigning input to g variable;change input into integer
        else:
            break#breaking the while loop
    print("you guessed it!")#printing information if win

b = []#initialization of an empty list b
b.append(random.randint(1, 49))#returns first random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns secon random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns third random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns fourth random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns fifth random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns sixth random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns seventh random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns eight random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns ninth random integer between 1 -49 and adding it to the list b
b.append(random.randint(1, 49))#returns tenth random integer between 1 -49 and adding it to the list b
for i in range(10):#looping through a list in range 0-9
    g = int(input("Enter an integer from 1 to 49: "))#asking for input; assigning input to g variable;change input into integer
    while b[i] != g:#looping by comparing of the value of the ith element of the list with value of the g
        if g < b[i]:#check if if the value of g is less than i element of the list b
            print("guess is low")#printing information about result of a guess
            g = int(input("Enter an integer from 1 to 49: "))#asking for input; assigning input to g variable;change input into integer
        elif g > b[i]:#checking if g is greater than ith element of the list b
            print("guess is high")#printing information about result of a guess
            g = int(input("Enter an integer from 1 to 49: "))#asking for input; assigning input to g variable;change input into integer
        else:
            break#breaking the while loop
    print("you guessed it!")#printing information if win 
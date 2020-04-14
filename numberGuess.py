
import random

number = random.randint(1,100)
guess = int(input("Guess my number\n")) 
i = 1
while (number != guess):
    if (guess<number):
        guess = int(input("Too low, guess another number\n"))
    else:
         guess = int(input("Too high, guess another number\n"))
    i=i+1
print("Correct, you made " + str(i) + " guesses")
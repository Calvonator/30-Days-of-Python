
# 1 Import the fractions module and create a Fraction from the float 2.25
import fractions

frac = fractions.Fraction(2.25)
print(frac)



# 2 Import only the fsum function from the math module and use it to find the sum of the following series of floats:

from math import fsum

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]

fracsum = fsum(numbers)

print(fracsum)


# 3 Import the random module using an alias, and find a random number between 1 and 100 using the randint function.

import random as rand

randNum = rand.randint(1, 100)

print(randNum)


# 4 Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. 
# This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

def guessGame():
    guessNum = rand.randint(1, 100)
    x = 0
    while x < 2:
        guess = input("Please guess a number between 1-100:\n")

        guess = int(guess)

        x += 1

        if guess == guessNum:
            print("You guess the correct number: " + str(guess))
            break
        
    else:
        if guess > guessNum:
            print("Your guess was greater than the number.")
        
        elif guess < guessNum:
            print("Your guess was less than the number.")



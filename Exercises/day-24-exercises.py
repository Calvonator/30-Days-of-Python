#Task 1
input = input("Enter a value between the numbers 1 and 10 inclusive\n")

if int(input) > 10 or int(input) < 1:
    raise ValueError("The number enetered was not between 1 and 10")

#task 2


def divide(a, b):

    try:
        return a / b

    except ArithmeticError as ex:
        print(f"Error: {str(ex)}")

#Task 3

def itemgetter(collection, identifier):
    try:
	    return collection[identifier]
    except LookupError as ex:
        with open("log.txt", "w") as f:
            f.write(f"itemgetter() Error:{str(ex)} Parameters: {str(identifier)}")
            f.close()
        raise

ar = [1, 2]

#a = itemgetter(ar, 3)


#Project

import argparse
import random

#Settings
logging = 0
repeat = 1


parser = argparse.ArgumentParser()

parser.add_argument("dice", help="[number of dice]d[number of sides]")
parser.add_argument("--log", help="")
parser.add_argument("--repeat", help="")

args = parser.parse_args()

dice_string = args.dice

if args.log:
    log_dir = args.log
    logging = 1

if args.repeat:
    repeat = args.repeat



no_of_dice = dice_string[0]
no_of_sides = dice_string[-1]


print(f"{no_of_dice}, {no_of_sides}")


def roll_dice(dice, sides):
    
    dice_rolls = []

    for _ in range(int(repeat)):
        roll = []
        for _ in range(int(dice)):
            roll.append(random.randint(1, int(sides)))

        dice_rolls.append(roll)


    if logging == 1:
        try:

            with open(log_dir, "a+") as f:
                #logged_rolls = f.readlines()
                #logged_rolls.append(dice_rolls)
                #f.truncate(0)
                f.write(str(dice_rolls) + "\n")
                f.close() 

        except FileNotFoundError:
            with open(log_dir, "w") as f:
                f.write(str(dice_rolls) + "\n")
                f.close()

    return dice_rolls

def roll_average(rolls):
    #Calculates the average of a single roll or the collective average of multiple rolls
    sum = 0

    roll_averages = []

    for roll in rolls:
        for dice in roll:

            sum += dice

        roll_avg = sum / len(roll)
        roll_averages.append(roll_avg)
    
    sum = 0

    for average in roll_averages:
        sum += average

    avg = sum / len(roll_averages)  #This is not calculating the correct collective average

    return avg


rolls = roll_dice(no_of_dice, no_of_sides)

average = roll_average(rolls)

print(rolls)
print(average)
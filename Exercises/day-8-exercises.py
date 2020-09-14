import random

def test():
    dividend = int(input("Please enter a number: "))

    # Grab numbers one at a time from the range sequence
    for divisor in range(2, dividend):
        # If user's number is divisible by the curent divisor, break the loop
        if dividend % divisor == 0:
            print(f"{dividend} is not prime!")
            break
    else:
        # This line only runs if no divisors produced integer results
        print(f"{dividend} is prime!")

def guessGame():
    guessNum = random.randint(1, 100)
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
        
def printNoO(word):
    for char in word:
        if char == 'o' or char == 'O':
            print("I am NOT printing this 'o' character >:(")
           

        else:
            print(char)


def printPrime(upperLimit):

    primes = []

    for num in range(2, int(upperLimit)):
        for integer in range(2, num):
            if num % integer == 0:
                break
        else:
            print(num)
            primes.append(num)

    print(primes)


while True:
    choice = input("[1] Guessing Game, [2] Python Print or [3] Print Primes\n")

    if choice == '1':
        #test()
        guessGame()
    elif choice == '2':
        wrd = input("What word would you like to print?\n")
        printNoO(wrd)
    elif choice == '3':
        num = input('Enter how many number you would like to check:\n')
        printPrime(num)
        #test()
def reverse(number):
    number = str(number)
    stripped_num = [int(num) for num in number]
    reversed_num = []

    for index in range(len(number), 0, -1):
        reversed_num.append(str(stripped_num[index - 1]))

    return_num = ''.join(reversed_num)

    return int(return_num)


def doubleEvenIndexNumbers(card_number):

    stripped_num = [num for num in card_number]   #Convert stringafied number into an array

    for even in range(0, len(card_number), 2):         #For every number at an even index
        even_num = stripped_num[even]
        even_num = int(even_num)
        even_num *= 2                                           #Double the number
        if even_num > 9:
            even_num -= 9                                       #Subtract by 9 if greater than 9 (mod(10))
        print(even_num)
        stripped_num[even] = str(even_num)                           #Place the new number back in it's place

    #return_num = ''.join(stripped_num)

    return stripped_num

def luhnValidateCard(card_number):
    
    card_number = str(card_number)
    print(f"Card Number {card_number}")
    
    checking_digit = card_number[len(card_number) - 1]  #Grab the checking digit
    card_number = card_number[:len(card_number) - 1]    #Remove last digit from card number
    
    print(f"Card Number - 1: {card_number}")
    print(f"Checking Digit: {checking_digit}")

    reversed_card_number = reverse(card_number)         #Reverse the card number
    print(f"Reversed Number: {reversed_card_number}")

    reversed_card_number = str(reversed_card_number)

    processed_number = doubleEvenIndexNumbers(reversed_card_number)     #Double each number at an even index and modulo 10; returns a list of the numbers as strings

    print(processed_number)

    processed_number.append(checking_digit)
    
    sum_result = 0

    for digit in processed_number:
        sum_result += int(digit)

    print(sum_result)
    if sum_result % 10 == 0:        
        print("The provided number is a valid credit card number!")
    
    else: 
        print("The provided numner is an invalid credit card number!")

num = 5893804115457289

luhnValidateCard(num)


numbers = [1, 2, 3, 4, 5]

print(*numbers, sep = " | ")


# Create a function that uses *args to usm numbers
#


def sum(*xs):

    sum = 0

    for x in xs:
        sum += x
    
    return sum

number = sum(1, 2, 3, 4, 5, 1)

print(number)


#Create a function that accepts any number of positional and keyword arguments,
# and that prints them back to the user. Your output should indicate which values were provided 
# as positional arguments, and which were provided as keyword arguments.

def some_func(*args, **kwargs):
    for positional in args:
        print(f"This is a positoinal arguement {positional}")
    
    for key, value in kwargs.items():
        print(f"This is a keyword arguement {key}: {value}")

some_func(1, 2, 3, lol = "hahha", nah = "no")
        

# Print the following dictionary using the format method and ** unpacking

country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
}

def print_country(*dictionary):
    for country in dictionary:
        print("\nName: {name}\nPopulation: {population}\nCapital: {capital}\nCurrency: {currency}".format(**country))

print_country(country)



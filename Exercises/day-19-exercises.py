
# 1 Create a short program that prompts the user for a list of grades separated by commas. 
# Split the string into individual grades and use a list comprehension to convert each string to an integer.
#
# 2 Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.

def get_grades():
    while True:

        input_grades = input("Please input grades in a CSV format: \n")

        grades = input_grades.split(',')

        try:
            grades = [int(x) for x in grades]
            return grades
        
        except ValueError:
            print("An inputted value was incorrect, please input the values again")

        else:
            break
    
        finally:
            print("Finally")
            return


get_grades()

# 3 Imagine you have a file named data.txt with this content:

#There is some data here!
#
#Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't exist. 


try:
    data_file = open("data.txt", "r")
    print(data_file.read())

except FileNotFoundError:
    data_file = open("data.txt", "w")
    data_file.write("Hello Data, I'm Python!")
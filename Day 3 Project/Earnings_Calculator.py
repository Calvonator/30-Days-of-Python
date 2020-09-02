print("\n\nWelcome to the Earnings Calculator!\n")
print("-" * 100)

def strFormat(str):
    str = str.strip()
    str = str.lower()
    str = str.title()
    return str

def calcPay(wage, hours):
    return float(wage) * float(hours)

emp_name = input("Input employees name: ")

emp_name = strFormat(emp_name)

emp_hourly_wage = input("What is the employees hourly wage?")

emp_hours = input("How many hours did the employee work this week?")

emp_pay = calcPay(emp_hourly_wage, emp_hours)

print(f"{emp_name} has worked {emp_hours} and earned ${str(emp_pay)} with an hourly wage of {emp_hourly_wage}")





#Task 1 and 2
def sum(ar):
    sum = 0
    
    for a in ar:
        sum += a
    
    return sum

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

sum1 = map(sum, numbers)

#print(next(sum1))
#print(next(sum1))


#Task 3
import math
from itertools import cycle


def find_weekday(week_iter, week_day):

    ctr = 1

    for day in week_iter:
        
        if ctr == week_day:
            return day
        
        ctr += 1

week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

employees = [
    "A",
    "B",
    "C"
]

week_days = cycle(week)

day_num = 7

schedule = []

for day in range(1, 31):
    
    week_day = next(week_days)

    employee = employees[day % 3 - 1]   #Can also use cycle on the employees but this method is more memory efficient

    schedule.append((day, employee, week_day))


for x in schedule:
    print(x)





print(find_weekday(week_days, day_num))
#print(week_days[day_num])
#print(week_days[math.floor(math.fmod(day_num, 7))])



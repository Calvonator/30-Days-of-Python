from time import perf_counter
from math import fsum
#Decorators

def example_decorator(func):
    def inner(*args):
        print(f"Hello, executing {func.__name__}")
        func(*args)
        print(f"{func.__name__} finished functioning")
    return inner


def timeit_decorator(func):
    def inner(*args):
        print(f"Timing the {func.__name__} function with 10 repeats")

        times = []

        for _ in range(10):
            start = perf_counter()
            func(*args)
            end = perf_counter()
            times.append(end - start)

        average = fsum(times) / len(times)

        print(f"\n{func.__name__} took an average of {average} seconds to execute over 10 executions\n")
    return inner


#1 Make a decorator which calls a given function twice. You can assume the functions don't 
# return anything important, but they may take arguments.

def twice_decorator(func):
    def inner(*args, **kwargs):
        for _ in range(2):
            func(*args, **kwargs)
    return inner

# 2 Imagine you have a list called books, which several functions in your application interact with. 
# Write a decorator which causes your functions to run only if books is not empty.

books = [1]

def book_decorator(func):
    def inner(*args, **kwargs):
        if len(books) != 0:
            func(*args, **kwargs)
    return inner


# 3 Write a decorator called printer which causes any decorated function to print their return values. 
# If the return value of a given function is None, printer should do nothing.

def printer_decorator(func):
    def inner(*args, **kwargs):
        returned = func(*args, **kwargs)
        if returned != None:
            print(returned)
    return inner



@timeit_decorator
def gen1000Double():
    x = [num * 2 for num in range(1000)]
    return

@timeit_decorator
def gen1000Expon():
    z = [num ** 2 for num in range(1000)]
    return

@timeit_decorator
def gen1000Addition():
    y = [num + 2 for num in range(1000)]
    return


@book_decorator
def hola():
    print("Hola, Amigos!")


@printer_decorator
def sum(*args):
    sum = 0
    for num in args:
        sum += num
    #print(sum)
    return sum


#hola = example_decorator(hola)


#hola()
#sum(1, 2, 3, 4, 5, 6, 10)
gen1000Double()
gen1000Expon()
gen1000Addition()

hola()
sum(1, 2, 3, 4, 5, 6)

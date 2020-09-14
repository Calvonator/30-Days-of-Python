from time import perf_counter


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
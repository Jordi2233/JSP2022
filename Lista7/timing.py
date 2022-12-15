from time import perf_counter


def timing(func):
    def wrapper(*args):
        start = perf_counter()
        result = func(*args)
        end = perf_counter()
        print(f"Function {func.__name__} took {(end - start):0.10} seconds")
        return result

    return wrapper

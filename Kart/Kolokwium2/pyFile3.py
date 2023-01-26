# main.py
from os import system
import random
import time
import sortowanie


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Time taken to execute the {func.__name__}: {end_time - start_time} ns")
        return result
    return wrapper


def main():
    system('clear')
    random_list = [random.randint(0, 1000) for _ in range(1000)]

    sorted_list_bubble = measure_time(sortowanie.bubble_sort)
    sorted_list_bubble(random_list)

    sorted_list_insertion = measure_time(sortowanie.insertion_sort)
    sorted_list_insertion(random_list)


if __name__ == "__main__":
    main()

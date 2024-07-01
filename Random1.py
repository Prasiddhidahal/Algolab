import random
import time

def generate_random_numbers(n):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(1, 10000))
    return numbers

def linear_search(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

def calculate_time_complexity(numbers, target):
    start_time = time.perf_counter()
    index = linear_search(numbers, target)
    end_time = time.perf_counter()
    time_complexity = end_time - start_time
    return time_complexity, index

sizes = [100, 1000, 10000, 100000]
target_best_case = 1
target_worst_case = 10000

for n in sizes:
    random_numbers = generate_random_numbers(n)

    # Best case
    random_numbers[0] = target_best_case
    time_complexity, index = calculate_time_complexity(random_numbers, target_best_case)
    print(f"Best case time complexity for n={n}: {time_complexity}, found at index {index}")

    # Worst case
    random_numbers[-1] = target_worst_case
    time_complexity, index = calculate_time_complexity(random_numbers, target_worst_case)
    print(f"Worst case time complexity for n={n}: {time_complexity}, found at index {index}")
import random
import time

def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] < target:
            low = mid + 1
        elif numbers[mid] > target:
            high = mid - 1
        else:
            return mid  
    return -1 

def calculate_time_complexity(numbers, target):
    start_time = time.perf_counter()
    index = binary_search(numbers, target)
    end_time = time.perf_counter()
    time_complexity = end_time - start_time
    return time_complexity, index

sizes = [100, 1000, 10000, 100000]
target_best_case = 1
target_worst_case = 10000

for n in sizes:
    random_numbers = [random.randint(1, 100) for _ in range(n)]
    sorted_numbers = sorted(random_numbers) 

    # Best case
    sorted_numbers[0] = target_best_case
    time_complexity, index = calculate_time_complexity(sorted_numbers, target_best_case)
    print(f"Best case time complexity for n={n}: {time_complexity}, found at index {index}")

    # Worst case
    sorted_numbers[-1] = target_worst_case
    time_complexity, index = calculate_time_complexity(sorted_numbers, target_worst_case)
    print(f"Worst case time complexity for n={n}: {time_complexity}, found at index {index}")
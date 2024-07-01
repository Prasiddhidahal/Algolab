import time
import random
import matplotlib.pyplot as plt

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def timed_sort(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr, 0, len(arr) - 1)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000000  # Converting to microseconds
    return arr, execution_time

sizes = [100, 200, 300, 400, 500]
best_case_times = []
worst_case_times = []
average_case_times = []
num_runs = 5

for size in sizes:
    best_case_avg = 0
    worst_case_avg = 0
    average_case_avg = 0
    
    for _ in range(num_runs):
        # Best case sorted
        best_case = sorted([random.randint(1, size) for _ in range(size)])
        _, time_taken = timed_sort(quicksort, best_case)
        best_case_avg += time_taken

        # Worst case reverse sorted
        worst_case = sorted([random.randint(1, size) for _ in range(size)], reverse=True)
        _, time_taken = timed_sort(quicksort, worst_case)
        worst_case_avg += time_taken

        # Average case
        average_case = [random.randint(1, size) for _ in range(size)]
        _, time_taken = timed_sort(quicksort, average_case)
        average_case_avg += time_taken

    best_case_times.append(best_case_avg / num_runs)
    worst_case_times.append(worst_case_avg / num_runs)
    average_case_times.append(average_case_avg / num_runs)

plt.plot(sizes, best_case_times, label='Best Case')
plt.plot(sizes, worst_case_times, label='Worst Case')
plt.plot(sizes, average_case_times, label='Average Case')
plt.ylabel('Time taken (in microseconds)')
plt.xlabel('Input size')
plt.title('Time complexity of Quicksort')
plt.legend()
plt.show()

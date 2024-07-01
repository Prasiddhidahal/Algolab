import time
import random
import matplotlib.pyplot as plt

def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

sizes = [100, 500, 1000, 5000, 10000]
insertion_sort_times = []
merge_sort_times = []
selection_sort_times = []
quick_sort_times = []

for size in sizes:
    random_list = generate_random_list(size)
    
    start_time = time.time()
    insertion_sort(random_list[:])
    insertion_sort_times.append(time.time() - start_time)
    
    start_time = time.time()
    merge_sort(random_list[:])
    merge_sort_times.append(time.time() - start_time)
    
    start_time = time.time()
    selection_sort(random_list[:])
    selection_sort_times.append(time.time() - start_time)
    
    random_list_for_quick_sort = random_list[:]  # Make a copy for fair comparison
    start_time = time.time()
    quick_sort(random_list_for_quick_sort)  # Quick Sort returns a new list
    quick_sort_times.append(time.time() - start_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_sort_times, label="Insertion Sort")
plt.plot(sizes, merge_sort_times, label="Merge Sort")
plt.plot(sizes, selection_sort_times, label="Selection Sort")
plt.plot(sizes, quick_sort_times, label="Quick Sort")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (s)")
plt.title("Sorting Algorithm Execution Time Comparison")
plt.legend()
plt.grid(True)
plt.show()

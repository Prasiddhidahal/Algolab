import time
import random

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Quick sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def timed_sort(sort_function, arr):
    start_time = time.perf_counter()
    sorted_arr = sort_function(arr)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000000  # Converting to microseconds
    return sorted_arr, execution_time


my_list = [random.randint(1, 100) for _ in range(1000)]  # Generating a list of 1000 random numbers between 1 and 100

sorted_list, time_taken = timed_sort(insertion_sort, my_list.copy())
print("Insertion sort - Time taken (in microseconds):", time_taken)

sorted_list, time_taken = timed_sort(quicksort, my_list.copy())
print("Quick sort - Time taken (in microseconds):", time_taken)

sorted_list, time_taken = timed_sort(merge_sort, my_list.copy())
print("Merge sort - Time taken (in microseconds):", time_taken)

sorted_list, time_taken = timed_sort(selection_sort, my_list.copy())
print("Selection sort - Time taken (in microseconds):", time_taken)
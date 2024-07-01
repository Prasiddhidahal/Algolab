def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr




def test_selection_sort():
    test_cases = [
        [3, 6, 8, 10, 1, 2, 1],
        [],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]
    
    for arr in test_cases:
        print("Original:", arr)
        sorted_arr = selection_sort(arr[:])
        print("Selection Sort:", sorted_arr)
        assert sorted_arr == sorted(arr), f"Failed for {arr}"
    print("Selection Sort passed all test cases!")

test_selection_sort()

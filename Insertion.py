#time complexity of insertion sort is  O(n^2) and best is 0(n)




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr


def test_insertion_sort():
    test_cases = [
        [3, 6, 8, 10, 1, 2, 1],
        [],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]
    
    for arr in test_cases:
        print("Original:", arr)
        sorted_arr = insertion_sort(arr[:])
        print("Insertion Sort:", sorted_arr)
        assert sorted_arr == sorted(arr), f"Failed for {arr}"
    print("Insertion Sort passed all test cases!")

test_insertion_sort()

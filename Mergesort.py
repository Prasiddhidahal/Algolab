import unittest


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


class SortTestCase(unittest.TestCase):
    def test_merge_sort(self):
        A = [10, 15, 5, 25, 30, 20]
        B = [5, 10, 15, 20, 25, 30]
        W = [30, 25, 20, 15, 10, 5]

        sortList = [5, 10, 15, 20, 25, 30]

        merge_sort(A)
        merge_sort(B)
        merge_sort(W)

        self.assertListEqual(A, sortList)
        self.assertListEqual(B, sortList)
        self.assertListEqual(W, sortList)

if __name__ == '__main__':
    unittest.main()
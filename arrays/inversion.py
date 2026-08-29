"""
Count Inversions

An inversion is a pair of indices (i, j) such that:
    i < j and arr[i] > arr[j]

Count the total number of inversions in an array.

Striver A2Z - Step 3: Arrays

Key idea:
Use merge sort. During merging, both halves are already sorted.

When arr1[i] > arr2[j], every remaining element from arr1[i] onward
is also greater than arr2[j]. Therefore, all of them form inversions
with arr2[j]:

    len(arr1) - i

The total count is:
    left_count + right_count + merge_count

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge(arr1, arr2):
    i = 0
    j = 0
    new_arr = []
    count = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
            count += len(arr1) - i

    new_arr.extend(arr1[i:])
    new_arr.extend(arr2[j:])

    return new_arr, count


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, left_count = mergeSort(arr[:mid])
    right, right_count = mergeSort(arr[mid:])

    merged, count = merge(left, right)
    total_count = left_count + right_count + count

    return merged, total_count


def inversion(arr):
    return mergeSort(arr)[1]


if __name__ == "__main__":
    print(inversion([5, 3, 2, 1]))
    # 6

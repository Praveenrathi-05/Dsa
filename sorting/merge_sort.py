"""
Merge Sort
Sort an array using the Divide and Conquer technique.

Striver A2Z - Step 2: Sorting Techniques

Key idea:
- Divide the array into two halves.
- Recursively sort both halves.
- Merge the sorted halves into one sorted array.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge(arr1, arr2):
    new_arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    new_arr.extend(arr1[i:])
    new_arr.extend(arr2[j:])

    return new_arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    return merge(
        mergeSort(arr[:mid]),
        mergeSort(arr[mid:])
    )


if __name__ == "__main__":
    arr = [6, 5, 4, 3, 2, 1]
    print(mergeSort(arr))
    # [1, 2, 3, 4, 5, 6]
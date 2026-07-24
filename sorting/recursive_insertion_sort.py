"""
Recursive Insertion Sort
Sort an array recursively using Insertion Sort.

Striver A2Z - Step 2: Sorting Techniques

Key idea:
- Recursively sort the first n-1 elements.
- Insert the last element into its correct position.

Time Complexity: O(n²)
Space Complexity: O(n) (recursive stack)
"""

def insertionSortRecursive(arr, n):
    if n <= 1:
        return arr

    insertionSortRecursive(arr, n - 1)

    key = arr[n - 1]
    j = n - 1

    while j > 0:
        if key < arr[j - 1]:
            arr[j] = arr[j - 1]
        else:
            break
        j -= 1

    arr[j] = key

    return arr


if __name__ == "__main__":
    arr = [5, 6, 4, 3, 2, 1]
    print(insertionSortRecursive(arr, len(arr)))
    # [1, 2, 3, 4, 5, 6]
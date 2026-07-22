"""
Selection Sort
Sort an array by repeatedly selecting the smallest element from the
unsorted portion and placing it at its correct position.

Striver A2Z - Step 2: Sorting Techniques

Key idea:
- Find the minimum element in the unsorted part.
- Swap it with the first unsorted position.
- Repeat until the array is sorted.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

def selectionSort(arr):
    for i in range(len(arr) - 1):
        index = i + 1

        for j in range(index + 1, len(arr)):
            if arr[index] > arr[j]:
                index = j

        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]

    return arr


if __name__ == "__main__":
    print(selectionSort([5, 4, 2, 1]))
    # [1, 2, 4, 5]
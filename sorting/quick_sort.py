"""
Quick Sort
Sort an array using the Divide and Conquer technique.

Striver A2Z - Step 2: Sorting Techniques

Key idea:
- Choose a pivot (last element here).
- Partition the array into smaller and larger elements.
- Recursively sort both partitions.

Time Complexity:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n²)

Space Complexity:
- Average: O(log n)
- Worst: O(n)
"""

def partition(arr, low, high):
    i = low - 1

    for j in range(low, high):
        if arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quickSort(arr, low, high):
    if low >= high:
        return arr

    pivot = partition(arr, low, high)

    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot + 1, high)

    return arr


if __name__ == "__main__":
    arr = [5, 6, 4, 3, 2, 1]
    print(quickSort(arr, 0, len(arr) - 1))
    # [1, 2, 3, 4, 5, 6]
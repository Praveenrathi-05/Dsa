"""
Recursive Bubble Sort
Sort an array recursively using Bubble Sort.

Striver A2Z - Step 2: Sorting Techniques

Key idea:
- One recursive call places the largest element at the end.
- Reduce the problem size by one and repeat.

Time Complexity: O(n²)
Space Complexity: O(n) (recursive stack)
"""

def bubbleSortRecursive(arr, n):
    if n <= 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return bubbleSortRecursive(arr, n - 1)


if __name__ == "__main__":
    arr = [6, 5, 4, 3, 2, 1]
    print(bubbleSortRecursive(arr, len(arr)))
    # [1, 2, 3, 4, 5, 6]
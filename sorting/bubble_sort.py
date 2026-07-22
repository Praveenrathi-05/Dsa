"""
Bubble Sort
Sort an array by repeatedly swapping adjacent elements if they are
in the wrong order.

Striver A2Z - Step 2: Sorting Techniques

Key idea:
- Compare adjacent elements.
- Swap if left element is greater.
- Largest element "bubbles" to the end after each pass.
- Stop early if no swaps occur.

Time Complexity:
- Best: O(n)
- Average: O(n²)
- Worst: O(n²)

Space Complexity: O(1)
"""

def bubbleSort(arr):
    for j in range(len(arr)):
        swapped = False

        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    print(bubbleSort([5, 4, 3, 2, 1]))
    # [1, 2, 3, 4, 5]
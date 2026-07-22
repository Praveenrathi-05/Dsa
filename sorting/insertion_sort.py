"""
Insertion Sort
Sort an array by building a sorted portion one element at a time.

Striver A2Z - Step 2: Sorting Techniques

Key idea:
- Pick the current element.
- Shift larger elements one position to the right.
- Insert the current element into its correct position.

Time Complexity:
- Best: O(n)
- Average: O(n²)
- Worst: O(n²)

Space Complexity: O(1)
"""

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i

        while j > 0:
            if key < arr[j - 1]:
                arr[j] = arr[j - 1]
            else:
                break

            j -= 1

        arr[j] = key

    return arr


if __name__ == "__main__":
    print(insertionSort([5, 4, 3, 2, 1]))
    # [1, 2, 3, 4, 5]
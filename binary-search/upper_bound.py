"""
Upper Bound

Find the first index in a sorted array where the element is strictly
greater than target.

Striver A2Z - Binary Search

Definition:
    upper_bound = first index i such that arr[i] > target

If no such element exists, return len(arr).

Key idea:
Use binary search.

If arr[mid] > target:
    mid could be the answer, so save mid and search left.

If arr[mid] <= target:
    mid cannot be the answer, so search right.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def upper_bound(arr, target):
    low = 0
    high = len(arr) - 1
    answer = len(arr)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


if __name__ == "__main__":
    print(upper_bound([4, 4, 4], 3))

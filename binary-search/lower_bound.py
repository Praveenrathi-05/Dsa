"""
Lower Bound

Find the first index in a sorted array where the element is greater
than or equal to num.

Striver A2Z - Binary Search

Definition:
    lower_bound = first index i such that arr[i] >= num

If no such element exists, return len(arr).

Key idea:
Use binary search.

If arr[mid] >= num:
    mid could be the answer, so save mid and search the left half.

If arr[mid] < num:
    mid cannot be the answer, so search the right half.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def lower_bound(arr, num):
    start = 0
    end = len(arr) - 1
    answer = len(arr)

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= num:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer


if __name__ == "__main__":
    print(lower_bound([2, 3, 5, 7, 7, 9], 6))

"""
Search Insert Position (LeetCode #35)

Given a sorted array and a target, return its index if found. Otherwise,
return the index where it should be inserted to keep the array sorted.

Striver A2Z - Binary Search

Key idea:
This is essentially a lower-bound problem: find the first index where
nums[index] >= target.

If nums[mid] >= target, save mid and search left.
If nums[mid] < target, search right.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search_insert(nums, target):
    start = 0
    end = len(nums) - 1
    answer = len(nums)

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] >= target:
            end = mid - 1
            answer = mid
        elif nums[mid] < target:
            start = mid + 1

    return answer


if __name__ == "__main__":
    print(search_insert([1, 3, 5, 6, 9], 8))

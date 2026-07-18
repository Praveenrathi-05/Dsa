"""
LeetCode #704 - Binary Search
Given a sorted array and a target, return the target's index, or -1
if it's not present.
Pattern: Binary Search (eliminate half the space each step)
"""

def search(nums, target):
    start, end = 0, len(nums) - 1
    while end >= start:
        mid = (start + end) // 2
        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    print(search([1, 3, 5, 7, 9], 5))   # 2
    print(search([1, 2], 3))            # -1 (must terminate, not hang)
    print(search([], 5))                # -1

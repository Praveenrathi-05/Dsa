"""
LeetCode #167 - Two Sum II (Input Array Is Sorted)
Same as Two Sum, but the array is sorted and answer is 1-indexed.
Pattern: Two Pointers (opposite ends, closing inward)
"""

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while right >= left:
        total = numbers[left] + numbers[right]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            return [left + 1, right + 1]
    return -1

if __name__ == "__main__":
    print(twoSum([1, 3, 4, 6, 10], 10))  # [3, 4]
    print(twoSum([2, 7, 11, 15], 9))     # [1, 2]

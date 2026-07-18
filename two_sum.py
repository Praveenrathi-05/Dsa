"""
LeetCode #1 - Two Sum
Given an array of integers and a target, return the indices of the two
numbers that add up to target.
Pattern: Arrays & Hashing (instant lookup via dictionary)
"""
 
def twoSum(nums, target):
    seen = {}  # value -> index
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [i, seen[complement]]
        seen[nums[i]] = i
 
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(twoSum([3, 2, 4], 6))       # [1, 2]
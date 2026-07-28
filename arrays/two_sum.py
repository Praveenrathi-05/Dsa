"""
Two Sum (LeetCode #1)

Return indices of two numbers that add up to the target.

Striver A2Z - Step 2: Arrays

Key idea:
Store visited numbers in a hash map and search for the complement.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        if target-num in seen:
            return [seen[target-num],i]
        seen[num]=i
    return []

if __name__=="__main__":
    print(two_sum([1,5,3,3],6))

"""
Single Number (LeetCode #136)

Every element appears twice except one.

Striver A2Z - Step 2: Arrays

Key idea:
XOR cancels duplicate numbers, leaving only the unique value.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def single_number(nums):
    ans=0
    for x in nums:
        ans^=x
    return ans

if __name__=="__main__":
    print(single_number([4,1,2,1,2]))

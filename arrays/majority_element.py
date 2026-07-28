"""
Majority Element (LeetCode #169)

Find the element appearing more than n/2 times.

Striver A2Z - Step 2: Arrays

Key idea:
Moore's Voting Algorithm repeatedly cancels different values.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def majority_element(nums):
    candidate=None
    count=0
    for num in nums:
        if count==0:
            candidate=num
            count=1
        elif num==candidate:
            count+=1
        else:
            count-=1
    return candidate

if __name__=="__main__":
    print(majority_element([2,2,1,1,1,2,2]))

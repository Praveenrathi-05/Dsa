"""
Rearrange Array Elements by Sign (LeetCode #2149)

Given an array with an equal number of positive and negative integers,
rearrange it so that positive and negative numbers appear alternately
while preserving their relative order.

Striver A2Z - Step 2: Arrays

Key idea:
Maintain two indices in the output array:
- Even indices for positive numbers.
- Odd indices for negative numbers.
Scan the input once and place each element at its next available
position.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def rearrange_elements_by_sign(nums):
    pos_index=0
    neg_index=1
    result=[0]*len(nums)

    for i in range(len(nums)):
        if nums[i]>0:
            result[pos_index]=nums[i]
            pos_index+=2
        else:
            result[neg_index]=nums[i]
            neg_index+=2

    return result

if __name__=="__main__":
    print(rearrange_elements_by_sign([3,1,-2,-5,2,-4]))
    # [3, -2, 1, -5, 2, -4]

"""
Sort Array of 0s and 2s

Sort an array containing only 0 and 2.

Striver A2Z - Step 2: Arrays

Key idea:
Two pointers swap misplaced values.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def sort_zero_and_two(nums):
    low,high=0,len(nums)-1
    while low<=high:
        if nums[low]==0:
            low+=1
        elif nums[high]==2:
            high-=1
        else:
            nums[low],nums[high]=nums[high],nums[low]
            low+=1
            high-=1
    return nums

if __name__=="__main__":
    print(sort_zero_and_two([2,2,0,0,2]))

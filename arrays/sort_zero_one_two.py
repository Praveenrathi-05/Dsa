"""
Sort Colors (LeetCode #75)

Sort an array containing only 0, 1 and 2.

Striver A2Z - Step 2: Arrays

Key idea:
Dutch National Flag algorithm.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def sort_zero_one_two(nums):
    low=mid=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1; mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

if __name__=="__main__":
    print(sort_zero_one_two([2,0,2,1,1,0]))

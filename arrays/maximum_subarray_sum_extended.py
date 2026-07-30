"""
Maximum Subarray (Kadane's Algorithm) - Extended (LeetCode #53)

Return the actual maximum-sum contiguous subarray.

Striver A2Z - Step 2: Arrays

Key idea:
Maintain a running sum. Reset it whenever it becomes negative and keep
track of the start and end indices of the best subarray.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maximum_subarray_sum_extended(nums):
    max_sum=float("-inf")
    current_sum=0
    start=0
    best_start=0
    best_end=0
    for i,num in enumerate(nums):
        current_sum+=num
        if current_sum>max_sum:
            max_sum=current_sum
            best_start=start
            best_end=i
        if current_sum<0:
            current_sum=0
            start=i+1
    return nums[best_start:best_end+1]

if __name__=="__main__":
    print(maximum_subarray_sum_extended([-2,1,-3,4,-1,2,1,-5,4]))
    print(maximum_subarray_sum_extended([-3,-1,-2]))

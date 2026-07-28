"""
Longest Subarray with Sum K (GeeksforGeeks)

Find the length of the longest subarray whose sum equals k.

Striver A2Z - Step 2: Arrays

Key idea:
Use prefix sums and store the first occurrence of each prefix sum.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def longest_subarray_with_sum_k(nums,k):
    max_len=0
    running_total=0
    notebook={0:-1}
    for i,num in enumerate(nums):
        running_total+=num
        if running_total-k in notebook:
            max_len=max(max_len,i-notebook[running_total-k])
        if running_total not in notebook:
            notebook[running_total]=i
    return max_len

if __name__=="__main__":
    print(longest_subarray_with_sum_k([10,5,2,7,1,-10],15))

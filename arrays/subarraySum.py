"""
Subarray Sum Equals K (LeetCode #560)

Count all subarrays whose sum equals k.

Striver A2Z - Step 2: Arrays

Key idea:
Store frequencies of prefix sums in a hash map.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def subarraySum(nums,k):
    notebook={0:1}
    running_total=0
    count=0
    for num in nums:
        running_total+=num
        count+=notebook.get(running_total-k,0)
        notebook[running_total]=notebook.get(running_total,0)+1
    return count

if __name__=="__main__":
    print(subarraySum([-1,1,0],0))

"""
Subarray Sum Equals K (LeetCode #560)

Given an integer array nums and an integer k, return the total number
of continuous subarrays whose sum equals k.

Striver A2Z - Step 2: Arrays

Key idea:
Use a prefix sum and a hash map to store how many times each prefix
sum has appeared.

At every element:
1. Add the element to the running total.
2. Calculate previous_total = running_total - k.
3. If previous_total exists in the notebook, every occurrence represents
   one subarray ending at the current index whose sum is k.
4. Store the current running total and increase its frequency.

The frequency is important because the same prefix sum can occur
multiple times, and each occurrence can produce a different valid
subarray.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def subarray_with_given_sum(nums, k):
    notebook = {0: 1}
    count = 0
    running_total = 0

    for i in range(len(nums)):
        running_total += nums[i]
        previous_total = running_total - k

        if previous_total in notebook:
            count += notebook[previous_total]

        notebook[running_total] = notebook.get(running_total, 0) + 1

    return count


if __name__ == "__main__":
    print(subarray_with_given_sum([1, 2, 3], 3))  # 2

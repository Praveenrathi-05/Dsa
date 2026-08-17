"""
Largest Subarray with 0 Sum (GeeksforGeeks)

Given an integer array, find the length of the longest contiguous
subarray whose elements add up to zero.

Striver A2Z - Step 3: Arrays

Key idea:
Use a prefix sum and a hash map to remember the first index where each
prefix sum appeared.

If the same prefix sum appears again at index i, the elements between
the first occurrence + 1 and i must sum to zero.

We store only the FIRST occurrence of each prefix sum because an earlier
index gives the longest possible subarray when the same sum appears
again.

The initial entry {0: -1} handles a zero-sum subarray that starts at
index 0.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def largest_subarray_with_zero_sum(nums):
    notebook = {0: -1}
    max_length = 0
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum in notebook:
            length = i - notebook[current_sum]

            if length > max_length:
                max_length = length
        else:
            notebook[current_sum] = i

    return max_length


if __name__ == "__main__":
    print(largest_subarray_with_zero_sum(
        [15, -2, 2, -8, 1, 7, 10, 23]
    ))
    # 5

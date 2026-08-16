"""
4Sum (LeetCode #18)

Given an integer array nums and an integer target, return all unique
quadruplets whose sum equals target.

Striver A2Z - Step 2: Arrays

Key idea:
1. Sort the array.
2. Fix the first number using i.
3. Fix the second number using j.
4. Use two pointers, left and right, for the remaining two numbers.
5. Move right left when the sum is too large.
6. Move left right when the sum is too small.
7. When the sum equals target, store the quadruplet and move both
   pointers.
8. Skip duplicates for i, j, left, and right.

The duplicate check for j is relative to the current i:
    j > i + 1 and nums[j] == nums[j - 1]

This prevents duplicate quadruplets without incorrectly skipping a
valid j when a new i value is being considered.

Time Complexity: O(n³)
Space Complexity: O(1) auxiliary space, excluding the output.
"""

def four_sum(nums, target):
    quad_pairs = []
    nums.sort()

    for i in range(len(nums) - 3):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):

            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = len(nums) - 1

            while right > left:
                number = nums[j] + nums[i] + nums[right] + nums[left]

                if number > target:
                    right -= 1

                elif number < target:
                    left += 1

                else:
                    quad_pairs.append([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right]
                    ])

                    right -= 1
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

    return quad_pairs


if __name__ == "__main__":
    print(four_sum([1, 0, -1, 0, -2, 2], 0))
    # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

"""
3Sum (LeetCode #15)

Given an integer array nums, return all unique triplets whose sum is 0.

Striver A2Z - Step 2: Arrays

Key idea:
1. Sort the array.
2. Fix one element at index i.
3. Use two pointers, left and right, to find the other two elements.
4. If the sum is too large, move right left.
5. If the sum is too small, move left right.
6. When the sum is zero, store the triplet and move both pointers.
7. Skip duplicate values to avoid duplicate triplets.

Because the array is sorted, if nums[i] becomes positive, we can stop:
the remaining numbers cannot produce a sum of zero.

Time Complexity: O(n²)
Space Complexity: O(n) for the sorted copy created by sorted(nums).
"""

def three_sum(nums):
    triplet_pairs = []
    nums = sorted(nums)

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        if nums[i] > 0:
            break

        left = i + 1
        right = len(nums) - 1

        while right > left:
            number = nums[i] + nums[right] + nums[left]

            if number > 0:
                right -= 1
            elif number < 0:
                left += 1
            else:
                triplet_pairs.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return triplet_pairs


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    # [[-1, -1, 2], [-1, 0, 1]]

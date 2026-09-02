"""
Find First and Last Position of Element in Sorted Array (LeetCode #34)

Given a sorted array nums and a target value, find the starting and
ending position of the target.

If the target is not present, return [-1, -1].

Striver A2Z - Binary Search

Example:

    nums = [5, 7, 7, 8, 8, 10]
    target = 8

Answer:

    [3, 4]


Key Idea
--------

We need to find TWO things:

1. The FIRST occurrence of target.
2. The LAST occurrence of target.

We can use binary search for both.

--------------------------------------------------
1. Find First Occurrence
--------------------------------------------------

We want the smallest index where:

    nums[index] >= target

If:

    nums[mid] >= target

then mid could be the first occurrence.

So:

    start = mid
    high = mid - 1

We move LEFT because there might be another target earlier.

If:

    nums[mid] < target

then target must be somewhere to the RIGHT.

So:

    low = mid + 1


--------------------------------------------------
2. Find Last Occurrence
--------------------------------------------------

We want the largest index where:

    nums[index] <= target

If:

    nums[mid] <= target

then mid could be the last occurrence.

So:

    end = mid
    low = mid + 1

We move RIGHT because there might be another target later.

If:

    nums[mid] > target

then target must be somewhere to the LEFT.

So:

    high = mid - 1


--------------------------------------------------
Why do we need two binary searches?
--------------------------------------------------

Normal binary search stops as soon as it finds the target.

But here we don't just want to know whether the target exists.

We want:

    FIRST target
    LAST target

For example:

    [5, 7, 7, 8, 8, 8, 10]
              ↑     ↑
            first  last

The answer is:

    [3, 5]


--------------------------------------------------
Important Check
--------------------------------------------------

After finding the first occurrence, we check:

    if start == len(nums) or nums[start] != target:

This means the target does not exist.

In that case, return:

    [-1, -1]


--------------------------------------------------
Time Complexity
--------------------------------------------------

First binary search:

    O(log n)

Second binary search:

    O(log n)

Together:

    O(log n) + O(log n)
    = O(log n)


Space Complexity:

    O(1)

We only use a few variables.
"""


def search_range(nums, target):

    low = 0
    high = len(nums) - 1

    # -----------------------------------------
    # Find first occurrence
    # -----------------------------------------

    start = len(nums)

    while low <= high:

        mid = (low + high) // 2

        if nums[mid] >= target:

            # mid could be the first occurrence
            start = mid

            # Search further left
            high = mid - 1

        else:

            # target must be on the right
            low = mid + 1

    # -----------------------------------------
    # Check if target actually exists
    # -----------------------------------------

    if start == len(nums) or nums[start] != target:
        return [-1, -1]

    # -----------------------------------------
    # Find last occurrence
    # -----------------------------------------

    low = 0
    high = len(nums) - 1

    end = -1

    while low <= high:

        mid = (low + high) // 2

        if nums[mid] <= target:

            # mid could be the last occurrence
            end = mid

            # Search further right
            low = mid + 1

        else:

            # target must be on the left
            high = mid - 1

    return [start, end]


# --------------------------------------------------
# Test Cases
# --------------------------------------------------

if __name__ == "__main__":

    print(search_range([1], 1))
    # [0, 0]

    print(search_range([5, 7, 7, 8, 8, 10], 8))
    # [3, 4]

    print(search_range([5, 7, 7, 8, 8, 10], 6))
    # [-1, -1]

    print(search_range([2, 2, 2, 2, 2], 2))
    # [0, 4]
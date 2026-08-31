"""
Reverse Pairs (LeetCode #493)

Given an integer array nums, count the number of important reverse pairs
(i, j) where:

    i < j
    nums[i] > 2 * nums[j]

Striver A2Z - Step 3: Arrays

Key idea:
Use merge sort.

After recursively sorting the left and right halves, both halves are
sorted. During the merge step, count cross-half reverse pairs before
actually merging the two halves.

For a value arr2[j] in the right half, if:

    arr1[i] > 2 * arr2[j]

then every remaining element from arr1[i] onward is also greater than
2 * arr2[j], because arr1 is sorted.

Therefore, we can add:

    len(arr1) - i

to the reverse-pair count.

After counting reverse pairs, perform the normal merge operation so the
combined array remains sorted for the next level of merge sort.

Important:
The condition is strictly greater than:

    arr1[i] > 2 * arr2[j]

not greater than or equal to.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


def merge(arr1, arr2):

    i = 0
    j = 0
    new_arr = []
    reverse_count = 0

    # -----------------------------------------
    # Step 1: Count reverse pairs
    # -----------------------------------------

    while i < len(arr1) and j < len(arr2):

        if arr1[i] > 2 * arr2[j]:

            reverse_count += len(arr1) - i

            j += 1

        else:
            i += 1

    # -----------------------------------------
    # Step 2: Normal merge
    # -----------------------------------------

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j]:

            new_arr.append(arr1[i])
            i += 1

        else:

            new_arr.append(arr2[j])
            j += 1

    # Add remaining elements
    new_arr.extend(arr1[i:])
    new_arr.extend(arr2[j:])

    return new_arr, reverse_count


def mergeSort(arr):

    # Base case
    if len(arr) <= 1:
        return arr, 0

    # Find middle
    mid = len(arr) // 2

    # Sort left half
    left, left_count = mergeSort(arr[:mid])

    # Sort right half
    right, right_count = mergeSort(arr[mid:])

    # Merge the two sorted halves
    merged, count = merge(left, right)

    # Total reverse pairs
    total_count = left_count + right_count + count

    return merged, total_count


def reverse_pairs(arr):

    return mergeSort(arr)[1]


# Example
print(reverse_pairs([2, 4, 3, 5, 1]))
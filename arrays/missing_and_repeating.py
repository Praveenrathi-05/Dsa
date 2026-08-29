"""
Find the Missing and Repeating Number

Given an array of size n containing numbers from 1 to n, one number is
missing and one number appears twice. Find both numbers.

Striver A2Z - Step 3: Arrays

Key idea:
Use the difference between the expected and actual sums to get:
    missing - repeated

Also calculate the difference between expected and actual square sums:
    missing² - repeated²

Using:
    a² - b² = (a - b)(a + b)

we can find missing + repeated and then solve for both numbers.

Time Complexity: O(n)
Space Complexity: O(n) because the squared list is created.
"""

def missing_and_repeating(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    sum_diff = expected_sum - actual_sum

    expected_square_sum = n * (n + 1) * (2 * n + 1) // 6
    actual_square_sum = sum([num * num for num in nums])
    square_diff = expected_square_sum - actual_square_sum

    total = square_diff // sum_diff
    missing = (total + sum_diff) // 2
    repeated = missing - sum_diff

    return missing, repeated


if __name__ == "__main__":
    print(missing_and_repeating([1, 2, 2, 4, 5]))
    # (3, 2)

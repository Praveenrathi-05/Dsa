"""
Striver A2Z - Basic Maths

This file contains fundamental mathematical problems from the
Striver A2Z DSA Sheet.

Problems covered:

1. Count Digits
2. Reverse a Number
3. Check Palindrome
4. Check Armstrong Number
5. Find All Divisors
6. Check Prime Number
7. GCD / HCF using Euclidean Algorithm

These problems build understanding of:
- Digit extraction
- Integer division and modulo
- Square-root optimization
- Divisors
- Prime numbers
- Euclidean Algorithm
"""


# --------------------------------------------------
# 1. Count Digits
# --------------------------------------------------

def count_digits(n):
    """
    Count the number of digits in a positive integer.

    Example:

        n = 12345

        12345 -> 1234 -> 123 -> 12 -> 1 -> 0

    We repeatedly remove the last digit using:

        n // 10

    Every removal represents one digit.

    Example:
        count_digits(12345) -> 5

    Time Complexity: O(log10(n))
    Space Complexity: O(1)
    """

    count = 0

    while n > 0:

        n = n // 10

        count += 1

    return count


# --------------------------------------------------
# 2. Reverse a Number
# --------------------------------------------------

def reverse_number(n):
    """
    Reverse the digits of a positive integer.

    Example:

        n = 1234

    Step-by-step:

        rev = 0

        digit = 4
        rev = 0 * 10 + 4
            = 4

        digit = 3
        rev = 4 * 10 + 3
            = 43

        digit = 2
        rev = 43 * 10 + 2
            = 432

        digit = 1
        rev = 432 * 10 + 1
            = 4321

    Result:

        4321

    Time Complexity: O(log10(n))
    Space Complexity: O(1)
    """

    rev_num = 0

    while n > 0:

        last_digit = n % 10

        n //= 10

        rev_num = (rev_num * 10) + last_digit

    return rev_num


# --------------------------------------------------
# 3. Check Palindrome Number
# --------------------------------------------------

def is_number_palindrome(n):
    """
    Check whether a number is a palindrome.

    A palindrome reads the same forwards and backwards.

    Examples:

        121 -> True
        1331 -> True
        123 -> False

    We reverse the number and compare it with the original.

        original == reversed

    Time Complexity: O(log10(n))
    Space Complexity: O(1)
    """

    return n == reverse_number(n)


# --------------------------------------------------
# 4. Check Armstrong Number
# --------------------------------------------------

def is_armstrong_number(n):
    """
    Check whether a number is an Armstrong number.

    An Armstrong number is a number where:

        sum(each digit ** number_of_digits) == original number

    Example:

        153

    Number of digits:

        3

    Therefore:

        1³ + 5³ + 3³

        = 1 + 125 + 27

        = 153

    So 153 is an Armstrong number.

    Another example:

        1634

        1⁴ + 6⁴ + 3⁴ + 4⁴
        = 1634

    Time Complexity: O(log10(n))
    Space Complexity: O(1)
    """

    digits = count_digits(n)

    original_number = n

    result = 0

    while n > 0:

        last_digit = n % 10

        n //= 10

        result += last_digit ** digits

    return result == original_number


# --------------------------------------------------
# 5. Find All Divisors
# --------------------------------------------------

def all_divisors(n):
    """
    Return all divisors of n in sorted order.

    Instead of checking every number from:

        1 to n

    we only check up to:

        sqrt(n)

    Why?

    Divisors occur in pairs.

    Example:

        n = 36

        1 * 36
        2 * 18
        3 * 12
        4 * 9
        6 * 6

    If i divides n, then:

        i

    and:

        n // i

    are both divisors.

    Example:

        i = 4

        36 // 4 = 9

    Therefore:

        4 and 9

    are both divisors.

    Time Complexity:
        O(sqrt(n)) for finding divisors,
        plus sorting the collected divisors.

    Space Complexity:
        O(number of divisors)
    """

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)

            # Avoid adding the square root twice.
            if (n // i) != i:

                divisors.append(n // i)

    return sorted(divisors)


# --------------------------------------------------
# 6. Check Prime Number
# --------------------------------------------------

def is_prime_number(n):
    """
    Check whether n is a prime number.

    A prime number has exactly two positive divisors:

        1 and itself

    Examples:

        2  -> Prime
        7  -> Prime
        11 -> Prime
        12 -> Not Prime

    We only need to check possible divisors up to sqrt(n).

    Why?

    If n has a divisor larger than sqrt(n), it must have a
    corresponding divisor smaller than sqrt(n).

    Example:

        36 = 4 * 9

    If we find 4, we already know that 9 exists.

    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """

    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True


# --------------------------------------------------
# 7. GCD / HCF - Euclidean Algorithm
# --------------------------------------------------

def gcd(n1, n2):
    """
    Find the Greatest Common Divisor (GCD) of two numbers.

    GCD is also called HCF:
        Highest Common Factor

    This implementation uses the Euclidean Algorithm.

    Main mathematical idea:

        gcd(a, b) = gcd(b, a % b)

    We repeatedly replace:

        n1 -> n2
        n2 -> n1 % n2

    until n2 becomes 0.

    Example:

        gcd(48, 18)

        48 % 18 = 12

        gcd(48, 18)
            ->
        gcd(18, 12)
            ->
        gcd(12, 6)
            ->
        gcd(6, 0)

    Therefore:

        GCD = 6

    Time Complexity: O(log(min(n1, n2)))
    Space Complexity: O(1)
    """

    while n2 > 0:

        n1, n2 = n2, n1 % n2

    return n1


# --------------------------------------------------
# Test Cases
# --------------------------------------------------

if __name__ == "__main__":

    print("Count Digits:")
    print(count_digits(12345))
    # 5

    print("\nReverse Number:")
    print(reverse_number(12345))
    # 54321

    print("\nPalindrome:")
    print(is_number_palindrome(121))
    # True

    print(is_number_palindrome(123))
    # False

    print("\nArmstrong Number:")
    print(is_armstrong_number(153))
    # True

    print(is_armstrong_number(123))
    # False

    print("\nAll Divisors:")
    print(all_divisors(36))
    # [1, 2, 3, 4, 6, 9, 12, 18, 36]

    print("\nPrime Number:")
    print(is_prime_number(17))
    # True

    print(is_prime_number(12))
    # False

    print("\nGCD:")
    print(gcd(48, 18))
    # 6
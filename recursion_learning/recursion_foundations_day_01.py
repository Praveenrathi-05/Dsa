"""DSA Journey — Day 01: Recursion Foundations.

Topics practiced:
- Recursion base cases and call-stack unwinding
- Printing during the unwinding phase
- Returning and combining results from smaller subproblems
- Digit extraction with // 10 and % 10
- LeetCode 258: Add Digits (recursive practice approach)

All functions here operate on nonnegative integers.
"""


def print_numbers(n: int) -> None:
    """Print integers 1 through n in ascending order."""
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)


def print_even_numbers(n: int) -> None:
    """Print even integers from 1 through n in ascending order."""
    if n == 0:
        return
    print_even_numbers(n - 1)
    if n % 2 == 0:
        print(n)


def recursive_sum(n: int) -> int:
    """Return 1 + 2 + ... + n; n=0 gives 0."""
    if n == 0:
        return 0
    val = recursive_sum(n - 1)
    return n + val


def sum_digits(n: int) -> int:
    """Return the sum of decimal digits of n."""
    if n == 0:
        return 0
    val = sum_digits(n // 10)
    return n % 10 + val


def add_digits(n: int) -> int:
    """Return the repeated digit sum until one digit remains (LC 258)."""
    if n < 10:
        return n
    val = sum_digits(n)
    return add_digits(val)


def mul_digits(n: int) -> int:
    """Multiply digits recursively using 1 as the empty-prefix identity.

    This helper returns 1 for n=0 as a recursion sentinel, not as the
    mathematical product of the digits of the number zero. The public
    digit_product_root(0) correctly returns 0.
    """
    if n == 0:
        return 1
    val = mul_digits(n // 10)
    return n % 10 * val


def digit_product_root(n: int) -> int:
    """Repeatedly multiply decimal digits until a single digit remains."""
    if n < 10:
        return n
    val = mul_digits(n)
    return digit_product_root(val)


if __name__ == "__main__":
    print("Print numbers 1..5:")
    print_numbers(5)
    print("\nPrint even numbers 1..8:")
    print_even_numbers(8)

    assert recursive_sum(0) == 0
    assert recursive_sum(5) == 15
    assert sum_digits(4725) == 18
    assert sum_digits(0) == 0
    assert add_digits(38) == 2
    assert add_digits(9875) == 2
    assert add_digits(0) == 0
    assert mul_digits(25) == 10
    assert mul_digits(105) == 0
    assert digit_product_root(77) == 8
    assert digit_product_root(105) == 0
    assert digit_product_root(0) == 0

    print("\nAll recursion checks passed!")

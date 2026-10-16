"""Striver A2Z DSA — Recursion Lesson 03: Parameterised and Functional Recursion.

Learning journal: solutions developed during the lesson and transfer practice.
Topics: accumulator parameters, return-value propagation, factorial, powers,
exponentiation by squaring.

Run: python3 recursion_lesson_03_parameterised_functional.py
"""


def parameterised_sum(n: int, total: int = 0) -> int:
    """Sum 1..n, carrying the partial total down the call stack.

    Time: O(n); auxiliary recursion space: O(n). Requires n >= 0.
    """
    if n == 0:
        return total
    return parameterised_sum(n - 1, total + n)


def factorial_functional(n: int) -> int:
    """Compute n! while combining results on return. O(n) time/stack."""
    if n == 0:
        return 1
    return factorial_functional(n - 1) * n


def factorial_parameterised(n: int, result: int = 1) -> int:
    """Compute n! carrying an accumulator. O(n) time/stack in Python."""
    if n == 0:
        return result
    return factorial_parameterised(n - 1, result * n)


def power_functional(x: int | float, n: int) -> int | float:
    """Compute x**n by linear recursion. O(n) time/stack; n >= 0."""
    if n == 0:
        return 1
    return x * power_functional(x, n - 1)


def power_parameterised(
    x: int | float, n: int, result: int | float = 1
) -> int | float:
    """Compute x**n with an accumulator. O(n) time/stack; n >= 0."""
    if n == 0:
        return result
    return power_parameterised(x, n - 1, result * x)


def fast_power(x: int | float, n: int) -> int | float:
    """Compute x**n by exponentiation by squaring.

    Reuse the single result for exponent n//2. O(log n) recursive calls
    and O(log n) stack space for n >= 1; n must be nonnegative.
    """
    if n == 0:
        return 1

    half = fast_power(x, n // 2)

    if n % 2 != 0:
        return half * half * x
    return half * half


def run_tests() -> None:
    # Parameterised sum and its return-value propagation.
    assert parameterised_sum(0, 0) == 0
    assert parameterised_sum(5, 0) == 15
    assert parameterised_sum(5, 10) == 25

    # Both factorial techniques, including the empty product case (0! = 1).
    for n, expected in [(0, 1), (1, 1), (4, 24), (8, 40320)]:
        assert factorial_functional(n) == expected
        assert factorial_parameterised(n, 1) == expected

    # Power variations; compare different recursive designs.
    for x, n, expected in [
        (3, 4, 81), (2, 7, 128), (2, 8, 256),
        (3, 0, 1), (5, 1, 5), (0, 5, 0), (-2, 3, -8), (-2, 4, 16),
    ]:
        assert power_functional(x, n) == expected
        assert power_parameterised(x, n, 1) == expected
        assert fast_power(x, n) == expected

    # Larger exponent to check the halving recursion.
    assert fast_power(2, 100) == 2**100
    print("All Lesson 03 tests passed!")


if __name__ == "__main__":
    run_tests()
    print("Sum 1..5:", parameterised_sum(5, 0))
    print("8! (functional):", factorial_functional(8))
    print("8! (parameterised):", factorial_parameterised(8, 1))
    print("3^4 (functional):", power_functional(3, 4))
    print("3^4 (parameterised):", power_parameterised(3, 4, 1))
    print("2^7 (fast):", fast_power(2, 7))

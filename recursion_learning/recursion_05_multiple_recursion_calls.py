"""Striver A2Z DSA — Recursion Lecture 05: Multiple Recursion Calls.

Learning progression:
    1. Fibonacci with two recursive calls
    2. Fibonacci with memoization
    3. LeetCode 70 — Climbing Stairs (plain + memoized)
    4. LeetCode 746 — Min Cost Climbing Stairs (memoized)
    5. LeetCode 198 — House Robber (memoized)

The solutions preserve the recursive techniques developed during the lesson.
Key idea: define what solve(state) returns, combine the alternatives correctly,
and cache repeated states when necessary.
"""


def fib(n: int) -> int:
    """Return Fibonacci(n) using basic recursion. Time O(2^n), stack O(n)."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_memo(n: int, memo: dict[int, int]) -> int:
    """Return Fibonacci(n), caching previously solved states. O(n) time/space."""
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result
    return result


def stairs(n: int) -> int:
    """Count 1-or-2-step paths to the top. Exponential time, O(n) stack."""
    if n <= 1:
        return 1
    return stairs(n - 1) + stairs(n - 2)


def stairs_memo(n: int, memo: dict[int, int]) -> int:
    """Count stair-climbing paths with memoization. O(n) time/space."""
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    result = stairs_memo(n - 1, memo) + stairs_memo(n - 2, memo)
    memo[n] = result
    return result


def min_cost_climbing_stairs(cost: list[int]) -> int:
    """Minimum cost to reach beyond the final stair. O(n) time/space."""
    memo: dict[int, int] = {}

    def solve(i: int) -> int:
        # solve(i): min cost to reach top, starting by paying for step i.
        if i >= len(cost):
            return 0
        if i in memo:
            return memo[i]
        result = cost[i] + min(solve(i + 1), solve(i + 2))
        memo[i] = result
        return result

    return min(solve(0), solve(1))


def max_money(nums: list[int]) -> int:
    """Maximum non-adjacent house loot. O(n) time/space."""
    memo: dict[int, int] = {}

    def solve(i: int) -> int:
        # solve(i): max amount possible from houses i onward.
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        result = max(nums[i] + solve(i + 2), solve(i + 1))
        memo[i] = result
        return result

    return solve(0)


class Solution:
    """LeetCode 198 submission-compatible class."""

    def rob(self, nums: list[int]) -> int:
        return max_money(nums)


def test_solutions() -> None:
    # Fibonacci: base cases and normal inputs.
    for n, expected in [(0, 0), (1, 1), (2, 1), (5, 5), (8, 21), (10, 55)]:
        assert fib(n) == expected
        assert fib_memo(n, {}) == expected

    # Climbing Stairs: 0 means one way (no moves needed).
    for n, expected in [(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8)]:
        assert stairs(n) == expected
        assert stairs_memo(n, {}) == expected

    # Min Cost Climbing Stairs.
    for cost, expected in [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1], 2),
        ([0, 0], 0),
        ([5, 5], 5),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ]:
        assert min_cost_climbing_stairs(cost) == expected

    # House Robber.
    for nums, expected in [
        ([], 0),
        ([5], 5),
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([0, 0, 0], 0),
    ]:
        assert max_money(nums) == expected
        assert Solution().rob(nums) == expected

    # Compare House Robber to exhaustive selection on small arrays.
    from itertools import product

    for length in range(6):
        for nums in product(range(3), repeat=length):
            best = 0
            for mask in range(1 << length):
                if mask & (mask << 1):
                    continue
                total = sum(nums[i] for i in range(length) if mask & (1 << i))
                best = max(best, total)
            assert max_money(list(nums)) == best, (nums, best)


if __name__ == "__main__":
    test_solutions()
    print("All Recursion Lecture 05 tests passed.")

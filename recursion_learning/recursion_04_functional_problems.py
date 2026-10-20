"""Striver A2Z — Recursion Lecture 04: Functional Problems.

Solutions practiced by the learner:
  1. Reverse an array recursively (in place).
  2. Check whether a sequence is a palindrome recursively.
  3. LeetCode 125 — Valid Palindrome (ignore non-alphanumeric characters/case).
  4. LeetCode 680 — Valid Palindrome II (at most one deletion).

The original recursive approaches are preserved. All functions take O(n) time
and O(n) call-stack space in the worst case; large inputs may exceed Python's
recursion limit. Run this file directly to execute the tests.
"""


def swap_array(arr, i=0):
    """Reverse arr in place recursively, returning the same list.

    Time: O(n). Auxiliary stack space: O(n).
    """
    if i >= len(arr) // 2:
        return arr
    j = len(arr) - 1 - i
    arr[i], arr[j] = arr[j], arr[i]
    return swap_array(arr, i + 1)


def palindrome(arr, i=0):
    """Test whether the input sequence reads the same forward and backward.

    Time: O(n). Auxiliary stack space: O(n).
    """
    if i >= len(arr) // 2:
        return True
    if arr[i] != arr[len(arr) - 1 - i]:
        return False
    return palindrome(arr, i + 1)


class ValidPalindrome125:
    """LeetCode 125: ignore non-alphanumeric characters and letter case."""

    def isPalindrome(self, s: str) -> bool:
        return self.check_palindrome(0, len(s) - 1, s)

    def check_palindrome(self, i: int, j: int, s: str) -> bool:
        if i >= j:
            return True
        if not s[i].isalnum():
            return self.check_palindrome(i + 1, j, s)
        if not s[j].isalnum():
            return self.check_palindrome(i, j - 1, s)
        if s[i].lower() != s[j].lower():
            return False
        return self.check_palindrome(i + 1, j - 1, s)


class ValidPalindrome680:
    """LeetCode 680: check whether at most one deletion makes a palindrome."""

    def validPalindrome(self, s: str) -> bool:
        return self.check_palindrome(0, len(s) - 1, s, False)

    def check_palindrome(self, i: int, j: int, s: str, is_checked: bool) -> bool:
        if i >= j:
            return True
        if s[i] != s[j]:
            if is_checked:
                return False
            # Either choice may work, so combine with OR.
            return (
                self.check_palindrome(i, j - 1, s, True)
                or self.check_palindrome(i + 1, j, s, True)
            )
        return self.check_palindrome(i + 1, j - 1, s, is_checked)


def run_tests():
    for original in ([], [1], [1, 2], [1, 2, 3, 4, 5, 6], [3, 3, 1]):
        values = original.copy()
        returned = swap_array(values)
        assert values == list(reversed(original))
        assert returned is values

    for value, expected in (
        ("", True), ("a", True), ("11211", True),
        ("abba", True), ("abca", False), ([1, 2, 1], True),
    ):
        assert palindrome(value) is expected, (value, expected)

    lc125 = ValidPalindrome125()
    for text, expected in (
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False), (" ", True),
        ("0P", False), ("A,ba", True), (".,!", True),
    ):
        assert lc125.isPalindrome(text) is expected, (text, expected)

    lc680 = ValidPalindrome680()
    for text, expected in (
        ("", True), ("a", True), ("aba", True),
        ("abca", True), ("abbca", True), ("abecba", True),
        ("abc", False), ("deeee", True), ("abcde", False),
    ):
        assert lc680.validPalindrome(text) is expected, (text, expected)

    # Exhaustive comparison against simple brute-force reference for all
    # strings of lengths 0..7 over a three-letter alphabet.
    from itertools import product

    def brute_valid_palindrome(s):
        if s == s[::-1]:
            return True
        return any((s[:i] + s[i + 1:]) == (s[:i] + s[i + 1:])[::-1]
                   for i in range(len(s)))

    for n in range(8):
        for characters in product("abc", repeat=n):
            s = "".join(characters)
            assert lc680.validPalindrome(s) == brute_valid_palindrome(s), s

    print("All recursion Lecture 04 tests passed.")


if __name__ == "__main__":
    run_tests()

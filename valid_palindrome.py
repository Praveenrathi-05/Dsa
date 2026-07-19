"""
LeetCode #125 - Valid Palindrome
Determine if a string is a palindrome, considering only alphanumeric
characters and ignoring case.
Pattern: Two Pointers (mirror check)
"""

def isPalindrome(s):
    left, right, s = 0, len(s) - 1, s.lower()
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[right] == s[left]:
            left += 1
            right -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(isPalindrome("race a car"))                       # False
    print(isPalindrome("123"))                               # False

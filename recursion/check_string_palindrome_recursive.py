"""
Check if a String is a Palindrome or Not (Naukri Code360) - recursive
Determine if a string reads the same forwards and backwards, ignoring
non-alphanumeric characters and case. Same requirement as LeetCode
Valid Palindrome (#125), solved recursively this time.
Striver A2Z - Step 1: Basics
Key idea: every branch that should keep checking MUST return the
recursive call's result -- calling it without returning just discards
the answer and falls through to the wrong default.
"""

def isPalindrome(s, left, right):
    if left >= right:
        return True
    else:
        if not s[left].isalnum():
            return isPalindrome(s, left + 1, right)
        elif not s[right - 1].isalnum():
            return isPalindrome(s, left, right - 1)
        elif s[left] != s[right - 1]:
            return False
        else:
            return isPalindrome(s, left + 1, right - 1)

if __name__ == "__main__":
    s = "c1 O$d@eeD o1c"
    print(isPalindrome(s.lower(), 0, len(s)))   # True
    print(isPalindrome("cabxc", 0, 5))           # False
    print(isPalindrome("civic", 0, 5))           # True
    print(isPalindrome("", 0, 0))                 # True

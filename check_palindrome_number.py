"""
GeeksforGeeks - Check if a Number is a Palindrome
Determine if an integer reads the same forwards and backwards.
Striver A2Z - Step 1: Basics
"""

def is_palindrome(n):
    if n < 0:
        n = abs(n)
    original_n = n
    rev_num = 0
    while n > 0:
        m = n % 10
        n = n // 10
        rev_num = rev_num * 10 + m
    return original_n == rev_num

if __name__ == "__main__":
    print(is_palindrome(121))  # True
    print(is_palindrome(10))   # False
    print(is_palindrome(0))    # True

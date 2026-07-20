"""
Factorial of N Numbers (using recursion)
Return n! = n * (n-1) * (n-2) * ... * 1, with 0! = 1.
Striver A2Z - Step 1: Basics (Recursion)
"""

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(5))   # 120
    print(factorial(1))   # 1
    print(factorial(0))   # 1
    print(factorial(6))   # 720

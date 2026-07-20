"""
Sum of First N Numbers (using recursion)
Return 1 + 2 + 3 + ... + n.
Striver A2Z - Step 1: Basics (Recursion)
Base case uses n < 1 (not n == 1) so it correctly handles n = 0
and n = 1 with the same rule, instead of needing a separate case.
"""

def sumFirstN(n):
    if n < 1:
        return 0
    else:
        return n + sumFirstN(n - 1)

if __name__ == "__main__":
    print(sumFirstN(5))    # 15
    print(sumFirstN(1))    # 1
    print(sumFirstN(0))    # 0 (doesn't crash)
    print(sumFirstN(10))   # 55

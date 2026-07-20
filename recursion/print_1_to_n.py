"""
Print 1 to N using recursion
Print numbers 1 through n, in increasing order.
Striver A2Z - Step 1: Basics (Recursion)
Key idea: recurse BEFORE printing, so the action happens on the way
back up the call stack -- smallest call finishes first.
"""

def print1ToN(n):
    if n == 0:
        return
    else:
        print1ToN(n - 1)
        print(n, end=" ")

if __name__ == "__main__":
    print1ToN(5)   # 1 2 3 4 5
    print()
    print1ToN(1)   # 1

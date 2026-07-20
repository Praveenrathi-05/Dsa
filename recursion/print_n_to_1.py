"""
Print N to 1 using recursion
Print numbers n down to 1, in decreasing order.
Striver A2Z - Step 1: Basics (Recursion)
Key idea: print BEFORE recursing, so the action happens on the way
down the call stack -- biggest call acts first.
"""

def printNTo1(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        printNTo1(n - 1)

if __name__ == "__main__":
    printNTo1(5)   # 5 4 3 2 1
    print()
    printNTo1(1)   # 1

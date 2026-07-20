"""
GeeksforGeeks - Print GFG N Times
Print "GFG" exactly n times, using recursion only (no loop).
Striver A2Z - Step 1: Basics (Recursion)
"""

def printGFG(n):
    if n == 0:
        return
    else:
        print("GFG ", end="")
        printGFG(n - 1)

if __name__ == "__main__":
    printGFG(5)
    print()
    printGFG(1)
    print()
    printGFG(0)
    print("(nothing printed above for n=0)")

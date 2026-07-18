"""
GeeksforGeeks - Count Digits
Count how many digits an integer has.
Striver A2Z - Step 1: Basics
"""

def countDigits(n):
    if n == 0:
        return 1
    if n < 0:
        n = abs(n)
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

if __name__ == "__main__":
    print(countDigits(1567))   # 4
    print(countDigits(0))      # 1
    print(countDigits(-123))   # 3

"""
GCD or HCF of Two Numbers
Find the greatest number that divides both inputs exactly.
Striver A2Z - Step 1: Basics
Two versions: brute force, then the optimized Euclidean algorithm.
"""

def gcd_brute_force(n1, n2):
    gcd = 0
    count = 1
    while min(n1, n2) >= count:
        if n1 % count == 0 and n2 % count == 0:
            gcd = count
        count += 1
    return gcd

def gcd_euclidean(num1, num2):
    n1 = max(num1, num2)
    n2 = min(num1, num2)
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

if __name__ == "__main__":
    print(gcd_brute_force(36, 60))   # 12
    print(gcd_euclidean(36, 60))     # 12
    print(gcd_euclidean(1000, 7))    # 1 (fast even with a big gap)

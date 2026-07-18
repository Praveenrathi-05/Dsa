"""
Print all Divisors of a Number (Naukri Code360)
Return every divisor of n, in ascending order.
Striver A2Z - Step 1: Basics
Optimized: only check up to sqrt(n), grabbing each divisor's pair for free.
"""

def all_divisors(n):
    count = round(n ** 0.5)
    divisors = []
    for i in range(1, count + 1):
        if n % i == 0:
            divisors.append(i)
            if i != (n // i):
                divisors.append(n // i)
    return sorted(divisors)

if __name__ == "__main__":
    print(all_divisors(36))   # [1, 2, 3, 4, 6, 9, 12, 18, 36]
    print(all_divisors(10))   # [1, 2, 5, 10]
    print(all_divisors(13))   # [1, 13]

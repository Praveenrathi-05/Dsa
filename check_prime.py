"""
Check Prime (Naukri Code360)
Return True if n is prime, False otherwise.
Striver A2Z - Step 1: Basics
Optimized: only check divisibility up to sqrt(n).
"""

def check_prime(n):
    if n < 2:
        return False
    count = round(n ** 0.5)
    for i in range(2, count + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(check_prime(1))    # False
    print(check_prime(97))   # True
    print(check_prime(100))  # False

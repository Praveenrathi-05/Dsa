"""
GeeksforGeeks - Armstrong Numbers
A number where the sum of each digit raised to the power of the total
digit count equals the number itself.
Striver A2Z - Step 1: Basics
"""

def is_armstrong(n):
    count = 0
    new_n = n
    while n > 0:
        n = n // 10
        count += 1
    new_count, n = count, new_n
    total = 0
    while new_count != 0:
        m = new_n % 10
        new_n = new_n // 10
        total += m ** count
        new_count -= 1
    return total == n

if __name__ == "__main__":
    print(is_armstrong(153))   # True
    print(is_armstrong(1634))  # True
    print(is_armstrong(120))   # False

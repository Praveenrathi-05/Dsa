"""
GeeksforGeeks - Reverse Digits of a Number
Reverse the digits of an integer. Leading zeros in the result vanish
(200 -> 2). Sign is preserved for negative numbers.
Striver A2Z - Step 1: Basics
"""

def reverse_number(n):
    is_negative = False
    if n < 0:
        n = abs(n)
        is_negative = True
    new_num = 0
    while n > 0:
        m = n % 10
        n = n // 10
        new_num = new_num * 10 + m
    if is_negative:
        return -(new_num)
    return new_num

if __name__ == "__main__":
    print(reverse_number(122))   # 221
    print(reverse_number(200))   # 2
    print(reverse_number(-240))  # -42

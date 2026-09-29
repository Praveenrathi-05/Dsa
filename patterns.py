"""
Striver A2Z - Pattern Problems

This file contains 17 pattern-printing problems for practicing:
- Nested loops
- Rows and columns
- Increasing/decreasing patterns
- Star patterns
- Number patterns
- Spaces and alignment
- Symmetry
- Hollow patterns
- Concentric patterns

These problems are useful for understanding how the outer loop controls
rows and how the inner loops control what gets printed inside each row.

For most patterns:
Time Complexity: O(n²)
Space Complexity: O(1), excluding the printed output.
"""


# --------------------------------------------------
# Pattern 1
# Square Star Pattern
# --------------------------------------------------

def pattern1(n):
    """
    Example for n = 4:

    * * * *
    * * * *
    * * * *
    * * * *

    Key idea:
    The outer loop creates n rows.
    The inner loop prints n stars in every row.
    """

    for _ in range(n):
        for _ in range(n):
            print("*", end=" ")
        print()


# --------------------------------------------------
# Pattern 2
# Right-Angled Star Triangle
# --------------------------------------------------

def pattern2(n):
    """
    Example for n = 4:

    *
    * *
    * * *
    * * * *

    Key idea:
    Row i contains i + 1 stars.
    """

    for i in range(n):
        for _ in range(i + 1):
            print("*", end=" ")
        print()


# --------------------------------------------------
# Pattern 3
# Increasing Number Triangle
# --------------------------------------------------

def pattern3(n):
    """
    Example for n = 4:

    1
    1 2
    1 2 3
    1 2 3 4

    Key idea:
    Every row starts from 1 and goes up to i + 1.
    """

    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()


# --------------------------------------------------
# Pattern 4
# Repeated Row Number Triangle
# --------------------------------------------------

def pattern4(n):
    """
    Example for n = 4:

    1
    2 2
    3 3 3
    4 4 4 4

    Key idea:
    Row i prints i + 1 exactly i + 1 times.
    """

    for i in range(n):
        for _ in range(i + 1):
            print(i + 1, end=" ")
        print()


# --------------------------------------------------
# Pattern 5
# Inverted Star Triangle
# --------------------------------------------------

def pattern5(n):
    """
    Example for n = 4:

    * * * *
    * * *
    * *
    *

    Key idea:
    The number of stars decreases by one after every row.
    """

    for i in range(n):
        for _ in range(n - i):
            print("*", end=" ")
        print()


# --------------------------------------------------
# Pattern 6
# Inverted Number Triangle
# --------------------------------------------------

def pattern6(n):
    """
    Example for n = 4:

    1 2 3 4
    1 2 3
    1 2
    1

    Key idea:
    Every row begins from 1, but the number of values decreases.
    """

    for i in range(n):
        for j in range(n - i):
            print(j + 1, end=" ")
        print()


# --------------------------------------------------
# Pattern 7
# Star Pyramid
# --------------------------------------------------

def pattern7(n):
    """
    Example for n = 4:

       *
      ***
     *****
    *******

    Key idea:

    Row i contains:

    spaces = n - i - 1
    stars  = 2 * i + 1

    The odd-number sequence:

    1, 3, 5, 7...

    creates the pyramid.
    """

    for i in range(n):

        for _ in range(n - i - 1):
            print(" ", end="")

        for _ in range(2 * i + 1):
            print("*", end="")

        for _ in range(n - i - 1):
            print(" ", end="")

        print()


# --------------------------------------------------
# Pattern 8
# Inverted Star Pyramid
# --------------------------------------------------

def pattern8(n):
    """
    Example for n = 4:

    *******
     *****
      ***
       *

    Key idea:

    spaces = i
    stars = 2 * (n - i) - 1

    Spaces increase while stars decrease.
    """

    for i in range(n):

        for _ in range(i):
            print(" ", end="")

        for _ in range(2 * (n - i) - 1):
            print("*", end="")

        for _ in range(i):
            print(" ", end="")

        print()


# --------------------------------------------------
# Pattern 9
# Diamond Star Pattern
# --------------------------------------------------

def pattern9(n):
    """
    Combine Pattern 7 and Pattern 8.

    Example for n = 3:

      *
     ***
    *****
    *****
     ***
      *
    """

    pattern7(n)
    pattern8(n)


# --------------------------------------------------
# Pattern 10
# Increasing + Decreasing Star Triangle
# --------------------------------------------------

def pattern10(n):
    """
    Example for n = 4:

    *
    * *
    * * *
    * * * *
    * * *
    * *
    *

    Key idea:
    Rows first increase from 1 to n stars and then decrease.

    For the second half:

        stars = 2 * n - i
    """

    for i in range(1, 2 * n):

        stars = i

        if i > n:
            stars = 2 * n - i

        for _ in range(stars):
            print("* ", end="")

        print()


# --------------------------------------------------
# Pattern 11
# Binary Number Triangle
# --------------------------------------------------

def pattern11(n):
    """
    Example for n = 4:

    1
    0 1
    1 0 1
    0 1 0 1

    Key idea:
    Use the parity of:

        i + j

    If it is even -> print 1.
    If it is odd  -> print 0.
    """

    for i in range(n):

        for j in range(i + 1):

            if (i + j) % 2 == 0:
                print("1 ", end="")

            else:
                print("0 ", end="")

        print()


# --------------------------------------------------
# Pattern 12
# Number Crown Pattern
# --------------------------------------------------

def pattern12(n):
    """
    Example for n = 4:

    1      1
    12    21
    123  321
    12344321

    Each row contains three parts:

    1. Increasing numbers
    2. Middle spaces
    3. Decreasing numbers

    Number of middle spaces:

        2 * (n - i)
    """

    for i in range(1, n + 1):

        # Increasing numbers
        for j in range(i):
            print(j + 1, end="")

        # Middle spaces
        for _ in range(2 * (n - i)):
            print(" ", end="")

        # Decreasing numbers
        for j in range(i, 0, -1):
            print(j, end="")

        print()


# --------------------------------------------------
# Pattern 13
# Increasing Number Triangle
# --------------------------------------------------

def pattern13(n):
    """
    Example for n = 4:

    1
    2 3
    4 5 6
    7 8 9 10

    Key idea:
    Keep one counter outside the loops.

    Every time a number is printed, increment the counter.
    """

    count = 0

    for i in range(n):

        for _ in range(i + 1):

            count += 1

            print(f"{count} ", end="")

        print()


# --------------------------------------------------
# Pattern 14
# Symmetric Butterfly / Star Pattern
# --------------------------------------------------

def pattern14(n):
    """
    This pattern has two halves.

    Upper half:
    - Stars decrease.
    - Middle spaces increase.

    Lower half:
    - Stars increase.
    - Middle spaces decrease.

    The left and right sides remain symmetric.
    """

    # Upper half
    for i in range(n):

        for _ in range(n - i):
            print("* ", end="")

        for _ in range(2 * i):
            print("  ", end="")

        for _ in range(n - i):
            print("* ", end="")

        print()

    # Lower half
    for i in range(1, n + 1):

        for _ in range(i):
            print("* ", end="")

        for _ in range(2 * (n - i)):
            print("  ", end="")

        for _ in range(i):
            print("* ", end="")

        print()


# --------------------------------------------------
# Pattern 15
# Expanding and Contracting Symmetric Pattern
# --------------------------------------------------

def pattern15(n):
    """
    Stars increase toward the middle and then decrease.

    The middle spaces do the opposite.

    stars:
        1, 2, 3 ... n ... 3, 2, 1

    spaces depend on:

        2 * (n - stars)
    """

    for i in range(1, 2 * n + 1):

        stars = i

        if i > n:
            stars = 2 * n - i

        # Left stars
        for _ in range(stars):
            print("* ", end="")

        # Middle spaces
        for _ in range(2 * (n - stars)):
            print("  ", end="")

        # Right stars
        for _ in range(stars):
            print("* ", end="")

        print()


# --------------------------------------------------
# Pattern 16
# Hollow Square
# --------------------------------------------------

def pattern16(n):
    """
    Example for n = 5:

    * * * * *
    *       *
    *       *
    *       *
    * * * * *

    Key idea:
    Print a star only when the current position belongs to a border.

    Border conditions:

        i == 0
        j == 0
        i == n - 1
        j == n - 1
    """

    for i in range(n):

        for j in range(n):

            if (
                i == 0
                or j == 0
                or i == n - 1
                or j == n - 1
            ):

                print("* ", end="")

            else:

                print("  ", end="")

        print()


# --------------------------------------------------
# Pattern 17
# Concentric Number Square
# --------------------------------------------------

def pattern17(n):
    """
    Example for n = 4:

    4 4 4 4 4 4 4
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4
    4 3 2 2 2 3 4
    4 3 3 3 3 3 4
    4 4 4 4 4 4 4

    The matrix size is:

        2 * n - 1

    For every position, calculate its distance from:

        top
        bottom
        left
        right

    The minimum of these distances tells us which layer the cell
    belongs to.

    Value:

        n - min(top, bottom, left, right)

    This creates concentric layers.
    """

    size = 2 * n - 1

    for i in range(size):

        for j in range(size):

            top = i

            left = j

            right = size - 1 - j

            bottom = size - 1 - i

            value = n - min(
                top,
                bottom,
                right,
                left
            )

            print(f"{value} ", end="")

        print()


# --------------------------------------------------
# Run Patterns
# --------------------------------------------------

if __name__ == "__main__":

    n = 5

    print("PATTERN 1")
    pattern1(n)

    print("\nPATTERN 2")
    pattern2(n)

    print("\nPATTERN 3")
    pattern3(n)

    print("\nPATTERN 4")
    pattern4(n)

    print("\nPATTERN 5")
    pattern5(n)

    print("\nPATTERN 6")
    pattern6(n)

    print("\nPATTERN 7")
    pattern7(n)

    print("\nPATTERN 8")
    pattern8(n)

    print("\nPATTERN 9")
    pattern9(n)

    print("\nPATTERN 10")
    pattern10(n)

    print("\nPATTERN 11")
    pattern11(n)

    print("\nPATTERN 12")
    pattern12(n)

    print("\nPATTERN 13")
    pattern13(n)

    print("\nPATTERN 14")
    pattern14(n)

    print("\nPATTERN 15")
    pattern15(n)

    print("\nPATTERN 16")
    pattern16(n)

    print("\nPATTERN 17")
    pattern17(n)
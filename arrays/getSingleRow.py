"""
Pascal's Triangle II (LeetCode #119)

Given rowIndex, return that row of Pascal's Triangle.

Striver A2Z - Step 2: Arrays

Key idea:
Calculate each value directly using the binomial coefficient relation,
so we do not need to generate the rows before it.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def getSingleRow(rowIndex):
    row = [1]
    value = 1
    for i in range(rowIndex):
        value *= rowIndex - i
        value //= i + 1
        row.append(value)
    return row

if __name__ == "__main__":
    print(getSingleRow(4))

"""
Pascal's Triangle (LeetCode #118)

Given numRows, generate the first numRows rows of Pascal's Triangle.

Striver A2Z - Step 2: Arrays

Key idea:
Build each row from the previous row. The first and last values are 1,
and every inner value is the sum of two adjacent values from the previous row.

Time Complexity: O(n²)
Space Complexity: O(n²)
"""

def getAllRows(numRows):
    triangle = [[1]]
    for _ in range(numRows - 1):
        prev_row = triangle[-1]
        next_row = [1]
        for j in range(len(prev_row) - 1):
            next_row.append(prev_row[j] + prev_row[j + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle

if __name__ == "__main__":
    print(getAllRows(4))

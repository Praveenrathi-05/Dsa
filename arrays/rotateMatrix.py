"""
Rotate Matrix by 90 Degrees (LeetCode #48)

Given an n x n matrix, rotate the matrix 90 degrees clockwise in-place.

Striver A2Z - Step 2: Arrays

Key idea:
The clockwise rotation is done in two steps:

1. Transpose the matrix by swapping matrix[i][j] with matrix[j][i]
   only when j > i. This prevents swapping the same pair twice.
2. Reverse every row.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

def rotateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        first = 0
        last = len(matrix[i]) - 1

        while first <= last:
            matrix[i][first], matrix[i][last] = matrix[i][last], matrix[i][first]
            first += 1
            last -= 1

    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row in rotateMatrix(matrix):
        print(row)

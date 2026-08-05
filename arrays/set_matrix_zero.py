"""
Set Matrix Zeroes (LeetCode #73)

Given an m × n matrix, if any element is 0, set its entire row and
column to 0 in-place.

Striver A2Z - Step 2: Arrays

Key idea:
Use the first row and first column as marker arrays instead of using
extra space. First record whether the first row or first column
originally contains a zero. Then mark rows and columns that need to be
zeroed, update the inner matrix, and finally process the first row and
first column.

Time Complexity: O(m × n)
Space Complexity: O(1)
"""

def set_matrix_zero(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    first_row_has_zero=False
    for j in range(cols):
        if matrix[0][j]==0:
            first_row_has_zero=True
            break

    first_column_has_zero=False
    for i in range(rows):
        if matrix[i][0]==0:
            first_column_has_zero=True
            break

    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0

    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j]=0

    if first_column_has_zero:
        for i in range(rows):
            matrix[i][0]=0

    return matrix

if __name__=="__main__":
    matrix=[
        [1,1,1,1],
        [1,0,1,1],
        [1,1,1,0],
        [1,1,1,1]
    ]
    for row in set_matrix_zero(matrix):
        print(row)

"""
Move Zeroes (LeetCode #283)

Move all zero values to the end while preserving the relative order
of non-zero elements.

Striver A2Z - Step 2: Arrays

Key idea:
Compact all non-zero elements toward the beginning, then fill the
remaining positions with zeroes.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def moveZeros(arr):
    k=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[k]=arr[i]
            k+=1
    for i in range(k,len(arr)):
        arr[i]=0
    return arr

if __name__=="__main__":
    print(moveZeros([0,1,0,3,12]))

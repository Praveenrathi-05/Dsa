"""
Check if Array is Sorted (Code360)

Determine whether an array is sorted in non-decreasing order.

Striver A2Z - Step 2: Arrays

Key idea:
Compare every adjacent pair. If any previous element is greater than
the next one, the array is not sorted.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def checkSorted(arr):
    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:
            return False
    return True

if __name__=="__main__":
    print(checkSorted([1,2,2,3]))
    print(checkSorted([3,2,1]))

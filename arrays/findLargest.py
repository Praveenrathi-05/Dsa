"""
Largest Element in an Array (GeeksforGeeks)

Given an array of integers, return the largest element present in the array.

Striver A2Z - Step 2: Arrays

Key idea:
Scan the array once while maintaining the largest element seen so far.
Whenever a larger element is found, update the answer. This is the
optimal O(n) solution and avoids sorting, which would take O(n log n).

Time Complexity: O(n)
Space Complexity: O(1)
"""

def findLargest(arr):
    if len(arr)>0:
        maximum=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>maximum:
                maximum=arr[i]
        return maximum

if __name__=="__main__":
    print(findLargest([3,2,1,5,4]))   # 5
    print(findLargest([-7,-2,-9]))    # -2
    print(findLargest([]))            # None

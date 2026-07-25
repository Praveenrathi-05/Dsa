"""
Remove Duplicates from Sorted Array (LeetCode #26)

Remove duplicates in-place from a sorted array and return the number
of unique elements.

Striver A2Z - Step 2: Arrays

Key idea:
Overwrite duplicate values by writing only the first occurrence of each
distinct element into the front portion of the array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def removeDuplicates(arr):
    k=0
    last_unique=float("-inf")
    i=0
    while i<len(arr):
        if last_unique!=arr[i]:
            arr[k]=arr[i]
            last_unique=arr[k]
            k+=1
        i+=1
    return k

if __name__=="__main__":
    nums=[0,0,1,1,2,2,3,4]
    k=removeDuplicates(nums)
    print(k)
    print(nums[:k])

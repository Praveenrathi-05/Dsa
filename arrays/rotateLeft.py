"""
Rotate Array to the Left by K Places

Rotate an array k positions to the left in-place.

Striver A2Z - Step 2: Arrays

Key idea:
Reverse the first k elements, reverse the remaining elements, then
reverse the entire array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverseArray(arr,left,right):
    if left>=right: return arr
    arr[left],arr[right-1]=arr[right-1],arr[left]
    reverseArray(arr,left+1,right-1)
    return arr

def rotateLeft(nums,k):
    if nums:
        k%=len(nums)
        reverseArray(nums,0,k)
        reverseArray(nums,k,len(nums))
        reverseArray(nums,0,len(nums))
    return nums

if __name__=="__main__":
    print(rotateLeft([1,2,3,4,5,6,7],3))

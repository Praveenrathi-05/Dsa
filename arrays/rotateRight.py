"""
Rotate Array to the Right by K Places (LeetCode #189)

Rotate an array k positions to the right in-place.

Striver A2Z - Step 2: Arrays

Key idea:
Use the three-reversal algorithm:
1. Reverse the whole array.
2. Reverse the first k elements.
3. Reverse the remaining elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverseArray(arr,left,right):
    if left>=right: return arr
    arr[left],arr[right-1]=arr[right-1],arr[left]
    reverseArray(arr,left+1,right-1)
    return arr

def rotateRight(nums,k):
    if nums:
        k%=len(nums)
        reverseArray(nums,0,len(nums))
        reverseArray(nums,0,k)
        reverseArray(nums,k,len(nums))
    return nums

if __name__=="__main__":
    print(rotateRight([1,2,3,4,5,6,7],3))

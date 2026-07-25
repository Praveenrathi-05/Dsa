"""
Left Rotate an Array by One Place

Move every element one position to the left. The first element becomes
the last element.

Striver A2Z - Step 2: Arrays

Key idea:
Save the first element, shift every remaining element left by one
position, then place the saved value at the end.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def leftRotateByOne(arr):
    if arr:
        first=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[-1]=first
    return arr

if __name__=="__main__":
    print(leftRotateByOne([1,2,3,4,5]))

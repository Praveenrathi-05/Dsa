"""
Linear Search (GeeksforGeeks)

Given an array and a target element, return its index or -1.

Striver A2Z - Step 2: Arrays

Key idea:
Traverse the array sequentially until the target is found.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

if __name__=="__main__":
    print(linearSearch([10,20,30,40],30))

"""
Union of Two Sorted Arrays (GeeksforGeeks)

Return all distinct elements from two sorted arrays.

Striver A2Z - Step 2: Arrays

Key idea:
Merge both arrays while skipping duplicate values.

Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""

def unionOfTwoSortedArray(arr1,arr2):
    def push(u,v):
        if not u or u[-1]!=v:
            u.append(v)
    i=j=0
    union=[]
    while i<len(arr1) or j<len(arr2):
        if i==len(arr1):
            push(union,arr2[j]); j+=1
        elif j==len(arr2):
            push(union,arr1[i]); i+=1
        elif arr1[i]<arr2[j]:
            push(union,arr1[i]); i+=1
        elif arr1[i]>arr2[j]:
            push(union,arr2[j]); j+=1
        else:
            push(union,arr1[i]); i+=1; j+=1
    return union

if __name__=="__main__":
    print(unionOfTwoSortedArray([-5,-3,0],[-4,-3,2]))

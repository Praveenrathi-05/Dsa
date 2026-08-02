"""
Next Permutation (LeetCode #31)

Given an array representing a permutation, transform it into the
lexicographically next greater permutation. If no such permutation
exists, rearrange the array into ascending order.

Striver A2Z - Step 2: Arrays

Key idea:
- Find the first index from the right where nums[i] < nums[i+1].
- Swap it with the smallest element greater than it on its right.
- Reverse the suffix after that index.
- If no such index exists, reverse the entire array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def nextPermutation(nums):
    breaking_point=-1

    j=len(nums)-1
    while j>0:
        if nums[j-1]<nums[j]:
            breaking_point=j-1
            break
        j-=1

    if breaking_point!=-1:
        partner=-1
        check=float("inf")

        i=breaking_point+1
        while i<len(nums):
            if nums[i]<=check and nums[i]>nums[breaking_point]:
                check=nums[i]
                partner=i
            i+=1

        nums[breaking_point],nums[partner]=nums[partner],nums[breaking_point]

    nums[breaking_point+1:]=reversed(nums[breaking_point+1:])
    return nums

if __name__=="__main__":
    print(nextPermutation([1,2,3]))
    print(nextPermutation([3,2,1]))
    print(nextPermutation([0,2,1,1]))

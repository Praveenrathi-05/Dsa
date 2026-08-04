"""
Leaders in an Array (GeeksforGeeks)

Return all leaders in an array. An element is a leader if it is greater
than or equal to every element on its right.

Striver A2Z - Step 2: Arrays

Key idea:
Traverse from right to left while maintaining the maximum value seen so
far. Every element greater than or equal to this maximum is a leader.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def leaders_in_array(nums):
    max_so_far=float("-inf")
    leaders=[]
    for i in range(len(nums)-1,-1,-1):
        if nums[i]>=max_so_far:
            max_so_far=nums[i]
            leaders.append(nums[i])
    return leaders[::-1]

if __name__=="__main__":
    print(leaders_in_array([4,10,6,8,2]))

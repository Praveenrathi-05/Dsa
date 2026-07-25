"""
Second Largest Element in an Array (GeeksforGeeks)

Return the second largest DISTINCT element. If it does not exist,
return -1.

Striver A2Z - Step 2: Arrays

Key idea:
Maintain two variables: the largest and the second largest distinct
element encountered so far. Update both in a single traversal.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def findSecondLargest(arr):
    if len(arr)<2:
        return -1
    first_max=float("-inf")
    second_distinct_max=float("-inf")
    for num in arr:
        if num>first_max:
            second_distinct_max=first_max
            first_max=num
        elif first_max>num>second_distinct_max:
            second_distinct_max=num
    return second_distinct_max if second_distinct_max!=float("-inf") else -1

if __name__=="__main__":
    print(findSecondLargest([12,35,1,10,34,1])) #34
    print(findSecondLargest([5,5,5])) #-1

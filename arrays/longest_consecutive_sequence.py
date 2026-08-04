"""
Longest Consecutive Sequence (LeetCode #128)

Find the length of the longest consecutive sequence.

Striver A2Z - Step 2: Arrays

Key idea:
Insert all values into a set. Only begin counting from numbers that do
not have a predecessor, ensuring every sequence is counted once.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def longest_consecutive_sequence(nums):
    values=set(nums)
    longest=0
    for current_value in values:
        if current_value-1 not in values:
            current_length=1
            next_value=current_value+1
            while next_value in values:
                current_length+=1
                next_value+=1
            longest=max(longest,current_length)
    return longest

if __name__=="__main__":
    print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))

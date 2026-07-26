"""
Missing Number (LeetCode #268)

Find the missing number from 0..n.

Striver A2Z - Step 2: Arrays

Key idea:
Expected sum minus actual sum gives the missing value.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def missing_number(arr):
    expected=((len(arr))*(len(arr)+1))//2
    return expected-sum(arr)

if __name__=="__main__":
    print(missing_number([3,2,1,5,4]))

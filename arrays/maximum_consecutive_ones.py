"""
Maximum Consecutive Ones (LeetCode #485)

Find the longest streak of consecutive 1s.

Striver A2Z - Step 2: Arrays

Key idea:
Track the current streak and the best streak.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maximum_consecutive_ones(arr):
    cur=best=0
    for x in arr:
        if x==1:
            cur+=1
            best=max(best,cur)
        else:
            cur=0
    return best

if __name__=="__main__":
    print(maximum_consecutive_ones([1,1,0,1,1,1]))

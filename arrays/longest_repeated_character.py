"""
Longest Consecutive Repeated Character

Return the length of the longest contiguous run of one character.

Striver A2Z - Step 2: Arrays / Strings

Key idea:
Maintain the current run length and the maximum seen so far.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def longest_repeated_character(word):
    cur=maxc=0
    prev=""
    for ch in word:
        if ch==prev:
            cur+=1
        else:
            cur=1
            prev=ch
        maxc=max(maxc,cur)
    return maxc

if __name__=="__main__":
    print(longest_repeated_character("aaabbccccd"))

# DSA Practice

Data Structures & Algorithms practice, working through [Striver's A2Z DSA Sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z) (474 problems, 18 topics) alongside targeted LeetCode pattern problems. Solving as part of my prep for backend / software engineering interviews.

## Structure

Each problem is its own file, numbered in the order I solved it. Every file includes:
- The problem statement as a docstring, with source (LeetCode / GeeksforGeeks / Code360)
- The final, tested solution
- A few verified test cases at the bottom (`if __name__ == "__main__":`)

```
01_two_sum.py
02_binary_search.py
...
```

## Progress — Striver's A2Z Sheet

| # | Section | Done / Total |
|---|---|---|
| 1 | Learn the Basics | 18 / 54 |
| 2 | Sorting Techniques | 0 / 7 |
| 3 | Arrays | 0 / 40 |
| 4 | Binary Search | 0 / 32 |
| 5 | Strings (Basic) | 0 / 15 |
| 6 | Linked List | 0 / 31 |
| 7 | Recursion | 0 / 25 |
| 8 | Bit Manipulation | 0 / 18 |
| 9 | Stack & Queues | 0 / 30 |
| 10 | Sliding Window & Two Pointers | 0 / 12 |
| 11 | Heaps | 0 / 17 |
| 12 | Greedy | 0 / 15 |
| 13 | Binary Trees | 0 / 38 |
| 14 | Binary Search Trees | 0 / 16 |
| 15 | Graphs | 0 / 53 |
| 16 | Dynamic Programming | 0 / 55 |
| 17 | Tries | 0 / 7 |
| 18 | Strings (Advanced) | 0 / 9 |

> **Note:** the recursion warm-ups solved so far (Print GFG N Times, Print 1 to N, Print N to 1, Sum of First N, Factorial, Fibonacci) are part of **Learn the Basics** (row 1) — not row 7, "Recursion." That's a separate, much bigger step (~25 problems) that comes later, after Arrays, Binary Search, Strings, and Linked List, and goes deeper into pattern-based recursion (subsequences, subsets) building toward Backtracking.

## Also solved — LeetCode patterns

A few interview-pattern problems solved before starting the sheet in full:

- Two Sum (Arrays & Hashing)
- Two Sum II (Two Pointers)
- Valid Palindrome (Two Pointers)
- Binary Search

## Approach

- Brute force first, then optimize — understand *why* the faster version works, not just that it does
- Every solution is traced by hand and tested against edge cases (zero, negatives, duplicates, empty input) before being considered done
- No shortcuts that skip the point of the problem (e.g. no `str()` conversion for digit-manipulation problems — the point is the math)

## Resources

- [Striver's A2Z Sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z)
- [LeetCode](https://leetcode.com)
- [GeeksforGeeks Practice](https://practice.geeksforgeeks.org)
- [Naukri Code360](https://www.naukri.com/code360)
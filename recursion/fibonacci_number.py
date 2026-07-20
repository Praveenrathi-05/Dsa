"""
Nth Fibonacci Using Recursion (GeeksforGeeks)
Return the nth Fibonacci number. F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).
Striver A2Z - Step 1: Basics (Recursion)
Note: this naive version is O(2^n) -- each call branches into two,
recomputing overlapping subproblems many times over. This is the
exact inefficiency that Dynamic Programming (memoization) exists
to fix, later in the roadmap.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    for i in range(10):
        print(fibonacci(i), end=" ")
    print()   # 0 1 1 2 3 5 8 13 21 34

"""
Merge Intervals (LeetCode #56)

Given an array of intervals, merge all overlapping intervals and return
an array of the non-overlapping intervals that cover all the intervals.

Striver A2Z - Step 3: Arrays

Key idea:
1. Sort the intervals by their starting point.
2. Keep a result list containing the merged intervals.
3. Compare each current interval with the last interval in result.
4. If they overlap, merge them using the smaller start and larger end.
5. Otherwise, add the current interval as a new interval.

Because the intervals are sorted by their starting points, if the
current interval does not overlap with the last merged interval, it
cannot overlap with any earlier interval either.

Time Complexity: O(n log n)
Space Complexity: O(n) for the result list.
"""

def merge_intervals(intervals):
    intervals.sort()
    result = []

    for current_interval in intervals:
        if len(result) == 0:
            result.append(current_interval)
        else:
            last_interval = result[-1]

            if last_interval[1] >= current_interval[0]:
                result[-1] = [
                    last_interval[0],
                    max(last_interval[1], current_interval[1])
                ]
            else:
                result.append(current_interval)

    return result


if __name__ == "__main__":
    intervals = [
        [1, 4],
        [3, 5],
        [6, 8],
        [7, 9],
        [12, 15]
    ]

    print(merge_intervals(intervals))
    # [[1, 5], [6, 9], [12, 15]]

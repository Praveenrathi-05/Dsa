"""
Find Highest and Lowest Frequency Element
Find the element with the highest frequency and the element with the
lowest frequency in an array.

Striver A2Z - Step 1: Learn the Basics (Hashing)

Key idea:
- Use a dictionary (hash map) to count frequencies.
- Traverse the frequency map to find:
    - Highest frequency element
    - Lowest frequency element

Time Complexity: O(n)
Space Complexity: O(n)
"""

def findHighLow(arr):
    frequency = {}

    # Count frequencies
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Initialize with first frequency values
    max_count = min(frequency.values())
    max_number = min(frequency.keys())

    low_count = max(frequency.values())
    low_number = max(frequency.keys())

    # Find highest and lowest frequency elements
    for key, value in frequency.items():
        if value > max_count:
            max_count = value
            max_number = key

        if value < low_count:
            low_count = value
            low_number = key

    return (max_number, low_number)


if __name__ == "__main__":
    print(findHighLow([10, 20, 5, 5, 5, 5, 20, 20]))
    # (5, 10)

    print(findHighLow([1, 1, 2, 2, 2, 3]))
    # (2, 3)
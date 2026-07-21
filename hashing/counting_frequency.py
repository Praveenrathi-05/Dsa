"""
Count Frequency of Elements
Count how many times each element appears in an array.
Striver A2Z - Step 1: Learn the Basics (Hashing)

Key idea: use a dictionary (hash map) where:
- Key = element
- Value = frequency of that element

Time Complexity: O(n)
Space Complexity: O(n)
"""

def counting_frequency(arr):
    frequency = {}

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return dict(sorted(frequency.items()))

if __name__ == "__main__":
    print(counting_frequency([10, 20, 10, 5, 20]))
    # {5: 1, 10: 2, 20: 2}

    print(counting_frequency([1, 1, 1, 2, 3]))
    # {1: 3, 2: 1, 3: 1}
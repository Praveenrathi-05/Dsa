"""
Majority Element II (LeetCode #229)

Return all elements that appear more than n/3 times.

Striver A2Z - Step 2: Arrays

Key idea:
At most two elements can appear more than n/3 times. Use the extended
Moore's Voting Algorithm to find two candidates, then verify their
frequencies in a second pass.

Time Complexity: O(n)
Space Complexity: O(1), excluding the output list
"""

def majority_element_2(nums):
    count1 = count2 = 0
    candidate1 = candidate2 = None

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    answer = []
    if count1 > len(nums) // 3:
        answer.append(candidate1)
    if count2 > len(nums) // 3:
        answer.append(candidate2)

    return answer

if __name__ == "__main__":
    print(majority_element_2([1, 2, 3, 4, 3, 5]))  # []
    print(majority_element_2([1, 1, 1, 2, 2, 3]))  # [1]

"""
Best Time to Buy and Sell Stock (LeetCode #121)

Return the maximum profit from one buy and one sell.

Striver A2Z - Step 2: Arrays

Key idea:
Track the minimum price seen so far and compute the profit for selling
on each day.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    min_price_so_far=prices[0]
    max_profit=0
    for i in range(1,len(prices)):
        max_profit=max(max_profit,prices[i]-min_price_so_far)
        min_price_so_far=min(min_price_so_far,prices[i])
    return max_profit

if __name__=="__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))

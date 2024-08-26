'''
Buy and Sell Crypto
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100

'''

from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        maximumProf = 0
        currentMax = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] < 0:
                    continue
                else:
                    currentMax = prices[j] - prices[i]
                    maximumProf = max(maximumProf, currentMax)
        return maximumProf
    
    # abduls answer
    def maxProfit2(self, prices: List[int]) -> int:
        res = 0
        min_val = float("inf")
        for price in prices:
            min_val = min(min_val, price) 
            res = max(res, price - min_val) 
        return res 

    def maxProfit3(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            res = max(res, p - lowest)
        return res


if __name__ == "__main__":
    solution = Solution()

    
    prices1 = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit1(prices1))  # Output: 5

    prices2 = [7, 6, 4, 3, 1]
    print(solution.maxProfit1(prices2))  # Output: 0

    prices3 = [1, 2, 3, 4, 5]
    print(solution.maxProfit1(prices3))  # Output: 4

    prices4 = [2, 4, 1]
    print(solution.maxProfit1(prices4))  # Output: 2

    prices5 = [3, 2, 6, 5, 0, 3]
    print(solution.maxProfit1(prices5))  # Output: 4

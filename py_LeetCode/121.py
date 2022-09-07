from typing import List

# Result:
# Runtime: 1193 ms, faster than 67.15% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 86.89% of Python3 online submissions for Best Time to Buy and Sell Stock. 
# https://leetcode.com/submissions/detail/704816052/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """strat: Kadane's Algorithm"""
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price
        return max_profit


print(Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))

from typing import List

"""
Problem: 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Sliding Window
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0
        while j < len(prices):
            if  prices[i] < prices[j]:
                profit = max(profit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return profit
        
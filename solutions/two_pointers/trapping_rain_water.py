from typing import List

"""
Problem: 42. Trapping Rain Water
Difficulty: Hard
Topic: Two Pointers
Link: https://leetcode.com/problems/trapping-rain-water/
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        frwd = [height[0]]*n
        bkwd = [height[n-1]]*n
        for i in range(1,n):
            frwd[i] = max(frwd[i-1],height[i])
            bkwd[n-1-i] = max(bkwd[n-i],height[n-1-i])
        sum = 0
        for i in range(n):
            sum += min(frwd[i],bkwd[i]) - height[i]
        return sum
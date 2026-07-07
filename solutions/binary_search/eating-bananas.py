import math
from typing import List

"""
Problem: 875. Koko Eating Bananas
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/koko-eating-bananas/
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_list = range(1,max(piles)+1)
        l, r = 0, max(piles)-1
        k = max(piles)
        while l <= r:
            m = (l+r)//2
            tgt_h = 0
            for p in piles:
                tgt_h += math.ceil(p/k_list[m])
            if tgt_h <= h:
                k = min(k,k_list[m])
                r = m-1
            else:
                l = m+1
        return k

        

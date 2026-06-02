from typing import List
from collections import Counter

"""
Problem: 347. Top K Frequent Elements
Difficulty: Medium
Topic: Arrays N Hashing
Link: https://leetcode.com/problems/top-k-frequent-elements/
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        cntr = Counter(nums).items()
        for num, freq in cntr:
            bucket[freq].append(num)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
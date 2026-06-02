from typing import List

"""
Problem: 128. Longest Consecutive Sequence
Difficulty: Medium
Topic: Arrays N Hashing
Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        count_longest_subseq = 0
        nums_set = set(nums)
        for n in nums_set:
            if n-1 not in nums_set:
                _n = n
                while _n+1 in nums_set:
                    _n += 1
                count_longest_subseq = max(count_longest_subseq, _n-n+1)

        return count_longest_subseq

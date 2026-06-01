import collections
from typing import List

"""
Problem: 49. Group Anagrams
Difficulty: Medium
Topic: Arrays N Hashing
Link: https://leetcode.com/problems/group-anagrams/
Date: 2026-06-02
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for s in strs:
            # sorted_s = "".join(sorted(s))
            # hmap[sorted_s].append(s)
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            
            hmap[tuple(count)].append(s)

        return list(hmap.values())
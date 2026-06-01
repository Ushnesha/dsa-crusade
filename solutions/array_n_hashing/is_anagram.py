from pathlib import Path

# Get the relative path from project root
_current_file = Path(__file__).resolve()
_project_root = _current_file.parents[2]  # Go up 2 levels
_relative_path = _current_file.relative_to(_project_root)

__doc__ = f"""
Problem: 242. Valid Anagram
Difficulty: Easy
Topic: Arrays N Hashing
Link: {_relative_path}
Date: 2026-06-02
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hash table
        hmap = dict()
        if len(s) != len(t):
            return False
        for i in s:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] = hmap[i] + 1
        
        for j in t:
            if j not in hmap:
                return False
            hmap[j] = hmap[j] - 1
    

        for key in hmap:
            if hmap[key] != 0:
                return False

        return True
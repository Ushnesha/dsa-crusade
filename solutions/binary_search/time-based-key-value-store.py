from collections import defaultdict

"""
Problem: 981. Time Based Key-Value Store
Difficulty: Medium
Topic: Binary Search
Link: https://leetcode.com/problems/time-based-key-value-store/
"""

class TimeMap:

    def __init__(self):
        self.mem = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        key_srch = self.mem[key]
        n = len(key_srch)
        if n == 0: return ""
        l , h = 0, n-1
        while (l <= h):
            m = (l+h)//2
            if key_srch[m][0] == timestamp or (m+1 < n and key_srch[m][0] < timestamp and key_srch[m+1][0] > timestamp):
                return key_srch[m][1]
            elif key_srch[m][0] > timestamp:
                h = m-1
            else:
                l = m+1
        return key_srch[h][1] if h >= 0 else ""
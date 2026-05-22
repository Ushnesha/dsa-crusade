class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_cnt = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                cnt = 1
                next_n = n + 1
                while(next_n in nums_set):
                    cnt = cnt + 1
                    next_n = next_n + 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt

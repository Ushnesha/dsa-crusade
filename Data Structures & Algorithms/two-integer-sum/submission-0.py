class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ctr = {}
        for i,num in enumerate(nums):
            if num in ctr:
                return [ctr[num], i]
            ctr[target-num] = i
        
        
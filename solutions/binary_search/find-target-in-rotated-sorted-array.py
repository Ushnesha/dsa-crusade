class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0, len(nums)-1
        while (l <= h):
            m = (l+h)//2
            if nums[m] == target: return m
            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    h = m
                else:
                    l = m + 1
            elif nums[m+1] <= nums[h]:
                if target >= nums[m+1] and target <= nums[h]:
                    l = m + 1
                else:
                    h = m
        return -1
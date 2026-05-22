class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # pref = [0] * N
        output = nums.copy()
        for i in range(1,N):
            nums[i] = nums[i-1] * nums[i]
        # print(nums)
        for i in range(N-2,-1,-1):
            output[i] = output[i+1] * output[i]
        # print(output)
        # output = []
        for i in range(0,N):
            prod = 1
            if i - 1 >= 0:
                prod = prod * nums[i-1]
            if i + 1 < N:
                prod = prod * output[i+1]
            output[i] = prod
        
        return output
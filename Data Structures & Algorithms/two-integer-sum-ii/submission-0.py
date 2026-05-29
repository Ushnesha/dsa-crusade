class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0 , len(numbers)-1
        while ( i < j ):
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return [i+1, j+1]
            elif sum_ > target:
                j = j - 1
            else:
                i = i + 1
        return [-1,-1]
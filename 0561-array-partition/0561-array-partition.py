class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_numbers = nums[0::2]
        return sum(min_numbers)
        
        
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        min_numbers = sorted(nums)[0::2]
        return sum(min_numbers)
        
        
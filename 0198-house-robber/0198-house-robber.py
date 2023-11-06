import collections

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        max_money = []
        max_money.append(nums[0])
        max_money.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            max_money.append(max(max_money[i-2] + nums[i], max_money[i-1]))
            
        return max(max_money)
        
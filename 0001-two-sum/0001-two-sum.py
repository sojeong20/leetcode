class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            number_to_add = target - nums[i]
            if number_to_add in nums:
                j = nums.index(number_to_add)
                if i != j:
                    return [i, j]
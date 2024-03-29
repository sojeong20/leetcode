class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and (str(nums[j-1]) + str(nums[j])) < (str(nums[j]) + str(nums[j-1])):
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
                
            i += 1
            
        return str(int(''.join([str(n) for n in nums])))
                
        
        
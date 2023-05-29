class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    triplets = [nums[i], nums[left], nums[right]]
                    if triplets not in result:
                        result.append(triplets)
                    
                    left += 1
                    right -= 1
                    
        return result
		
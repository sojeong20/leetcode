class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = []
        
        for x in nums:
            if x in result:
                result.remove(x)
            else:
                result.append(x)
        
        return result[0]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(0, len(nums) + 1):
            combinations = itertools.combinations(nums, i)
            
            for combi in combinations:
                result.append(list(combi))
        
        return result
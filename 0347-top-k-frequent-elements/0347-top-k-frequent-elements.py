class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        
        counter = collections.Counter(nums).most_common(k)
        
        return [num[0] for num in counter]
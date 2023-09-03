class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        
        for itv in sorted(intervals, key=lambda x: x[0]):
            if merged and (merged[-1][0] <= itv[0] <= merged[-1][1] or merged[-1][0] <= itv[1] <= merged[-1][1]):
                merged[-1][0] = min(merged[-1][0], itv[0])
                merged[-1][1] = max(merged[-1][1], itv[1])
            else:
                merged.append(itv)
                
        return merged
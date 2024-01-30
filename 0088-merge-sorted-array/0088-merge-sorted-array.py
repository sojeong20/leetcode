class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1
                
        if p1 < m:
            result += nums1[p1:m]
        
        if p2 < n:
            result += nums2[p2:n]
            
        for i, num in enumerate(result):
            nums1[i] = num
                
                    
                
                
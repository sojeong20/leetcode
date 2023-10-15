class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        
        for cookie in s:
            if g:
                if cookie >= g[0]:
                    result += 1
                    g.pop(0)
            else:
                return result
                           
        return result
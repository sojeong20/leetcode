class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        strs.remove(shortest)
        
        for i, s in enumerate(shortest):
            for str in strs:
                if str[i] != s:
                    return shortest[:i]
        
        return shortest
                
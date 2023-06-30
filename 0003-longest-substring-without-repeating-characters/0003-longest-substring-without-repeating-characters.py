class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        import collections
        seen = collections.defaultdict()
        max_length = 1
        left = 0
        right = left + 1
        seen[s[left]] = left
        
        while left < len(s) - 1 and right < len(s):
            if s[right] not in seen:
                seen[s[right]] = right
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                left += 1
                right = left + 1
                seen = {s[left]: left}
            
        return max_length
                
                
            
        
        
        
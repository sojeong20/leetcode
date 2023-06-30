class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        max_length = 1
        substring = [s[0]]
        left = 0
        right = left + 1
        
        while left < len(s) - 1 and right < len(s):
            if s[right] not in substring:
                substring.append(s[right])
                if len(substring) > max_length:
                    max_length = len(substring)
                right += 1
            else:
                left += 1
                right = left + 1
                substring = [s[left]]
            
        return max_length
                
                
            
        
        
        
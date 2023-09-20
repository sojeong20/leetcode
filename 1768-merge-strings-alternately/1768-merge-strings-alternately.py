class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        
        left, right = 0, 0
        while left < len(word1) or right < len(word2):
            if left < len(word1):
                result += word1[left]
                left += 1
            if right < len(word2):
                result += word2[right]
                right += 1
                
                
        return result
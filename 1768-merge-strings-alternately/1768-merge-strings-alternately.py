class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        
        min_len = min(len(word1), len(word2))
        
        for i in range(0, min_len):
            result += word1[i]
            result += word2[i]
                
        if len(word1) > min_len:
            result += word1[min_len:]
        if len(word2) > min_len:
            result += word2[min_len:]
                
                
        return result
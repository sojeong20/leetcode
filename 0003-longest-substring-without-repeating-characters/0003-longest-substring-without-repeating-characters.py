class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            # If the current character is already in the dictionary and its last index is after the start of the window
            if s[end] in char_map and start <= char_map[s[end]]:
                # Move the start of the window to the next index after the last occurrence of the current character
                start = char_map[s[end]] + 1

            # Update the last index of the current character
            char_map[s[end]] = end

            # Calculate the length of the current substring without repeating characters
            current_length = end - start + 1

            # Update the maximum length if necessary
            max_length = max(max_length, current_length)

        return max_length
                
            
        
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "{":"}","[":"]"}
        stack = []
        
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            elif not stack or c != brackets[stack[-1]]:
                return False
            else:
                stack.pop()
        
        return True if not stack else False
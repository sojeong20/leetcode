class Solution:
    def isValid(self, s: str) -> bool:
        def is_open(c: str):
            if c in ["(", "{", "["]:
                return True
            return False
        
        def is_pair(x:str, y: str):
            if x == "(":
                if y == ")":
                    return True
            elif x == "{":
                if y == "}":
                    return True
            elif x == "[":
                if y == "]":
                    return True
            return False
            
        stack = []
        
        for c in s:
            if is_open(c):
                stack.append(c)
            elif not stack:
                return False
            elif not is_pair(stack[-1], c):
                return False
            else:
                stack.pop()
        
        if not stack:
            return True
        else:
            return False
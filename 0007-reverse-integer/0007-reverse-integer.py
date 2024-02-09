class Solution:
    def reverse(self, x: int) -> int:
        result = ''
        is_minus = True if x < 0 else False
        x = str(abs(x))
        
        for i in range(len(x)-1, -1, -1):
            result += x[i]
            
        result = int(result)
        
        if is_minus:
            result = - result
            
        if result <= -2**31 or result >= 2**31 - 1:
            return 0

        return result
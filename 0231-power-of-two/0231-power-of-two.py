class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: 
            return False
        
        power_of_two = [1]
        
        x = 1
        for i in range(1, 32):
            x *= 2
            power_of_two.append(x)
            
        return True if n in power_of_two else False
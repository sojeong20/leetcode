class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = ""
        big_step = numRows*2-2

        for i in range(numRows):
            p = i
            if i == 0 or i == numRows - 1:
                while p < len(s):
                    result += s[p]
                    p += big_step
            else:
                small_step = (numRows-i)*2-2
                j = 0
                while p < len(s):
                    now_step = small_step if j % 2 == 0 else big_step - small_step
                    result += s[p]
                    p += now_step
                    j += 1
   
        return result
                
            

                
                
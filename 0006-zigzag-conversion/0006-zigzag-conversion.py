class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [""] * len(s)
        cur_row, step = 0, 1
        
        for ch in s:
            rows[cur_row] += ch
            
            if cur_row == numRows - 1:
                step = -1
            elif cur_row == 0:
                step = 1
            
            cur_row += step
            
   
        return "".join(rows)
                
            

                
                
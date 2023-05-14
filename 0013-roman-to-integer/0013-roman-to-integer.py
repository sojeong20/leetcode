class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        result_int = 0
        for i in range(len(s)-1):
            if roman.get(s[i]) >= roman.get(s[i+1]):
                result_int += roman.get(s[i])
            else:
                result_int -= roman.get(s[i])
        
        result_int += roman.get(s[-1])

        return result_int

            
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = [bin(d)[2:].zfill(8) for d in data]
        start = 0
        
        def get_length(c: str):
            if c[:5] == '11110':
                return 4
            elif c[:4] == '1110':
                return 3
            elif c[:3] == '110':
                return 2
            else:
                return 1
        
        def check_followed_character(c: str):
            return c[:2] == '10'


        while start < len(data):
            length = get_length(data[start])
            if length > len(data):
                return False
            
            if length > 1:
                for c in data[start+1:start+length]:
                    if not check_followed_character(c):
                        return False
            else:
                if data[start][0] != '0':
                    return False
                
            start += length

        return True
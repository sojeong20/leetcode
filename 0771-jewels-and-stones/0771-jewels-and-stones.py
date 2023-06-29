class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        import collections
        stones_count = collections.Counter(stones)
        count = 0
        
        for j in jewels:
            count += stones_count.get(j, 0)
            
        return count
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i, p in enumerate(prices):
            if i == 0:
                continue
                
            if p > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit
            
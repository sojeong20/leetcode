class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] <= low_price:
                low_price = prices[i]
            if prices[i] >= low_price and prices[i] - low_price >= profit:
                profit = prices[i] - low_price

        return profit
        
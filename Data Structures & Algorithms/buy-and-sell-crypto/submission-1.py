class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_seen = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_buy_seen)
            min_buy_seen = min(price, min_buy_seen)
            
        return max_profit
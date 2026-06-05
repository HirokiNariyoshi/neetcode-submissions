class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = []
        min_buy_seen = prices[0]

        for price in prices:
            profit_list.append(price - min_buy_seen)
            min_buy_seen = min(price, min_buy_seen)
            
        return max(profit_list)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        min_price = math.inf

        for i, price in enumerate (prices):
            if i != 0:
                profits.append(max(0, price - min_price))
            min_price = min(min_price, price)

        return max(profits) if profits else 0
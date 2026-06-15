class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for price in prices:

            # Find smaller buying price
            if price < buy:
                buy = price

            # Calculate profit
            profit = max(profit, price - buy)

        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        profit = 0

        buy = prices[0]

        for sell in prices:

            if sell < buy:
                buy = sell

            profit = max(profit, sell - buy)

        return profit
        
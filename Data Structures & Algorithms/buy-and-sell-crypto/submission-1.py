class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        understand - 
        input is an array of prices of a stock, and it's index represent the day that the price is
        need to return the max profit (sell - buy)
        if never good time, then return 0

        plan - 

        keep track of max profit seen so far - initialize
        keep a buy pointer to the first in the list
        for loop through the prices
        while the buy is more than sell keep moving right
        check the profit and see if better than max
        return the max

        edge - if prices is only one length return 0

        implement - 
        '''

        max_profit = -1

        buy = 0

        for sell in range(len(prices)):

            while prices[buy] > prices[sell]:
                buy += 1
            
            max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit

        
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy = prices[i]

            profit = prices[i]-buy
            max_profit = max(profit,max_profit)

        return max_profit
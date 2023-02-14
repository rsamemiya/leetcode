class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                profit = max(profit, price - lowest)
        return profit
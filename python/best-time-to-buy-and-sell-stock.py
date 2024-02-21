class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = sell = prices[0]
        profit = 0
        for current in prices:
            if buy >= current:
                buy = current
                sell = current
            elif current > sell:
                profit = max(profit, current - buy)
                sell = current
        return profit

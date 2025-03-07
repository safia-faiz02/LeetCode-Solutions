class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 1, 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                result = prices[sell] - prices[buy]
                profit = max(profit,result)
            else:
                buy = sell
            sell+=1
        return profit

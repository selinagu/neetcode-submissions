class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(n-1):
            buy = prices[i]
            sell = max(prices[i+1:])
            profit = max(sell-buy, profit)

        return profit
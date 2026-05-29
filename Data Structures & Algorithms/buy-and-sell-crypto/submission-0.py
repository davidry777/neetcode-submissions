class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        for i in range(n):
            buy = prices[i]
            for j in range(i + 1, n):
                sell = prices[j]
                max_profit = max(max_profit, sell - buy)

        return max_profit


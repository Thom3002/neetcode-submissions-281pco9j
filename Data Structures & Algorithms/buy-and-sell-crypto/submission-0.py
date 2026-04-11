class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = len(prices)
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        
        return max_profit
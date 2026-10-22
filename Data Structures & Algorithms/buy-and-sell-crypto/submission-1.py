class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxMoney = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                maxMoney = max(maxMoney, prices[j] - prices[i])
        return maxMoney
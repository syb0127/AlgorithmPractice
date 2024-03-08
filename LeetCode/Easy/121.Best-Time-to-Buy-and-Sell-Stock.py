class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0

        for sell in range(1, len(prices)):
            while prices[sell]<prices[buy]:
                buy += 1
            if profit < (prices[sell]-prices[buy]):
                profit = prices[sell]-prices[buy]

        return profit
            
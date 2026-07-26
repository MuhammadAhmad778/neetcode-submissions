class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0
        Min = prices[0]

        for i in range(1, len(prices)):
            current = prices[i] - Min
            Max = max(Max, current)

            Min = min(Min, prices[i])

        return Max
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max=0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>Max:
                    Max=prices[j]-prices[i]
        if Max>0:
            return Max
        else:
            return 0


        
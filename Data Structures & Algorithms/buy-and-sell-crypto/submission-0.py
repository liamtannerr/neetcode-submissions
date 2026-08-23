class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max = 0

        for i in range (len(prices)):
            buyAt = prices[i]
            j = i + 1
            while j < len(prices):
                sellAt = prices[j]
                if (sellAt - buyAt) > max:
                    max = sellAt - buyAt
                j += 1
        
        return max


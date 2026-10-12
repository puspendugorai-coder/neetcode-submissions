class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l= sorted(prices)
        res=0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                sell = prices[j] - prices[i]
                if sell > res:
                    res= sell
        return res  
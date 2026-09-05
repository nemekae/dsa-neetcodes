class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
            
        profit = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                gain = prices[i] - prices[i - 1]
                profit += gain
        
        return profit


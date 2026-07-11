class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
                return 0

        n = len(prices)
        # Initialize states for day 0
        held = -prices[0]   # bought on day 0
        sold = 0             # can't have sold on day 0 (impossible, but 0 is safe lower bound)
        rest = 0              # haven't done anything

        for i in range(1, n):
            prev_held, prev_sold, prev_rest = held, sold, rest

            held = max(prev_held, prev_rest - prices[i])
            sold = prev_held + prices[i]
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)
from functools import cache

class Solution:
    def maxProfit(self, prices):
        n = len(prices)

        @cache
        def dfs(i, holding):

            if i >= n:
                return 0

            if not holding:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)
                return max(buy, skip)

            else:
                sell = prices[i] + dfs(i + 2, False)
                hold = dfs(i + 1, True)
                return max(sell, hold)

        return dfs(0, False)
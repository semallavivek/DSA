class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        ans = 0

        for price in prices:
            min_p = min(min_p, price)
            profit = price - min_p
            ans = max(ans, profit)

        return(ans)
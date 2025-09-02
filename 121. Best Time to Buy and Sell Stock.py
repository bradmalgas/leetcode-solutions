class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # This solution comes from https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/7117621/121-best-time-to-buy-and-sell-stock-cpp-100-beat and I take no credit whatsoever for coming up with it
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

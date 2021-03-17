class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        
        for day in range(1, len(prices)):
            cash = max(cash, hold+prices[day]-fee)
            hold = max(hold, cash-prices[day])
        return cash
        
 # time O(n) space O(n)

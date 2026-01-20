class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        
        for day in range(1, len(prices)):
            cash = max(cash, hold+prices[day]-fee)
            hold = max(hold, cash-prices[day])
        return cash

    # time O(n) space O(n)

    def dp_approach_no_fee(self, prices: List[int]) -> int:
        mini = prices[0]
        max_profit=float('-inf')
        for i in range(1, len(prices)):
            if prices[i]-mini>max_profit:
                max_profit=prices[i]-mini
            mini = min(mini, prices[i])
        print(max_profit)

# t.c O(n) space O(1)

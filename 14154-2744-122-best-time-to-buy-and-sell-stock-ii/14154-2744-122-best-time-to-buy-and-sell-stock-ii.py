class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]

        return profit
        
        # time: O(n) bc of one pass
        # space: O(1) because of single var
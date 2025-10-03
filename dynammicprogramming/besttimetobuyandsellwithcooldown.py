#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

#After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_range = len(prices)
        dp = [[0,0,0] for i in range(day_range)]
        
        
        dp[0][0] = -prices[0]
        
        
        for i in range(1,day_range):
            for S in range(3):
                if S == 0:
                    dp[i][0] = max(dp[i-1][2] - prices[i], dp[i-1][0])
                elif S == 1: 
                    dp[i][1] = dp[i-1][0] + prices[i]
                elif S == 2:
                    dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        
        return max(dp[-1][2], dp[-1][1])

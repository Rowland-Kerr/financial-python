#You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

#Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

#Note:

#You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#The transaction fee is only charged once for each stock purchase and sale.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        day_range = len(prices)
        dp = [[0,0] for j in range(day_range)]
        dp[0][0] = -prices[0]

        for i in range(1, day_range):
            for s in range(2):
                if s == 0:
                    dp[i][s] = max(dp[i-1][1] - prices[i], dp[i-1][0])
                elif s == 1:
                    dp[i][s] = max(dp[i-1][0] + prices[i] - fee, dp[i-1][1])
        
        return dp[-1][1]

#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#Find the maximum profit you can achieve. You may complete at most two transactions.

def maxProfit(prices: list[int]):

    dr = len(prices)
    dp = [[[0,0,0], [0,0,0]] for i in range(dr)]
    ##array st first triple is state of hold/buy, and second is able to buy. three indices represent how many buys you have left.
    dp[0][0][1] = -prices[0]
    dp[2][0][0] = prices[1] - prices[2] - prices[0]
    #holding at day 0 will cost initial price (initialize)

    for i in range(1, dr):
        for s in range(2):
            for c in range(3):

                if s == 0 and c == 0 and i > 2:
                    #holding stock, no trades left
                    dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][1][1] - prices[i])

                elif s == 0 and c == 1:
                    #holding stock, 1 trade left
                    dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][2] - prices[i])

                elif s == 1 and c == 0 and i > 2:
                    #not holding stock, no trades left.
                    dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] + prices[i])

                elif s == 1 and c == 1 and i > 0:
                    #not holding stock, 1 trade left
                    dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][1] + prices[i])

                elif s == 1 and c == 2 or s == 0 and c == 2:
                    #not holding stock, 2 trades - (should be 0 as no trade has been made)
                    dp[i][s][c] = 0

    return max(dp[-1][1][0], dp[-1][1][1], dp[-1][1][2])

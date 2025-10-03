#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(1,m):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for j in range(1,n):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        for j in range(1,m):
            for i in range(1,n):
                
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        
        return dp[-1][-1]
    

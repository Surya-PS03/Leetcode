from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        # @cache
        # def solve(i,j):

        #     if i == m-1 and j == n-1:
        #         return grid[i][j]
        #     elif i == m or j == n:
        #         return float("inf")

        
        #     right = grid[i][j] + solve(i+1,j)
        #     down = grid[i][j] + solve(i,j+1)
        #     return min(right,down)

        
        # return solve(0,0)


        # tabulation
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):

                if i == m-1 and j == n-1:
                    dp[i][j] = grid[i][j]
                elif i == m-1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif j == n-1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                else:
                    print(i,j)
                    dp[i][j] = min(grid[i][j] + dp[i+1][j], grid[i][j] + dp[i][j+1])
        
        return dp[0][0]

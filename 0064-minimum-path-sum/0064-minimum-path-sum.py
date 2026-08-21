from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        @cache
        def solve(i,j):

            if i == m-1 and j == n-1:
                return grid[i][j]
            elif i == m or j == n:
                return float("inf")

        
            right = grid[i][j] + solve(i+1,j)
            down = grid[i][j] + solve(i,j+1)
            return min(right,down)

        
        return solve(0,0)
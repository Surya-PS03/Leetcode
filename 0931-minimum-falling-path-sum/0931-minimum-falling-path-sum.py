from functools import cache
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        @cache
        def solve(i,j):
            if j<0 or j>=n:
                return float("inf")
            
            if i == m-1:
                return matrix[i][j]

            down = matrix[i][j] + solve(i+1,j)
            down_left = matrix[i][j] + solve(i+1,j-1)
            down_right = matrix[i][j] + solve(i+1,j+1)

            return min(down,down_left,down_right)
            
        
        res = float("inf")
        for i in range(n):

            res = min(res,solve(0,i))
        
        return res
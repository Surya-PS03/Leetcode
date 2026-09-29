from functools import cache
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        # start from (0,0)
        # if open ( push into stack
        # if close pop out of stack
        # if it is possible to make the stack empty return True

        st = []
        m = len(grid)
        n = len(grid[0])

        @cache
        def solve(i,j,bal):
            if i>=m or j>=n:
                return False

            if grid[i][j] == "(":
                bal+=1
            elif grid[i][j] == ")":
                bal-=1
            
            if bal<0:
                return False

            if i==m-1 and j==n-1:
                return bal==0

            down = solve(i+1,j,bal)
            right = solve(i,j+1,bal)

            return down or right
        

        return solve(0,0,0)


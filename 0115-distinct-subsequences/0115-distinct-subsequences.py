from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)

        @cache
        def solve(i,j):
            
            if j==n:
                return 1
            
            if i==m:
                return 0
            

            skip = solve(i+1,j)
            
            if s[i] == t[j]:

                skip += solve(i+1,j+1)
            
            return skip
           

        return solve(0,0)
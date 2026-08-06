from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        s2 = s[::-1]
        
        N = len(s)

        @cache
        def solve(i,j):

            if i>=N or j>=N:
                return 0
            
            x,a,b = float("-inf"),float("-inf"),float("-inf")
            if s[i]==s2[j]:
                x = 1+solve(i+1,j+1)
            else:
                a = solve(i,j+1)
                b = solve(i+1,j)
            

            return max(x,a,b)
        
        return solve(0,0)
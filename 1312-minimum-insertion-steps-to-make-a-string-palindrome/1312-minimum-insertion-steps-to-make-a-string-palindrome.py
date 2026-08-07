from functools import cache
class Solution:
    def minInsertions(self, s: str) -> int:
        
        s2 = s[::-1]

        N = len(s)

        # dp = [[-1]*N for _ in range(N)]

        # def solve(i,j):

        #     if i>=N or j>=N:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]

        #     x,a,b = float("-inf"),float("-inf"),float("-inf")

        #     if s[i] == s2[j]:
        #         x = 1 + solve(i+1,j+1)
        #     else:
        #         a = solve(i+1,j)
        #         b = solve(i,j+1)

        #     dp[i][j] = max(x,b,a) 
        #     return dp[i][j]
        

        # return N-solve(0,0)


        # Bottom up
        dp = [[0]*(N+1) for _ in range(N+1)]

        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):

                if s[i]==s2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        
        return N-dp[0][0]

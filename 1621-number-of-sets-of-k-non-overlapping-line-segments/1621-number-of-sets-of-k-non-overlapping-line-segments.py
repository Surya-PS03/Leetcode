from functools import lru_cache
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        
        N = n
        MOD = 10**9 + 7

        # @lru_cache(None)
        # def solve(i,k):

        #     if k==0:
        #         return 1
            
        #     if i>=N:
        #         return 0

        #     # skip

        #     skip = solve(i+1,k)%MOD

        #     # take
        #     take = 0
        #     for j in range(i+1,N):
        #         take = (take + solve(j,k-1))%MOD
            
        #     return (skip+take)%MOD

        # return solve(0,k)


        # # # BOTTOM UP


        dp = [[0]*(N+1) for _ in range(k+1)]

        # base case
        for i in range(N):
            dp[0][i] = 1

        for K in range(1,k+1):

            prev = [0]*(N+1)

            for x in range(N-1,-1,-1):
                prev[x] = prev[x+1] + dp[K-1][x]

            for i in range(N-1,-1,-1):

                take = prev[i+1]                
                
                skip = dp[K][i+1] % MOD

                dp[K][i] = (skip+take)%MOD

        return dp[k][0]
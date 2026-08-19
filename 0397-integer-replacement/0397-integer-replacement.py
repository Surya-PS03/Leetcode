from functools import cache
class Solution:
    def integerReplacement(self, n: int) -> int:
        
        dp = {}

        def solve(n):

            if n==1:
                return 0
            if n in dp:
                return dp[n]

            even = float("inf")
            odd = float("inf")

            if n & 1 == 0:
                even = 1 + solve(n>>1)
            else:
                plus_one = 1 + solve(n+1)
                minus_one = 1 + solve(n-1)
                odd = min(plus_one,minus_one)

            dp[n] = min(even,odd)
            return dp[n]
            
        return solve(n)
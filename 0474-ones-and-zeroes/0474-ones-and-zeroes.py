from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # use i to iterate over the strs array
        # m,n reduce at every step by count[0] and count[1] respectively
        # pick and not pick dp (found from discussion section)
        # use collections counter to find freq of 0 an 1 since constraints are small
        # if m==0 and n==0 valid state return 1
        # if (m<0 and n>=0) or (m>=0 and n<0) violated condition return 0

        N = len(strs)

        dp = [[[-1]*(n+1) for _ in range(m+1)] for _ in range(N)]

        def solve(i,m,n):
            if i==N:
                return 0
            if dp[i][m][n]!=-1:
                return dp[i][m][n]

            freq = Counter(strs[i])

            notPick = solve(i+1,m,n)
            pick = 0

            if freq["0"]<=m and freq["1"]<=n:
                pick = 1 + solve(i+1,m-freq["0"],n-freq["1"])

            dp[i][m][n] = max(pick,notPick)

            return dp[i][m][n]
        ans = solve(0,m,n)
        return ans
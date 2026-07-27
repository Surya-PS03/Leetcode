class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        #  partition dp

        n = len(arr)
        dp = [-1]*n
         
        def solve(i):
            if i>=n:
                return 0

            if dp[i]!= -1:
                return dp[i]

            curr_max = -1
            result = -1
            j = i
            while j<n and j-i+1<=k:
                curr_max = max(curr_max,arr[j])
                result = max(result,curr_max*(j-i+1)+solve(j+1))
                j+=1
            dp[i] = result
            return result        
        return solve(0)
class Solution:
    def rob(self, nums: list[int]) -> int:
        
        N = len(nums)
        dp = [[0]*2 for _ in range(N+1)]

        for i in range(N-1,-1,-1):
                
            notPick = dp[i+1][0]
            pick = nums[i] + dp[i+1][1]

            dp[i][0] = max(pick,notPick)

            dp[i][1] = dp[i+1][0]
        
        return dp[0][0]

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(i):

            if i>=n-1:
                return 0

            if dp[i]!=-1:
                return dp[i]

            take = helper(i+2)+nums[i]
            notTake = helper(i+1)

            dp[i] = max(take,notTake)

            return dp[i]

        def helper2(i):

            if i>=n:
                return 0
            
            if dp[i]!=-1:
                return dp[i]

            take = helper2(i+2)+nums[i]
            notTake = helper2(i+1)

            dp[i] = max(take,notTake)

            return dp[i]
        
        n = len(nums)
        if n==1:
            return nums[0]
        dp = [-1]*n
        left = helper(0)
        dp = [-1]*n
        right = helper2(1)

        print(right,left)
        return max(right,left)
        
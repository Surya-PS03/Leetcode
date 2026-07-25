class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        m = max(nums)
        n = len(nums)

        points = [0]*(m+1)

        for num in nums:
            points[num]+=num
        
        dp = [0]*(m+1)

        def helper(i):

            if i>m:
                return 0
            if dp[i]!=0:
                return dp[i]

            take = helper(i+2)+points[i]
            notTake = helper(i+1)

            dp[i] = max(take,notTake)
            return dp[i]
        
        return helper(1)
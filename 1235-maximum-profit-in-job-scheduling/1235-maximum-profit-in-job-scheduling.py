from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        events = sorted(list(zip(startTime,endTime,profit)))
        startTime = sorted(startTime)
        N = len(startTime)
        dp = [-1]*N

        def helper(i):
            
            if i==N:
                return 0
            
            if dp[i]!=-1:
                return dp[i]

            st,ed,pf = events[i]
            # pick
            pick = pf + helper(bisect_left(startTime,ed))

            # notPick
            notPick = helper(i+1)


            dp[i] = max(pick,notPick)

            return dp[i]
        

        return helper(0)
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        N = len(nums)
        maxPref = [0]*N
        minSuff = [0]*N
        
        maxPref[0] = nums[0]
        minSuff[N-1] = nums[N-1]

        for i in range(1,N):

            maxPref[i] = max(maxPref[i-1],nums[i])

        for i in range(N-2,-1,-1):

            minSuff[i] = min(minSuff[i+1],nums[i]) 
            
        sm = -1
        for i in range(N):
            
            if maxPref[i]-minSuff[i]<=k:
                return i
        
        return sm

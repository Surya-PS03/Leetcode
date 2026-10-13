class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        N = len(nums)
        if N&1:
            pos = (N>>1) + 1
        else:
            pos = N>>1
        
        nums = sorted(nums,key = lambda x: abs(x),reverse=True)
        res = 0

        i = 0

        while i<N:

            if i<pos:
                res += nums[i]**2
            else:
                res -= nums[i]**2
            
            i+=1
        
        return res
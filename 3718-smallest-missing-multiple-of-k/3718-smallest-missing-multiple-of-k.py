class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        
        if max(nums)%k==0:
            N = max(nums)//k
        else:
            N = max(nums)%k + max(nums)//k

        s = set(nums)
        for i in range(1,N+2): 

            if i*k in s:
                continue
            else:
                return i*k
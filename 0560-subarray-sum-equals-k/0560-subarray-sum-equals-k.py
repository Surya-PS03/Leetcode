from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        N = len(nums)
        j = 0
        hmap = defaultdict(int)
        
        prefix = [0]*N
        prefix[0] = nums[0]


        # if subarray begins at index 0
        hmap[0]=1
        
        for i in range(1,N):
            prefix[i] = prefix[i-1]+nums[i]

        count = 0
        while j<N:

            if prefix[j]-k in hmap:
                count += hmap[prefix[j]-k]
            
            hmap[prefix[j]]+=1
        
            j+=1
        
        return count


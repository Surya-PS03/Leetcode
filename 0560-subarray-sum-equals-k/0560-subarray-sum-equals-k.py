class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         
        #  prefix sum + hashmap
        #   p[j]-p[i-1] = k
        #   p[j]-k = p[i-1]

        # pefix Sum
        
        N = len(nums)
        p = [0]*N
        p[0] = nums[0]

        for i in range(1,N):
            p[i] = p[i-1]+nums[i]
        
        hmap = {0:1}
        count = 0
        
        for j in range(N):

            if p[j]-k in hmap:
                count+=hmap[p[j]-k]

            if p[j] not in hmap:
                hmap[p[j]]=1
            else:
                hmap[p[j]]+=1

        return count

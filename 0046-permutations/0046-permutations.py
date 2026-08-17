class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        N = len(nums)
        pathVis = []
        vis = set()
        res = []
        

        def dfs():

            if len(pathVis)==N:
                res.append(pathVis[:])
                return

            for k in range(N):
                if nums[k] not in vis:

                    pathVis.append(nums[k])
                    vis.add(nums[k])

                    dfs()

                    pathVis.pop()
                    vis.remove(nums[k])
        
        dfs()
        return res
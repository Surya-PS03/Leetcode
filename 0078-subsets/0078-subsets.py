class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # BACKTRACKING

        # take and not take
        N = len(nums)
        res = []
        path = []

        def solve(i):

            if i==N:
                res.append(path.copy())
                return
            

            # take

            path.append(nums[i])
            solve(i+1)
            path.pop()

            # not take
            solve(i+1)
        solve(0)
        return res
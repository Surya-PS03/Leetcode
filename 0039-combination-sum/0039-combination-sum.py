class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        N = len(candidates)

        path = []
        def solve(prev,t):

            if t==0:
                res.append(path.copy())
            
            if t<0:
                return

            for i in range(prev,N):

                path.append(candidates[i])

                solve(i,t-candidates[i])

                path.pop()
        
        solve(0,target)

        return res

from functools import cache
class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def solve(curr,copy,al):

            if curr>n:
                return float("inf")

            if curr==n:
                return 0

            # copy
            cpy = float("inf")
            if al==0:
                cpy = 1 + solve(curr,curr,1)

            # paste
            paste = float("inf")
            if copy!=0:
                paste = 1 + solve(curr+copy,copy,0)

            return min(cpy,paste)

        return solve(1,0,0)
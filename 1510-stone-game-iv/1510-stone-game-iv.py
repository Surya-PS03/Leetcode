from functools import cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        

        @cache
        def solve(N):

            if N==0:
                return False
            

            k = 1
            while k*k<=N:
                if not solve(N-k*k):
                    return True
                k+=1
                
            return False
        return solve(n)


        
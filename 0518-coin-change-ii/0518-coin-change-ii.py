from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        N = len(coins)
        @cache
        def solve(amt,i):
            if amt<0:
                return 0

            if amt == 0:
                return 1
            
            if i==N:
                return 0
            
            take = solve(amt-coins[i],i)
            notTake = solve(amt,i+1)

            return take+notTake
        
        return solve(amount,0)
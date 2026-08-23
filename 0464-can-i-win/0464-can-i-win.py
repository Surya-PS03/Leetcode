from functools import cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:


        # edge case 1 when desired total < maxChoosableInteger
        if desiredTotal<maxChoosableInteger:
            return True
            
        # edge case 2
        total = maxChoosableInteger*(maxChoosableInteger+1)//2
        if total<desiredTotal:
            return False
        
        @cache
        def solve(mask,total):

            for i in range(1,maxChoosableInteger+1):
                
                if mask&(1<<i) == 0 :

                    if i>=total or not solve(mask | (1<<i),total-i):
                        return True
            return False
        
        return solve(0,desiredTotal)
                   

                  
                

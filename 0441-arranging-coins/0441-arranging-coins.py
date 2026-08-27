class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # for each row maintain coins

        i = 1
        count = 0
        while n>0:
            
            if n>=i:
                count+=1
            n = n-i
            i+=1
        
        return count
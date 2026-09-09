class Solution:
    def countCommas(self, n: int) -> int:
        
        if n<1000: return 0
        lowerBound = 1000
        comma = 1
        total = 0
        while lowerBound<=n:

            upperBound = lowerBound*1000 - 1

            if upperBound>n:
                upperBound = n

            total += comma * (upperBound-lowerBound + 1)
            
            comma +=1

            lowerBound = upperBound + 1
        
        return total


            


        

        
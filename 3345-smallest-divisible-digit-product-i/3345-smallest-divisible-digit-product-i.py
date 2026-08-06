class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def findProd(num):
            prod = 1

            while num!=0:
                prod*=(num%10)
                num = num//10
            
            return prod
        
        x = findProd(n)
        num = n

        while x%t!=0:
            num = num+1
            x = findProd(num)
        
        return num


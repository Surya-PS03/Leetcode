class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        for k in range(32):
            
            countOne = 0

            for num in nums:

                if num & (1<<k):
                    countOne+=1
            
            if countOne % 3 == 1:
                res = res | (1<<k)
        
        # don't return res in python, python don't reset overflow and gives even more bigger number

        return  res - (1<<32) if res>=(1<<31) else res

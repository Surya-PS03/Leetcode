class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def findSum(n):
            n = str(n)

            s = 0

            for char in n:
                s += int(char)
            
            return s

        for i,n in enumerate(nums):

            sum = findSum(n)

            if sum == i:
                return i
        
        return -1
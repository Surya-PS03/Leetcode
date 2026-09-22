class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        copy = set(nums.copy())

        N = len(copy)

        if N == 0:
            return 0
        
        res = 1

        for num in copy:

            if num-1 in copy:
                continue
            
            count = 1
            x = num
            while x+1 in copy:
                count+=1
                x = x + 1
            
            res = max(res,count)
        return res
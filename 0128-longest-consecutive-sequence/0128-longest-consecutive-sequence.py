class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:      
        dumy = nums.copy()

        dumy = set(dumy)
        res = 1

        N = len(dumy)

        if N==0:
            return 0

        for num in dumy:
            
            count = 1
            if num-1 in dumy:
                continue
            
            x = num

            while x+1 in dumy:
                count+=1
                x+=1

            res = max(res,count)
            


        return res 

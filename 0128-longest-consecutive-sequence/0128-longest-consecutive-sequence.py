class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count=1
        res = 1
        N = len(nums)
        if N==0:
            return 0
        for j in range(1,N):

            if nums[j]-nums[j-1]==1:
                count+=1
            elif nums[j]-nums[j-1]==0:
                continue
            else:
                res = max(count,res)
                count = 1
        return max(count,res)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #  kadane's algorithm
        res = float("-inf")
        curr_sum = 0
        
        for num in nums:
            
            curr_sum = max(curr_sum+num,num)
            res = max(res,curr_sum)
        
        return res

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
    
        def Kadane(nums):
            max_res = float("-inf")
            max_curr_sum = 0
            min_res = float("inf")
            min_curr_sum = 0
            for num in nums:
                max_curr_sum = max(max_curr_sum+num,num)
                max_res = max(max_curr_sum,max_res)
                min_curr_sum = min(min_curr_sum+num,num)
                min_res = min(min_res,min_curr_sum)

            
            return max(abs(min_res),max_res)
        
        return Kadane(nums)
        
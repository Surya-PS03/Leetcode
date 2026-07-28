class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def maxKadane(array):

            res = float("-inf")
            curr_sum = 0

            for num in array:

                curr_sum = max(curr_sum+num,num)
                res = max(res,curr_sum)

            return res
        
        def minKadane(array):

            res = float("inf")
            curr_sum = 0

            for num in array:
                curr_sum = min(curr_sum+num,num)
                res = min(res,curr_sum)
            
            return res
        
    
        N = len(nums)
        m = float("-inf")

        maxK = maxKadane(nums)

        if maxK<0:
            return maxK

        minK = minKadane(nums)
        total = sum(nums)
        
        return max(maxK,total-minK)
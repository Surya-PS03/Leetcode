from functools import cache
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        N = len(nums)

        @cache
        def solve(i,k):

            if i==N:
                return float("-inf")

            if k==1:
                return sum(nums[i:])/(N-i)

            result = float("-inf")
            
            for j in range(i,N):

                result = max(result,(sum(nums[i:j+1])/(j-i+1)) + solve(j+1,k-1))
            
            return result

        return solve(0,k)
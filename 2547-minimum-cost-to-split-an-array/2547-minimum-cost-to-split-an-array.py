from collections import Counter
from functools import cache
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        
        N = len(nums)


        # helper function
        @cache
        def helper(i):

            if i==N:
                return 0

            freq = Counter()
            trimmed_length = 0
            ans = float("inf")

            for j in range(i,N):
                val = nums[j]
                # new occurence added in freq
                freq[val]+=1

                # if free[val] becomes 2 it mean it can't be trimmed hence increase trimmed length
                if freq[val]==2:
                    trimmed_length+=2
                # if val frequency become more than 2 increase normally by 1 as usual
                elif freq[val]>2:
                    trimmed_length +=1
            
                imp = k+trimmed_length

                ans = min(ans,imp + helper(j+1))
            return ans

        return helper(0)
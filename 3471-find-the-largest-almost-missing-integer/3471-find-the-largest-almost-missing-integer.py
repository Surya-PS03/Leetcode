from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        ans = -1
        freq = Counter(nums)
        if k==1:

            for val,fr in freq.items():

                if fr==1:
                     ans = max(ans,val)
        
        N = len(nums)
        if k==N:
            return max(nums)
        
        if freq[nums[0]]==1:
            ans = max(ans,nums[0])
        if freq[nums[-1]]==1:
            ans = max(ans,nums[-1])

        return ans

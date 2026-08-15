class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        total = 0
        N = len(nums)

        if not any(nums):
            return 0

        for num in nums:
            total^=num
        
        if total!=0:
            return N
        
        return N-1
        

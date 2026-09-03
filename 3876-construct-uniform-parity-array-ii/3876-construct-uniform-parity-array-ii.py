class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        nums1 = sorted(nums1)

        if not nums1[0]&1:

            for num in nums1[1:]:
                if num&1: return False
        
        return True
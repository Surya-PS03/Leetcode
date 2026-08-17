from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = Counter(nums)
        N = len(nums)
        res = []
        for num,fr in freq.items():

            if fr>N//3:
                res.append(num)
        
        return res

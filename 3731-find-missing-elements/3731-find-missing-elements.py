class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        intr = set()
        ma = max(nums)
        mb = min(nums)

        for i in range(mb,ma+1):
            intr.add(i)

        intr = sorted(list(intr-set(nums)))

        return intr
        
import heapq
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        
        heap = []
        N = len(nums)
        i = N-k-1
        j = N-1
        maxSum = 0
        while i>=0:

            heapq.heappush(heap,-1*nums[j])

            maxSum = max(maxSum,nums[i]+ -1*heap[0])

            i-=1
            j-=1
        
        return maxSum
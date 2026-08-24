import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        heap = []
        N = len(nums)

        for i in range(N):

            heapq.heappush(heap,-1*nums[i])
        
        
        for i in range(k):

            if i==k-1:
                return -1*heapq.heappop(heap)
            
            heapq.heappop(heap)
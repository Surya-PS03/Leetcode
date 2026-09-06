import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        count = 0

        s = set()
        while count<n:
            x = heapq.heappop(heap)
            count+=1
            if x*2 not in s:
                heapq.heappush(heap,x*2)
                s.add(x*2)
            if x*3 not in s:    
                heapq.heappush(heap,x*3)
                s.add(x*3)
            if x*5 not in s:
                heapq.heappush(heap,x*5)
                s.add(x*5)
        
        return x
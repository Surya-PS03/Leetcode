from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)

        heap = []

        heapq.heapify(heap)

        for char,fr in freq.items():

            heapq.heappush(heap,(-1*fr,char))

        

        res = ""

        while heap:

            fr,char = heapq.heappop(heap)
            fr = -1*fr
            res+=(char*fr)
        
        return res


import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)

        heap = []
        
        for _,fr in freq.items():
            heapq.heappush(heap,-1*fr)
        
        time = 0

        while heap:

            # storing the available task (by freq), we gonna decrease by using most frequent task
            temp = []

            # pop n+1 elements for A __N__ A
            for i in range(n+1):
                if heap:
                    fr = -1*heapq.heappop(heap)
                    # decrease process frequency marking it as completed
                    fr-=1
                    # append remaining freq to temp array
                    temp.append(fr)
                
            # append the freq of processes if they are not zero
            for fr in temp:
                if fr>0: 
                    heapq.heappush(heap,-1*fr)
            

            # incrementing time after process completion

            # if there are no more processes left in the queue update time with just process left in the temp array
            if not heap:
                time += len(temp)
            # else update time with standard waiting time of n+1 for next occurrence of top process n+1( inclusive of the process and n processes ahead of the current processes if idle then also it will be counted)
            else:
                time += (n+1)
        
        return time
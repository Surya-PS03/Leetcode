from bisect import bisect_right
from functools import cache
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        N = len(events)
        events = sorted(events,key=lambda x:x[0])
        value = []
        start = []
        end = []

        for st,ed,val in events:
            value.append(val)
            start.append(st)
            end.append(ed)
        
        @cache
        def helper(i,k):

            if k==0 or i==N:
                return 0

            # pick 
            pick = value[i] + helper(bisect_right(start,end[i]),k-1)

            # not pick
            notPick = helper(i+1,k)


            return max(pick,notPick)
        
        return helper(0,2)
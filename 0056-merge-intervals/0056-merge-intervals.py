class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        

        intervals = sorted(intervals,key = lambda x: (x[0],x[1]))
        N = len(intervals)
        res = []
        res.append(intervals[0])

        for i in range(1,N):
            
            curr = intervals[i]

            st = res[-1][0]
            end = res[-1][1]

            nextSt = curr[0]
            nextEnd = curr[1]

            if end>=nextSt:

                finalEnd = max(end,nextEnd)
                
                res[-1][1] = finalEnd
            else:
                res.append(curr)
        
        return res


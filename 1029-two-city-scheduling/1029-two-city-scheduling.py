class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)//2
        C = [(a-b,i) for i,(a,b) in enumerate(costs)]
        C = sorted(C)
        an = 0
        cost = 0
        for fr,i in C:
            if an<n:
                cost+=costs[i][0]
                an+=1
                continue
            cost+= costs[i][1]

        

        return cost

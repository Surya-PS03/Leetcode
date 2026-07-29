class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        fn = lambda gas,cost: [a-b for a,b in zip(gas,cost)]

        if sum(gas)<sum(cost):
            return -1
        
        cum = fn(gas,cost)

        s = 0
        i = 0
        res = 0
        while i<len(cum):
            s += cum[i]
            
            if s<0:
                s = 0
                res = i+1
        
            i+=1
        

        return res
            
        



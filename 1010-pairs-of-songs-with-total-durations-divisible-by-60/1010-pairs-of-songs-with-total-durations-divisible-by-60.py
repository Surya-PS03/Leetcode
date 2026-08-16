from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        occ = defaultdict(int)
        count = 0
        for t in time:

            need = (t*-1)%60

            if need in occ:
                count+=occ[need]

            occ[t%60]+=1

        return count
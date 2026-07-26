from collections import defaultdict
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        # (h[i]+h[j])%D = 0 (D = 24)

        # h[j]%D = D - (h[i]%D)%D

        hmap = defaultdict(int)
        count = 0
        for hr in hours:
            x = (24-hr%24)%24 #what the current number that is hr%24 needs
            if  x in hmap:
                count += hmap[x]
            
            hmap[hr%24]+=1 # storing in map if some pair eg hr = 11 in future 13 appears so it finds 11
        
        return  count
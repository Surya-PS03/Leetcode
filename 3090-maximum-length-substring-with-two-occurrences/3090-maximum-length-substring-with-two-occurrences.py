from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        maxLen = 0

        hmap = defaultdict(int)

        N = len(s)
        i = 0

        for j in range(N):

            val = s[j]
            hmap[val]+=1
            
            while hmap[val]>2:
                hmap[s[i]]-=1
                i+=1
            
            maxLen = max(maxLen,j-i+1)
        
        return maxLen
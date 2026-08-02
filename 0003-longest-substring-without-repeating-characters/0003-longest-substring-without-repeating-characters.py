from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hmap = {}
        mlen = 0
        i = 0 
        j = 0
        N = len(s)
        while j<N:
            
            if s[j] in hmap:
                last = hmap[s[j]]
                while i<=last:
                    hmap.pop(s[i])
                    i+=1
            
            hmap[s[j]] = j

            mlen = max(mlen,j-i+1)

            j+=1
        
        return mlen
from functools import cache
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        MOD = 10**9 + 7

        # previous current character last occurence - 1 index
        lastSeen = [0]*26
        n = len(s)
        prev = [0]*(n+1)

        for i in range(1,n+1):
            idx = ord(s[i-1]) - ord('a')
            prev[i] = lastSeen[idx]
            lastSeen[idx] = i

        @cache
        def solve(n):
            if n==0:
                return 1
            
            # every time begining from "" we increase subsequence set length by 2 for every char iter
            total = (2*solve(n-1))%MOD
            
            if prev[n]!=0:
                dups =  solve(prev[n]-1)

                # adding MOD because total-dups<0
                return (total-dups+MOD)%MOD
            
            return total%MOD
            
        return (solve(n)-1+MOD)%MOD
from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(s)
        m = len(p)

        @cache
        def solve(i,j):
            
            # if p exhasuted and s also exhausted means string matched
            if j==m:
                return i==n
            
            #  if current s[i] and p[j] matches and for vlaidity that s[i] don't go out of bound i<n
            first_match = (i<n) and (s[i]==p[j] or p[j]==".")

            if j+1<m and p[j+1]=="*":

                # Option A skip * since no occurence of prev character
                # Option B compare next character to * to consume it eg: s=aaa (_aa) p=a*
                return solve(i,j+2) or (first_match and solve(i+1,j))
            
            # not * next but we have first_match(current chars of s and p matches) so call for next chars in both strings
            return first_match and solve(i+1,j+1)

        
        return solve(0,0)

            

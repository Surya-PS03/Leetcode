from functools import cache
class Solution:
    def minCut(self, s: str) -> int:
        
        N = len(s)
        palindrome = [[0]*N for _ in range(N)]
        for end in range(N):
            for start in range(end+1):
                if s[start]==s[end]:
                    if end-start<=2 or palindrome[start+1][end-1]:
                        palindrome[start][end] = 1

        @cache
        def helper(i):
            
            if i==N:
                return -1

            result = float("inf")
            for j in range(i,N):

                if palindrome[i][j]:
                    result = min(result,1 + helper(j+1))

            return result

        return helper(0)
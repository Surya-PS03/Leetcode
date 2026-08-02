from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # quick palindrome lookup

        N = len(s)

        palindromeLookup = [[0]*N for _ in range(N)]

        for end in range(N):
            palindromeLookup[end][end]=1
            for start in range(end):
                if s[start]==s[end]:
                    if end-start<=2 or palindromeLookup[start+1][end-1]:
                        palindromeLookup[start][end] = 1

        
        # partition dp + backtracking
        path = []
        res = []


        def solve(i):

            if i==N:
                res.append(path[:])
                return

            for j in range(i,N):
                

                if palindromeLookup[i][j]:
                    path.append(s[i:j+1])
                
                    solve(j+1)

                    path.pop()
                
        solve(0)

        return res
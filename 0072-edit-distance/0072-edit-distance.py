from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        m = len(word1)
        n = len(word2)

        @cache
        def solve(i,j):

            if i>=m and j<n:
                return n-j
            elif j>=n and i<m:
                return m-i
            elif i>=m and j>=n:
                return 0

            x,a,b,c,d = float("inf"),float("inf"),float("inf"),float("inf"),float("inf")

            if word1[i]==word2[j]:
                x = solve(i+1,j+1)

            else:
                # insert
                a = 1+solve(i,j+1)

                # delete
                b = 1+solve(i+1,j)

                # replace
                c = 1+solve(i+1,j+1)

            return min(x,a,b,c)

        return solve(0,0)
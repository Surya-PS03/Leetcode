class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        
        newDict  = set(wordDict)

        N = len(s)

        res = []

        path = []

        def solve(i,j):

            if i==N:
                res.append(" ".join(path))
                return

            elif j==N:
                return

            solve(i,j+1)

            word = s[i:j+1]
            if word in newDict:
                path.append(word)
                solve(j+1,j+1)
                path.pop()
        
        solve(0,0)
        return res


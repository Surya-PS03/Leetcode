from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        newDict = set(wordDict)
        N = len(s)

        # i and j

        # s[i:j] in newDict then two choices expand the previous word or begin new Word

        @cache
        def solve(i,j):

            if j == N and s[i:j+1] in newDict:
                return True
            elif j==N:
                return False
            

            cont = solve(i,j+1)
            newWord = False
            if s[i:j+1] in newDict:
                newWord = solve(j+1,j+1)
            
            return cont or newWord
        
        return solve(0,0)
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        comb = [0, 0, ['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]

        path = []

        res = []

        N = len(digits)

        def solve(i):

            if i>=N:
                res.append("".join(path))
                return
            
            for ch in comb[int(digits[i])]:
                path.append(ch)
                solve(i+1)
                path.pop()
        
        solve(0)
        return res

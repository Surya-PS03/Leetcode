class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        path = []

        res = []


        def solve(a,b):

            if a==0 and b==0:
                res.append("".join(path))
                return
            
            if a>0:
                path.append("(")
                solve(a-1,b)
                path.pop()
            
            if b>a:
                path.append(")")
                solve(a,b-1)
                path.pop()
        
        solve(n,n)
        return res

        
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        col = set()
        posDiag = set() # (r+c) is constant since row decrease and col increase
        negDiag = set() # (r-c) is constant since row increase and col increase


        board = [["."]*n for  _ in range(n)]

        res = []

        def backmaxxing(r): # passing row number as argument

            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or r-c in negDiag or r+c in posDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backmaxxing(r+1)

                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = "."
        

        backmaxxing(0)

        return res
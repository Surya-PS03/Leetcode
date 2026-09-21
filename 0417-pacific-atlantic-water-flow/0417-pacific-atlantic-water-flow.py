class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r,c,visited):

            visited.add((r,c))

            dirs = [(-1,0),(0,-1),(1,0),(0,1)]

            for x,y in dirs:

                nr = r + x
                nc = c + y

                if (
                0<=nr<m and
                0<=nc<n and 
                (nr,nc) not in visited and 
                heights[nr][nc]>=heights[r][c]
                ):

                    dfs(nr,nc,visited)
        

        # top row

        for i in range(n):
            dfs(0,i,pacific)
        
        # left column

        for i in range(m):
            dfs(i,0,pacific)
        

        # bottom row

        for i in range(n):
            dfs(m-1,i,atlantic)
        
        # right column

        for i in range(m):
            dfs(i,n-1,atlantic)
        
        res = []

        for r in range(m):
            for c in range(n):

                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
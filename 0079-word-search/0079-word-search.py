class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        N = len(word) 

        def dfs(i,j,curr):

            if curr==N:
                return True
            
            if i>=m or i<0 or j<0 or j>=n:
                return False
            
            if board[i][j]!=word[curr]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"
            found = (dfs(i,j+1,curr+1) or dfs(i+1,j,curr+1) or dfs(i-1,j,curr+1) or dfs(i,j-1,curr+1))
            board[i][j] = temp
            return found
        

        for i in range(m):

            for j,ch in enumerate(board[i]):

                if ch==word[0]:

                    if dfs(i,j,0):
                        return True
        return False
        
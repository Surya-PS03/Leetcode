class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # replace diagonals
        N = len(matrix)
        
        for i in range(N):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # reverse all rows

        for i in range(N):
            for j in range(N//2):
                matrix[i][N-j-1],matrix[i][j] = matrix[i][j],matrix[i][N-j-1]
        
        
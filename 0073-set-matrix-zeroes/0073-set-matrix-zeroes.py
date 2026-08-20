class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # set first row and column marked as impacted if 0 found in them
        m,n = len(matrix),len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # col impacted
        for i in range(n): 
            if matrix[0][i]==0: 
                first_row_zero = True
                break

        # row impacted
        for j in range(m): 
            if matrix[j][0] == 0:
                first_col_zero = True
                break
        

        # set impacted rows and columns to 0

        for i in range(1,m):
            for j in range(1,n):

                if not matrix[i][j]:

                    matrix[i][0] = 0
                    matrix[0][j] = 0
        

        for i in range(1,m):
            for j in range(1,n):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # if column impacted turn whole first row to 0
        if  first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        #  if row impacted turn whole first column to 0
        if first_row_zero:
            for i in range(n):
                matrix[0][i] = 0
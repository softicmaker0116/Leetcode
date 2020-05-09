class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # sol.1 - t=O(m*n);s=O(n)
        indexs = set()
        m = len(matrix) # the number of rows
        n = len(matrix[0]) # the number of columns
        for row in range(m):
            if matrix[row].count(0)>0:
                for col in range(n):
                    if matrix[row][col] == 0:
                        indexs.add(col)
                    matrix[row][col] = 0
        for row in range(m):
            for col in indexs:
                matrix[row][col] = 0
        print indexs
                
        
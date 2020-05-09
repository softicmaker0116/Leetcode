class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # sol.1: t=O(n^2)=O(1)
        n = len(matrix)
        im = n//2
        jm = n-im
        tmp = 0
        for i in range(im): # ceiling
            for j in range(jm):
                tmp =  matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = matrix[i][j]
                matrix[i][j] = tmp
                print(i, j, matrix)
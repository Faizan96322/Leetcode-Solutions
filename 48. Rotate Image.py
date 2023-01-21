class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(A[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                A[j][N - 1 - i] = temp

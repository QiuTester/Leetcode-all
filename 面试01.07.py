'''给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # 矩阵顺时针翻转：先对角线翻转，再水平翻转
        # 逆时针翻转：先水平翻转，再对角线翻转
        # 不拆分成两步翻转的话，矩阵的值不是互换从而无法同时传递，导致混乱
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(N):
            matrix[i][:] = matrix[i][::-1]     # [::-1]指倒序遍历数组，按行依次水平翻转数组

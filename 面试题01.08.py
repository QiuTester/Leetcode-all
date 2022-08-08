'''编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])
        row, column = [False]*M, [False]*N
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:     # 记录存在0的行和列位置
                    row[i], column[j] = True, True 
        
        for i in range(M):
            for j in range(N):
                if row[i] or column[j] :  # 若当前行/列存在0，则当前遍历元素置0
                    matrix[i][j] = 0

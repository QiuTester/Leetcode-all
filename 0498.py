'''给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        x, y = 0, 0
        ans = []
        for i in range(m+n-1):                     # 对角线数量=行数+列数-1
            if i % 2:  
                for j in range(y, i-x-1, -1):      # 对角线为奇数次，向左斜下方遍历
                    ans.append(mat[i-j][j])        # 遍历开始位置=[当前对角线-当前列][当前列]
            else: 
                for j in range(x, i-y-1, -1):      # 对角线为偶数次，向右斜上方遍历
                    ans.append(mat[j][i-j])        # 遍历开始位置=[当前行][当前对角线-当前行]
            
            x = x+1 if x<m-1 else m-1     # x表示行
            y = y+1 if y<n-1 else n-1     # y表示列
        return ans

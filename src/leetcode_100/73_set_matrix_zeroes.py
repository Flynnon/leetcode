# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

# 进阶:
#
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。      copy一份数组
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。    使用两个数组记录某一行/某一列是否归零
# 你能想出一个常数空间的解决方案吗？

class Solution:
    def setZeroes(self, matrix):
        """
            https://www.cnblogs.com/higerzhang/p/4099114.html
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        row_zero, col_zero = False, False
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                col_zero = True
                break
        for j in range(0, len(matrix[0])):
            if matrix[0][j] == 0:
                row_zero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col_zero:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0
        if row_zero:
            for j in range(0, len(matrix[0])):
                matrix[0][j] = 0
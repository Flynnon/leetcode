# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 示例 2:
#
# 输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false

class Solution:
    def searchMatrix(self, matrix, target):
        """
            全局的二分查找  或者

            如果矩阵右上角的值比target大，删除所在的列，列号-1，在剩下的元素中继续找；
            如果矩阵右上角的值不大于target，删除所在的行，行号+1，在剩下的元素中继续找，
            找到相等的元素就退出.
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])

        i, j = 0, cols - 1
        found = False
        while 0 <= j < cols and i < rows:
            if matrix[i][j] == target:
                found = True
                break
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return found

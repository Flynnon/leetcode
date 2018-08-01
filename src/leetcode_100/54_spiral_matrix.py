# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。


# DEMO:
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix):
        """
            一行一行的输出即可
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 对于空输入的处理
        if not matrix:
            return matrix

        result = []
        # 初始化各个边的长度
        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        while left <= right and top <= bottom:
            # 当前最上面的一行
            for index in range(left, right + 1):
                result.append(matrix[top][index])

            # 当前最右面的一列
            for index in range(top + 1, bottom):
                result.append(matrix[index][right])

            # 避免重复
            if top < bottom:
                # 当前最下面的一行
                for index in range(right, left - 1, -1):
                    result.append(matrix[bottom][index])

            if left < right:
                # 当前最左面的一列
                for index in range(bottom - 1, top, -1):
                    result.append(matrix[index][left])

            # 修整边界
            right -= 1
            left += 1
            top += 1
            bottom -= 1

        return result


print(Solution().spiralOrder([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]))

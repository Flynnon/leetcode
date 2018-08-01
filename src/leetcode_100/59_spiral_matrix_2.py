# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# DEMO:
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    def generateMatrix(self, n):
        """
            与 54 思路类似，注意边界...
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for _ in range(n)] for _ in range(n)]
        top = left = 0
        bottom = right = n - 1
        cur_num = 1
        while left <= right and top <= bottom:
            for index in range(left, right + 1):
                array[top][index] = cur_num
                cur_num += 1
            for index in range(top + 1, bottom):
                array[index][right] = cur_num
                cur_num += 1
            if top < bottom:
                for index in range(right, left - 1, -1):
                    array[bottom][index] = cur_num
                    cur_num += 1
            if left < right:
                for index in range(bottom - 1, top, -1):
                    array[index][left] = cur_num
                    cur_num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return array

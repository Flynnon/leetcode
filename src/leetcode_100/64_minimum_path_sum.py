# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# DEMO:
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

class Solution:
    def minPathSum(self, grid):
        """
            动态规划. gird[i][j] = min(gird[i-1][j], gird[i][j-1]) + gird[i][j]
        :type grid: List[List[int]]
        :rtype: int
        """
        # 求出边长
        m, n = len(grid), len(grid[0])
        # 遍历每一个点
        for i in range(m):
            for j in range(n):
                # 跳过左边或上边上的节点
                if i == 0 and j == 0:
                    continue
                # 对于只能往下的, 直接加上上方节点的次数
                if i == 0 and j != 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                    continue
                # 对于只能往右的, 直接加上左面节点的次数
                if i != 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                    continue
                # 否则, 加上左面节点和上面节点中的最小值
                if i != 0 and j != 0:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
                    continue
        return grid[m - 1][n - 1]

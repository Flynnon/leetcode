# 一个机器人位于一个 m x n 网格的左上角
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
# 问总共有多少条不同的路径？
#

# 说明：m 和 n 的值均不超过 100。
#
# DEMO:
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右

class Solution:
    def uniquePaths(self, m, n):
        """
            https://blog.csdn.net/linhuanmars/article/details/22126357
            动态规划， ways[i][j] = ways[i-1][j] + ways[i][j-1]
        :type m: int
        :type n: int
        :rtype: int
        """

        # 减少空间复杂度. 即: 减少初始化数组长度
        if m < n:
            return self.uniquePaths(n, m)

        # 最左面一列和最上方一列的初始路径数为1
        ways = [1] * n

        # 每一个点的路径数 = 上方的点的路径数 + 左面的点的路径数
        # 注意，把最左面一列和最上面一列忽略了
        for _ in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j - 1]
        # 最终的路径数
        return ways[n - 1]
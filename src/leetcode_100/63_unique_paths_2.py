# 一个机器人位于一个 m x n 网格的左上角
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径?

# 说明：m 和 n 的值均不超过 100。
#      网格中的障碍物和空位置分别用 1 和 0 来表示
#
# DEMO:
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
            与 62 类似，动态规划. 当遇到 1 时,将当前节点置为不可达(0).
            可以仅仅使用一维数组
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        # m: 长  n: 高
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 初始化路径列表
        ways = [0] * n
        # 第一个节点初始化为0
        ways[0] = 1
        # 进行层序遍历
        for i in range(m):
            # 第一行某个节点为1时,将该节点标记为不可达
            if obstacleGrid[i][0] == 1:
                ways[0] = 0
            for j in range(n):
                # 某节点为1时, 标记为不可达
                if obstacleGrid[i][j] == 1:
                    ways[j] = 0
                # 某节点的可达数 = 上方节点可达数 + 左面节点可达数
                elif j > 0:
                    ways[j] += ways[j - 1]
        return ways[-1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
            与 62 类似，动态规划. 当遇到 1 时,将当前节点置为不可达(0).
            二维数组解法
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        # m: 长  n: 高
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 初始化路径列表
        ways = [[0] * n] * m
        # 进行层序遍历
        for i in range(m):
            # 每一个点
            for j in range(n):
                # 标记不可达节点
                if obstacleGrid[i][j] == 1:
                    ways[i][j] = 0
                # 第一行和第一列的初始化
                elif i == j == 0:
                    ways[i][j] = 1
                elif i == 0 and j > 0:
                    # 第一列
                    ways[i][j] = ways[i][j - 1]
                elif i > 0 and j == 0:
                    # 第一行
                    ways[i][j] = ways[i - 1][j]
                    # 其余点
                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
        return ways[m - 1][n - 1]

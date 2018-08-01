# 假设你正在爬楼梯。需要 n 步你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
#
# DEMO:
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 步 + 1 步
# 2.  2 步
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 步 + 1 步 + 1 步
# 2.  1 步 + 2 步
# 3.  2 步 + 1 步

class Solution:
    def climbStairs(self, n):
        """
            动态规划.  way[n] = way[n - 1] + way[n - 2] 且 way[1] = 1 way[2] = 2
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre, cur = 1, 2
        for _ in range(3, n + 1):
            pre, cur = cur, pre + cur
            # temp = cur
            # cur = cur + pre
            # pre = temp
        return cur
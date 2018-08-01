# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。

# DEMO:
# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"

import math


class Solution:
    def getPermutation(self, n, k):
        """
            按照数学公式推导
        :type n: int
        :type k: int
        :rtype: str
        """
        # seq: 结果集
        # k: 当前位置有多少种情况
        # fact: (n - 1)!
        seq, k, fact = "", k - 1, math.factorial(n - 1)

        # 从小到大排出所有位置
        perm = [i for i in range(1, n + 1)]
        # 从 n - 1 开始向前遍历 直到 0
        for i in reversed(range(n)):
            # fact 指当前位选定后,后续有多少种情况
            # k / fact 当前位下标
            # 由此求出 curr 为当前数
            curr = perm[k // fact]
            seq += str(curr)
            # 当前数字不能再次出现
            perm.remove(curr)

            # 还有剩余位数
            if i > 0:
                # 当前位共有多少种情况
                k %= fact
                # fact 降一级. 即 (n-1)! / (n-1)
                fact //= i
        return seq

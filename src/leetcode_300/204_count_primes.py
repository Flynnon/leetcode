# 计算质数

# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

import math


class Solution:
    def countPrimes(self, n):
        """
            http://www.cnblogs.com/grandyang/p/4462810.html
            数学规律...
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        prime_flags = [True] * (n - 1)
        prime_flags[0] = False
        count, limit = 0, int(math.sqrt(n))
        for i in range(2, limit + 1):
            if prime_flags[i - 1]:
                j = i * i
                while j < n:
                    prime_flags[j - 1] = False
                    j += i
        for flag in prime_flags:
            if flag:
                count += 1

        return count
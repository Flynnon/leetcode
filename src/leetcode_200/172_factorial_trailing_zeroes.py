# 阶乘后的零

# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例:
#
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n) 。


class Solution:
    def trailingZeroes(self, n):
        """
            https://www.cnblogs.com/hutonm/p/5624996.html

            令f(x)表示正整数x末尾所含有的“0”的个数，则有：
            当0 < n < 5时，f(n!) = 0;
            当n >= 5时，f(n!) = k + f(k!), 其中 k = n / 5（取整）
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            result += n // 5
            n //= 5
        return result
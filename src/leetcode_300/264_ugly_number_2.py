# 丑数2

# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:
#
# 1 是丑数。
# n 不超过1690。


class Solution:
    def nthUglyNumber(self, n):
        """
            枚举法...
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2 = i3 = i5 = 0
        # 限定结果集个数
        while len(ugly) < n:
            # 新数中，当前最小的2的倍数
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            # 新数中，当前最小的3的倍数
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            # 新数中，当前最小的5的倍数
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            # 将其中最小的一个加进来
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        # 取出结果集中最大的一个
        return ugly[-1]

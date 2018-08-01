# 快乐数

# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例:
#
# 输入: 19
# 输出: true
# 解释:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


class Solution:
    def isHappy(self, n):
        """
            穷举???....
        :type n: int
        :rtype: bool
        """
        # 已遍历的数字集合
        recorded_set = set()
        while n != 1 and n not in recorded_set:
            recorded_set.add(n)
            # 求出下一位
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            n = _sum

        return n == 1
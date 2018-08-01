# 位1的个数

# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
#
# 示例:
#
# 输入: 11
# 输出: 3
# 解释: 整数11的二进制表示为 00000000000000000000000000001011
#
# 输入: 128
# 输出: 1
# 解释: 整数128的二进制表示为 00000000000000000000000010000000


class Solution(object):
    def hammingWeight(self, n):
        """
            n & (n - 1) 即可去掉末尾的一个1
            当全部去除完成后，结束循环
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result
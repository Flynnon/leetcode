# 2的幂

# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例:
#
# 输入: 1
# 输出: true
# 解释: 20 = 1
#
# 输入: 16
# 输出: true
# 解释: 24 = 16
#
# 输入: 218
# 输出: false


class Solution:
    def isPowerOfTwo(self, n):
        """
            二的幂只有最高位为1, 其余为均为0
            因此一位一位的比较即可.
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        count = 0
        while n:
            if n % 2:
                count += 1
            if count > 1:
                return False
            n //= 2
        return True


class Solution1:
    def isPowerOfTwo(self, n):
        """
            二的幂只有最高位为1, 其余为均为0
            n & (n -1) 是去掉n的二进制中的最高位1
        :type n: int
        :rtype: bool
        """
        # 去掉最高位的1之后，是否为0
        return n > 0 and (n & (n - 1)) == 0

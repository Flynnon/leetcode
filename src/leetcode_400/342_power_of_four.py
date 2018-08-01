# 4的幂
#
# 给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。
#
# 示例:
# 当 num = 16 时 ，返回 true 。 当 num = 5时，返回 false。
#
# 问题进阶：你能不使用循环/递归来解决这个问题吗？

class Solution:
    def isPowerOfFour(self, num):
        """
            https://blog.csdn.net/chenchaofuck1/article/details/51227222
        :type num: int
        :rtype: bool
        """
        # num 首先是2的幂
        # 然后, 4的幂只能是奇数位为1, 因此对num的位进行校验...
        return num > 0 and (num & (num - 1)) == 0 and ((num & 0b01010101010101010101010101010101) == num)


# 循环/递归  每次除以4,最终结果为1
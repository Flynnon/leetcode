# 颠倒二进制位

# 颠倒给定的 32 位无符号整数的二进制位。
#
# 示例:
#
# 输入: 43261596
# 输出: 964176192
# 解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
#      返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？


class Solution1:
    def reverseBits(self, n):
        """
            倒着一个个加即可
        :param n: 输入数字
        :rtype: int
        """
        result = 0
        for i in range(32):
            # result进位
            result <<= 1
            # 查看n的第i位是否为1
            # 如果为1, 将当前位设为1
            result |= n & 1
            n >>= 1
        return result

class Solution2:
    def reverseBits(self, n):
        """
            得到 二进制 数字后直接倒置即可
            注意Python的bin方法的返回值的前几位是符号与类型相关的
        :param n: 输入数字
        :rtype: int
        """
        string = bin(n)
        if '-' in string:
            string = string[:3] + string[3:].zfill(32)[::-1]
        else:
            string = string[:2] + string[2:].zfill(32)[::-1]
        return int(string, 2)

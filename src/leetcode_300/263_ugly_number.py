# 丑数

# 编写一个程序判断给定的数是否为丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: 6
# 输出: true
# 解释: 6 = 2 × 3
#
# 输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
#
# 输入: 14
# 输出: false
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
# 说明：
#
# 1 是丑数。
# 输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。

class Solution:
    def isUgly(self, num):
        """
            直接算即可. 若最终可以整除，则为丑数
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        for i in [2, 3, 5]:
            # 可以整除
            while num % i == 0:
                num //= i
        return num == 1

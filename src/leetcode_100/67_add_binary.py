# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# DEMO:
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"


class Solution:
    def addBinary(self, a, b):
        """
            一位一位的加就行
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry, val = [], 0, 0

        # 遍历长的
        for i in range(max(len(a), len(b))):
            val = carry
            # 已经遍历完的, 不再参与计算
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            # 算 进位 与 当前位的值
            carry, val = val // 2, val % 2
            # 加上当前位
            result.append(str(val))
        # 如果有进位, 再加上进位
        if carry:
            result.append(str(carry))
        result.reverse()
        return ''.join(result)
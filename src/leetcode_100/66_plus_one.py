# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# DEMO:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。


class Solution:
    def plusOne(self, digits):
        """
            直接按位加即可.注意进位
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        for i in range(length - 1, -1, -1):
            if digits[i] == 9:
                # 如果要进位,当前位一定是9
                digits[i] = 0
            else:
                # 无需进位直接结束
                digits[i] += 1
                return digits
        # 此时肯定是第一位有进位(类似 9999 ), 那么在前面补1即可
        digits.insert(0, 1)
        # 效率可能更高
        # digits[0] = 1
        # digits.append(0)
        return digits

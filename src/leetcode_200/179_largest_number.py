# 最大数

# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例:
#
# 输入: [10,2]
# 输出: 210
#
# 输入: [3,30,34,5,9]
# 输出: 9534330
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

import functools

class Solution:
    def largestNumber(self, nums):
        """
            直接比较排序即可。
            比较方法：直接拼接，值更大的位于前方..
        :type nums: list
        :rtype: str
        """

        def compare(a, b):
            return int(b + a) - int(a + b)
        # python3中需要多一步函数转化....
        nums = sorted([str(x) for x in nums], key=functools.cmp_to_key(compare))
        # 过滤掉0开头的部分
        ans = ''.join(nums).lstrip('0')

        return ans or '0'

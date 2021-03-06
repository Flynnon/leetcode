# 只出现一次的数字II

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例:
# 输入: [2,2,3,2]
# 输出: 3
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99

# TODO 剩余解法

class Solution1(object):
    def singleNumber(self, nums):
        """
            去重后，三倍的元素 - 原元素集 = 2 * 多余数字
            空间复杂度 O(n)，时间复杂度 O(n)
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) // 2


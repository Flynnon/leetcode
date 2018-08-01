# 旋转数组

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。


# TODO 找到三种方法
class Solution2:
    def rotate(self, nums, k):
        """
            跟倒转字符串类似，先反转前一部分个元素，再反转后一部分元素，然后再反转全部
        :type nums: list
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        turns = k % len(nums)
        middle = len(nums) - turns
        self.reverse(nums, 0, middle - 1)
        self.reverse(nums, middle, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, array, left, right):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1



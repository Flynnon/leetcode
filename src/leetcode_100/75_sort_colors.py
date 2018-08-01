# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
#
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？

class Solution:
    def sortColors(self, nums):
        """
            以一为中心, 碰到1不变. 从两边向中间遍历, 交换大于一和小于一的值
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 以1(白色)为中间值
        target = 1

        # left 左面是最小值0,右面是1, right 左面是1,右面是最大值
        left, cur, right = 0, 0, len(nums) - 1

        while cur <= right:
            if nums[cur] < target:
                # 将小于 1 的值移至最前
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] > target:
                # 将大于 1 的值移至之后
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:
                # 等于 1 的值不变
                cur += 1

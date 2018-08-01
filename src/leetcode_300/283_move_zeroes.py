# 移动零

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。

class Solution:
    def moveZeroes(self, nums):
        """
            直接从头遍历, 将为0的移动到前面即可
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 当前第一个为0的元素的下标
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
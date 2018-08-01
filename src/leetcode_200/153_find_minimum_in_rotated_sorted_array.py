# 寻找旋转排序数组中的最小值
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0

class Solution:
    def findMin(self, nums):
        """
            二分法...
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        last_value = nums[-1]
        while left < right:
            mid = (left + right) // 2

            # 当中值位于 右部分 时，右边界左移
            if nums[mid] <= last_value:
                right = mid
            # 否则，左边界右移
            else:
                left = mid + 1

        return nums[left]
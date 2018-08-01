# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
# 进阶:
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # 如果直接命中,返回
            if nums[mid] == target:
                return True
            # 当中间值等于左边界值时, 左边界右移
            elif nums[mid] == nums[left]:
                left += 1
            # 当中间值位于左顺序子序列且目标值位于左边界与中间值之间时, 右边界左移
            # 当中间值位于右顺序子序列且目标值位于右边界与中间值之间时, 右边界左移
            elif (nums[mid] > nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            # 否则, 左边界右移
            else:
                left = mid + 1

        return False

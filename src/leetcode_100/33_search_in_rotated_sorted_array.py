# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


class Solution:
    def search(self, nums, target):
        """
            二分查找
            先找到中间节点，这个中间节点如果不是在左顺序子数组，就一定在右顺序子数组，反之亦成立
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # 直接找到了
            if nums[mid] == target:
                return mid
            # 当中间节点位于左顺序子数组 且 查找的值也位于这片区域, 右边界左移
            # 当中间节点位于右顺序子数组 但 查找的值不位于middle右面时, 右边界左移
            elif (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1

        return -1
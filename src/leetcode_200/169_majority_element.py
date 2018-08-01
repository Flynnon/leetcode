# 求众数

# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2


class Solution:
    def majorityElement(self, nums):
        """
            排序后，众数肯定位于中间
        :type nums: list
        :rtype: int
        """
        nums.sort()
        mid = len(nums) // 2
        return nums[mid]


class Solution2:
    def majorityElement(self, nums):
        """
            每次从数组中找出一对不同的元素，将它们从数组中删除，直到遍历完整个数组

        :type nums: list
        :rtype: int
        """
        # cur: 当前出现超过一半的元素
        # count: 出现最多的元素个数与其余元素个数的差值
        count, cur = 0, nums[0]

        for i in range(len(nums)):
            if not count:
                count += 1
                cur = nums[i]
            elif nums[i] == cur:
                count += 1
                cur = nums[i]
            else:
                count -= 1
        return cur
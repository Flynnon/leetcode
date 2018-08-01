# 两数之和


# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution1(object):
    def twoSum(self, nums, target):
        """
            注意，给定的数组没有排序
            哈希表存储 已经放进去的值, 进行遍历
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_dict = {}
        for index, num in enumerate(nums):
            sub = target - num
            sub_index = tmp_dict.get(sub, None)
            if sub_index is not None and sub_index != index:
                return [index, sub_index]
            tmp_dict[num] = index

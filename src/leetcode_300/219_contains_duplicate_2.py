# 存在重复元素 II

# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
#
# 示例:
#
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
#
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
#
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
            使用字典保存 值-下标 对应关系
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                # It the value occurs before, check the difference.
                if i - lookup[num] <= k:
                    return True
                # Update the index of the value.
                lookup[num] = i
        return False

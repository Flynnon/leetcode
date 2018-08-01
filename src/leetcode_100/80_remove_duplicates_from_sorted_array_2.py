# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定 nums = [1,1,1,2,2,3],
#
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,1,2,3,3],
#
# 函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

class Solution:
    def removeDuplicates(self, nums):
        """
            直接写就行...
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        cur_index = 2
        for n in nums[2:]:
            # 直接通过 当前值 与 前前个值 的大小关系来判断是否增加
            if n > nums[cur_index - 2]:
                nums[cur_index] = n
                cur_index += 1
        return cur_index

# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
    def subsets(self, nums):
        """
            nums共 n 位, 那么,结果中总共有 2^n 个记录. 每一个记录都是一组二进制情况, 遍历 2^n,
            每遍历到一个, 根据它的二进制情况, 处理当前位.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i, count = 0, 1 << len(nums)

        while i < count:
            cur = []
            # 计算i中有那几位为1, 将为1的加入其中
            for j in range(len(nums)):
                # 判断i中第j位是否为1
                if i & 1 << j:
                    cur.append(nums[j])
            result.append(cur)
            i += 1

        return result
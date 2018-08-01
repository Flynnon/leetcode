# 乘积最大子序列

# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


class Solution:
    def maxProduct(self, nums):
        """
            动态规划
            前 n 位的乘积最大子序列分以下3种情况：
               之前的乘积总和与当前位同正同负  1. 前n - 1位的乘积最小子序列的乘积 * A[n]最大
               之前乘积总和为正，当前位为负    2. 前n - 1位的乘积最大子序列的乘积 * A[n]最大
               之前乘积总和为负，当前位为正    3. 前n - 1位的乘积最大子序列和乘积最小子序列的乘积 * A[n]都不是最大，而A[n]本身最大

            因此只需记住其前一步的整数最大值和负数的最小值
        :type nums: List[int]
        :rtype: int
        """
        # global_max 总的最大值
        # local_max  截止上一个的最大值，正数
        # local_min  截止上一个的最小值，负数
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in nums:
            # 当乘积小于0时, 归1
            local_max = max(1, local_max)
            # 计算当前最大可能与最小可能， local_min
            if x > 0:
                local_max, local_min = local_max * x, local_min * x
            else:
                local_max, local_min = local_min * x, local_max * x
            # global_max 为每一次最大值中最大的那个
            global_max = max(global_max, local_max)
        return global_max

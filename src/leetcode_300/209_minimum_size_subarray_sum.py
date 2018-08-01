# 长度最小的子数组

# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 进阶:
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。


class Solution:
    def minSubArrayLen(self, s, nums):
        """
            滑动窗口
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right, length, the_sum = 0, 0, len(nums), 0
        min_length = length + 1
        while right < length:
            the_sum += nums[right]

            while the_sum >= s and left <= right:
                min_length = min(min_length, right - left + 1)
                the_sum -= nums[left]
                left += 1

            right += 1

        return min_length if min_length != length + 1 else 0


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

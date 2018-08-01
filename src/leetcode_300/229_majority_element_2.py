# 求众数 II

# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
#
# 示例:
#
# 输入: [3,2,3]
# 输出: [3]
#
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]


class Solution:
    def majorityElement(self, nums):
        """
            https://blog.csdn.net/magicbean2/article/details/73737526
            BM（Boyer-Moore Majority Vote Algorithm）投票法
            时间: O(n), 空间: O(1)
        :type nums: List[int]
        :rtype: List[int]
        """
        # 处理异常输入
        if not nums:
            return []
        # 进行投票, 最终结果一定在 num_1, num_2 之间
        num_1 = num_2 = count_1 = count_2 = 0
        for num in nums:
            if num == num_1:
                count_1 += 1
            elif num == num_2:
                count_2 += 1
            elif count_1 == 0:
                num_1 = num
                count_1 += 1
            elif count_2 == 0:
                num_2 = num
                count_2 += 1
            else:
                count_2 -= 1
                count_1 -= 1
        # 算出两个数字的实际出现次数
        count_1 = count_2 = 0
        for num in nums:
            if num == num_1:
                count_1 += 1
            elif num == num_2:
                count_2 += 1
        # 将出现次数大于 1/3 的, 加入其中
        result = []
        if count_1 > len(nums) // 3:
            result.append(num_1)
        if count_2 > len(nums) // 3:
            result.append(num_2)
        return result

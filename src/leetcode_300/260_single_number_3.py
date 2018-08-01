# 只出现一次的数字 III

# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
# 注意：
#
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

class Solution1:
    def singleNumber(self, nums):
        """
            直接使用集合操作即可.. 时间: O(N), 空间: O(N/2)
        :type nums: List[int]
        :rtype: List[int]
        """
        result = set()
        for num in nums:
            if num not in result:
                result.add(num)
            else:
                result.remove(num)
        return list(result)


class Solution2:
    def singleNumber(self, nums):
        """

        :type nums: List[int]
        :rtype: List[int]
        """
        # x XOR x == 0
        # x XOR y == z  --->  x XOR z == y
        # 这里是找出 nums 中所有的元素的异或的值
        x_xor_y = 0
        for i in nums:
            x_xor_y ^= i

        # 找到异或的值中,第一个不为0的位
        bit = x_xor_y & ~(x_xor_y - 1)

        # 按照该位将数据分成两个部分
        # 算出第一个值
        x = 0
        for i in nums:
            if i & bit:
                x ^= i
        # 算出结果集(也可以在上一步进行计算)
        return [x, x ^ x_xor_y]

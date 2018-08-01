# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# DEMO:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

class Solution:
    def mySqrt(self, x):
        """
            二分法减少比较次数
        :type x: int
        :rtype: int
        """
        # 输入小于2时, 不用继续算了
        if x < 2:
            return x

        # 算出可能的边界. 当x>=2时, x 的 平方根一定小于等于 x // 2
        left, right = 1, x // 2
        while left <= right:
            # 二分法查找
            mid = left + (right - left) // 2
            # x > mid * mid 时, mid在结果的左面
            if mid > x / mid:
                right = mid - 1
            # 否则在结果的右面
            else:
                left = mid + 1
        # left 一定在结果左面
        return left - 1

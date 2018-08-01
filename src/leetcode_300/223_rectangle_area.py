# 矩形面积

# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
#
# https://leetcode-cn.com/problems/rectangle-area/description/
#
# 示例:
#
# 输入: -3, 0, 3, 4, 0, -1, 9, 2 输出: 45
#
# 说明: 假设矩形面积不会超出 int 的范围。

class Solution:
    # TODO
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # return (D - B) * (C - A) + \
        #        (G - E) * (H - F) - \
        #        max(0, (min(C, G) - max(A, E))) * \
        #        max(0, (min(D, H) - max(B, F)))
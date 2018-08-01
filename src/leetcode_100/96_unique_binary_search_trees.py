# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 二叉搜索树: 空树或者二叉树的所有节点比他的左子节点大，比他的右子节点小

class Solution:
    # TODO 处理一下...
    def numTrees(self, n):
        """
            https://blog.csdn.net/u012501459/article/details/46622501
        :type n: int
        :rtype: int
        """
        counts = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]
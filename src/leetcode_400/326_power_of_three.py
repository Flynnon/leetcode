# 3的幂

# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例:
#
# 输入: 27
# 输出: true
# 示例 2:
#
# 输入: 0
# 输出: false
# 示例 3:
#
# 输入: 9
# 输出: true
# 示例 4:
#
# 输入: 45
# 输出: false
# 进阶：
# 你能不使用循环或者递归来完成本题吗？

import math


"""
If log10(n) / log10(3) returns an int (more precisely, a double but has 0 after decimal point), 
then n is a power of 3. (original post). 
But be careful here, you cannot use log (natural log) here, because it will generate round off error for n=243. This is more like a coincidence.
I mean when n=243, we have the following results:

log(243) = 5.493061443340548    log(3) = 1.0986122886681098
   ==> log(243)/log(3) = 4.999999999999999
 
log10(243) = 2.385606273598312    log10(3) = 0.47712125471966244
   ==> log10(243)/log10(3) = 5.0
This happens because log(3) is actually slightly larger than its true value due to round off, which makes the ratio smaller.

public boolean isPowerOfThree(int n) {
    return (Math.log10(n) / Math.log10(3)) % 1 == 0;
}

"""

class Solution:
    def isPowerOfThree(self, n):
        """
            若 n 是3的幂次方，则 n 的对数可以整除 3 的对数

        :type n: int
        :rtype: bool
        """
        # 注意这里用的是 /, 因为我们要看的是最终结果是否为整数而不是整除
        return n > 0 and (math.log10(n) / math.log10(3)).is_integer()

# 递归/循环  直接整除三,若最终结果为1,则为3的幂
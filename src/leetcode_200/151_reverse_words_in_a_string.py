# 翻转字符串里的单词

# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 示例:
#
# 输入: "the sky is blue",
# 输出: "blue is sky the".
# 说明:
#
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 进阶: 请选用C语言的用户尝试使用 O(1) 时间复杂度的原地解法。


class Solution(object):
    def reverseWords(self, s):
        """
            python 没有指针，数组也不是真数组...因此只有这种办法...
            C语言 可以通过两次指针反转来实现
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed([t for t in s.split(' ') if t]))



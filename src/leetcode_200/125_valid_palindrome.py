# 验证回文串

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false


class Solution(object):
    def isPalindrome(self, s):
        """
            从两边遍历即可，注意跳过不满足条件的字符即可
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s_len = len(s)
        left, right = 0, s_len - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].upper() != s[right].upper():
                return False
            left += 1
            right -= 1
        return True

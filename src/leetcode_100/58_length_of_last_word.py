# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。

# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。


# DEMO:
# 输入: "Hello World"
# 输出: 5


class Solution:
    def lengthOfLastWord(self, s):
        """
            直接从后往前遍历即可. 注意 刚开始可能存在空格
        :type s: str
        :rtype: int
        """
        length = 0
        for index in range(len(s) -1, -1, -1):
            if s[index] == ' ':
                if length == 0:
                    continue
                break
            length += 1
        return length
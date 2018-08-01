# 单词拆分

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
# 示例:
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

import functools

class Solution(object):
    # TODO 弄清楚
    def wordBreak(self, s, wordDict):
        """
            动态规划

            定义A[i]表示0到下标为i的子字符能否被分割成dict中的多个单词。
            那么A[i]与A[j],0<=j< i都有关系，即A[i]与前A[]中的前i-1项都有关系，具体为：

            如果A[0]为1，判断s中下标从1开始到i结束的字符是否在dict中，如果在，设置A[i]为1，跳出，否则进入第二步；
            如果A[1]为1，判断s中下标从2开始到i结束的字符是否在dict中，如果在，设置A[i]为1，跳出，否则进入第二步；
            …..
            这样一直遍历到A[i-1]位置。
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 字符串长度
        n = len(s)
        # 最长单词长度
        max_len = functools.reduce(max, [len(string) for string in wordDict])

        # 初始化标记数组
        can_break = [False for _ in range(n + 1)]
        can_break[0] = True
        # 遍历每一个字母
        for i in range(1, n + 1):
            # 遍历每一个
            for l in range(1, min(i, max_len) + 1):

                if can_break[i - l] and s[i - l:i] in wordDict:
                    can_break[i] = True
                    break

        return can_break[-1]

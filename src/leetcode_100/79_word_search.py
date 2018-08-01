# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.


class Solution:
    def exist(self, board, word):
        """
            DFS遍历矩阵
            https://www.cnblogs.com/linxiong/p/4489224.html
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # 用来记录当前访问过的元素
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visited):
                    return True
        return False

    def existRecu(self, board, word, cur, i, j, visited):
        """

        :param board:   源数组
        :param word:    要匹配的单词
        :param cur:     当前要匹配的字母下标
        :param i:       当前要匹配的字母下标(数组中的行)
        :param j:       当前要匹配的字母下标(数组中的列)
        :param visited: 以访问的字母坐标集合
        :return:
        """
        # 当单词全部遍历完成, 认为成功
        if cur == len(word):
            return True

        # 当下标超出边界 或者 当前元素已经被访问过 或者 当前字母无法匹配, 匹配失败
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        # 标记匹配过的字母位置
        visited[i][j] = True
        # 查看下一个字母是否可以匹配(上下左右)
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or \
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or \
                 self.existRecu(board, word, cur + 1, i, j + 1, visited) or \
                 self.existRecu(board, word, cur + 1, i, j - 1, visited)
        # 复原标记
        visited[i][j] = False

        return result
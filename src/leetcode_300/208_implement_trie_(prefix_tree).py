# 实现 Trie (前缀树)

# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
# 说明:
#
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。


class Node:
    def __init__(self):
        self.leaves = {}
        self.is_end = False


class Trie:
    """ 使用 字典保存对应关系即可 """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            if char not in cur.leaves:
                cur.leaves[char] = Node()
            cur = cur.leaves[char]
        cur.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        end_node = self.child_search(word)
        return False if not end_node else end_node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.child_search(prefix) is not None

    # 搜索某个单词的根节点
    def child_search(self, word):
        """
            search one word in cur tree
        :type word: str
        :rtype: Node
        """
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

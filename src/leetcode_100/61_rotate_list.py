# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# DEMO:
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
            求出长度后进行处理
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 处理空输入
        if not head or not head.next:
            return head

        # 求出链表长度
        n, cur = 1, head
        while cur.next:
            cur = cur.next
            n += 1
        # cur指向当前链表尾, 将链表变成环
        cur.next = head

        # 将表头向后推 k 位, 移动指针即可
        cur, tail = head, cur
        for _ in range(n - k % n):
            tail = cur
            cur = cur.next
        # 尾部需要指向NULL
        tail.next = None

        return cur
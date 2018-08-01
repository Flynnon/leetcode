# 反转链表

# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# Definition for singly-linked list.
import threading

import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def reverseList(self, head):
        """
            递归
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


class Solution2:
    def reverseList(self, head):
        """
            非递归
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            _next = cur.next
            cur.next = pre
            pre = cur
            cur = _next
        return pre

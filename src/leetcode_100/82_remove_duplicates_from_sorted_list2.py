# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
            双指针处理即可. 使用哑结点减少复杂度
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            # 如果当前节点重复
            if cur.next and cur.val == cur.next.val:
                # 排除当前重复节点.
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                # 处理cur为空的特殊情况
                if cur is None:
                    pre.next = cur
            else:
                # pre 与 cur 均后移
                pre.next = cur
                pre = cur
                cur = cur.next
        return dummy.next
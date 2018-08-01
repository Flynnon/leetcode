# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例
# 输入: 1->1->2
# 输出: 1->2
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
            一个一个往后处理即可
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        while cur:
            runner = cur.next
            while runner and runner.val == cur.val:
                runner = runner.next
            cur.next = runner
            cur = cur.next

        return head

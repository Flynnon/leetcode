# 环形链表

# 给定一个链表，判断链表中是否有环。
#
# 进阶：
# 你能否不使用额外空间解决此题？


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
            快慢指针即可，快指针每一次移动两步，慢指针每一次移动一步，如果能相遇就说明有环
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False

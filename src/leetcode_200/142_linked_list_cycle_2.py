# 环形链表2
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 说明：不允许修改给定的链表。
#
# 进阶：
# 你是否可以不用额外空间解决此题？


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
    def detectCycle(self, head):
        """
            用集合保存遍历过的节点...通俗易懂...
        :type head: ListNode
        :rtype: ListNode
        """
        node_set = set()
        while head and head.next:
            if head in node_set:
                return head
            node_set.add(head)
            head = head.next
        return None

class Solution2(object):
    def detectCycle(self, head):
        """
            快慢指针处理，推导如下

            // head
            //  1 -- 2 -- 3 -- 4 -- 5
            //            |         |
            //            7 --------6 fast和slow在6相遇
            //设 2,3段为a, 4,5,6为b, 7,3为c
            //slow = a + b
            //fast = a + b + c + b
            //2*slow = fast
            //所以 a = c
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            # 刚开始快慢指针
            slow = slow.next
            fast = fast.next.next
            # 当快慢指针相遇时
            if slow is fast:
                fast = head
                # 快指针重头开始，快慢指针同时向后移动，当再次相遇时即为环的开始节点
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None



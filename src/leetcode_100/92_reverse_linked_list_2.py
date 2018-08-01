#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# TODO
class Solution:
    def reverseBetween(self, head, m, n):
        """

        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 先求出差多少元素
        diff, dummy, cur = n - m + 1, ListNode(-1), head
        dummy.next = head

        last_unswapped = dummy

        #
        while cur and m > 1:
            cur = cur.next
            last_unswapped = cur
            m -= 1

        prev = last_unswapped
        first_swapped  = cur
        while cur and diff > 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1

        last_unswapped.next, first_swapped.next = prev, cur

        return dummy.next

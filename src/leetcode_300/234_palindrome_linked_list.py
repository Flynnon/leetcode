# 回文链表


# 请判断一个链表是否为回文链表。
#
# 示例:
#
# 输入: 1->2
# 输出: false
#
# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
    def isPalindrome(self, head):
        """
            使用栈保存前半部分节点，然后退栈并与后半部分节点比较
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        new_list = []

        # 快慢指针法找链表的中点
        slow = fast = head
        while fast and fast.next:
            new_list.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # 链表有奇数个节点
        if fast:
            slow = slow.next

        for val in new_list[::-1]:
            if val != slow.val:
                return False
            slow = slow.next
        return True


class Solution:
    def isPalindrome(self, head):
        """
            反转一半的链表, 然后遍历看元素是否全相等
            可以反转前半部分，也可以反转后半部分
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

            # 快慢指针法找链表的中点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next  # slow指向链表的后半段
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True


    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head
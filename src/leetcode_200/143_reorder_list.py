# 重排链表

# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例:
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
    # TODO 完成这个
    def reorderList(self, head):
        """
            反转链表 + 列表合并
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 对于异常输入进行检查
        if not head or not head.next:
            return

        # 利用快慢指针找到链表中间节点
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, slow

        pass


class Solution2(object):
    def reorderList(self, head):
        """
            使用栈保存节点，并反转合并
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 对于异常输入进行检查
        if not head or not head.next:
            return

        # 利用快慢指针找到链表中间节点
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # 使用栈保存后半部分
        stack = []
        half = slow.next
        while half:
            stack.append(half)
            half = half.next

        # 断掉最后一个节点的关系
        slow.next = None
        current = head
        while current and stack:
            next_node = current.next
            current.next = stack.pop()
            current.next.next = next_node
            current = next_node

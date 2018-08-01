# 相交链表

# 编写一个程序，找到两个单链表相交的起始节点。
# 例如，下面的两个链表：

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# 在节点 c1 开始相交。
#
#
#
# 注意：
#
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
#
#
# 致谢:
# 特别感谢 @stellari 添加此问题并创建所有测试用例。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, head1, head2):
        """
            方法一:  将一个链表首尾相接，然后判断另外一个链表是否有环，如果有环，则两个链表相交。那么求第一个交点则求出有环的的那个链表的环结点即是
            方法二:  分别遍历两个单链表，直到尾结点。判断尾结点地址是否相等即可，在这个过程中记录下两个链表的长度，算出长度差len，接着先让较长的链表遍历len
            个长度，然后两个链表同时遍历，一个个判断是否相等，第一个相等的节点即为相交节点
        :type head1: ListNode
        :type head2: ListNode
        :rtype: ListNode
        """
        if not head1 or not head2:
            return None

        len_1 = len_2 = 0

        first = head1
        while first and first.next:
            len_1 += 1
            first = first.next

        second = head2
        while second and second.next:
            len_2 += 1
            second = second.next

        # 无交点
        if first is not second:
            return None

        sub_len = len_1 - len_2
        if sub_len > 0:
            long, short = head1, head2
        else:
            long, short = head2, head1
            sub_len = -sub_len

        while sub_len > 0:
            long = long.next
            sub_len -= 1

        while long and short:
            if long is short:
                break
            long = long.next
            short = short.next

        return long

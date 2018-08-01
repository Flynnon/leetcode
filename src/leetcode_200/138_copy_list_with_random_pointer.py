# 复制带随机指针的链表

# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
#
# 要求返回这个链表的深度拷贝。


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
            遍历且copy并使用字典存储对应关系，然后从字典还原对应关系
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        current, prev, copies = head, dummy, {}

        # 遍历旧链表
        while current:
            # 对于每一个遍历到的节点，拷贝一份
            copied = RandomListNode(current.label)
            # 保存 旧节点与新节点的对应关系
            copies[current] = copied
            # 将新节点加入新链表中
            prev.next = copied
            # 指针后移
            prev, current = prev.next, current.next

        current = head
        # 遍历旧的链表
        while current:
            # 如果某节点存在随机指针，将新链表中对应的节点的随机指针指向
            if current.random:
                # 更新新链表中的对应节点的随机指针
                copies[current].random = copies[current.random]
            # 指针后移
            current = current.next

        return dummy.next



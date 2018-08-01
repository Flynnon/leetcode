# 用队列实现栈

# 使用队列实现栈的下列操作：
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


class MyStack(object):

    """
        使用两个队列进行模拟，
        当出栈时，将其中一个队列中的元素导入到另一个中(最后一个元素弹出)
        入栈时，将元素加入到存在元素的栈中即可。
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # q1作为进栈出栈，q2作为中转站
        self.q1 = Queue()
        self.q2 = Queue()
        self._top = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.push(x)
        self._top = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        _old_top = self._top
        # 将q1中除尾元素外的所有元素转到q2中
        while self.q1.size() > 1:
            self._top = self.q1.pop()
            self.q2.push(self._top)
        self.q1.pop()
        # 这里为了简单，直接倒转两个队列了...(其实使用一个队列也可以，只要循环次数为队列的大小即可)
        self.q1, self.q2 = self.q2, self.q1

        return _old_top

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q1.size() + self.q2.size() <= 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

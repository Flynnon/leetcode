# 最小栈

# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。

# 示例:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.


class MinStack:
    """
        使用一个栈存储实际数字与上一个最小值的差值

        也可以使用辅助栈存储每一个阶段的最小值
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 存储当前最小值
        self.min = None
        # 存储差值列表
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # 当栈为空的时候，将当前元素加入
        if not self.stack:
            self.stack.append(0)
            self.min = x
        # 否则，加入差值，并更新最小值
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        # 弹栈时，更新最小值即可
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        """
        :rtype: int
        """
        # 取栈顶时，拼凑原值
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

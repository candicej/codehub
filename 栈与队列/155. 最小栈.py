# 这道题就是用列表来实现栈

# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 这道题就是用列表来实现栈
# 当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；
# 当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；
# 在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中

# 看这个图解就明白了 https://leetcode-cn.com/problems/min-stack/solution/zui-xiao-zhan-by-leetcode-solution/

class MinStack:
    # 我第一个不会的地方就是 构造函数写啥
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 存进去较小的那个
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # 栈和最小栈的元素个数一样，出栈要同时出栈
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
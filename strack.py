'''
Date: 2021-02-14 01:17:07
Author: Ye-P
Descripttion: 栈，先进后出 结构
'''


class Stack(object):
    def __init__(self, limit=10):
        self.data = []  # 栈容器
        self.limit = limit  # 栈容器上限

    # 入栈
    def push(self, data):
        if len(self.data) >= self.limit:
            raise Exception('the overflow of stack.')
        self.data.append(data)

    # 出栈
    def pop(self):
        if not self.data:
            raise IndexError('can not pop a empty stack.')
        self.data.pop()

    # 获取栈容
    def size(self):
        return len(self.data)

    # 判断是否为空栈
    def is_empty(self):
        return bool(self.data)

    # 查询栈顶
    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]


if __name__ == '__main__':
    stack = Stack(limit=5)
    for a in range(1, 6):
        stack.push(a)
        print(stack.data)
    for a in range(1, 6):
        stack.pop()
        print(stack.data)

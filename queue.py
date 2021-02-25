'''
Date: 2021-02-22 19:11:54
LastEditTime: 2021-02-24 17:12:34
Author: Ye-P
Descripttion: 队列实现，只允许在一端进行增加(入队)，在另一端进行删除(出队)
'''


class Queue():
    def __init__(self, items):
        self.datas = []  # 队列内数据
        self.length = 0  # 队列的长度
        self.datas = items
        self.length = len(items)

    def enqueue(self, item):
        """入对 添加新元素"""
        self.datas.append(item)
        self.length += 1  # 长度+1

    def dequeue(self):
        """出对 删除顶层的元素"""
        if self.length == 0:
            raise IndexError('can not dequeue,length of queue is 0')
        self.datas.pop(0)
        self.length -= 1

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return self.length == 0

    def size(self) -> int:
        """返回队列元素大小"""
        return self.length

    def peek(self) -> object:
        """查看队列的首位"""
        return self.datas[0]

    def clear(self):
        del self.datas[:]

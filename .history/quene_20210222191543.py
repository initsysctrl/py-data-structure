'''
Date: 2021-02-22 19:11:54
LastEditTime: 2021-02-22 19:15:37
Author: Ye-P
Descripttion: 队列实现，只允许在一端进行增加(入队)，在另一端进行删除(cjhu dui)
'''


class Queue():
    def __init__(self):
        self.datas = []  # 表示队列内的参数
        self.length = 0  # 表示队列的长度
        self.front = 0  # 表示队列头部位置

    def enqueue(self, item):
        self.datas.append(item)  # 添加元素到队列里面
        self.length = self.length + 1  # 队列长度增加 1

    def dequeue(self):
        self.length = self.length - 1  # 队列的长度减少 1
        dequeued = self.datas[self.front]  # 队首元素为dequeued
        self.front -= 1  # 队首的位置减少1
        self.datas = self.datas[self.front:]  # 队列的元素更新为退队之后的队列
        return dequeued

    def peek(self):
        return self.datas[0]  # 直接返回队列的队首元素

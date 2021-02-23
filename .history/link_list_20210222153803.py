'''
Date: 2021-02-15 16:55:39
LastEditTime: 2021-02-22 15:38:03
Author: Ye-P
Descripttion: python 实现的链表结构
'''
import numpy as np
import mat
# 链表节点


class Node(object):
    def __init__(self, data=None, next=None) -> None:
        super().__init__()
        self._data = data  # 数值
        self._next = next  # 指针

    def set_data(self, data):
        self._data = data

    def set_next(self, next):
        self._next = next
        pass

    def get_data(self) -> object:
        return self._data

    def get_next(self) -> object:
        return self._next


class LinkList():
    def __init__(self) -> None:
        self._head = Node()
        self._tail = None
        self._length = 0

    def is_empty(self):
        return self._head == None

    def add(self, data):
        """[summary]

        Arguments:
            data {[type]} -- [description]
        """
        new_node = Node(data=data)
        new_node.set_next(self._head)
        self._head = new_node

        pass

    def append(self, data):

        pass

    def remove(self):
        pass


node = Node()
print(node)

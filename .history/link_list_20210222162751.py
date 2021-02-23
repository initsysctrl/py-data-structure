'''
Date: 2021-02-15 16:55:39
LastEditTime: 2021-02-22 16:27:47
Author: Ye-P
Descripttion: python 实现的链表结构
'''
import matplotlib.pyplot as plt
import sys
import numpy as np
# 链表节点
import json
import math
math.pow(2)
a = list()
a.append(1)


class Node(object):
    # 单个节点
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
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._length = 0

    def is_empty(self):
        # 链表头没有节点时为空链表
        return self._head == None

    def length(self):
        """遍历节点，直到找到尾部节点，返回节点数量即链表长度"""
        len = 0
        temp_node = self._head
        while temp_node != None:
            len += 1
            temp_node = temp_node._next
        return len

    def insert(self, index, value):
        assert index > 0, 'insert error,index<0'
        assert index < self.length(), 'insert error,index > length'
        temp_node = self._head
        i = 0
        while i <= index:
            pre_node = temp_node
            temp_node = temp_node._next

            pass

        pass

    def remove(self):
        pass


node = Node()
print(node)

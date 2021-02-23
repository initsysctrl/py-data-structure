'''
Date: 2021-02-15 16:55:39
LastEditTime: 2021-02-22 17:15:51
Author: Ye-P
Descripttion: python 实现的链表结构
'''


class Node(object):
    # 单个节点
    def __init__(self, data=None, next=None) -> None:
        super().__init__()
        self._data = data  # 数值
        self._next = next  # 指针


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
        assert index >= 0, 'insert error,index<0'
        assert index <= self.length()-1, 'insert error,index > length'
        current_node = self._head
        pre_node = None
        i = 0
        while i <= index:
            pre_node = current_node
            current_node = current_node._next
            i += 1
        # 把原链拆开，插入新的节点，连接前后
        pre_node._next = Node(data=value, next=current_node)

    def remove(self, index):
        assert index >= 0, 'remove error,index<0'
        assert index <= self.length()-1, 'remove index >length'

        current_node = self._head
        pre_node = None
        i = 0
        while i <= index:
            pre_node = current_node
            current_node = current_node._next
            i += 1
            pass
        pre_node._next = current_node._next
        return True


node = Node()
print(node)

'''
Date: 2021-02-15 16:55:39
LastEditTime: 2021-02-22 18:32:44
Author: Ye-P
Descripttion: python 实现的链表结构
'''


from typing import Iterable


class Node(object):
    # 单个节点
    def __init__(self, data=None, next=None) -> None:
        super().__init__()
        self._data = data  # 数值
        self._next = next  # 指针


class LinkList():
    def __init__(self, datas: Iterable):
        """初始化,遍历数据源依次塞入链表，前后相连"""
        self._head = Node(data=datas[0])
        current_node = self._head
        for value in datas[1:]:
            node = Node(data=value)
            current_node._next = node
            current_node = current_node._next

    def is_empty(self):
        """链表头没有节点时为空链表"""
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
        """插入数据到指定的位置"""
        assert index >= 0, 'insert error,index<0'
        assert index < self.length(), 'insert error,index > length'
        current_node = self._head
        pre_node = None
        i = 0
        while i <= index:
            pre_node = current_node
            current_node = current_node._next
            i += 1
        # 把原链拆开，插入新的节点，连接前后
        pre_node._next = Node(data=value, next=current_node)
        return self

    def remove(self, index) -> bool:
        assert index >= 0, 'remove error,index<0'
        assert index < self.length(), 'remove index >length'
        current_node = self._head
        pre_node = None
        i = 0
        while current_node <= index:
            pre_node = current_node
            current_node = current_node._next
            i += 1
        pre_node._next = current_node._next
        return self

    def to_list(self):
        l = []
        temp = self._head
        while temp != None:
            d = temp._data
            temp = temp._next
            l.append(d)
        return l


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7]
    link_list = LinkList(values)
    print(link_list.to_list())
    print(link_list.is_empty())
    print(link_list.insert(index=5, value=-99).to_list())
    print(link_list.remove(1).to_list())
